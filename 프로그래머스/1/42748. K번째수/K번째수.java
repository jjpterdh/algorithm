import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int i=0;
        for (int[] command : commands) {
            int[] sorted_arr= Arrays.copyOfRange(array, command[0]-1, command[1]);
            Arrays.sort(sorted_arr);
            answer[i++]=sorted_arr[command[2]-1];
        }
        return answer;
    }
}