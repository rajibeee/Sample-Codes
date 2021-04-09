#include <iostream>
#include <math.h>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include <cstdio>
#include <string>
#include "external_functions.h"

using namespace std;

class address_Properties{
public:
    string tag;
    int index;
    int block_Offset;

    address_Properties(){
        tag = "";
        index = 0;
        block_Offset = 0;
    }
    address_Properties(string tag_, int index_, int block_Offset_){
        tag = std::move(tag_);
        index = index_;
        block_Offset = block_Offset_;
    }
    void printout_Everything(){
        cout << "tag: " << tag << endl;
        cout << "index: " << index << endl;
        cout << "block_offset: " << block_Offset << endl;
    }
};

class Block{

public:
    string addr;
    string tag;
    bool isItDirty;
    int polCount;

    Block(){
        addr = "";
        tag = "";
        isItDirty = false;
        polCount = 0;
    }

};

struct r_w_Return{
    int is_It_Hit;
    Block victim;
};

class Set{
public:
    Block *blockArray;;
    int polVector;
    Set(){    }
    explicit Set(const int& assoc){
		polVector = 0;
        blockArray = new Block[assoc];
		//cout<<"blockArray= "<<blockArray<<endl;
    }
    int matchTag(const string& tag, const int& assoc) {
        for (int i = 0; i < assoc; i++) {
			//cout<<"i= "<<i<<endl;
            if (tag == blockArray[i].tag){
				//cout<<"i= "<<i<<endl;
				//cout<<"blockArray[i]= "<<blockArray[i]<<endl;
                return i;
            }
        }
        return -1;
    }

    void displaySet(const int& assoc, const int& setNumber){
		//cout<<"assoc= "<<assoc<<endl;
        cout << "Set\t" << setNumber << ":\t";
        for (int i = 0; i < assoc; i++){
			//cout<<"i= "<<i<<endl;
            cout << blockArray[i].tag << " ";
            if (blockArray[i].isItDirty == 1){
				//cout<<"blockArray[i]= "<<blockArray[i]<<endl;
                cout << "D";
            } else{
				//cout<<"blockArray[i]= "<<blockArray[i]<<endl;
                cout << " ";
            }
            cout << " ";
        }
        cout<<endl;
    }
};

class Cache{

public:
    Set *setArray;
    int cacheSize;
    int blockSize;
    int assoc;
    int numSets;
    
	//replacement policy
    int replacement_Policy; // 0 = LRU, 1 = Pseudo-LRU, 2 = Optimal
    //Inclusion policy
    bool inclusion_Policy; // 0 = Non-Inclusive, 1 = Inclusive

    filedata fileData;
    final_Numbers s;

    Cache(int blockSize_, int cacheSize_, int assoc_, int replacement_Policy_, bool inclusion_Policy_, const filedata& fileData_){

        cacheSize = cacheSize_;
        blockSize = blockSize_;
        replacement_Policy = replacement_Policy_;
        inclusion_Policy = inclusion_Policy_;
        assoc = assoc_;
        fileData = fileData_;
        numSets = cacheSize/(assoc*blockSize);
        setArray = new Set[numSets];

        s={0,0,0,0, 0, 0};

        for (int i = 0; i < numSets; ++i) {
			//cout<<"i= "<<i<<endl;
			//cout<<"setArray[i]= "<<setArray[i]<<endl;
            setArray[i] = *(new Set(assoc));
            
        }

        if (replacement_Policy == 2){
            for (int i = 0; i < numSets; ++i) {
                for (int j=0; j < assoc; j++){
					//cout<<"i= "<<i<<"j= "<<j<<endl;
					//cout<<"setArray[i].blockArray[j].polCount= "<<setArray[i].blockArray[j].polCount<<endl;
                    setArray[i].blockArray[j].polCount = my_Infinite_Number;
                    
                }
            }
        }

    }

void updateNumbers(const bool& opr, const bool& is_It_Hit, const Block& victim){
        if (opr == 1){
            s.write_Count++;
			//cout<<"s.write_Count= "<<s.write_Count<<endl;
            if (is_It_Hit == 0){
                s.write_Miss_Count++;
				//cout<<"s.write_Miss_Count= "<<s.write_Miss_Count<<endl;
                if (victim.addr.length() != 0 && victim.isItDirty == 1){
                    s.write_Back_Count++;
					//cout<<"s.write_Back_Count= "<<s.write_Back_Count<<endl;
                }
            }
        }
        else{
            s.read_Count++;
            if (is_It_Hit == 0){
                s.read_Miss_Count++;
				//cout<<"s.read_Miss_Count= "<<s.read_Miss_Count<<endl;
                if (victim.addr.length() != 0 && victim.isItDirty == 1){
                    s.write_Back_Count++;
				//cout<<"s.write_Back_Count= "<<s.write_Back_Count<<endl;
                }
            }
        }
    }
void updatePol_Count(const int& index, const int& way, const bool& is_It_Hit, const string& addr, const int& itr){
        if (replacement_Policy == 0){ //For LRU
            setArray[index].polVector++;
            setArray[index].blockArray[way].polCount = setArray[index].polVector;
        } else if (replacement_Policy == 1){///Function for Pseudo-LRU
            if (is_It_Hit == 0){
                setArray[index].polVector++;
				//cout<<"setArray[index].polVector= "<< setArray[index].polVector<<endl;
                setArray[index].blockArray[way].polCount = setArray[index].polVector;
            }
        } else if (replacement_Policy == 2){ //For Optimal

            for (int i=0; i<assoc; i++){
				//cout<<"i= "<<i<<endl;
                if (setArray[index].blockArray[i].polCount != my_Infinite_Number){
					//cout<<"setArray[index].blockArray[i].polCount= "<<setArray[index].blockArray[i].polCount<<endl;
                    setArray[index].blockArray[i].polCount--;
                }
            }
            int num = matchAddress(addr, fileData, itr);
            if (num != my_Infinite_Number){
				//cout<<"itr= "<<itr<<endl;
                num = num-itr;
            }
            setArray[index].blockArray[way].polCount = num;
        }
    }

void nullify(const string& addr) {
		address_Properties ap = address_2_Parts(addr);
        int way_id = setArray[ap.index].matchTag(ap.tag, assoc);
        int is_It_Hit = way_id > -1;
        if (is_It_Hit == 1){
            if (setArray[ap.index].blockArray[way_id].isItDirty == 1)
            s.mem_write_Back_Count++;
			//cout<< "s.mem_write_Back_Count= "<< s.mem_write_Back_Count <<endl;
            setArray[ap.index].blockArray[way_id].addr = "";
            setArray[ap.index].blockArray[way_id].tag = "";
            setArray[ap.index].blockArray[way_id].isItDirty = 0;
        }
    }
address_Properties address_2_Parts(const string& addr){
        int index_bits = log2(numSets);
        int block_Offset_bits = log2(blockSize);
        int tag_bits = 32 - index_bits - block_Offset_bits;

        string address_binary = hex_To_Bin(addr);
        string tag = address_binary.substr(0, tag_bits);
        string index_str = address_binary.substr(tag_bits, index_bits);
        string block_Offset_str = address_binary.substr(tag_bits+index_bits, 5);

        // int index = std::stoi(index_str, nullptr, 2);
        // int block_Offset = std::stoi(block_Offset_str, nullptr, 2);

        int index;
		//cout<<"index_str= "<<index_str<<endl;
        if (index_str != "")
            index = std::stoi(index_str, nullptr, 2);
        else
            index = 0;
        int block_Offset = std::stoi(block_Offset_str, nullptr, 2);
        tag = bin_To_Hex(tag);
		//cout<<"tag= "<<tag<<endl;
        tag.erase(0, min(tag.find_first_not_of('0'), tag.size()-1));
        address_Properties ap;
        ap.tag = tag;
		//cout<<"ap.tag= "<<ap.tag<<endl;
        ap.index = index;
        ap.block_Offset = block_Offset;
        return ap;
    }

int replacement_Index_Generator(const int& index){
        if (replacement_Policy != 2){
            int min = my_Infinite_Number;
            int way = -1;
            for (int i = 0; i < assoc; i++) {
				//cout<<"i= "<<i<<endl;
                if (setArray[index].blockArray[i].polCount < min){
                    min = setArray[index].blockArray[i].polCount;
					//cout<<"min= "<<min<<endl;
                    way = i;
                }
            }
            return way;
        } else{
            int max = -99;
            int way = -1;
            for (int i = 0; i < assoc; i++) {
				//cout<<"i= "<<i<<endl;
                if (setArray[index].blockArray[i].polCount > max){
                    max = setArray[index].blockArray[i].polCount;
					//cout<<"max= "<<max<<endl;
                    way = i;
                }
            }
            return way;
        }
    }


    r_w_Return accessData(const string& original_Address, const bool& opr, const int& itr){
		//cout<<"Check1"<<endl;
        string addr = original_Address;
		//cout<< "original_Address= "<< original_Address <<endl;
		//cout<<"original_Address.length= "<<original_Address.length()<<endl;
		//cout<< "opr= "<< opr <<endl;
		//cout<< "itr= "<< itr <<endl;
        //cout<<"Check2"<<endl;
		//cout<<"addr.length()= "<<addr.length()<<endl;
        
		 if (original_Address.length()>8){
			//cout<<"original_Addressess = "<<original_Address<<endl;
			//cout<<"original_Address.length()= "<<original_Address.length()<<endl;
			//cout<<"original_Address.length() is greater than 8"<<endl;
			
			addr = addr.substr(3);
			//original_Address=original_Address.substr(3,original_Address.length());
			//cout<<"original_Addressess 2= "<<addr<<endl;
			//cout<<"addr 2 length()= "<<addr.length()<<endl;
			addr.insert(0, 8 - addr.length(), '0'); 
		}
		else {
		addr.insert(0, 8 - original_Address.length(), '0'); 
        } 
		//addr.insert(0, 8 - original_Address.length(), '0'); 
		//addr.insert(0, 8 - static_cast<int>(addr.length()), '0');
        //cout<<"Check3"<<endl;
        address_Properties ap = address_2_Parts(addr);
        int way_id = setArray[ap.index].matchTag(ap.tag, assoc);
		//cout<<"way_id= "<<way_id<<endl;
        int is_It_Hit = way_id > -1;

        // This is for Miss
        Block victim;
        if (is_It_Hit == 0){
            way_id = replacement_Index_Generator(ap.index);
			//cout<<"way_id= "<<way_id<<endl;
            victim = setArray[ap.index].blockArray[way_id];
			//cout<<"victim= "<<victim<<endl;
            setArray[ap.index].blockArray[way_id].addr = addr;
			//cout<<"addr= "<<addr<<endl;
            setArray[ap.index].blockArray[way_id].tag = ap.tag;
			//cout<<"ap.tag= "<<ap.tag<<endl;
            setArray[ap.index].blockArray[way_id].isItDirty = 0;
        }

        if (opr != 0){
            setArray[ap.index].blockArray[way_id].isItDirty = 1;
        }
        updateNumbers(opr, is_It_Hit, victim);
        updatePol_Count(ap.index, way_id, is_It_Hit, original_Address, itr);
        struct r_w_Return  r = {is_It_Hit, victim};
        return r;
    }

    void printout_Everything(){
        for (int i = 0; i < numSets; ++i) {   // will work on each row
            setArray[i].displaySet(assoc, i);
        }
    }
};

class Simulator{
public:
    Cache* L1;
    Cache* L2;
    int blockSize;
    int L1_size;
    int l1_Associativity;
    int L2_size;
    int l2_Associativity;
    int replacement_Policy; // 0 = LRU, 1 = Pseudo-LRU, 2 = Optimal
    bool inclusion_Policy; // 0 = Non-Inclusive, 1 = Inclusive
    string traceFile;

    filedata fileData;

    void read_file(){
        ifstream myfile(traceFile);
        int number_Lines = 0;
        string temp;
        string* fdata;
        if(!myfile){
            cout<<"Error: Can not open the output file"<<endl;
        } else {
            while (!myfile.eof()) {
                getline(myfile, temp);
                number_Lines++;
				//cout<<"number_Lines= "<<number_Lines<<endl;
				//cout<<temp.length()<<endl;
            }
            number_Lines--;
			//cout<<"number_Lines 2= "<<number_Lines<<endl;
            fdata = new string[number_Lines + 1];
			//cout<<"fdata= "<<fdata<<endl;
			//cout<<"traceFile= "<<traceFile<<endl;
            ifstream newfile(traceFile);
            int count = 0;
            while (!newfile.eof()) {
                getline(newfile, temp);
				if (temp.length()!=0)
				{
				//cout<<"Check2 + count = "<<count<<endl;
                fdata[count] = temp;
                //cout<< count<<" + " << temp << endl;
				//cout<<fdata[count]<<endl;
                count++;
				}
            }
			
			//cout<<"Count = "<<count<<"; numLines = "<<number_Lines<<endl;
            fileData = {number_Lines, new bool[number_Lines], new string[number_Lines]};
            for (int m = 0; m < number_Lines; m++) {
				//cout<<"m= "<<m<<endl;
                if (fdata[m][0] == 'r') {
                    fileData.opr[m] = 0;
                    //cout<<"R + "<<m<<endl;
                } else{
                    fileData.opr[m] = 1;
                    //cout<<"W + "<<m<<endl;
                }
				//cout<<"Check before substring, m = "<<m<<" string = "<<fdata[m]<<endl;
                fileData.address_vector[m] = fdata[m].substr(2, fdata[m].length());
				//cout<<"Check after substring, m = "<<m<<" string = "<<fileData.address_vector[m]<<endl;
            }
        }
		//cout<<fileData.number_Lines<<endl;
        //for(int i=0; i<fileData.number_Lines; i++){
        //    cout<< i << " " << fileData.opr[i] << " " << fileData.address_vector[i]<< endl;
       //}

    }

Simulator(int blockSize_, int L1_size_, int l1_Associativity_, int L2_size_, int l2_Associativity_, int replacement_Policy_, bool inclusion_Policy_, string traceFile_)
{		blockSize = blockSize_;
        L1_size = L1_size_;
        l1_Associativity = l1_Associativity_;
        L2_size = L2_size_;
        l2_Associativity = l2_Associativity_;
        replacement_Policy = replacement_Policy_;
        inclusion_Policy = inclusion_Policy_;
        traceFile = traceFile_;
        read_file();//Reading from the file

        if (L2_size == 0){
            L1 = new Cache(blockSize, L1_size, l1_Associativity, replacement_Policy, inclusion_Policy, fileData);
            //cout<<"L1 "<<L1<<endl;
			L2 = new Cache(32, 256, 2, replacement_Policy, inclusion_Policy, fileData);
			//cout<<"L2 "<<L2<<endl;
			
        } else{
            L1 = new Cache(blockSize, L1_size, l1_Associativity, replacement_Policy, inclusion_Policy, fileData);
            //cout<<"L1 "<<L1<<endl;
			L2 = new Cache(blockSize, L2_size, l2_Associativity, replacement_Policy, inclusion_Policy, fileData);
			//cout<<"L2 "<<L2<<endl;
        }
 }
void for_L2_0(){
		
        r_w_Return r;
        //cout<<"Check"<<endl;
        for(int m=0; m<fileData.number_Lines; m++){
        //	cout<<"Check before, m = "<<m<<endl;
        //cout<<"accessData = "<<fileData.address_vector[m]<<endl;
            r = L1->accessData(fileData.address_vector[m], fileData.opr[m], m);
         //   cout<<"Check after, m = "<<m<<endl;
        }
    }
void printout_Everything(){
        cout << "===== Simulator configuration =====" << endl;
        cout << "BLOCKSIZE: \t\t\t\t" << blockSize << endl;
        cout << "L1_SIZE: \t\t\t\t" << L1_size << endl;
        cout << "L1_ASSOC: \t\t\t\t" << l1_Associativity << endl;
        cout << "L2_SIZE: \t\t\t\t" << L2_size << endl;
        cout << "L2_ASSOC: \t\t\t\t" << l2_Associativity << endl;
        cout << "REPLACEMENT POLICY: \t";
        if (replacement_Policy == 0) cout<< "LRU" << endl;
        else if (replacement_Policy == 1) cout<< "Pseudo-LRU" << endl;
        else if (replacement_Policy == 2) cout<< "optimal" << endl;

        cout << "INCLUSION PROPERTY: \t";
        if (inclusion_Policy == 0) cout<< "non-inclusive" << endl;
        else cout<< "inclusive" << endl;

        cout << "trace_file: \t\t\t" << traceFile << endl;
        cout << "===== L1 contents =====" << endl;
        L1->printout_Everything();

        if (L2_size != 0){
            cout << "===== L2 contents =====" << endl;
            L2->printout_Everything();
        }

        cout << "===== Simulation results (raw) =====" << endl;
        cout << "a. number of L1 reads: \t\t\t"<< L1->s.read_Count << endl;
        cout << "b. number of L1 read misses: \t"<< L1->s.read_Miss_Count << endl;
        cout << "c. number of L1 writes: \t\t"<< L1->s.write_Count << endl;
        cout << "d. number of L1 write misses: \t"<< L1->s.write_Miss_Count << endl;
        // cout << "e. L1 miss rate: \t\t\t\t"<< float(L1->s.read_Miss_Count + L1->s.write_Miss_Count)/float(L1->s.read_Count + L1->s.write_Count) << endl;
        cout << "e. L1 miss rate: \t\t\t\t"<< std::fixed << std::setprecision(6) << float(L1->s.read_Miss_Count + L1->s.write_Miss_Count)/float(L1->s.read_Count + L1->s.write_Count) << endl;
        cout << "f. number of L1 writebacks: \t"<< L1->s.write_Back_Count << endl;
        cout << "g. number of L2 reads: \t\t\t"<< L2->s.read_Count << endl;
        cout << "h. number of L2 read misses: \t"<< L2->s.read_Miss_Count << endl;
        cout << "i. number of L2 writes: \t\t"<< L2->s.write_Count << endl;
        cout << "j. number of L2 write misses: \t"<< L2->s.write_Miss_Count << endl;
        // if (L2_size != 0) cout << "k. L2 miss rate: \t\t\t\t"<< float(L2->s.read_Miss_Count)/float(L2->s.read_Count) << endl;
        if (L2_size != 0) cout << "k. L2 miss rate: \t\t\t\t" << std::fixed << std::setprecision(6) << float(L2->s.read_Miss_Count)/float(L2->s.read_Count) << endl;
        else cout << "k. L2 miss rate: \t\t\t\t"<< 0 << endl;
        cout << "l. number of L2 writebacks: \t"<< L2->s.write_Back_Count << endl;
        if (L2_size != 0) cout << "m. total memory traffic: \t\t"<< L2->s.read_Miss_Count + L2->s.write_Miss_Count + L2->s.write_Back_Count + L1->s.mem_write_Back_Count << endl;
        else cout << "m. total memory traffic: \t\t"<< L1->s.read_Miss_Count + L1->s.write_Miss_Count + L1->s.write_Back_Count << endl;
    }

void inclusive_Simulator(){
        r_w_Return rL1;
        r_w_Return rL2;
        for(int m=0; m<fileData.number_Lines; m++){
			//cout<<"m "<<m<<endl;
            rL1 = L1->accessData(fileData.address_vector[m], fileData.opr[m], m);
			//cout<<"rL1 "<<rL1<<endl;
            if (rL1.victim.isItDirty == 1){
                L2->accessData(rL1.victim.addr, 1, m);
            }
            if (rL1.is_It_Hit == 0){
                rL2 = L2->accessData(fileData.address_vector[m], 0, m);
                if (rL2.victim.addr.length() != 0){
                    L1->nullify(rL2.victim.addr);
                }
            }
        }
    }
	
void non_Inclusive_Simulator(){
        r_w_Return r;
        for(int m=0; m<fileData.number_Lines; m++){
			//cout<<"m "<<m<<endl;
            r = L1->accessData(fileData.address_vector[m], fileData.opr[m], m);
			//cout<<"r "<<r<<endl;
            if (r.victim.isItDirty == 1){
                L2->accessData(r.victim.addr, 1, m);
            }
            if (r.is_It_Hit == 0){
                L2->accessData(fileData.address_vector[m], 0, m);
            }
        }
    }

void run(){

        if (L2_size == 0){
        	//cout<<"Check"<<endl;
            for_L2_0();
        } else{
            if (inclusion_Policy == 0)
                non_Inclusive_Simulator();
            else
                inclusive_Simulator();
        }

        printout_Everything();
    }
};

int main(int argc, char** argv) {
Simulator s( atoi(argv[1]), atoi(argv[2]), atoi(argv[3]), atoi(argv[4]), atoi(argv[5]), atoi(argv[6]), atoi(argv[7]), argv[8]);
   s.run();
//Simulator s(16, 1024, 2, 8192, 4, 0, 0, gcc_trace.txt);
//Simulator s(16, 1024, 1, 8192, 4, 0, 0, go_trace.txt);
//Simulator s(16, 1024, 2, 8192, 4, 0, 1, gcc_trace.txt);
//Simulator s(16, 1024, 2, 0, 0, 0, 0, gcc_trace.txt);
//Simulator s(16, 1024, 1, 0, 0, 0, 0, perl_trace.txt);
//Simulator s(16, 1024, 2, 0, 0, 1, 0, gcc_trace.txt);
//Simulator s(16, 1024, 2, 0, 0, 2, 0, vortex_trace.txt);
   return 0;

    // cout << "Received =  " << argc 
    //      << " Arguments:" << "\n"; 
  
    // for (int i = 0; i < argc; ++i) 
    //     cout << argv[i] << "\n"; 
  
    // return 0; 

}
