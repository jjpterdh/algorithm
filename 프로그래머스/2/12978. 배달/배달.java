import java.util.*;

class Solution {
    int[][] board;
    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        board= new int[N+1][N+1];
        for(int i=1;i<=N;i++) {
            Arrays.fill(board[i], 500001);
        }
        
        // init
        for(int[] arr: road) {
            int start=arr[0];
            int end=arr[1];
            int cost=arr[2];
            board[start][end]=Math.min(board[start][end], cost);
           board[end][start]=Math.min(board[end][start], cost);
        }
        
        // 플로이드-와샬
        for(int k=1;k<=N;k++) {
            for(int start=1;start<=N;start++) {
                
                if(start==k) {
                    board[start][k]=0;
                    continue;
                }
                for(int end =1; end<=N; end++) {
                    if(end==k) continue;
                    board[start][end]=Math.min(board[start][end], board[start][k]+board[k][end]);
                    board[end][start]=Math.min(board[end][start], board[end][k]+board[k][start]);
                }
            }
        }
        
        for(int i=1;i<=N;i++){
            if(board[1][i]<=K) {
                // System.out.println("start : "+ 1 + " end : "+i + " cost : "+K);
                answer++;
            }
        }
        return answer;
    }
}