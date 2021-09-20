#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;
int main() {
    // solution comes here
    int w;
    bool even = false;

    scanf("%d", &w);

    for(int i = 2; i < w; i+=2){
        int target = w - i;
        if(w % 2 == 0 && target % 2 == 0){
            even = true;
        }
    }

    if(even){
        printf("YES");
    }else{
        printf("NO");
    }

    return 0;
}


