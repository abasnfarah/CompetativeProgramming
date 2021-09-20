#include <bits/stdc++.h>

using namespace std;

void solve(int N, int n, int a, int b){
    // solution comes here
    // print a string of length n
    // each substring of length a has b distinct letters
    //printf("%d %d %d %d\n", N, n, a, b);

    int i = a;
    int j = b;
    string sv;
    while(n){
        sv.push_back(char('a') + char(j-1));
        --j;
        --i;
        if(!i){
            i = a;
            j = b;
        }else if (!j){
            j = b;
        }
        --n;
    }
    printf("%s\n", sv.c_str());
}

int main() {
    ios_base::sync_with_stdio(0);
    int N;

    scanf("%d", &N);

    int count = 1;
    while(N){
        int n, a, b;
        scanf("%d %d %d", &n, &a, &b);
        solve(count, n, a, b);
        --N;
        ++count;
    }
    return 0;
}

