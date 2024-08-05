import java.util.*;
class Solution {
    int answer = Integer.MAX_VALUE;
    Map<Integer, List<Integer>> map = new HashMap<>();
    public int solution(int n, int[][] wires) {



        // map 초기화
        for (int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }

        // 양방향 추가해주기
        for(int i = 0; i< wires.length; i++) {
            map.get(wires[i][0]).add(wires[i][1]);
            map.get(wires[i][1]).add(wires[i][0]);
        }

        for(int i = 0; i< wires.length; i++) {
            map.get(wires[i][0]).remove(Integer.valueOf(wires[i][1]));
            map.get(wires[i][1]).remove(Integer.valueOf(wires[i][0]));
            int cnt= bfs(1, n);

            map.get(wires[i][0]).add(wires[i][1]);
            map.get(wires[i][1]).add(wires[i][0]);

            int cnt2=n-cnt;
            answer=Math.min(answer, Math.abs(cnt2-cnt));
        }




        return answer;
    }


    int bfs(int start, int n ) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);

        boolean[] visited = new boolean[n+1];
        visited[start]=true;
        int count=1;
        while(!queue.isEmpty()) {
            int node= queue.poll();
            for(int i=0;i<map.get(node).size();i++) {
                if(!visited[map.get(node).get(i)]) {
                    visited[map.get(node).get(i)] = true;
                    queue.offer(map.get(node).get(i));
                    count++;
                }

            }

        }
        return count;
    }
}