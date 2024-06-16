#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstring>

#define inf int(1e9)

typedef long long ll;
using namespace std;
vector<pair<ll, ll> > graph[200001];
ll d[200001];
ll parent[200001];

void init() {
    for(int i=0;i<200000;i++) {
        graph[i].clear();
        parent[i]=i;
    }
    
    fill(d, d+200001, inf);
}
ll getCost(int a, int b) {
    ll cost=0;

    for(int i=0;i<graph[a].size();i++) {
        if(graph[a][i].first==b)
            return graph[a][i].second;
    }
    return cost;
}


void dijkstra(ll start) {
    priority_queue<pair<ll, ll> > pq;

    pq.push(make_pair(0, start));
    d[start]=0;

    while(!pq.empty()) {
        ll dist=-pq.top().first;
        ll cur=pq.top().second;

        pq.pop();
        if(d[cur]< dist) 
            continue;
        
        for(ll i=0;i<graph[cur].size();i++) {
            ll cost=dist+graph[cur][i].second;
            
            if(cost<=d[graph[cur][i].first]) {
                
                if(parent[graph[cur][i].first]==graph[cur][i].first) {
                    // 부모가 자기자신
                    parent[graph[cur][i].first]=cur;
                }
                else {
                    ll costCur=getCost(graph[cur][i].first, cur);
                    ll costOri=getCost(graph[cur][i].first, parent[graph[cur][i].first]);

                    if(costOri>costCur)
                        parent[graph[cur][i].first]=cur;
                }
                d[graph[cur][i].first]=cost;
                pq.push(make_pair(-cost, graph[cur][i].first));
                
                
            }
        }
    }
    
    return;
}

ll sol(int n) {
    ll ans=0;
    
    

    for(int i=1;i<=n;i++){
        ans+=d[i];
        ans-=d[parent[i]];
    }



    return ans;
}

int main()
{
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // freopen("shortest_way_input.txt", "r", stdin);

    int T;
    cin>>T;

    for(int t=1;t<=T;t++) {
        init();
        ll n,m;
        cin>>n>>m;
        
        for(ll i=1;i<=m;i++) {
            ll a,b,c;
            cin>>a>>b>>c;

            graph[a].push_back(make_pair(b,c));
            graph[b].push_back(make_pair(a,c));
        }
        ll start=1;
        dijkstra(start);
        


        ll ans=sol(n);
        
            
        cout<<"#"<<t<<" "<< ans<<endl;

    }

    return 0;
}