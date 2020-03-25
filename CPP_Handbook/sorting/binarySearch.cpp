#include <bits/stdc++.h>

using namespace std;

int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);

  // Code goes here

  array<int,14> arr {1,2,3,4,5,6,6,7,7,7,7,9,10};
  int n = arr.size();

  // Binary Search - O(lgn) time
  int a = 0, b = n-1; 
  while(a <= b){
    int k = (a+b)/2;
    if(arr[k] == 8){
      cout << "Found it" << "\n";
      break;
    } 
    if(arr[k] > 8) b = k-1;
    else a = k + 1;
  }

  // Built in Binary Search - O(lgn)
  auto k = lower_bound(arr, arr+n, 7)-arr;
  if( k < n && arr[k] == 7){
    cout << "Found it again" << "\n";
  }

}

