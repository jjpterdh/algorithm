#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<cmath>
#include<queue>

typedef long long ll;
using namespace std;



vector<pair<ll, pair<ll, ll> > > graph;
ll parent[1001];
ll xpos[1001];
ll ypos[1001];

void init() {
    for(int i=0;i<1001;i++) {
        parent[i]=i;
        
    }
    
    graph.clear();
    memset(xpos, 0, sizeof(xpos));
    memset(ypos, 0, sizeof(ypos));
}

ll find(ll x) {
    
    if(parent[x]==x)
        return x;
    return parent[x]=find(parent[x]);

}

void merge(ll x, ll y) {
    x=find(x);
    y=find(y);
    if(x==y)
        return;
    
    parent[y]=x;
}

ll dist(ll a, ll b) {
    ll dis=0;
    dis=pow((xpos[a]-xpos[b]), 2) + pow((ypos[a]-ypos[b]), 2);
    

    return dis;
}

bool checkParent(ll a, ll b) {
    a=find(a);
    b=find(b);
    if(a==b)
        return true;
    return false;

}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout<<fixed;
    cout.precision(0);
    freopen("re_sample_input.txt", "r", stdin);
    int T;
    cin>>T;

    for(int t=1;t<=T;t++) {
        init();
        ll N;
        cin>>N;

        for(ll n=1;n<=N;n++) {
            // x input
            cin>>xpos[n];

        }
        for(ll n=1;n<=N;n++) {
            // y input
            cin>>ypos[n];

        }
        double e;
        cin>>e;

        double total=0;
        

        for(ll n=1;n<=N;n++) {
            for(ll k=n+1;k<=N;k++) {
                ll dis=dist(n, k);
                graph.push_back(make_pair(dis, make_pair(n,k)));
            }
        }

        sort(graph.begin(), graph.end());
        for(ll i=0;i<graph.size();i++) {
            if(!checkParent(graph[i].second.first, graph[i].second.second)) {
                
                merge(graph[i].second.first, graph[i].second.second);
                total+=graph[i].first*e;
            }
        }


        
        cout<<"#"<<t<<" "<< total <<endl;


    }

    return 0;
}