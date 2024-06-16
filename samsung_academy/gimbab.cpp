#include <cstdio>
#include <vector>
#include<cmath>


using namespace std;


const int INF = int(1e9);
vector<pair<int, int> > triangle;



void init(){
	triangle.push_back(make_pair(INF,INF));
	int row=0;
	
	for(int i=1;i<=150;i++) {
		for(int y=0;y<i;y++) {
			triangle.push_back(make_pair(row, y));
		}
		row++;
	}
}

pair<int, int> find_pos(int num) {
	pair<int, int>pos;
	int y=0;
	int x=0;
	int row = static_cast<int>((sqrt(8 * static_cast<double>(num) + 1) - 1) / 2);

    
	int tNumber = row * (row + 1) / 2;
    int col = num - tNumber - 1;
	if(col==-1) {
		row-=1;
		col=row;
	}
		
	pos.first=row;
	pos.second=col;
	return pos;
}

int sol(int s, int e) {

	int ans=0;
	pair<int, int> ss=find_pos(s);
	// int sy=triangle[s].first;
	// int sx=triangle[s].second;
	int sy=ss.first;
	int sx=ss.second;

	pair<int, int> ee=find_pos(e);
	// int ey=triangle[e].first;
	// int ex=triangle[e].second;

	int ey=ee.first;
	int ex=ee.second;

	// cout<<s<<": " <<sy<<' '<< sx<<endl;
	// cout<<e<<": "<<ey<< ' '<<ex<<endl;
	ans=((sx>ex && s<e) || (s>e && sx<ex)) ? abs(sx-ex)+abs(sy-ey) :max(abs(sy-ey), abs(sx-ex));
	
	return ans;

}

int main(void)
{

	freopen("sample_input.txt", "r", stdin);
	// init();

	int T;
	scanf("%d", &T);
	// cin >> T;
	

	for (int t = 0; t < T; t++)
	{

		int s;
		int e;
		// cin >> s >> e;
		scanf("%d %d", &s, &e);
		int ans=sol(s, e);
		// cout<<"#"<<(t+1)<<' '<<ans<<endl;
		printf("#%d %d\n", (t+1), ans);
		
		
	}

	return 0;
}