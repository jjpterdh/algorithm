
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N= Integer.parseInt(st.nextToken());
        int D= Integer.parseInt(st.nextToken());

        // init
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for(int i=0;i<10001;i++) {
            graph.add(new ArrayList<Node>());
        }

        int start;
        int end;
        int length;
        for(int i=0;i<N;i++) {
            st = new StringTokenizer(br.readLine());
            start= Integer.parseInt(st.nextToken());
            end= Integer.parseInt(st.nextToken());
            length= Integer.parseInt(st.nextToken());
            graph.get(start).add(new Node(end,length));
        }






        System.out.println(dijkstra(graph, D));
    }
    public static int dijkstra(ArrayList<ArrayList<Node>> graph, int D) {
        int answer=0;

        int[] distance = new int[10001];
        for(int i=0;i<10001;i++) distance[i]=i;


        for(int i=0;i<D;i++) {
            if(distance[i+1]> distance[i]+1) distance[i+1]=distance[i]+1;


            for(int j=0;j<graph.get(i).size();j++){
                if(distance[i]+graph.get(i).get(j).weight < distance[graph.get(i).get(j).node]) {
                    distance[graph.get(i).get(j).node]=distance[i]+graph.get(i).get(j).weight;
                }
            }
        }



        answer=distance[D];
        return answer;
    }



}

class Node implements Comparable<Node> {
    int node;
    int weight;
    public Node(int node, int weight) {
        this.node = node;
        this.weight = weight;
    }

    @Override
    public int compareTo(Node o) {
        return this.weight - o.weight;
    }
}