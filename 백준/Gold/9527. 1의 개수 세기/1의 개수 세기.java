

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long[] DP = new long[55];	//1의 개수 누적합 저장 배열
    public static void main(String[] args) throws IOException {
        //입력값 처리하는 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        //A(N)과 B(M)을 저장
        long N = Long.parseLong(st.nextToken());
        long M = Long.parseLong(st.nextToken());
        setDp();	//누적합 계산!
        //A ≤ n ≤ B : B의 누적합 - (A-1)의 누적합 구하기
        long result = calOne(M) - calOne(N-1);
        System.out.print(result);	//A ≤ n ≤ B 의 1의 개수 출력
    }
    //1~N 정수에 대한 1의 개수 구하는 함수
    static long calOne(long N) {
        long count = N & 1;
        //N보다 작은 2ⁿ의 n의 최대값
        int size = (int) (Math.log(N)/Math.log(2));
        //비트마스킹을 이용한 1의 개수 계산 진행
        //DP[i-1] : 000 ~ 111 개수
        //N - (1L << i) : 지정된 1이 반복 사용될 개수
        // + 1 : 1000...
        for(int i=size;i>0;i--) {
            if((N & (1L<<i)) != 0L) {
                count += DP[i-1] +(N - (1L<<i) + 1);
                N -= (1L << i);	//비트 이동시키기
            }
        }
        return count;	//1의 개수 반환
    }
    //DP[n] = DP[n-1] × 2 + 2ⁿ을 이용하여 누적합 저장하는 함수
    static void setDp() {
        DP[0] = 1;	//DP[0]은 1으로 초기화
        //점화식 적용
        //DP[i-1] << 1 : DP[n-1] × 2
        //1L << i : 2ⁿ
        for(int i=1;i<55;i++)
            DP[i] = (DP[i-1] << 1) + (1L << i);
    }
}
