/**
 * 80. 删除有序数组中的重复项 II
 * 给定有序数组 nums，原地删除重复元素使每个元素最多出现两次，
 * 返回新长度。前 length 项即为结果。
 * 快慢双指针：slow 表示下一个写入位置，
 * 通用条件：slow < 2 或 nums[fast] !== nums[slow - 2]。
 */
function removeDuplicates(nums: number[]): number {
    const k = 2;
    let slow = 0;
    for (let fast = 0; fast < nums.length; fast++) {
        if (slow < k || nums[fast] !== nums[slow - k]) {
            nums[slow] = nums[fast];
            slow++;
        }
    }
    return slow;
}

export default removeDuplicates;