#include <cstdio>
#include <string>
#include <iostream>
#include <math.h>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include <string.h>
#include "external_functions.h"
#include "smith.h"

using namespace std;
struct File_data{
    int number_Lines;
    bool* opr;
    string* address_vector;
};

class Statistics{
public:
    int total;
    int miss;

    Statistics(){
        total = 0;
        miss = 0;
    }

    void update(bool decision, bool ActualDecision){
        if (decision != ActualDecision){
            miss++;
			//cout<<"Miss= "<<miss<<endl;
        }
        total++;
		//cout<<"total= "<<total<<endl;
    }
};

class Record{
public:
    string regi;
    int N;
    Record(){}
    Record(int N_){
        N = N_;
        regi = "";
        for (int j=0; j<N; j++)
            regi.insert(0, "0");
    }
    void update(bool ActualDecision){
        string str ="";
        if (ActualDecision == 0) str = "0";
        else str = "1";
		//cout<<"str= "<<str<<endl;
        regi.insert(0, str);
        regi = regi.substr(0, N);
		//cout<<"regi= "<<regi<<endl;
    }

    void Print_normal(){
        cout<< regi << endl;
    }

};

class ReadFile{
public:
    string TraceFile;
    File_data F_Data;

    ReadFile(string TraceFile_){
        TraceFile = TraceFile_;
		//cout<<"TraceFile_= "<<TraceFile_<<endl;
        read_file();
    }

    void read_file(){
        ifstream myfile(TraceFile);
        int number_Lines = 0;
        string temp;
        string* fdata;
		string current_reality;
        if(!myfile){
            cout<<"Error opening output file"<<endl;
        } else {
            while (!myfile.eof()) {
                getline(myfile, temp);
                number_Lines++;
				//cout<<"number_Lines= "<<number_Lines<<endl;
            }
            number_Lines--;
			//cout<<"number_Lines= "<<number_Lines<<endl;
            fdata = new string[number_Lines + 1];
			//cout<<"fdata= "<<fdata<<endl;
            ifstream newfile(TraceFile);
            int count = 0;
            while (!newfile.eof()) {
                getline(newfile, temp);
                fdata[count] = temp;
                count++;
				//cout<<"temp= "<<temp<<endl;
				//cout<< "count= "<<count <<" temp= "<< temp << endl;
				//current_reality = temp.substr (7,1);
				//cout<< "current_reality= "<< current_reality<<endl;;
            }

            F_Data = {number_Lines, new bool[number_Lines], new string[number_Lines]};
			//cout<<"F_Data= "<<F_Data<<endl;
            for (int j = 0; j < number_Lines; j++) {
				//cout<<"fdata[j][7]= "<<fdata[j][7]<<endl;
                if (fdata[j][7] == 'n') {
                    F_Data.opr[j] = 0;
                } else{
                    F_Data.opr[j] = 1;
                }
				//cout<<"F_Data.opr[j]= "<<F_Data.opr[j]<<endl;
                F_Data.address_vector[j] = fdata[j].substr(0, fdata[j].length()-2);
            }
        }

//        for(int i=0; i<F_Data.number_Lines; i++){
//            cout<< i << " " << F_Data.opr[i] << " " << F_Data.address_vector[i]<< endl;
//        }

    }

};

class ParseString{
public:
    int M;
    int N;
    int type; // 0= Bimodal, 1= Gshare, 2= Hybrid, 3=Smith

    ParseString(){
    }

    ParseString(int M_, int N_, int type_){
		//cout<< "Inside ParseString"<<endl;
        M = M_;
        N = N_;
        type = type_;
    }

    string string_XOR(string str1, string str2){
        string out = "";
        for (int i=0; i<str1.length(); i++){
			//cout<<"str1[i]= "<<str1[i]<<endl;
			//cout<<"str2[i]= "<<str2[i]<<endl;
            if (str1[i] == str2[i])
                out.append("0");
            else
                out.append("1");
        }
		//cout<<"out= "<<out<<endl;
        return out;
    }

    string get_pc_bits(string addr){
        string Binary_address = hex_To_Bin(addr);
        string Address_bits = Binary_address.substr(Binary_address.length()-2-M, M);
		//cout<<"Address_bits= "<<Address_bits<<endl;
        return Address_bits;
    }
    int get_pid(string addr){
        string Address_bits = get_pc_bits(addr);
        int id = stoi(Address_bits, 0, 2);
		//cout<<"id= "<<id<<endl;
        return id;
    }
    int get_pid(string addr, string record){

        string Address_bits = get_pc_bits(addr);
        string temp = string_XOR(Address_bits.substr(M-N, N), record);
        temp.insert(0, Address_bits.substr(0, M-N));
		//cout<<"temp= "<<temp<<endl;
        int id = stoi(temp, 0, 2);
		//cout<<"id= "<<id<<endl;
        return id;
    }

};

class Predict{
public:
    int counter;
    int nbits;
    int Counter_Max_Value;

    Predict(){}

    Predict(int counter_, int nbits_){
		//cout<< "Inside Predict"<<endl;
        counter = counter_;
        nbits = nbits_;
        Counter_Max_Value = pow(2, nbits) - 1;
		//cout<<"Counter_Max_Value= "<<Counter_Max_Value<<endl;
    }

    void increment(){
        if (counter < Counter_Max_Value)
            counter++;
    }

    void decrement(){
        if (counter > 0)
            counter--;
    }

    int predict(){
        int prediction;
		//cout<< "Inside Predict"<<endl;

        if (counter < (Counter_Max_Value+1)/2){
            prediction = 0;
			//cout<< "Prediction= "<< prediction <<endl;
        }
        else {
            prediction = 1;
			//cout<< "Prediction= "<< prediction <<endl;
        }

        return prediction;
    }

    void update(bool ActualDecision){
        if (ActualDecision == 0){
            decrement();
			//cout<<"counter= "<<counter<<endl;
        }
        else {
            increment();
			//cout<<"counter= "<<counter<<endl;
        }
    }
};

class Bimodal{
public:
    int M;
    int num_predictors;
    Predict *predictor_array;
    Statistics stats;
    ParseString parser;
    int pid;

    Bimodal(){}

    Bimodal(int M_, int predictor_count_start, int predictor_bits){
        M = M_;
        pid = -1;
        num_predictors = pow(2, M);
		//cout<<"num_predictors= "<<num_predictors<<endl;
        parser = ParseString(M, 0, 0);
		//cout<< "Check 2"<<endl;
        predictor_array = new Predict[num_predictors];
		//cout<< "Check 2.1"<<endl;
        for (int i = 0; i < num_predictors; ++i) {
            predictor_array[i] = *(new Predict(predictor_count_start, predictor_bits));
        }
		//cout<< "predictor_array ="<< predictor_array <<endl;
    }

    bool predict(string addr, bool ActualDecision){
		//cout<< "Check 2.9"<<endl;
        pid = parser.get_pid(addr);
		//cout<<"pid= "<<pid<<endl;
        bool prediction = predictor_array[pid].predict();
		//cout<< "Check 3"<<endl;
		//cout<<"prediction= "<<prediction<<endl;
		//cout<<"ActualDecision= "<<ActualDecision<<endl;
        stats.update(prediction, ActualDecision);
        return prediction;
    }

    void update(bool ActualDecision){
		//cout<< "predictor_array ="<< predictor_array <<endl;
        predictor_array[pid].update(ActualDecision);
        pid = -1;
    }

    void PrintStuff(){
        cout<< "FINAL BIMODAL CONTENTS" << endl;
		//cout<<"num_predictors= "<<num_predictors<<endl;
        for (int j=0; j<num_predictors; j++){
            cout<< j << "\t" << predictor_array[j].counter << endl;
        }
    }

    void Print_normal(){
        cout<< "OUTPUT" << endl;
        cout<< "number of predictions:" << "\t" << stats.total << endl;
        cout<< "number of mispredictions:" << "\t" << stats.miss << endl;
        float temp = round(10000*float(stats.miss)/float(stats.total));
        cout<< "misprediction rate:" << "\t" << std::fixed << std::setprecision(2) << float(temp)/100 << "%" << endl;
        PrintStuff();
    }
};

class Gshare{
public:
    int M;
    int N;
    int num_predictors;
    Predict *predictor_array;
    Statistics stats;
    ParseString parser;
    Record record;
    int pid;

    Gshare(){}

    Gshare(int M_, int N_, int predictor_count_start, int predictor_bits){
        M = M_;
        N = N_;
        pid = -1;
        num_predictors = pow(2, M);
		//cout<<"num_predictors= "<<num_predictors<<endl;
        parser = ParseString(M,N, 1);
        record = Record(N);
        predictor_array = new Predict[num_predictors];
		//cout<< "predictor_array ="<< predictor_array <<endl;

        for (int i = 0; i < num_predictors; ++i) {
            predictor_array[i] = *(new Predict(predictor_count_start, predictor_bits));
			//cout<< "predictor_array ="<< predictor_array <<endl;
        }
    }

    bool predict(string addr, bool ActualDecision){
        pid = parser.get_pid(addr, record.regi);
		//cout<<"pid= "<<pid<<endl;
        bool prediction = predictor_array[pid].predict();
        record.update(ActualDecision);
		//cout<<"prediction= "<<prediction<<endl;
		//cout<<"ActualDecision= "<<ActualDecision<<endl;
        stats.update(prediction, ActualDecision);
        return prediction;
    }

    void update(bool ActualDecision){
        predictor_array[pid].update(ActualDecision);
		//cout<< "predictor_array ="<< predictor_array <<endl;
        pid = -1;
    }

    void PrintStuff(){
        cout<< "FINAL GSHARE CONTENTS" << endl;
		//cout<<"num_predictors= "<<num_predictors<<endl;
        for (int i=0; i<num_predictors; i++){
            cout<< i << "\t" << predictor_array[i].counter << endl;
        }
    }

    void Print_normal(){
        cout<< "OUTPUT" << endl;
        cout<< "number of predictions:" << "\t" << stats.total << endl;
        cout<< "number of mispredictions:" << "\t" << stats.miss << endl;
        float temp = round(10000*float(stats.miss)/float(stats.total));
        cout<< "misprediction rate:" << "\t" << std::fixed << std::setprecision(2) << float(temp)/100 << "%" << endl;
        PrintStuff();
    }
};

class Hybrid{
public:
    int M1;
    int M2;
    int N;
    int K;
    int pid;
    int NumChoose;
    Predict *ArrayChooser;

    Bimodal bimodal;
    Gshare gshare;

    Statistics stats;
    ParseString parser;

    Hybrid(int M1_, int M2_, int N_, int K_){
        M1 = M1_;
        M2 = M2_;
        N = N_;
        K = K_;
        pid = -1;
        NumChoose = pow(2, K);
		//cout<<"NumChoose= "<<NumChoose<<endl;
        bimodal = Bimodal(M2, 4, 3);
		//cout<<"bimodal= "<<bimodal<<endl;
        gshare = Gshare(M1, N, 4, 3);
		//cout<<"gshare= "<<gshare<<endl;
        parser = ParseString(K,0, 0);
		//cout<<"parser= "<<parser<<endl;
        ArrayChooser = new Predict[NumChoose];
		//cout<<"ArrayChooser= "<<ArrayChooser<<endl;
        for (int i = 0; i < NumChoose; ++i) {
            ArrayChooser[i] = *(new Predict(1, 2));
			//cout<<"ArrayChooser[i]= "<<ArrayChooser[i]<<endl;
        }
    }

    bool predict(string addr, bool ActualDecision){
        pid = parser.get_pid(addr);
		//cout<<"pid= "<<pid<<endl;
		//cout<<"addr= "<<addr<<endl;
        bool gsharePrediction = gshare.predict(addr, ActualDecision);
        bool bimodalPrediction = bimodal.predict(addr, ActualDecision);
		//cout<<"gsharePrediction= "<<gsharePrediction<<endl;
		//cout<<"bimodalPrediction= "<<bimodalPrediction<<endl;
        bool cp = ArrayChooser[pid].predict();
        bool prediction;
        if (cp == 1) {
            prediction = gsharePrediction;
            gshare.update(ActualDecision);
        }
        else {
            prediction = bimodalPrediction;
            bimodal.update(ActualDecision);
        }

        stats.update(prediction, ActualDecision);
        update(ActualDecision, gsharePrediction, bimodalPrediction);
		//cout<<"prediction= "<<prediction<<endl;
        return prediction;
    }

    void update(bool ActualDecision, bool gsharePrediction, bool bimodalPrediction){
        if (ActualDecision == gsharePrediction && ActualDecision != bimodalPrediction)
            ArrayChooser[pid].increment();
        else if (ActualDecision != gsharePrediction && ActualDecision == bimodalPrediction)
            ArrayChooser[pid].decrement();
        pid = -1;
    }

    void PrintStuff(){
        cout<< "FINAL CHOOSER CONTENTS" << endl;
        for (int i=0; i<NumChoose; i++){
			//cout<<"ArrayChooser[i]= "<<ArrayChooser[i]<<endl;
            cout<< i << "\t" << ArrayChooser[i].counter << endl;
        }
    }

    void Print_normal(){
        cout<< "OUTPUT" << endl;
        cout<< "number of predictions:" << "\t" << stats.total << endl;
        cout<< "number of mispredictions:" << "\t" << stats.miss << endl;
        float temp = round(10000*float(stats.miss)/float(stats.total));
        cout<< "misprediction rate:" << "\t" << std::fixed << std::setprecision(2) << float(temp)/100 << "%" << endl;
        PrintStuff();
        gshare.PrintStuff();
        bimodal.PrintStuff();
    }
};


class Simulate{
public:

    int M1;
    int M2;
    int N;
    int K;
    int type; // 0=Bimodal, 1=Gshare, 2=Hybrid, 3=Smith
    string str_type;
    string TraceFile;
    Bimodal *bimodal;
    Gshare *gshare;
    Hybrid *hybrid;
    ReadFile *f;

    Simulate(int M1_, int M2_, int N_, int K_, string str_type_, string TraceFile_){
        M1 = M1_;
        M2 = M2_;
        N = N_;
        K = K_;
        str_type = std::move(str_type_);
		//cout<<"M1= "<<M1<<endl;
		//cout<<"M2= "<<M2<<endl;
		//cout<<"N= "<<N<<endl;
		//cout<<"K= "<<K<<endl;
        if (str_type == "bimodal") type = 0;
        else if (str_type == "gshare") type=1;
        else if (str_type == "hybrid") type=2;
		//else if (str_type == "smith") type=3;
		//cout<<"type= "<<type<<endl;
        TraceFile = std::move(TraceFile_);
        f = new ReadFile(TraceFile);

        if (type == 0)
		{
			//cout<<"Working on Bimodal"<<endl;
            bimodal = new Bimodal(M1, 4, 3);
		}
        else if (type == 1)
		{
			//cout<<"Working on Gshare"<<endl;
            gshare = new Gshare(M1, N, 4, 3);
		}
        else if (type == 2)
		{
			//cout<<"Working on hybrid"<<endl;
            hybrid = new Hybrid(M1, M2, N, K);
		}
		/* else if (type == 3)
		{
			//cout<<"Working on smith"<<endl;
            smith = new Smith(M1, 4, 3);
		} */
    }

    void Start(){
			 //cout<<"F_Data.number_Lines= "<<F_Data.number_Lines<<endl;
        if (type == 0){
            for(int i=0; i<f->F_Data.number_Lines; i++) {
				//cout<<"F_Data.address_vector[i]= "<<F_Data.address_vector[i]<<endl;
				//cout<<"F_Data.opr[i]= "<<F_Data.opr[i]<<endl;
                bimodal->predict(f->F_Data.address_vector[i], f->F_Data.opr[i]);
                bimodal->update(f->F_Data.opr[i]);
            }
            bimodal->Print_normal();
        } else if (type == 1){
            for(int i=0; i<f->F_Data.number_Lines; i++) {
				//cout<<"F_Data.address_vector[i]= "<<F_Data.address_vector[i]<<endl;
				//cout<<"F_Data.opr[i]= "<<F_Data.opr[i]<<endl;
                gshare->predict(f->F_Data.address_vector[i], f->F_Data.opr[i]);
                gshare->update(f->F_Data.opr[i]);
            }
            gshare->Print_normal();
        } else if (type == 2){
            for(int i=0; i<f->F_Data.number_Lines; i++) {
				//cout<<"F_Data.address_vector[i]= "<<F_Data.address_vector[i]<<endl;
				//cout<<"F_Data.opr[i]= "<<F_Data.opr[i]<<endl;
                hybrid->predict(f->F_Data.address_vector[i], f->F_Data.opr[i]);
            }
            hybrid->Print_normal();
        } /* else if (type == 3){
            for(int i=0; i<f->F_Data.number_Lines; i++) {
                smith->predict(f->F_Data.address_vector[i], f->F_Data.opr[i]);
                smith->update(f->F_Data.opr[i]);
            }
            smith->Print_normal();
        } */
    }

};

int main(int argc, char** argv) {

    Simulate *s;
    cout << "COMMAND" << endl;
    if (string(argv[1]) == "bimodal") {
		//cout<< "Check 1"<<endl;
		//cout<< "argv[1]= "<<argv[1]<<" argv[2]= "<<argv[2]<<" argv[3]= "<<argv[3]<<endl;
        cout << "./sim " << "bimodal" << " " << argv[2] << " " << argv[3] << endl;
        s = new Simulate(atoi(argv[2]), 0, 0, 0, argv[1], argv[3]);
    }
    else if (string(argv[1]) == "gshare") {
		//cout<< "Check 1"<<endl;
		//cout<< "argv[1]= "<<argv[1]<<" argv[2]= "<<argv[2]<<" argv[3]= "<<argv[3]<<endl;
        cout << "./sim " << "gshare" << " " << argv[2] << " " << argv[3] << " " << argv[4] << endl;
        s = new Simulate(atoi(argv[2]), 0, atoi(argv[3]), 0, argv[1], argv[4]);
    }
    else if (string(argv[1]) == "hybrid") {
		//cout<< "Check 1"<<endl;
		//cout<< "argv[1]= "<<argv[1]<<" argv[2]= "<<argv[2]<<" argv[3]= "<<argv[3]<<endl;
        cout << "./sim " << "hybrid" << " " << argv[2] << " " << argv[3] << " " << argv[4] << " " << argv[5] << " " << argv[6] << endl;
        s = new Simulate(atoi(argv[3]), atoi(argv[5]), atoi(argv[4]), atoi(argv[2]), argv[1], argv[6]);
    }
	else if (string(argv[1]) == "smith") {
        cout << "./sim " << "smith" << " " << argv[2] << " " << argv[3] << endl;
		//cout<< "Check 1"<<endl;
		//cout<< "argv[1]= "<<argv[1]<<" argv[2]= "<<argv[2]<<" argv[3]= "<<argv[3]<<endl;
		SmithReadFile_and_predict(atoi(argv[2]),argv[3]);
		displaySmith();
    }
    s->Start();
    return 0;

}
