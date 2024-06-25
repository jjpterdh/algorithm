class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] cries = {"aya", "ye", "woo", "ma"};
        for(String b : babbling) {
            for (String c : cries) {
                if (c.equals("aya")) {
                    b=b.replace("aya", "*");
                }
                else if (c.equals("ye")) {
                    b=b.replace("ye", "!");
                }
                else if(c.equals("woo")) {
                    b=b.replace("woo", "@");
                }
                else if(c.equals("ma")) {
                    b=b.replace("ma", "#");
                }
            }
            char prev_alpha=b.charAt(0);
            boolean flag=true;

            if(prev_alpha!='*'&&prev_alpha!='!' && prev_alpha !='@' && prev_alpha!='#') {

//                System.out.println("prev_alpha: "+prev_alpha);
                flag=false;
            }
            for (int i=1; i<b.length(); i++) {

                if (prev_alpha==b.charAt(i)) {
                    flag=false;
                    break;
                } else if (b.charAt(i)!='*' && b.charAt(i)!='!' && b.charAt(i) !='@' && b.charAt(i)!='#') {
                    flag=false;
                    break;
                }
                prev_alpha=b.charAt(i);
            }

            if(flag) {
                answer++;
//                System.out.println(b);
            }
        }
        return answer;
    }
}