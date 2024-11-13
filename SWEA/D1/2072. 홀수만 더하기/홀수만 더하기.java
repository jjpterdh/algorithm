
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int sum=0;
        int time=0;
        while (T-- > 0) {
            time++;
            st = new StringTokenizer(br.readLine());
            sum=0;
            for(int i=0;i<10;i++) {
                int num=Integer.parseInt(st.nextToken());
                if(num%2==0) continue;
                sum+=num;
            }
            System.out.println("#"+time+" "+sum);

        }
    }
}
