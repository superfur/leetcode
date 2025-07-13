import "sort"

func fourSum(nums []int, target int) [][]int {
    sort.Ints(nums)
    result := [][]int{}
    
    // 如果数组长度小于4，无法找到四数之和
    if len(nums) < 4 {
        return result
    }
    
    for i := 0; i < len(nums) - 3; i++ {
        if i > 0 && nums[i] == nums[i - 1] {
            continue
        }
        for j := i + 1; j < len(nums) - 2; j++ {
            if j > i + 1 && nums[j] == nums[j - 1] {
                continue
            }
            left := j + 1
            right := len(nums) - 1
            for left < right {
                // 使用int64来避免整数溢出
                sum := int64(nums[i]) + int64(nums[j]) + int64(nums[left]) + int64(nums[right])
                if sum == int64(target) {
                    result = append(result, []int{nums[i], nums[j], nums[left], nums[right]})
                    for left < right && nums[left] == nums[left + 1] {
                        left++
                    }
                    for left < right && nums[right] == nums[right - 1] {
                        right--
                    }
                    left++
                    right--
                } else if sum < int64(target) {
                    left++
                } else {
                    right--
                }
            }
        }
    }
    return result
}