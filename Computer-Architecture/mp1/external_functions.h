#ifndef external_functions
#define external_functions

using namespace std;
string reverse_String(string str);
int my_Infinite_Number = 99999999;
string reverse_String(string str)
{	int n = str.length();
    for (int i = 0; i < n / 2; i++)
		//cout<<"i= "<<i<<endl;
		//cout<<"str[i]= "<<str[i]<<endl;
		//cout<<"str[n-i-1]= "<<str[n-i-1]<<endl;
        swap(str[i], str[n - i - 1]);
    return str;
}

string bin_To_Hex(const string &s){
    string s_R = reverse_String(s);
    int string_Length = s.length();
    int r_M = 4 - string_Length%4;
    if (r_M < 4){
        for (int i = 0; i<r_M; i++){
			//cout<<"i= "<<i<<endl;
            s_R.append("0");
        }
    }
    s_R = reverse_String(s_R);
	//cout<<"s_R= "<<s_R<<endl;
    string out;
    for(uint i = 0; i < s_R.size(); i += 4){
        int8_t x = 0;
		//cout<<"i= "<<i<<endl;
        for(uint j = i; j < i + 4; ++j){
			//cout<<"j= "<<j<<endl;
            x <<= 1;
            if(s_R[j] == '1')
                x |= 1;
        }
        if(x<=9)
            out.push_back('0' + x);
        else
            out.push_back('a' + x - 10);
    }
    return out;
}

string hex_To_Bin(const string &s){
    //cout<<"Check"<<endl;
	string binary;
    for(auto a: s){
        uint8_t x;
        if(a <= '9' and a >= '0')
			//cout<<"a= "<<a<<endl;
            x = a - '0';
		//cout<<"x= "<<x<<endl;
        else
            x = 10 + a - 'a';
        for(int8_t b = 3; b >= 0; --b)
			//cout<<"b= "<<x<<endl;
            binary.push_back((x & (1<<b))? '1':'0');
    }
    return binary;
}


struct filedata{
    int number_Lines;
    bool* opr;
    string* address_vector;
};
struct final_Numbers{
    int read_Count;
    int read_Miss_Count;
    int write_Count;
    int write_Miss_Count;
    int write_Back_Count;
    int mem_write_Back_Count;
};


int matchAddress(const string& addr, filedata fileData, const int& itr) {
    for (int i = itr+1; i < fileData.number_Lines; i++) {
		//cout<<"i= "<<i<<endl;
        if (addr == fileData.address_vector[i]){
			//cout<<"fileData.address_vector[i]= "<<fileData.address_vector[i]<<endl;
            return i;
        }
    }
    return my_Infinite_Number;
}


#endif