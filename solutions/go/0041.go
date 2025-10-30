func firstMissingPositive(nums []int) int {
    n := len(nums)

    // 第一步：将每个数字放到它应该在的位置（数字 i 放到索引 i-1）
    for i := 0; i < n; i++ {
        // 持续把 nums[i] 放到正确位置，直到不需要或不在范围内
        for nums[i] > 0 && nums[i] <= n && nums[nums[i]-1] != nums[i] {
            target := nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]
        }
    }

    // 第二步：找到第一个不满足 nums[i] == i+1 的位置
    for i := 0; i < n; i++ {
        if nums[i] != i+1 {
            return i + 1
        }
    }

    return n + 1
}