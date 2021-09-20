#include "/Users/abasfarah/workspaces/competativeProgramming/stdc++.h"

using namespace std;

bool findIsPossible(string s){

    unordered_set<char> set;
    for(char &c: s){
        set.insert(c);
    }
    bool output;

    if(set.size() >= (s.size()/2 + 1)){
        output = true;
    }else {
        output = false;
    }
    cout << endl;

    return output;
}

void solve(int N, string s){
    // solution comes here
    
    string S = s;
    bool isPossible = findIsPossible(s);
    
    if(!isPossible){
        printf("Case #%d: IMPOSSIBLE\n", N);
        return;
    }
    
    unordered_set<int> avaliableSet;
    unordered_map<char, vector<int>> excludedMap;

    // Build our map and set
    for(int i; i < (int) s.size(); ++i){
        printf("%c\n", s[i]);
        char c = s[i];
        avaliableSet.insert(c);
        if(excludedMap.count(c)){
            excludedMap[c].push_back(i);
        }else {
            vector<int> n;
            excludedMap.insert(pair<char , vector<int>> (c, vector<int>()));
        }
    }

    for(auto x: excludedMap){
        // find available value - add it to our string output remove from set 
        
    }

    printf("%lu, %lu\n", avaliableSet.size(), excludedMap.size());

    printf("Case #%d: \n", N);
}

int main() {
    ios_base::sync_with_stdio(0);
    int N;
    int count = 1;

    scanf("%d", &N);
    
    while(N){
        char s[8];
        scanf("%s", s); 
        printf("%s\n", s);
        string S(s);
        solve(count, S);
        ++count;
        --N;
    }
    return 0;
}

