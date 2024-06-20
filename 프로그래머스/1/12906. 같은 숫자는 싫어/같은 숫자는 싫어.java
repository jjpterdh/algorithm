import java.util.*;

public class Solution {
    public static Object[] solution(int []arr) {
//        int[] answer = {};
//        ArrayList<Integer> answer=new ArrayList<Integer>();
        Stack<Integer> stack = new Stack<>();
        stack.push(arr[0]);
        int n=arr.length;

        for(int i=1;i<n;i++){
            if(stack.peek()==arr[i]){
                continue;
            }
            else {
                stack.push(arr[i]);
            }
        }

        Object[] answer=stack.toArray();


        return answer;
    }
}