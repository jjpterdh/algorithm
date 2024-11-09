class Solution
{
    
    public int solution(String s)
    {
        for(int i = s.length(); i > 0; i--) { //팰린드롬의 길이
            for(int j = 0; j + i <= s.length(); j++) { // j는 팰린드롬 검사를 시작할 위치
                boolean isPalindrome = true;
                for(int k = 0; k < i / 2; k++) { // 팰린드롬을 검사할 횟수
                    if(s.charAt(j + k) != s.charAt(j + i - k - 1)) {
                        isPalindrome = false;
                        break;
                    }
                }
                if(isPalindrome) return i;
            }
        }
        return 1;
    }
    
    
}