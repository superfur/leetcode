public class Solution {
    /**
     * 90. 子集 II
     * 排序 + 回溯：同一层若 nums[i] == nums[i-1] 则跳过，避免重复子集。
     */
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        java.util.Arrays.sort(nums);
        List<List<Integer>> result = new java.util.ArrayList<>();
        List<Integer> path = new java.util.ArrayList<>();
        backtrack(nums, 0, path, result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<Integer> path, List<List<Integer>> result) {
        result.add(new java.util.ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            path.add(nums[i]);
            backtrack(nums, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }
}