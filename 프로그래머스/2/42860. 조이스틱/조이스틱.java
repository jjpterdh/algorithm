import java.util.*;
class Solution {
    public int solution(String name) {
    
        String alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        int answer = 0;
        int move=name.length()-1;
        int length=0;
        for(int i=0;i<name.length();i++) {
            int index= alpha.indexOf(name.charAt(i));
            int count=Math.min(index, alpha.length()-index);
            answer+=count;
            if (i < name.length() - 1 && name.charAt(i + 1) == 'A') {
                int endA = i + 1;
                while(endA < name.length() && name.charAt(endA) == 'A')
                    endA++;
                move = Math.min(move, i * 2 + (name.length() - endA));// 오른쪽으로 갔다 다시 왼쪽으로 꺾기
                move = Math.min(move, i + (name.length() - endA) * 2);// 왼쪽으로 갔다 다시 오른쪽으로 꺾기
            }
        }
        answer+=move;
        return answer;
    }
}