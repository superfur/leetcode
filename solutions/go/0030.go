// findSubstring 找到字符串s中所有串联子串的起始位置
//
// 思路：
// 1. 使用滑动窗口遍历字符串s
// 2. 对于每个窗口，检查是否包含words中的所有字符串
// 3. 使用map记录words中每个字符串的出现次数
// 4. 维护当前窗口中的字符串计数
//
// 时间复杂度：O(n * m)，其中n是s的长度，m是words的长度
// 空间复杂度：O(m)
func findSubstring(s string, words []string) []int {
	var result []int
	
	// 边界情况处理
	if len(s) == 0 || len(words) == 0 || len(words[0]) == 0 {
		return result
	}
	
	wordLen := len(words[0])  // 每个单词的长度
	wordCount := len(words)   // 单词数量
	totalLen := wordLen * wordCount  // 目标子串的总长度
	
	// 如果s长度小于目标长度，直接返回空数组
	if len(s) < totalLen {
		return result
	}
	
	// 统计words中每个字符串的出现次数
	wordFreq := make(map[string]int)
	for _, word := range words {
		wordFreq[word]++
	}
	
	// 只需要检查前wordLen个起始位置
	// 因为后续位置会被前面的滑动窗口覆盖
	for i := 0; i < wordLen; i++ {
		left := i
		right := i
		currentFreq := make(map[string]int)  // 当前窗口中的字符串计数
		
		// 滑动窗口遍历
		for right+wordLen <= len(s) {
			// 获取当前单词
			currentWord := s[right : right+wordLen]
			right += wordLen
			
			// 如果当前单词不在words中，重置窗口
			if _, exists := wordFreq[currentWord]; !exists {
				// 清空当前频率映射
				for k := range currentFreq {
					delete(currentFreq, k)
				}
				left = right
			} else {
				currentFreq[currentWord]++
				
				// 如果当前单词出现次数超过words中的次数，移动左边界
				for currentFreq[currentWord] > wordFreq[currentWord] {
					leftWord := s[left : left+wordLen]
					currentFreq[leftWord]--
					left += wordLen
				}
				
				// 如果窗口大小等于words的总长度，找到一个有效子串
				if right-left == totalLen {
					result = append(result, left)
				}
			}
		}
	}
	
	return result
}