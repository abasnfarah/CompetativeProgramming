#include <bits/stdc++.h>
//#include <boost/algorithm/string/join.hpp>

using namespace std;

vector<string> values;

void backtrack(int left, int right, string curr, int n){
    if ((int) values.size() == (n)){
        return;
    }
    if((int) curr.size() == (n * 2)){
            values.push_back(curr); 
            return;
    } 
    if (left < n){
        backtrack(left+1,right,curr+"(",n);

    }

    if (right <n){
        backtrack(left,right+1,curr+")",n);
    }

}

vector<string> solve(int n){
    values= vector<string>();
    backtrack(0,0,"",n);
    return values;
}

void printV(vector<string> arr){

    for(auto s: arr){
        printf("%s\n", s.c_str());
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    int N;

    scanf("%d", &N);

    while(N){
        vector<string> solution;
        int n;
        scanf("%d", &n);
        solution = solve(n);
        printV(solution);
        --N;
    }
    return 0;
}

