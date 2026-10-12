class Solution {
    /**
     * 128. 最长连续序列
     * 哈希集合去重，只从「序列起点」（x - 1 不在集合里）出发往后数 x+1, x+2, ...，
     * 每个数最多被数一次，所以整体 O(n)。
     */
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int x : nums) {
            set.add(x);
        }

        int best = 0;
        for (int x : set) {
            if (set.contains(x - 1)) {
                continue;
            }
            int end = x;
            while (set.contains(end + 1)) {
                end++;
            }
            best = Math.max(best, end - x + 1);
        }
        return best;
    }
}
