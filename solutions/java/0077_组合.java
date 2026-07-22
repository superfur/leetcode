import java.util.ArrayList;
import java.util.List;

public class Solution {
    /**
     * 77. 组合
     * 回溯 + 剪枝，返回 [1, n] 中所有 k 个数的组合
     */
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(1, n, k, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, int n, int k, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == k) {
            result.add(new ArrayList<>(path));
            return;
        }
        // 剪枝: i 最大值 = n - (k - path.size()) + 1
        int upper = n - (k - path.size()) + 1;
        for (int i = start; i <= upper; i++) {
            path.add(i);
            backtrack(i + 1, n, k, path, result);
            path.remove(path.size() - 1);
        }
    }
}
