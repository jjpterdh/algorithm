import java.util.*;

class Solution {
    // ArrayList<String> visited = new ArrayList<String>();
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        boolean[] visited= new boolean[words.length];
        Queue<WordState> queue = new LinkedList<>();
        queue.add(new WordState(begin, 0));
        
        
        for(int i=0;i<words.length;i++) {
            if(words[i].equals(begin)) visited[i]=true;
        }
        
        // 다른 글자 횟수대로 분리하기
        while(!queue.isEmpty()) {
            WordState state = queue.poll();
            
            if(state.word.equals(target)) {return state.count;}
            for(int i=0; i<words.length; i++) {
                if(!visited[i] && Level(words[i], state.word)==1) {
                    queue.add(new WordState(words[i], state.count+1));
                    visited[i] = true;
                }
            }

        }
        
        
        
        return answer;
    }
    
    public int dfs(String start, int level, int targetLevel) {
        
        return 0;
    }
    
    public int Level(String begin, String word) {
        int level=0;
        for(int i=0;i<begin.length();i++) {
            if(begin.charAt(i)!=word.charAt(i)) level++;
        }
        
        return level;
    }
    
    
}

class WordState {
    String word;
    int count;
    WordState(String word, int count) {
        this.word=word;
        this.count=count;
    }
}