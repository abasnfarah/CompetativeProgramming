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
#define mei(v) std::max_element((v).begin(),(v).end()) - (v).begin() 
#define me(v) *std::max_element((v).begin(),(v).end())
#define nei(v) std::min_element((v).begin(),(v).end()) - (v).begin() 
#define ne(v) *std::min_element((v).begin(),(v).end())
#define case(i) cout<<"Case #"<<i<<": "
#define tolower(s) transform(s.begin(),s.end(),s.begin,::tolower)
#define toupper(s) transform(s.begin(),s.end(),s.begin,::toupper)
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

void solve(ll N, ll H, vll v){
    // solution comes here

    ll output = 0;

    for(ll val: v){
        if(val > H){
            output+=2;
        }else{
            output++;
        }
    }
    pf(output);
}

int main() {
    ios_base::sync_with_stdio(0);
    ll N;
    ll H;

    scanf("%lld %lld", &N, &H);

    vll v;
    while(N){
        ll val;
        scanf("%lld", &val) ;
        v.pb(val);
        --N;
    }
    solve(N, H, v);
    return 0;
}

