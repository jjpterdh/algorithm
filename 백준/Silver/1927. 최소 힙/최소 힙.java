
import java.io.*;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw =new BufferedWriter(new OutputStreamWriter(System.out));
        PriorityQueue<Integer> pq=new PriorityQueue<Integer>();
        StringBuilder sb= new StringBuilder();

        int test=Integer.parseInt(br.readLine());
        int num;
        for(int i=0;i<test;i++) {
            num=Integer.parseInt(br.readLine());

            if(num==0 && pq.isEmpty()){
                sb.append("0").append("\n");
            }
            else if(num==0) {
                sb.append(pq.poll()).append("\n");
            }
            else{
                pq.offer(num);
            }

        }
        br.close();
        bw.write(sb.toString());
        bw.flush();



    }
}
