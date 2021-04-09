#ifndef smith
#define smith

using namespace std;

int bits;
int smithcounter;
int mispredictioncount=0;
int predictioncount=0;

void Smith(int initial_value, int max_value, int current_reality){
	
	/* cout<<"current_reality= "<<current_reality<<endl;
	cout<<"initial_value= "<<initial_value<<endl;
    cout<<"max_value= "<<max_value<<endl; */
	int predicted;
	
//At first predict
    if (smithcounter>=initial_value) //at first predict taken
	{
		predicted=1; //taken
		//cout<<"smithcounter= "<< smithcounter<<endl;
        //cout<<"predicted "<< predicted<<endl;
        predictioncount+=1;
	}
    else
	{
        predicted=0; // #else predict not taken
		//cout<<"smithcounter= "<< smithcounter<<endl;
        //cout<<"predicted "<< predicted<<endl;
        predictioncount+=1;
	}
	//cout<<"current_reality= "<<current_reality<<endl;
    //Then update the counter
if (current_reality==1 && smithcounter<max_value)// #if taken, increment the counter
{
	smithcounter+=1;
}
else if (current_reality==1 && smithcounter==max_value)
{   smithcounter=max_value;
}
else if (current_reality==0 && smithcounter>0)// #if not_taken, decrement the counter
{
	smithcounter-=1;
}
else if (current_reality==0 && smithcounter==0)
{       smithcounter=0;
}
	
//check if predicted correctly 
	if (current_reality==predicted)
	{
		; //do nothing
        //cout<<"Predicted correctly !!"<<endl;
	}
    else if(current_reality!=predicted)
	{
		mispredictioncount+=1;
        //cout<<"---- Wrong ----"<<endl;
	}
        
	
	//cout<<"End smith counter= "<<smithcounter<<endl;
	//cout<<"Misprediction count= "<<mispredictioncount<<endl;
	//cout<<"Prediction count= "<< predictioncount<<endl<<endl;
 }
 
void displaySmith()
 {
	cout<< "OUTPUT" << endl;
    cout<< "number of predictions:" << "\t" << predictioncount << endl;
    cout<< "number of mispredictions:" << "\t" << mispredictioncount << endl;
    float temp = round(10000*float(mispredictioncount)/float(predictioncount));
    cout<< "misprediction rate:" << "\t" << std::fixed << std::setprecision(2) << float(temp)/100 << "%" << endl;
    cout<< "FINAL COUNTER CONTENT:\t" << smithcounter<<  endl;
	}

int SmithReadFile_and_predict(int bits, string Smith_trace_file){
	int count=0;
	int current_reality;
    //int number_Lines = 0;
	int prediction;
	int initial_value;
	int max_value;
	//cout<<"bits= "<<bits;
	initial_value=pow(2.0,float(bits))/2;
	max_value=pow(2.0,float(bits))-1;
	/* if (bits==1)
	{initial_value=1;
    max_value=1; //something is wrong here, for 1 bit
	}
    else if (bits==2)
	{ initial_value=2;
    max_value=3;}
	else if (bits==3)
	{  initial_value=4;
    max_value=7;}
	else if (bits==4)
	{
	initial_value=8;
    max_value=15;
	}
	else if (bits==5)
	{
	initial_value=16;
    max_value=31;
	}
	else if (bits==6)
	{
	initial_value=32;
    max_value=63;
	} */
    smithcounter=initial_value;
	string line;
  ifstream myfile (Smith_trace_file);
  
  //new
/* while (!myfile.eof()) {
                getline(myfile, line);
                //number_Lines+=1;
                count++;
				//cout<< "string(line.substr (7,1))= "<< string(line.substr (7,1))<<endl;;
	if (string(line.substr (7,1))=="t")
	{
		current_reality=1;
		Smith(initial_value,max_value, current_reality);
	}
	else
	{
		current_reality=0;
		Smith(initial_value,max_value, current_reality);
	}
	//cout<< "current_reality= "<< current_reality<<endl;;
    
	}
    //myfile.close();
             
		
//end new	 */	
			
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      //cout << "Line = "<<line << '\n';
	  count++;
	//cout<< "count= "<<count <<" temp= "<< temp << endl;
	//cout<<"line.substr (7,1)= "<<line.substr (7,1)<<endl;
	if (string(line.substr (7,1))=="t")
	{
		current_reality=1;
		Smith(initial_value,max_value, current_reality);
	}
	else
	{
		current_reality=0;
		Smith(initial_value,max_value, current_reality);
	}
	//cout<< "current_reality= "<< current_reality<<endl;;
    
	}
    myfile.close();
  } 
  
  else cout << "Unable to open file"; 
 

return 0;
}


#endif