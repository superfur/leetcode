public class Solution {
    /**
     * 75. 颜色分类
     * 荷兰国旗算法，三指针一趟扫描原地排序
     * Do not return anything, modify nums in-place instead.
     */
    public void sortColors(int[] nums) {
        int low = 0;
        int current = 0;
        int high = nums.length - 1;

        while (current <= high) {
            if (nums[current] == 0) {
                int tmp = nums[low];
                nums[low] = nums[current];
                nums[current] = tmp;
                low++;
                current++;
            } else if (nums[current] == 2) {
                int tmp = nums[current];
                nums[current] = nums[high];
                nums[high] = tmp;
                high--;
            } else {
                current++;
            }
        }
    }
}
