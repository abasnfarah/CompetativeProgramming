#include <bits/stdc++.h>

using namespace std;

int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);

  // Code goes here

  vector<int> v = {4,2,5,3,5,8,3};
  sort(v.begin(), v.end());
  for (int i = 0; i < v.size(); i++){
    cout << v[i] << "\n";
  }

  sort(v.rbegin(), v.rend());
  for (int i = 0; i < v.size(); i++){
    cout << v[i] << "\n";
  }

  string m = "monkey";
  sort(m.begin(), m.end());
  for (int i = 0; i < m.size(); i++){
    cout << m[i] << "\n";
  }

}

