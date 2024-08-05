
import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;


        // 트리 구조로 바꾸기
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }
        for (int i = 0; i < edge.length; i++) {
            int s =edge[i][0];
            int e =edge[i][1];

            // 양방향 추가하기
            map.get(s).add(e);
            map.get(e).add(s);

        }

        // bfs
        int[] visited=bfs(n, map);

        int max=0;
        for(int i=0;i<visited.length;i++) {
            if (visited[i]>max) {
                max=visited[i];
                answer=1;
            }
            else if(visited[i]==max) answer++;
//            System.out.println(i+" "+visited[i]);
        }

        return answer;
    }

    int[] bfs(int n, Map<Integer, List<Integer>> map) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        int[] visited = new int[n+1];
        visited[1] = 1;

        while (!queue.isEmpty()) {
            int id = queue.poll();

            for (int i = 0; i < map.get(id).size(); i++) {
                if (visited[map.get(id).get(i)] == 0) {
                    visited[map.get(id).get(i)] = visited[id] + 1;
                    queue.offer(map.get(id).get(i));

                }
            }
        }

        return visited;

    }
}