#include<iostream>
#include<cstring>

using namespace std;

int people[101];

void init() {
    memset(people, 0, sizeof(people));
    for(int i=1;i<=100;i++){
        people[i]=i;
    }
}

int Find(int x){
    if(x==people[x]) return x;
    else return Find(people[x]);
}





int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // freopen("s_input.txt", "r", stdin);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int N, M;

        for(int m=0;m<M;m++){

        }

        cout<<"#"<<t<<" "<<endl;
    }

}