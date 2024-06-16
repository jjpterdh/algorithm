#include<iostream>
#include<cstring>


using namespace std;

int tree[10001][3]={0, };
int common[10001]={0, };

void init() {
    memset(common, 0, sizeof(common));
    memset(tree, 0, sizeof(tree));
}
int find_ancestor(int idx) {
    
    if(common[idx]==1)
        return idx;
    
    return find_ancestor(tree[idx][2]);
}

void ancestor(int idx) {
    
    common[idx]=1;
    if(idx==1)
            return;

    ancestor(tree[idx][2]);

}


int subtree_size(int idx) {
    int ans=0;    
    int left=0;
    int right=0;

    if(tree[idx][0]!=0) {
        left=subtree_size(tree[idx][0]);        
    }
    if(tree[idx][1]!=0) {
        right=subtree_size(tree[idx][1]);
    }
    ans=left+right;


    return ans+1;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    freopen("ancestor_input.txt", "r", stdin);

    int T;
    cin>>T;

    for(int t=0;t<T;t++){
        init();
        int V, E, n1, n2;
        cin>>V>>E>>n1>>n2;

        for(int e=0;e<E;e++){
            int parent, child;

            cin>>parent>>child;

            if(tree[parent][0]==0) { //no left child
                tree[parent][0]=child;
            }
            else { // no right child
                tree[parent][1]=child;
            }
            tree[child][2]=parent;



        }
        
        int ans, subtree;
        //find common ancestor
        ancestor(n1);
        ans=find_ancestor(n2);
        
        subtree=subtree_size(ans);

        cout<<"#"<<(t+1)<<" "<<ans<<" "<<subtree<<endl;



    }

    




    return 0;
}