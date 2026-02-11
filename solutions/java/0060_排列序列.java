import java.util.ArrayList;
import java.util.List;

public class Solution {
    /**
     * 返回字典序第 k 个由 1..n 组成的排列（1-indexed）
     */
    public String getPermutation(int n, int k) {
        if (n <= 0 || k <= 0) return "";

        int[] fact = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
        if (k > fact[n]) return "";

        List<Integer> nums = new ArrayList<>();
        for (int i = 1; i <= n; i++) nums.add(i);

        k--; // 转为 0-index
        StringBuilder sb = new StringBuilder();
        for (int i = n; i >= 1; i--) {
            int f = fact[i - 1];
            int idx = k / f;
            sb.append(nums.get(idx));
            nums.remove(idx);
            k = k % f;
        }

        return sb.toString();
    }

    /**
     * 中文包装方法，保留原接口风格
     */
    public String 排列序列(int n, int k) {
        return getPermutation(n, k);
    }
}
