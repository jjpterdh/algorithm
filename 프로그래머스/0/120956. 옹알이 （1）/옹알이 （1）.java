class Solution {
    public int solution(String[] babbling) {
       int answer = 0;
        String[] cries = {"aya", "ye", "woo", "ma"};
        for(String b : babbling) {
            for (String c : cries) {
                b=b.replace(c, " ");
            }
            b=b.strip();
            if (b.length()==0) {
                answer += 1;
            }
        }
        return answer;
    }
}