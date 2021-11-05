#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<pll> vpll;
typedef unordered_map<ll,ll> umap;
typedef set<ll> uset;
template<typename T, typename S> ostream &operator << (ostream &os, const pair<T, S> &p) {return os << "(" << p.first << ", " << p.second << ")";}
template <typename T> ostream &operator << (ostream &os, const vector<T> &v){os << "[";for (ll i = 0; i < v.size(); ++i) {os << v[i];if (i != v.size() - 1)os << ", ";}os << "]\n";return os;}
template <typename T> ostream &operator << (ostream &os, const set<T> &v){os << "{";for (auto it : v) {os << it;if (it != *v.rbegin())os << ", ";}os << "}\n";return os;}
template <typename T> ostream &operator << (ostream &os, const unordered_set<T> &v){os << "{";for (auto it : v) {os << it;if (it != *v.rbegin())os << ", ";}os << "}\n";return os;}
template <typename T, typename S> ostream &operator<<(ostream &os, const map<T, S> &v) { os << "{ \n"; for (auto it : v) os << it.first << " : " << it.second << "\n"; os << " }\n"; return os;}
template <typename T, typename S> ostream &operator<<(ostream &os, const unordered_map<T, S> &v) { os << "{ \n"; for (auto it : v) os << it.first << " : " << it.second << "\n"; os << " }\n"; return os;}
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
#define gl(str, buff) fgets(str, buff, stdin)
#define ar array
#define mei(v) std::max_element((v).begin(),(v).end()) - (v).begin() 
#define me(v) *std::max_element((v).begin(),(v).end())
#define nei(v) std::min_element((v).begin(),(v).end()) - (v).begin() 
#define ne(v) *std::min_element((v).begin(),(v).end())
#define sum(v) accumulate(all(v), 0)
#define case(i) cout<<"Case #"<<i<<": "
#define tolower(s) transform(s.begin(),s.end(),s.begin(),[](unsigned char c){ return std::tolower(c); })
#define toupper(s) transform(s.begin(),s.end(),s.begin(),[](unsigned char c){ return std::tolower(c); })
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

void solve(string s, ll T, ll N, ll D, ll C, ll M){
    // solution comes here
    //debug(N,D,C,M,s);
    // 6 10 4 0
    // CCDCDD
    ll nd = 0, nc = 0;
    for(auto c: s){
        if(c == 'D')
            nd++;
        if(c == 'C')
            nc++;
    }

    for(auto c: s){
        debug(C,D,nd)
        if(c == 'D'){
            if(D == 0){
                case(T) << "NO"<< endl;
                return;
            }
            D--;
            nd--;
            C += M;
            
        }else if( c == 'C'){
            if(C == 0){
                if(nd != 0){
                    case(T) << "NO"<< endl;
                    return;
                }
                break;
            }
            C--;
            nc--;
        }
    }

    case(T) << "YES" <<endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll T;
    ll t = 1;

    scanf("%lld", &T);

    while(T){
        ll N, D, C, M;
        scanf("%lld %lld %lld %lld", &N, &D, &C, &M);
        char temp[N];
        //gl(temp,(int) N-1);
        scanf("%s", temp);
        string s = temp;
        solve(s, t, N, D, C, M);
        ++t;
        --T;
    }
    return 0;
}
