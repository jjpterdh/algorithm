
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Relative implements Comparable<Relative> {
    int idx;
    int cost;
    Relative(int idx, int cost) {
        this.idx = idx;
        this.cost = cost;

    }
    @Override
    public int compareTo(Relative o) {
        return cost - o.cost;
    }
}


public class Main {
    static ArrayList<ArrayList<Relative>> list = new ArrayList<>();
    static StringTokenizer st;
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int n= Integer.parseInt(br.readLine());
        for(int i=0;i<=n;i++){
            list.add(new ArrayList<>());
        }
        st= new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int m= Integer.parseInt(br.readLine());
        for(int i=0;i<m;i++){
            st= new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.get(a).add(new Relative(b,1));
            list.get(b).add(new Relative(a,1));
        }


        dijk(n, start, end);

    }


    public static void dijk(int n, int start, int end) {
        int[] dis=new int[n+1];
        Arrays.fill(dis, Integer.MAX_VALUE);
        dis[start]=0;
        PriorityQueue<Relative> pq = new PriorityQueue<>();
        pq.offer(new Relative(start,0));
        while(!pq.isEmpty()){

            Relative r = pq.poll();
            if(dis[r.idx]< r.cost) continue;

            for(int i=0;i<list.get(r.idx).size();i++) {
                int newDist= r.cost+ list.get(r.idx).get(i).cost;
                int next = list.get(r.idx).get(i).idx;
                if(dis[next]>newDist){
                    dis[next]=newDist;
                    pq.offer(new Relative(next,newDist));
                }
            }



        }
        if(dis[end]==Integer.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(dis[end]);


    }


}
