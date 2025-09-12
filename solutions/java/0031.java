class Solution {
    /**
     * 下一个排列算法
     * 
     * 算法步骤：
     * 1. 从右往左找到第一个满足 nums[i] < nums[i+1] 的位置 i
     * 2. 从右往左找到第一个满足 nums[j] > nums[i] 的位置 j  
     * 3. 交换 nums[i] 和 nums[j]
     * 4. 反转从位置 i+1 到数组末尾的部分
     */
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        if (n <= 1) {
            return;
        }
        
        // 步骤1: 从右往左找到第一个满足 nums[i] < nums[i+1] 的位置 i
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // 如果找不到这样的位置，说明整个数组是降序的，直接反转整个数组
        if (i == -1) {
            reverse(nums, 0, n - 1);
            return;
        }
        
        // 步骤2: 从右往左找到第一个满足 nums[j] > nums[i] 的位置 j
        int j = n - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        
        // 步骤3: 交换 nums[i] 和 nums[j]
        swap(nums, i, j);
        
        // 步骤4: 反转从位置 i+1 到数组末尾的部分
        reverse(nums, i + 1, n - 1);
    }
    
    /**
     * 交换数组中两个位置的元素
     */
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    /**
     * 反转数组中从 start 到 end 的部分
     */
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
}