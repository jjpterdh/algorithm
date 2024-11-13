

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Solution
{
 
    public static void main(String [] args )throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
         
        int T = Integer.parseInt(br.readLine());
         
        for(int i = 1; i <= T; i++) {
            String S = br.readLine();
            String E = br.readLine();
             
            String answer = canTransform(S, E) ? "Yes" : "No";
            sb.append("#").append(i).append(" ").append(answer).append("\n");
        }
         
        System.out.println(sb.toString());
    }
     
    public static boolean canTransform(String S, String E) {
        while (E.length() > S.length()) {
            if (E.endsWith("X")) {
                E = E.substring(0, E.length() - 1);
            } else if (E.endsWith("Y")) {
                E = new StringBuilder(E.substring(0, E.length() - 1)).reverse().toString();
            }
        }
        return E.equals(S);
    }
}