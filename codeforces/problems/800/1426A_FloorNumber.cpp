#include <bits/stdc++.h>

using namespace std;

int solve(int N, int n, int x){
    // solution comes here
    // (1, 2)
    // ((floor-2)*x + 3) to ((floor - 1)*x + 2)
    // for each floor value upto (n+2)/x
    if (n < 3){
        return 1;
    }

    int maxFloor = 1000;
    int floor = 1;
    for(int i = 2; i <= maxFloor; ++i){
        int least = ((i-2)*x +3); // 6 
        int max = ((i-1)*x + 2); // 8
        if((least <= n) && (max >= n)){
            floor = i;
        }  
    }
    //printf("values %d %d: \n", n, x);
    return floor;
}

int main() {
    ios_base::sync_with_stdio(0);
    int N;

    scanf("%d", &N);

    while(N){
        int n, x;
        scanf("%d %d", &n, &x);
        int floor = solve(N, n, x);
        printf("%d\n", floor);
        --N;
    }
}

