/**
 * 两数之和
 * @param nums 整数数组
 * @param target 目标值
 * @return 两个数的索引
 */
func twoSum(nums []int, target int) []int {
    // 创建一个map来存储数字和对应的索引
    numMap := make(map[int]int)

    // 遍历数组
    for i, num := range nums {
        // 计算需要查找的补数
        complement := target - num
        // 如果补数在map中存在，返回两个数的索引
        if index, exists := numMap[complement]; exists {
            return []int{index, i}
        }
        // 将当前数字和索引存入map
        numMap[num] = i
    }
    // 如果没有找到解，返回空切片
    return []int{}
}
