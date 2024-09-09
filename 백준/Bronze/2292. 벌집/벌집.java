
import java.io.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb= new StringBuilder();
        try {
            int n = Integer.parseInt(br.readLine());

            if(n==1) {System.out.println(1);}
            else {
                int range = 2;
                int count = 1;

                while (n >= range) {
                    range = range + (count * 6);
                    count++;
                }
                sb.append(count);
                bw.write(sb.toString());
                bw.flush();
                bw.close();
            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
