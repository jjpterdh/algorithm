import java.util.LinkedList;
import java.util.Queue;

class Solution {
    int[] dy={-1,0,1,0};
    int[] dx={0,-1,0,1};

    public int[] solution(String[][] places) {

        int[] answer = new int [places.length];


        for(int i=0;i<places.length;i++){
            int a=1;
            for(int j=0;j<places[i].length;j++){
                for(int k=0;k<places[i][j].length();k++){
                    if(places[i][j].charAt(k)=='P'){
                        // p이면 bfs시작
                        a=Math.min(bfs(j, k, places[i]), a);

                    }
                }
            }
//            System.out.println("-------------------------------");
            answer[i]=a;
        }

        return answer;
    }


    int bfs(int y, int x, String[] places) {
        Queue<int[]> queue= new LinkedList<int[]>();
        queue.add(new int[]{y,x});
        int[][] visited = new int[5][5];
        visited[y][x]=1;

        while(!queue.isEmpty()) {
            int[] pos=queue.poll();

            int yy=pos[0];
            int xx=pos[1];
            //이게 중요하다... 2이하니깐 2이하 범위만 조사하면 끝...
            if (visited[yy][xx]>=3){continue;}
            for(int i=0;i<4;i++) {
                int ny=yy+dy[i];
                int nx=xx+dx[i];


                // out of boundary
                if(ny<0 || ny>=5 || nx<0 || nx>=5) continue;
                // wall
                else if(places[ny].charAt(nx)=='X') continue;

                // not visited
                else if (visited[ny][nx]==0) {

                    if(places[ny].charAt(nx)=='P') {

                        return 0;
                    }
                    visited[ny][nx]=visited[yy][xx]+1;
                    queue.add(new int[]{ny,nx});
                }
            }
        }


        return 1;
    }
}