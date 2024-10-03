import java.util.*;

class Node implements Comparable<Node> {
    int idx;
    int cost;
    
    Node(int idx, int cost) {
        this.idx= idx;
        this.cost=cost;
    }
    
    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

class Solution {
    int[] dist; 
    ArrayList<ArrayList<Node>> graph;
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        graph=new ArrayList<ArrayList<Node>>();
                
        for(int i=0;i<=n;i++) {
            graph.add(new ArrayList<Node>());
        }
        
        for(int[] road : roads) {
            int u=road[0];
            int v=road[1];
            
            
            graph.get(u).add(new Node(v, 1));
            graph.get(v).add(new Node(u, 1));
        }
        int idx=0;
        dist= new int[n+1];
        dijkstra(destination, n);
        for(int s: sources) {
            int ans=dist[s];            
            answer[idx++]=ans==99999999 ? -1 : ans;
        }
        
        return answer;
    }
    
    public void dijkstra(int start, int n) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        
        Arrays.fill(dist, 99999999);
        dist[start]=0;
        pq.offer(new Node(start, 0));
        
        while(!pq.isEmpty()) {
            Node cur= pq.poll();
            if(dist[cur.idx]< cur.cost) continue;
            
            for(Node next : graph.get(cur.idx)) {
                int new_dist= dist[cur.idx] + next.cost;
                if(dist[next.idx] >= new_dist) {
                    dist[next.idx]=new_dist;
                    pq.offer(new Node(next.idx, new_dist));
                }
            }
        }
        
        
    }
}