#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int robot[3];
int graph[51][3];

int dp[51];

void init()
{
	memset(robot, 0, sizeof(int) * 3);
	for (int i = 0; i < 51; i++)
	{
		memset(graph[i], 0, sizeof(int) * 3);
	}
	memset(dp, 0, sizeof(int) * 51);
}

int dfs(int n, int count)
{
	if (count == 3)
	{
		return 0;
	}
	return 0;
}

int sol(int n)
{
	int ans = 0;

	for (int i = 1; i <= n; i++)
	{

		// if (robot[0] == 0 || robot[1] == 0 || robot[2] == 0)
		// {
		// 	if (graph[i - 1][0] > graph[i - 1][1] && graph[i - 1][0] > graph[i - 1][2])
		// 	{
		// 		robot[0] = graph[i - 1][0];
		// 	}
		// 	else if (graph[i - 1][1] > graph[i - 1][0] && graph[i - 1][1] > graph[i - 1][2])
		// 	{
		// 		robot[1] = graph[i - 1][1];
		// 	}
		// 	else if (graph[i - 1][2] > graph[i - 1][0] && graph[i - 1][2] > graph[i - 1][1])
		// 	{
		// 		robot[2] = graph[i - 1][2];
		// 	}
		// }
		// else
		// {
		// 	dp[i] = max({dp[i - 1] + graph[i - 1][0], dp[i - 1] + graph[i - 1][1], dp[i - 1] + graph[i - 1][2]});
		// }
		dp[i] = max({dp[i - 1] + graph[i - 1][0], dp[i - 1] + graph[i - 1][1], dp[i - 1] + graph[i - 1][2]});
	}

	ans = dp[n];
	return ans;
}

int main(void)
{

	freopen("sample_input (1).txt", "r", stdin);
	int T;
	cin >> T;

	for (int t = 0; t < T; t++)
	{
		int n;
		cin >> n;

		init();

		int total = 0;
		for (int i = 0; i < n; i++)
		{
			int a, b, c;
			cin >> a >> b >> c;
			total += (a + b + c);

			graph[i][0] = a;
			graph[i][1] = b;
			graph[i][2] = c;
		}

		int answer = sol(n);

		if (n < 3)
		{
			cout << "#" << (t + 1) << ' ' << -1 << endl;
		}

		else
		{
			cout << "#" << (t + 1) << ' ' << total - answer << endl;
		}
	}
}