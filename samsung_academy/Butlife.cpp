#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

vector<int> Ws;
vector<int> Ss;

void init() {


}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    freopen("butLife_input.txt", "r", stdin);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        int N, K;
        cin>> N>>K;

        for(int i=0;i<N;i++) {
            int num;
            cin>>num;
            Ws.push_back(num);
        }

        for(int i=0;i<K;i++) {
            int num;
            cin>>num;
            Ss.push_back(num);
        }

    }

    return 0;
}