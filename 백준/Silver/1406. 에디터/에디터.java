
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str=br.readLine();

        int t=Integer.parseInt(br.readLine());


        Stack<Character> stack = new Stack<>();
        Stack<Character> stack2 = new Stack<>();

        // init
        for(int i=0; i<str.length(); i++) {
            stack.push(str.charAt(i));
        }

        StringTokenizer st;

        for(int i=0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            String command=st.nextToken();
            if(command.equals("L")) {
                if(stack.isEmpty()) continue;
                Character alpha=stack.pop();
                stack2.push(alpha);
            }
            else if(command.equals("D")) {
                if(stack2.isEmpty()) continue;
                Character alpha=stack2.pop();
                stack.push(alpha);
            }
            else if(command.equals("B")) {
                if(stack.isEmpty()) continue;
                stack.pop();
            }

            else if(command.equals("P")) {
                String alpha=st.nextToken();
                stack.push(alpha.charAt(0));

            }
        }
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()) {
            Character c = stack.pop();
            stack2.push(c);
        }
        while(!stack2.isEmpty()) {
            sb.append(stack2.pop());

        }
        sb.append("\n");
        System.out.println(sb);
    }

}
