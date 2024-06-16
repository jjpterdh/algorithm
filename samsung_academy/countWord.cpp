#include<iostream>
#include<cstring>

using namespace std;

char B[500001];
char S[100001];
int P[100001];

void init() {
    memset(B, '0', sizeof(B));
    memset(S, '0', sizeof(S));
    memset(P, 0, sizeof(P));
}


int sol() {
    for(int i=1;i<=strlen(S);i++) {
        int j=P[i-1];
        while(j>0) {
            if(S[i]==S[j]) break;
            j=P[j-1];

        }
        if(S[i]==S[j])P[i]=j+1;
        else P[i]=0;


    }

    int count=0;
    int ans=0;
    int pivot=0;

    while(B[pivot]) {
        if(B[pivot]==S[count]) {
            if(!S[count+1]) {
                ans++;
                count=P[count];

            } 
            else 
                count++;
            pivot++;
        }
        else if(count>0) {
            count=P[count-1];
        }
        else 
            pivot++;
    }

    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    int T;
    cin>>T;

    for(int t=1;t<=T;t++) {
        init();

        cin>>B>>S;

        
        int ans=sol();

        cout<<"#"<<t<<" "<<ans<<endl;



    }


    return 0;

}