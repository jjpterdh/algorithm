import java.util.*;

class Solution {
    int[] dy={-1,0,1,0};
    int[] dx={0,-1,0,1};
    boolean[][]visited;
    ArrayList<int[]> oils = new ArrayList<>();
    public int solution(int[][] land) {
        int answer = 0;
        
        
        visited=new boolean[land.length][land[0].length];
        
        for(int i=0;i<land[0].length;i++) {
            for(int j=0;j<land.length;j++) {
                if(!visited[j][i] && land[j][i]==1) {
                    bfs(j, i , land);
                }
            }
        }
        
        for(int i=0;i<land[0].length;i++) {
            int total=0;
//             for(int[] pos : oils) {
//                 int l=pos[0];
//                 int r=pos[1];
//                 if(i>=l && i<=r) total+=pos[2];
                
//             }
            for(int r=0;r<oils.size();r++) {
                if(i>=oils.get(r)[0] && i<=oils.get(r)[1]) {
                    total+=oils.get(r)[2];
                }
            }
            answer=Math.max(answer, total);
        }
        
        return answer;
    }
    public void bfs(int y, int x, int[][] land) {
        Queue<int[]> queue = new LinkedList<>();        
        queue.offer(new int[] {y, x});
        
        int count=1;
        int leftmost=x;
        int rightmost=x;
        while(!queue.isEmpty()) {
            int[] pos=queue.poll();
            int cy=pos[0];
            int cx=pos[1];
            visited[cy][cx]=true;
            
            
            for(int i=0;i<4;i++) {
                int ny=cy+dy[i];
                int nx=cx+dx[i];
                
                // out of boundary
                if(ny<0 || ny>= land.length || nx<0 || nx>=land[0].length) continue;
                
                // visited or not oil
                else if(visited[ny][nx] || land[ny][nx]==0) continue;
                
                // visit
                else{
                    leftmost=Math.min(leftmost, nx);
                    rightmost=Math.max(rightmost,nx);
                    
                    visited[ny][nx]=true;
                    queue.offer(new int[] {ny, nx});
                    count++;
                }   
            }
        }
        
        oils.add(new int[] {leftmost, rightmost, count});
        
    }
    
    
    
}