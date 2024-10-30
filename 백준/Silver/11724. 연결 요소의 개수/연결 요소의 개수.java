

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer st;
    static ArrayList<ArrayList<Integer>> graph= new ArrayList<>();
    static int answer=0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st= new StringTokenizer(br.readLine());
        int nodes= Integer.parseInt(st.nextToken());
        int edges= Integer.parseInt(st.nextToken());

        // init graph
        for(int i=0; i<=nodes; i++){
            graph.add(new ArrayList<Integer>());
        }

        // add edges
        for(int i=0;i<edges;i++){
            st= new StringTokenizer(br.readLine());
            int from= Integer.parseInt(st.nextToken());
            int to= Integer.parseInt(st.nextToken());
            graph.get(from).add(to);
            graph.get(to).add(from);
        }

        dfs(nodes);
        System.out.println(answer);

    }

    public static void dfs(int nodes) {
        boolean[] visited = new boolean[nodes+1];
        Stack<Integer> stack = new Stack<Integer>();
        for(int i=1; i<=nodes; i++){
            if(!visited[i]){
//                System.out.println(i);
                answer++;
                visited[i] = true;
                stack.push(i);
                while(!stack.isEmpty()){
                    int curr = stack.pop();
                    for(int n=0; n<graph.get(curr).size(); n++){
                        int next=graph.get(curr).get(n);
                        if(!visited[next]){
                            visited[next]=true;
                            stack.push(next);
                        }
                    }

                }

            }
        }

    }
}

