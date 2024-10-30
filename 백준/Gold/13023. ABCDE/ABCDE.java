
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer st;
    static ArrayList<ArrayList<Integer>> friends = new ArrayList<>();
    static int answer=0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());


        for(int i=0;i<n;i++) {
            friends.add(new ArrayList<>());
        }

        for(int i=0;i<m;i++) {
            st = new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            friends.get(a).add(b);
            friends.get(b).add(a);
        }
        boolean[] visited=new boolean[n];
        for(int i=0;i<n;i++) {

            dfs(visited, n, m, i, 1);
            if(answer==1) break;

        }
        System.out.println(answer);
    }

    public static void dfs(boolean[] visited, int n, int m, int idx, int count) {
        if(count>=5 || answer==1) {answer=1; return;}
        visited[idx]=true;
        for(int i=0;i<friends.get(idx).size();i++) {
            int next=friends.get(idx).get(i);
            if(!visited[next]) {

                dfs(visited, n, m, next, count + 1);
            }
        }
        visited[idx]=false;
    }

}
