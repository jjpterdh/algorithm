import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
class Solution {
    int attribute;
    int tuple;
    HashSet<List<Integer>> candidates;
    String[][] relation;
    public int solution(String[][] relation) {
        this.relation = relation;
        candidates = new HashSet<>();
        tuple = relation.length;
        attribute = relation[0].length;

        // 속성 수 계산하기
        for (int k = 1; k <= attribute; k++) {
            findCombinations(0, k, new ArrayList<>());
        }
        return candidates.size();
    }

    void findCombinations(int start, int k, List<Integer> current) {
        if (current.size() == k) {
            if (isUnique(current) && isMin(current)) {
                candidates.add(new ArrayList<>(current));
            }
            return;
        }

        for (int i = start; i < attribute; i++) {
            current.add(i);
            findCombinations(i + 1, k, current);
            current.remove(current.size() - 1);
        }
    }

    boolean isUnique(List<Integer> current) {
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < tuple; i++) {
            StringBuilder sb = new StringBuilder();
            for (int index : current) {
                sb.append(relation[i][index]);
            }
            set.add(sb.toString());
        }
        return set.size() == tuple;
    }

    boolean isMin(List<Integer> cur) {
        for (List<Integer> candidate : candidates) {
            if (cur.containsAll(candidate)) {
                return false;
            }
        }
        return true;
    }
}