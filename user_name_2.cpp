#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 109;

int n;
char s[N][N];
string s1;

// B illGates
// k = 0 Bien danh dau
// k ++ = 1// check 
// Bool check = T; a<b check=F 


void Xuly(int i) {
    for (int u = 0; u < s1.length(); u++) {
        if (s1[u] == ' ') {
            int k = 0;

            // lay chuoi dang sau
            for (int v = u+1; v < s1.length(); v++) {
                s[i][k++] = s1[v];
            }

            // lay chuoi dang truoc
            s[i][k++] = ','; s[i][k++] = ' ';
            for (int v = 0; s1[v] != ' '; v++) {
                s[i][k++] = s1[v];
            }
            break;
        }
    }
}

bool Compare(char s1[], char s2[] ) {
    int ok = 1;
    int k = min(strlen(s1), strlen(s2));
    
    if (strlen(s1) < strlen(s2)) {
        ok = 0;
    }
    for (int i = 0; i < k; i++) {
        if (s1[i] > s2[i]) {
            return 1;
        } else if (s1[i] < s2[i]) {
            return 0;
        }
    }
    return ok;
}


// sort chọn
void SortString() {
    for (int i = 0; i < n; i++) {
        for(int j = i+1; j < n; j++) {
            if (Compare(s[i], s[j]) ) {
                swap(s[i], s[j]);
            }
        }
    }
}

void Init() {
    cout << "How many names do you want to enter? ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Enter name #" << i+1 << ": ";
        string s2; cin >> s2;
        s1 = s2 + " "; cin >> s2;
        s1 += s2;
        Xuly(i);
    }
}

int main() {
    Init();
    cout << "The names in order are:" << endl;
    SortString();
    for (int i = 0; i < n; i++) {
        cout << s[i] << endl;
    }
    return 0;
}
