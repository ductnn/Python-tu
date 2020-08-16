#include <bits/stdc++.h>
using namespace std;

void print(vector<string> f_names){
	for(int i=0; i<f_names.size(); i++){
        cout<<f_names[i]<< endl;
    }	    
	printf("\n");
}

bool mycomp(string a, string b){
	return a<b;
}

vector<string> alphabaticallySort(vector<string> a){
	int n=a.size();
	sort(a.begin(),a.end(),mycomp);
	return a;
}

vector<string> last_name(vector<string> a){
	int n=a.size();
	return a;
}

int main()
{   
	int n;
	cout <<"How many names do you want to enter? ";
	cin >> n;

	vector<string> f_names, l_names;
	string fname, lname;

	for(int i=0;i<n;i++){
        cout << "Enter name #" << i+1 << ":" << " ";
		cin>>lname>>fname;
		f_names.push_back(fname); 
        l_names.push_back(lname);
	}

	f_names = alphabaticallySort(f_names);
    l_names = last_name(l_names);

	cout <<"The name in order are: " << "\n";
	print(f_names);
	// print(f_names, l_names);
    // cout << ", ";
    // print(l_names);
	return 0;
}