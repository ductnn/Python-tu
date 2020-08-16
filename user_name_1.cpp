#include<iostream>
#include<string>

using namespace std;

int main(){
    int n;
	char str[20][20], t[20];

	cout << "How many names do you want to enter? ";
    cin >> n;

	for(int i=0; i<n; i++){
        cout << "Enter name #" << i+1 << ":" << " ";
		cin >> str[i];
	}

	for(int i=1; i<n; i++){
		for(j=1; j<n; j++){
			if(strcmp(str[j-1], str[j])>0){
				strcpy(t, str[j-1]);
				strcpy(str[j-1], str[j]);
				strcpy(str[j], t);
			}
		}
	}

	cout <<"The name in order are: " << "\n";

	for(int i=0; i<n; i++){
		cout << str[i] << "\n";
	}
	
    return 0;
}