class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int count=0;
        boolean[] visited= new boolean[n+1];
        
        
        for(int i=0;i<n;i++) {
            if(visited[i]) continue;
            dfs(n, computers, visited, i);
            count++;
        }
        
        return count;
    }
    
    void dfs(int n, int[][] computers, boolean[] visited, int idx) {
        visited[idx]=true;
        for(int i=0;i<n;i++) {
            if(!visited[i] && computers[idx][i]==1)
                dfs(n, computers, visited, i);
        }
    }
}