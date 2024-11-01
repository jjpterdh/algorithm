

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dy={-1,0,1,0};
    static int[] dx={0,-1,0,1};
    static StringTokenizer st;
    static int answer=Integer.MAX_VALUE;

    static int[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        st=new StringTokenizer(br.readLine());
        int n= Integer.parseInt(st.nextToken());
        int m= Integer.parseInt(st.nextToken());

        board= new int[n+1][m+1];


        for(int i=1;i<=n;i++){
            String s= br.readLine();
            for(int j=1;j<=m;j++){
                board[i][j]=Integer.parseInt(s.charAt(j-1)+"");
            }
        }

        bfs(board, n,m);

        if(answer==Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else {
            System.out.println(answer);
        }
    }

    public static void bfs(int[][] board, int n, int m) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{1,1, 0});
        int[][][] visited = new int[n+1][m+1][2];
        visited[1][1][0] = 1;


        while(!q.isEmpty()){
            int[] pos= q.poll();
            // 목적지 도착
            if(pos[0]==n && pos[1]==m) {
                answer=Math.max(visited[n][m][0], visited[n][m][1]);
                return;
            }


            for(int i=0;i<4;i++){
                int ny=pos[0]+dy[i];
                int nx=pos[1]+dx[i];

                if(ny<=0 || nx <=0 || ny>n || nx>m) continue;

                else if(board[ny][nx]==0) { // road
                    if(visited[ny][nx][pos[2]]==0) {
                        visited[ny][nx][pos[2]]=visited[pos[0]][pos[1]][pos[2]]+1;
                        q.offer(new int[] {ny,nx,pos[2]});
                    }
                }
                else { // wall

                    if(pos[2]==0 && visited[ny][nx][1]==0) {
                        q.offer(new int[] {ny,nx,1});
                        visited[ny][nx][1]=visited[pos[0]][pos[1]][pos[2]]+1;
                    }
                }

            }
        }


    }


}
