

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer st;
    static int[] dy={-1, 0, 1, 0};
    static int[] dx={0,-1,0,1};
    static char[][] board;
    static int answer=0;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        st= new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());

        board=new char[n+1][m+1];
        for(int i=1;i<=n;i++){
            String s=br.readLine();
            for(int j=1;j<=m;j++){
                board[i][j]=s.charAt(j-1);
            }
        }
        ArrayList<Character> arr = new ArrayList<>();
        boolean[][] visited=new boolean[n+1][m+1];
        visited[1][1]=true;
        arr.add(board[1][1]);
        dfs(arr, 1, 1, visited, n, m, 1);
        System.out.println(answer);
    }
    public static void dfs(ArrayList<Character> arr, int y, int x, boolean[][] visited, int n, int m, int count) {
        int ny;
        int nx;
//        System.out.println("alphabet : "+ board[y][x]);
        for(int i=0;i<4; i++) {
            ny=y+dy[i];
            nx=x+dx[i];
            if(ny <=0 || nx <=0 || ny>n || nx>m) continue;
            else if(visited[ny][nx]) continue;
            else if(arr.contains(board[ny][nx])) continue;
            arr.add(board[ny][nx]);
            visited[ny][nx]=true;
            dfs(arr, ny, nx, visited, n, m, count+1);
            visited[ny][nx]=false;
            arr.remove(arr.size()-1);
        }
        answer=Math.max(answer,count);
    }
}
