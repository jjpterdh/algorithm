import java.util.*;
class Node implements Comparable<Node> {
    int idx;
    int cost;
    Node(int idx, int cost) {
        this.idx=idx;
        this.cost=cost;
    }
    
    @Override
    public int compareTo(Node o) {
        return this.cost-o.cost;
    }
}

class Solution {
    ArrayList<ArrayList<Node>> graph;
    int[] dist;
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        graph=new ArrayList<ArrayList<Node>>();
        
        for(int i=0;i<=N;i++) {
            graph.add(new ArrayList<Node>());
        }
        
        for(int[] arr : road) {
            int start=arr[0];
            int end= arr[1];
            int cost= arr[2];
            graph.get(start).add(new Node(end, cost));
            graph.get(end).add(new Node(start, cost));
        }
        
        
        dist=new int[N+1];
        dijkstra(1, N);
        
        for(int i=1;i<=N;i++) {
            if(dist[i]<=K) answer++;
        }
        
        return answer;
    }
    public void dijkstra(int start, int N) {
        PriorityQueue<Node> pq= new PriorityQueue<Node>();
        Arrays.fill(dist, 99999999);
        pq.offer(new Node(start, 0));
        dist[start]=0;
        
        while(!pq.isEmpty()) {
            Node cur= pq.poll();
            if(dist[cur.idx]< cur.cost) continue;
            
            for(Node next : graph.get(cur.idx)) {
                int new_dist= dist[cur.idx]+next.cost;
                if(dist[next.idx] >= new_dist) {
                    dist[next.idx]=new_dist;
                    pq.offer(new Node(next.idx, new_dist));
                }
            }
        }
        
        
    }
}