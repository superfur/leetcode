package main

func lengthOfLongestSubstring(s string) int {
    // 使用 map 存储字符最后出现的位置
    charMap := make(map[rune]int)
    maxLength := 0
    left := 0

    // 遍历字符串
    for right, char := range s {
        // 如果字符已经在 map 中，更新左边界
        if lastPos, exists := charMap[char]; exists {
            if lastPos+1 > left {
                left = lastPos + 1
            }
        }
        // 更新字符位置
        charMap[char] = right
        // 更新最大长度
        if right-left+1 > maxLength {
            maxLength = right - left + 1
        }
    }
    return maxLength
}
