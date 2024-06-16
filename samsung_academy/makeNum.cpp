#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#define INF 99999
using namespace std;

priority_queue<pair<int, int>, vector<pair<int,int> >, greater<pair<int,int> > > pq;
vector<int> arr;

void init() {
    while(!pq.empty()){
        pq.pop();
    }

    arr.clear();
}

void sol() {

    while(pq.top().second) {
        
        pair<int, int> top=pq.top();
        pq.pop();
        pq.push(make_pair(top.first+top.second, 0));
        for(int i=0;i<arr.size();i++){
            pq.push(make_pair(top.first+top.second%arr[i], top.second/arr[i]));
        }

        
    }

    
    
    

}

int main()
{   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    freopen("makeNum_input.txt", "r", stdin);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++){

        init();
        int N, K;
        int x=0;
        int D=1;
        cin>>N;
        
        for(int n=0;n<N;n++){
            int num;
            cin>>num;
            arr.push_back(num);



        }
        cin>>K;
        pq.push(make_pair(0,K));

        sol();
        cout<<"#"<<t<<" "<<pq.top().first<<endl;
    }

    return 0;
}