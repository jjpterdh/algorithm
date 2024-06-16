#include<iostream>
#include<algorithm>
#include<vector>


using namespace std;

vector<int> days;
vector<int> spaces;


void init() {
	days.clear();
	spaces.clear();
	spaces.push_back(0);
}




int sol(int p) {
	int ans = 0;
    int max=0;
	for (int i = 0; i < days.size(); i++) {
        int start=i, end=spaces.size()-1;

        while(end>=start) {
            int mid=(start+end)/2;
            int x=spaces[mid]-spaces[i];
            int tmp=p;

            if(p-x > 0) 
                tmp=p-x;
            else 
                tmp=0;

            if(x <= p) {
                ans=days[mid]-days[i]+1+tmp;
                start=mid+1;
            }
                
            else {
                end=mid-1;
            }

        }
        if(max<ans)
            max=ans;

	}
    
    


	return max;
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    freopen("studyEnglish_input.txt", "r", stdin);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		init();
		int n, p;
		cin >> n >> p;

        int space=0;
		for (int i = 0; i < n; i++) {
			int num = 0;
			cin >> num;
			days.push_back(num);

            
			if (i > 0) {
                space+=days[i] - days[i - 1]-1;
				spaces.push_back(space);
			}
		}

        int ans=sol(p);
        cout<<"#"<<t<<" "<<ans<<endl;



		

	}

}