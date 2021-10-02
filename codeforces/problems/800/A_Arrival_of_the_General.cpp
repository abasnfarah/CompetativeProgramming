#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll; 
typedef pair<int, int> pii;
typedef vector<ll> vll;
typedef vector<pll> vpll;
typedef unordered_map<ll,ll> umap;
#define loop(i, a, b) for(ll i=a;i<b;i++)
#define For(i, n) for(int i=0;i<(ll)n;i++)
#define Rev(i, n) for(int i=n;i>=0;i--)
#define Rep(i, n) for(int i=1;i<=n;++i)
#define all(v) (v).begin(),(v).end()
#define mems(x, y) memset(x, y, sizeof(x))
#define sz(v) (v).size()
#define F first
#define S second
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define pf(n) cout<<n<<"\n"
#define pff(n) cout<<n<<" "
#define ar array
#define mei(v) std::max_element((v).begin(),(v).end()) - (v).begin() ;
#define me(v) *std::max_element((v).begin(),(v).end());
#define nei(v) std::min_element((v).begin(),(v).end()) - (v).begin() ;
#define ne(v) *std::min_element((v).begin(),(v).end());
#define case(i) cout<<"Case #"<<i<<": "
#define tolower(s) transform(s.begin(),s.end(),s.begin,::tolower);
#define toupper(s) transform(s.begin(),s.end(),s.begin,::toupper);
ll max(ll a, ll b){ return a > b ? a : b; }
ll min(ll a, ll b){ return a < b ? a : b; }
#define debug(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }

void err(istream_iterator<string> it) {}
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
	cerr << *it << " = " << a << endl;
	err(++it, args...);
}
//const ll inf = 1e16;
const ll inf = numeric_limits<ll>::max();

void pv(vll arr){
    printf("Array size: %lu\n", arr.size());
    printf("[");
    for(ll val: arr){
        printf("%lld ", val);
    }
    printf("]\n");
}

void solve(int N){
    // solution comes here
    vll arr;
    while(N--){
        ll val;
        scanf("%lld", &val); 
        arr.push_back(val);
    }

    //pv(arr);
    //for(auto v: arr){
        //debug(v);
    //}
    
    ll m = mei(arr);
    ll n = nei(arr);
    if(arr[n] == arr.back() && arr[m] == arr[0]){
        pf(0);
        return;
    }
    Rev(l, m-1){
        if(arr[l] == arr[m]){
            //pf(l);
            m = l;
        }
    }
    ll count = 0;

    // swap left 
    for(ll i = m; i > 0; i--){
        ll t = arr[i-1];
        ll tt = arr[i];
        arr[i] = t;
        arr[i-1] = tt;
        count++;
    }
    //pff(count) << " - Count\n";
    n = nei(arr);
    loop(i, n, arr.size()){
        if(arr[i] == arr[n]){
            n = i;
        }
    }
    // swap right
    for(ll i = n; i < arr.size() - 1; i++){
        ll t = arr[i+1];
        ll tt = arr[i];
        arr[i] = t;
        arr[i+1] = tt;
        count++;
    }
    //pff(count) << " - Count\n";
    //printf("max: %lld, min: %lld\n", m, n);

    printf("%lld\n", count);

}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll N;

    scanf("%lld", &N);

    solve(N);
    return 0;
}

