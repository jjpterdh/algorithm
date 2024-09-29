

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        int[] arr=new int[N];
        int idx=0;
        while(st.hasMoreTokens()){
            arr[idx++]= Integer.parseInt(st.nextToken());
        }

        int max = 0;
        int total=0;
        int answer=1;
        for(int i=0;i<X;i++){
            total+=arr[i];
        }
        max=total;
//        System.out.println("total : "+total);
        for(int i=X;i<N;i++){
            total-=arr[i-X];
            total+=arr[i];
//            System.out.println(arr[i]);
//            System.out.println(total);
            if(total>max){
                max=total;
                answer=1;
            }
            else if(total==max){
                answer++;
            }


        }


        // answer
        if (max == 0) System.out.println("SAD");
        else {
            System.out.println(max);
            System.out.println(answer);
        }


    }

}