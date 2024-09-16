
import java.io.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        String password;

        String acc = "> is acceptable.\n";
        String not = "> is not acceptable.\n";
        StringBuilder sb = new StringBuilder();
        char[] pass;
        try {
            while(!(password = br.readLine()).equals("end")) {
                pass=password.toCharArray();

                char prev='.';
                boolean flag=false;
                int count=0;
                for(char c : pass) {
                    // 모음 체크
                    if(isVowel(c)) {
                        flag=true;
                    }

                    // 종류 체크
                    if(isVowel(prev)!=isVowel(c)) {
                        count=1;
                    }
                    else count++;

                    if(count>2 || (prev==c && (c!='e' && c!='o'))) {flag=false; break;}


                    prev=c;

                }

                if(flag) {
                    sb.append('<').append(password).append(acc);
                }
                else {
                    sb.append('<').append(password).append(not);
                }




            }


            System.out.println(sb.toString());

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static boolean isVowel(char c) {
        return c=='a' || c=='e' || c=='o' || c=='u' || c=='i';
    }
}
