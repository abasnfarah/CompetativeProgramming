#include "/Users/abasfarah/workspaces/competativeProgramming/stdc++.h"

using namespace std;

void solve(int a, int b, int c, int m){
    // solution comes here
    vector<int> arr = {a,b,c};
    sort(arr.begin(), arr.end());
    int mn = max(0, arr[2]-arr[1]-arr[0]-1);
    int mx = (a-1) + (b-1) + (c-1); 

    //printf("min: %d - ", minDiff);
    if(m >= mn && m <= mx){
        printf("YES\n");
        return;
    }
    printf("NO\n");
}

int main() {
    ios_base::sync_with_stdio(0);
    int N;

    scanf("%d", &N);

    while(N){
        int a, b, c, m; 
        scanf("%d %d %d %d", &a, &b, &c, &m);
        solve(a,b,c,m);
        --N;
    }
    return 0;
}

