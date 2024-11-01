

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer st;
    static int[] road= new int[200001];
    static int answer=Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st= new StringTokenizer(br.readLine());
        int n =Integer.parseInt(st.nextToken());
        int k= Integer.parseInt(st.nextToken());
//        System.out.println(n);
        int[] visited = new int[200001];
        Arrays.fill(visited, Integer.MAX_VALUE);
        bfs(visited, n, k);
        System.out.println(visited[k]);

    }
    public static void bfs(int[] visited, int idx, int k){
        Queue<Integer> q= new LinkedList<>();
        q.offer(idx);
        visited[idx]=0;

        while(!q.isEmpty()){
            idx= q.poll();

            int nextMove=visited[idx]+1;

            if(idx-1 >=0 && visited[idx-1] > nextMove) {
                visited[idx-1]=nextMove;
                q.offer(idx-1);
            }
            if(idx+1 <=100000 && visited[idx+1] > nextMove) {
                visited[idx+1]=nextMove;
                q.offer(idx+1);
            }
            if(idx*2 <= 100000 && visited[idx*2]>nextMove) {
                visited[idx*2]=nextMove;
                q.offer(idx*2);
            }

        }



    }
}
