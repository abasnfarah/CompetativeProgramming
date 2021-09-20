#include <bits/stdc++.h>

using namespace std;

void printArr(vector<int> arr){
    for(int &i: arr){
        cout << i << ", ";
    }
    cout << endl;
} 

void solve(int n, int m, vector<int> arr){
    // solution comes here

    sort(arr.begin(), arr.end());
    //printArr(arr);
    //printf("we made it here: %lu\n",arr.size());
    int total = 0;

    for(int i; i < (int) arr.size() && i < m; ++i){
        //printf("total: %d, i: %d\n", total, i);
        if(arr[i] > 0)
            break;
        total += arr[i];
    }

    printf("%d\n", (total * -1));
}

int main() {
    ios_base::sync_with_stdio(0);
    int n, m;
    vector<int> arr;
    

    //scanf("%d %d", &n, &m);
    cin >> n >> m;
    //printf("%d %d\n", n, m);

    int x;
    while(cin >> x){
        arr.push_back(x);
    }
    solve(n, m, arr);
    return 0;
}

