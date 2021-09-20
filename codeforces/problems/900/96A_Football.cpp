#include <bits/stdc++.h>

using namespace std;

string solve(string N){
    // solution comes here
        
     
    int count = 7;
    string output = "NO";
    char last = 'n';
    for(char const &c: N){ 
        if(last == '1' && c == '1'){
            --count;
        }else if(last == '0' && c == '0'){
            --count;
        } else{
            count = 6;
        }

        last = c;
        if(!count){
            output = "YES";
            break;
        }

    }
    
    return output;
}

int main() {
    ios_base::sync_with_stdio(0);


    string N;
    cin >> N;
    
    string isDangerous;
    isDangerous = solve(N);

    printf("%s\n", isDangerous.c_str());
    return 0;
}

