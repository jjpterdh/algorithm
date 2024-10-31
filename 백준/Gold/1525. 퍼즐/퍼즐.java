

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int answer=Integer.MAX_VALUE;

    static StringTokenizer st;
    static HashMap<String, Integer> map = new HashMap<>();
    static int[] dy={-1,0,1,0};
    static int[] dx={0,-1,0,1};
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        // init board
        StringBuilder sb= new StringBuilder();

        for(int i=0;i<3;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<3;j++){
               sb.append(st.nextToken());
            }
        }


        map.put(sb.toString(), 0);
        bfs(sb.toString());
        if(answer==Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(answer);
    }

    public static void bfs(String sent) {
        Queue<String> q = new LinkedList<>();
        q.offer(sent);

        while(!q.isEmpty()){
            String s = q.poll();
            int zeroIndex= s.indexOf("0");

            if(s.equals("123456780")) {
                answer=map.get(s);
                return;
            }
            for(int i=0;i<4;i++){
                int nr = zeroIndex/3 + dx[i];
                int nc = zeroIndex%3 + dy[i];
                if(nr < 0 || nr >= 3 || nc < 0 || nc >= 3) continue;

                int nTempZeroIdx = nr * 3 + nc;
                StringBuilder nSb = new StringBuilder(s);
                char saveWords = nSb.charAt(nTempZeroIdx);
                nSb.setCharAt(nTempZeroIdx, '0');
                nSb.setCharAt(zeroIndex, saveWords);
                if(map.containsKey(nSb.toString()) == false) { //처음으로 들어온 값일경우에만
                    q.offer(nSb.toString());
                    map.put(nSb.toString(), map.get(s) + 1);
                }

            }

        }
    }


    public static String board2String(int[][] board) {
        String ans="";
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                ans+=board[i][j]+" ";

            }
        }
        return ans;
    }
}
