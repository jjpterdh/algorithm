

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int T=Integer.parseInt(br.readLine());
        for (int i = 1; i <= T; i++) {
            String S=br.readLine();
            String E =br.readLine();
            boolean flag=false;

            while(E.length()>S.length()) {

                if(E.endsWith("X")) {
                    E=E.substring(0, E.length()-1);
                }
                else if(E.endsWith("Y")) {
                    E=E.substring(0, E.length()-1);
                    E = new StringBuilder(E).reverse().toString();
                }

//                System.out.println(E);

            }


            if(E.equals(S)) System.out.println("#"+i+" Yes");
            else System.out.println("#"+i+" No");
        }
    }
}
