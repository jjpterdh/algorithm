import java.util.*;
class Solution {
    int[] dy={-1,0,1,0};
    int[] dx={0,-1,0,1};
    int y=0;
    int x=0;
    public int solution(String[] maps) {
        int answer = 0;
        
         
        for(int i=0;i<maps.length;i++) {
            for(int j=0;j<maps[i].length();j++) {
                if(maps[i].charAt(j)=='S') {
                    y=i;
                    x=j;
                }
            }
        }
        
        int a=bfs(maps, 'L');
        if(a <0) return -1;
        int b=bfs(maps, 'E');
        if(b <0) return -1;
        answer=(a+b);
        return answer-2;
    }
    
    int bfs(String[] maps, char target) {
        
        int[][] visited=new int[maps.length][maps[0].length()];
        Queue<int[]> queue=new LinkedList<>();
        
        queue.offer(new int[]{y,x});
        visited[y][x]=1;
        while(!queue.isEmpty()) {
            int[] pos=queue.poll();
            y=pos[0];
            x=pos[1];
            System.out.println("y : " + y + ", x : " + x);
            
            for(int i=0;i<4;i++) {
                int ny=y+dy[i];
                int nx=x+dx[i];
                
                // out of boundary
                if(ny<0 || ny>=maps.length || nx<0 || nx>=maps[0].length()) continue;
                
                // not visited and not a wall
                if(visited[ny][nx]==0 && maps[ny].charAt(nx)!='X') {
                    visited[ny][nx]=visited[y][x]+1;
                    // queue.offer(new int[] {ny,nx});
                    queue.offer(new int[]{ny,nx});
                    if (maps[ny].charAt(nx)==target) { 
                        y=ny;
                        x=nx;
                        return visited[ny][nx];
                    }
                }
                
            }
            
            
        }
        
        
        return -1;
    }
}