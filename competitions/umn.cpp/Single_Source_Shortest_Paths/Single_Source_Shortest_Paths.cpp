#include <bits/stdc++.h>
#include "unordered_set"
#include "unordered_map"

using namespace std;

vector< pair<int,int> > graph[10000];
unordered_map<int, int> distance;


void djikstra(int end, int s){
  priority_queue< pair<int, int> > frontier;

  unordered_set<int> visited;

  frontier.push(make_pair(0,s));
  distance[s] = 0;

  while(!frontier.empty()){
    int d = frontier.top().first;
    int curr = frontier.top().second;
    frontier.pop();

    if(visited.count(curr)) continue;

    visited.insert(curr);
    distance[curr] = -1*d;
    //cout << "curr: " << curr << " Disance: "<< distance[curr] << endl;

    if( curr == end) break;

    for(int i = 0; i < graph[curr].size(); i++){       
      int w = graph[curr][i].first; 
      int b = graph[curr][i].second;
      //cout << w<< " -- " << d << endl;

      frontier.push(make_pair(-1*(w+(-1*d)), b));
    }
    
  }
  if(!distance.count(end)){
    distance[end] = -1;
  }

  
}

int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);

  // Code goes here

  int v, e, q, s;

  cin >> v >> e >> q >> s;
  //cout<< v << " " << e << " " << q << " " << s << endl;

  // building graph

  int n1, n2, w;

  for(int i = 0; i < e; i++){
    cin >> n1 >> n2 >> w;
    graph[n1].push_back(make_pair(w,n2));
  }

  for(int i = 0; i < q; i++){
    int query;
    cin >> query; 
    int value = djikstra(graph, query, s);
    if(value == -1){
      cout<< "IMPOSSIBLE" << "\n";
      cout<< "\n";
    } else {
      cout << djikstra(graph, query , s) << "\n";
      cout<< "\n";
    }
  }

  return 1;
}

