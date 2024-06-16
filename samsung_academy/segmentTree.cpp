#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#define inf 1e9
using namespace std;

int arr[100001];
int min_tree[400004];
int max_tree[400004];

void init() {
    memset(arr, 0, sizeof(arr));
    memset(min_tree,0,sizeof(min_tree));
    memset(max_tree,0, sizeof(max_tree));
}

int init_max_tree(int* tree, int node, int s, int e) {
    if(s==e) return tree[node]=arr[s];

    int m=(s+e)/2;
    int a=init_max_tree(tree, node*2, s,m );
    int b=init_max_tree(tree, node*2+1, m+1,e);

    return max(a,b);
}


int init_min_tree(int* tree, int node, int s, int e) {
    if(s==e) return tree[node]=arr[s];

    int m=(s+e)/2;
    int a=init_min_tree(tree, node*2, s,m );
    int b=init_min_tree(tree, node*2+1, m+1,e);

    return min(a,b);
}


int min_update(int* tree, int node, int s, int e, int ii, int value) {
    //ii 수정할 인덱스
    //value 더해서 갱신
    if(s>ii||ii>e) return tree[node];
    tree[node]+=value;

    if(s==e) return tree[node];
    int m=(s+e)/2;
    int a=min_update(tree, node*2, s, m, ii, value);
    int b=min_update(tree, node*2+1, m+1, e, ii, value);
    return min(a,b);
}

int max_update(int* tree, int node, int s, int e, int ii, int value) {
    if(s>ii||ii>e) return tree[node];
    tree[node]+=value;

    if(s==e) return tree[node];
    int m=(s+e)/2;
    int a=max_update(tree, node*2, s, m, ii, value);
    int b=max_update(tree, node*2+1, m+1, e, ii, value);
    return max(a,b);
}


int max_query(int* tree, int node, int ts, int te, int qs, int qe) {
    if(ts>=qs && qe>=te) return tree[node];

    if(te<qs||qe<ts) return 0;

    int m=(ts+te)/2;
    int a=max_query(tree, node*2, ts, m, qs, qe);
    int b=max_query(tree, node*2+1, m+1, te,qs,qe);

    return max(a,b);
}

int min_query(int* tree, int node, int ts, int te, int qs, int qe) {
    if(ts>=qs && qe>=te) return tree[node];

    if(te<qs||qe<ts) return inf;

    int m=(ts+te)/2;
    int a=min_query(tree, node*2, ts, m, qs, qe);
    int b=min_query(tree, node*2+1, m+1, te,qs,qe);

    return min(a,b);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    int T;
    cin>>T;


    for(int t=1;t<=T;t++){
        init();
    
        int n , q;
        cin>>n>>q;

        // 배열 입력
        for(int i=1;i<=n;i++) {
            cin>>arr[i];
        }
        cout<<"#"<<t<<" ";
        init_max_tree(max_tree, 1, 1, n);
        init_min_tree(min_tree, 1, 1, n);

        //나무 출력
        for(int i=1;i<=n;i++){
            cout<<"min_tree["<<i<<"] = "<<min_tree[i]<<endl;
            cout<<"max_tree["<<i<<"] = "<<max_tree[i]<<endl;
        }

        // 쿼리 입력
        for(int i=0;i<q;i++) {
            int ans=0;
            int type, s, e;
            cin>>type>>s>>e;


            

            if(type==0) {
                arr[s]=e;
                min_update(min_tree, 1, 1, n, s, e);
                max_update(max_tree, 1, 1, n, s, e);
            }
            else {
                int min_num=min_query(min_tree, 1, 1, n, s, e);
                int max_num=max_query(max_tree, 1, 1, n, s, e);
                ans=max_num-min_num;
                cout<<ans<<" ";
            }
            
            
            
        }
        cout<<endl;

        
    }

}