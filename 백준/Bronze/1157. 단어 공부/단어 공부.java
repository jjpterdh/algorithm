
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int[] counts= new int[26];
        try {
            String sent=br.readLine();
            sent=sent.toUpperCase();
            for(int i=0;i<sent.length();i++){
                counts[sent.charAt(i)-'A']++;
            }

            //count words
            int idx=0;
            int max=-1;
            char ans='?';
            for(int i=0;i<26;i++) {
                if(max<counts[i]) {
                    max=counts[i];
                    idx=i;
                }
                else if(max==counts[i]) {
                    idx=-1;
                }
            }

            if(idx==-1) System.out.println(ans);
            else System.out.println(Character.toString(idx+'A'));


        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
}
