#include<stdio.h>
#include<queue>
#include<algorithm>
#include<cstring>
#define inf 999999

using namespace std;

int graph[101][101];

//상 우 하 좌
int dy[]={-1, 0, 1, 0};
int dx[]={0, 1, 0, -1};

void init() {
    memset(graph, 0, sizeof(graph));
}

int bfs(int n) {
    int ans=0;
    int dp[101][101];
    fill(&dp[0][0], &dp[100][101], inf);

    queue<pair<int, int> > pos;
    pos.push(make_pair(1,1));
    dp[1][1]=0;
    
    while(!pos.empty()) {
        int y= pos.front().first;
        int x=pos.front().second;
        pos.pop();
        
        
      
        
        for(int i=0;i<4;i++) {
            int ny=y+dy[i];
            int nx=x+dx[i];
            
            if(ny <1 || ny>n || nx<1 || nx>n)
                continue;
            else{
                
                if(dp[ny][nx] > dp[y][x]+graph[ny][nx]) {
                    
                    dp[ny][nx]=dp[y][x]+graph[ny][nx];
                    pos.push(make_pair(ny,nx));
                }
            }
        }

    }
    
    ans=dp[n][n];

    return ans;
}

int main()
{  
    
    freopen("supply_input.txt", "r", stdin);
    
    int T;
    scanf("%d", &T);

    for(int t=1;t<=T;t++) {
        init();
        int N;
        scanf("%d", &N);

        for(int i=1;i<=N;i++) {
            for(int j=1;j<=N;j++) {
                int num;
                scanf("%1d", &num);
                graph[i][j]=num;
            }
        }
        int ans=bfs(N);
        printf("#%d %d\n", t, ans);
    }

    return 0;
}