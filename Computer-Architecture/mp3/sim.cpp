#include <fstream>
#include <map>
#include <stdlib.h>
#include <string>
#include <stack>
#include <algorithm>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define regFileLength 128
#define SYSERR 1

int cycCount=0,insCount=0;   
enum insEnum {IF,ID,IS,EX,WB}; //Defined 5 stages according to 6.1 
class insM
{
    public:
    int tag, pc, oprType,source1,source2,desti;
    int src1Tag=-1,src2Tag=-1,ifStart=0,ifDuration=0,idStart=0,idDuration=0;
    int isStart=0,isDuration=0, exStart=0,exDuration=0,wbStart=0,wbDuration=0;
	insEnum currStage;
};
class Scheduler
{
    int n,s,lineNo=0,queueSizeDispatch,regFile[128];
    string traceFile; 
	bool reachEOF=false;
	map<int,int> insLatency={{0,1},{1,2},{2,5},{3,5},{8,10}, {5,20}, {10,20}};
    ifstream infile;
    map<int,insM*> fakeROB;
    vector<int> listDispatch, listIssue;
    vector<pair<int,int>> listExecute;
    vector<insM*> insRetired;
	
    bool Advance_Cycle(){
    //cout<<"inside AdvanceCycle\n";
    bool exContinue=true;
	auto it=insRetired.begin();
    if(reachEOF && fakeROB.empty()) exContinue=false; //if fake-ROB is empty AND the trace is depleted
    cycCount++;    
	while(it!=insRetired.end())
	{ cout<<(*it)->tag <<" fu{"<<(*it)->oprType<<"} src{"<<(*it)->source1<<","<<(*it)->source2<<"} dst{"<<(*it)->desti
      <<"} IF{"<<(*it)->ifStart<<","<<(*it)->ifDuration<<"} ID{"<<(*it)->idStart<<","<<(*it)->idDuration<<"} IS{"<<(*it)->isStart<<","<<(*it)->isDuration<<"} EX{"<<(*it)->exStart<<","<<(*it)->exDuration
      <<"} WB{"<<(*it)->wbStart<<","<<(*it)->wbDuration<<"}\n";
        delete *it;
		++it;
	}
    return exContinue; //returns “false” to terminate the loop
}
	
	
    public:
    
    Scheduler(int argumS, int argumN, string argumTraceFile){
    s=argumS;
    n=argumN;
	int a=0;
	string instruction;
    queueSizeDispatch=2*n;  
	
	while (a<regFileLength)
	{ regFile[a]=-1;
			a++;
	}
    traceFile=argumTraceFile;
    infile.open(traceFile);
    if(!infile.is_open()){
        cerr<<"Unable to open "<<traceFile<<"!!!";
        return;
    }
    
    do
    {//Calling the functions as instructed in 6.4
        FakeRetire();
        Execute();
        Issue();
        Dispatch();
        Fetch();
    }while(Advance_Cycle());
}
	
	
    void FakeRetire(){
    //cout<<"inside FakeRetire\n";
    insRetired.clear();
	auto it=fakeROB.begin();
    stack<map<int,insM*>::iterator> listRetire; 
	// Removing instructions from top of the fake-ROB
 
	while(fakeROB.size()!=0 && it->second->currStage==WB)
	{
		insRetired.push_back(it->second);
        it->second->wbDuration=1;
        listRetire.push(it);
		it++;
	}
    while(!listRetire.empty())
    {
        fakeROB.erase(listRetire.top());
        listRetire.pop();
    }
}
    void Execute(){
    stack<int> listComplete;
	unsigned int a=0;
   
	while(a<listExecute.size())
	{
		listExecute[a].second--;  
        if(listExecute[a].second==0) //check for instructions that are finishing the execution this cycle
        { 
            listComplete.push(a); //Remove the instruction from the execute_list
        }  
		a++;
	}
	
	for (;!listComplete.empty();)
	{
		int index = listComplete.top();
		fakeROB[listExecute[index].first]->wbStart=cycCount;
		int tag = fakeROB[listExecute[index].first]->tag;
		auto it=fakeROB.begin();
		fakeROB[listExecute[index].first]->exDuration=cycCount-fakeROB[listExecute[index].first]->exStart;
        fakeROB[listExecute[index].first]->currStage=WB; // Transition from EX state to WB state.       
       regFile[fakeROB[listExecute[index].first]->desti]==tag ? regFile[fakeROB[listExecute[index].first]->desti]=-1 : a=1 ;
		
		while(it!=fakeROB.end())
		{
			it->second->src2Tag==tag ? it->second->src2Tag=-1 : a=1 ;
			it->second->src1Tag==tag ? it->second->src1Tag=-1 : a=1;
			it++;
		}
        listExecute.erase(listExecute.begin()+index);
        listComplete.pop();
	}
    
}
	
    void Issue(){
    unsigned int freeSlot= n, a=0;
    stack<int> listReady;
   stack<int> listReadyOrdered;
	while (a<listIssue.size())
	{
		if((fakeROB[listIssue[a]]->src1Tag==-1 || fakeROB[listIssue[a]]->source1==-1) && (fakeROB[listIssue[a]]->src2Tag==-1 || fakeROB[listIssue[a]]->src2Tag==-1))
        { 
            if(listReady.size()<freeSlot)
            { 
                listReady.push(a);
            }
            else
            { 
                break;
            }            
        }
		a++;
	}
    
    for (;!listReady.empty();)
    { 
        int index=listReady.top();
		listReadyOrdered.push(listIssue[index]);  
		listReady.pop();
        listIssue.erase(listIssue.begin()+index);
        
    }
    for (;!listReadyOrdered.empty();)
    { int latency;
      int tag=listReadyOrdered.top();
      listReadyOrdered.pop();
	  fakeROB[tag]->isDuration=cycCount-fakeROB[tag]->isStart;	
	  fakeROB[tag]->exStart=cycCount;
      fakeROB[tag]->currStage=EX; //Transition from the IS state to the EX state.
    fakeROB[tag]->oprType==2 ? latency=insLatency[fakeROB[tag]->oprType] : latency=insLatency[fakeROB[tag]->oprType];	
    listExecute.push_back(pair<int,int>(tag,latency)); //Remove the instruction from the issue_list and add it to the execute_list
	}

}
    void Dispatch(){
    
    unsigned int freeSlotSL= s-listIssue.size();
    int recsRemoveCount=0,c;
	unsigned int a=0,b=0;
	while (a<freeSlotSL && a<listDispatch.size())
	{
		if(fakeROB[listDispatch[a]]->currStage==ID)
        {
            recsRemoveCount++;
            fakeROB[listDispatch[a]]->currStage=IS; //Transition from the ID state to the IS state
			fakeROB[listDispatch[a]]->source1!=-1 ? fakeROB[listDispatch[a]]->src1Tag=regFile[fakeROB[listDispatch[a]]->source1] : c=0 ;
			fakeROB[listDispatch[a]]->source2!=-1 ? fakeROB[listDispatch[a]]->src2Tag=regFile[fakeROB[listDispatch[a]]->source2] : c=0 ;
			fakeROB[listDispatch[a]]->desti!=-1 ? regFile[fakeROB[listDispatch[a]]->desti]=fakeROB[listDispatch[a]]->tag : c=0 ;		
            fakeROB[listDispatch[a]]->idDuration=cycCount-fakeROB[listDispatch[a]]->idStart;
			fakeROB[listDispatch[a]]->isStart=cycCount;
            listIssue.push_back(listDispatch[a]);
        }
	a++;
	}
    while (recsRemoveCount!=0)
    {
        listDispatch.erase(listDispatch.begin());
        recsRemoveCount--;
    }   
    
	while (b<listDispatch.size())
	{
		
		fakeROB[listDispatch[b]]->currStage==IF ? (fakeROB[listDispatch[b]]->currStage=ID,fakeROB[listDispatch[b]]->idStart=cycCount,
		fakeROB[listDispatch[b]]->ifDuration=cycCount-fakeROB[listDispatch[b]]->ifStart) : c=0 ;
		++b;
	}
	
}

    void Fetch(){
	int a=0;
    int recordFetch=min(n,(int)(queueSizeDispatch-listDispatch.size()));
    string instruction="";
    
	while (a<recordFetch)
	{
		getline(infile,instruction); 
        if(instruction!="")
        {
            vector<string> split;
            string seg="";
            for(unsigned int b=0;b<instruction.length();b++)
            {
                if(instruction[b]==' ')
                {
                    split.push_back(seg);
                    seg="";
                }
                else
                {
                    seg.push_back(instruction[b]);
                } 	
            } 
            split.push_back(seg);
            insM* present=new insM();
            present->tag = lineNo++;
			present->oprType = stoi(split[1]);
			present->desti = stoi(split[2]);
			present->source2 = stoi(split[4]);
			present->source1 = stoi(split[3]);
            present->pc = stoi(split[0],nullptr,16);
            present->ifStart = cycCount;
            present->currStage = IF;
            fakeROB.insert(pair<int,insM*>(present->tag,present));
            listDispatch.push_back(present->tag);
			insCount++;
        }
        else
        {
            reachEOF=true;
        }  
		a++;
	} } };


int main(int argc, char* argv[])
{
int s = atoi(argv[1]), n = atoi(argv[2]); 
string traceFile = argv[3];	
Scheduler sched(s,n,traceFile);
cout<<"number of instructions = "<<insCount<<"\n";
cout<<"number of cycles       = "<<cycCount-1<<"\n";
printf("IPC                    = %0.5f\n",float(insCount)/float(cycCount-1));
}