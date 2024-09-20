
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        HashMap<String, Integer> map = new HashMap<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());



        for(int i=0;i<N;i++){
            String word= br.readLine().trim();
//            System.out.println(word);
            if(word.length()<M) continue;

            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        List<String> words= new ArrayList(map.keySet());
        Collections.sort(words, new Comparator<String> (){
            @Override
            public int compare(String o1, String o2) {
                // 자주 등장하는 단어 순서대로 정렬
                if (Integer.compare(map.get(o1), map.get(o2)) != 0) {
                    return Integer.compare(map.get(o2), map.get(o1));
                }
                // 등장 횟수가 같으면 길이가 긴 단어가 먼저 오도록 정렬
                else if(o1.length()!=o2.length()) return o2.length()-o1.length();

                // 등장 횟수와 길이가 같으면 사전 순으로 정렬
                else return o1.compareTo(o2);
            }

        });

        StringBuilder sb= new StringBuilder();
        for(String word: words) {
            sb.append(word).append("\n");
        }

        System.out.println(sb.toString());



    }
}
