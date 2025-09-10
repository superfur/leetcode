package main

import (
	"fmt"
	"sort"
)

// findSubstring 找到字符串s中所有串联子串的起始位置
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

// isEqual 比较两个切片是否相等（忽略顺序）
func isEqual(slice1, slice2 []int) bool {
	if len(slice1) != len(slice2) {
		return false
	}
	
	// 创建副本进行排序
	s1 := make([]int, len(slice1))
	s2 := make([]int, len(slice2))
	copy(s1, slice1)
	copy(s2, slice2)
	
	sort.Ints(s1)
	sort.Ints(s2)
	
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			return false
		}
	}
	
	return true
}

func main() {
	// 测试用例1
	s1 := "barfoothefoobarman"
	words1 := []string{"foo", "bar"}
	expected1 := []int{0, 9}
	result1 := findSubstring(s1, words1)
	fmt.Printf("测试用例1: s='%s', words=%v\n", s1, words1)
	fmt.Printf("期望结果: %v\n", expected1)
	fmt.Printf("实际结果: %v\n", result1)
	fmt.Printf("测试结果: %s\n", map[bool]string{true: "通过", false: "失败"}[isEqual(result1, expected1)])
	fmt.Println()
	
	// 测试用例2
	s2 := "wordgoodgoodgoodbestword"
	words2 := []string{"word", "good", "best", "word"}
	expected2 := []int{}
	result2 := findSubstring(s2, words2)
	fmt.Printf("测试用例2: s='%s', words=%v\n", s2, words2)
	fmt.Printf("期望结果: %v\n", expected2)
	fmt.Printf("实际结果: %v\n", result2)
	fmt.Printf("测试结果: %s\n", map[bool]string{true: "通过", false: "失败"}[isEqual(result2, expected2)])
	fmt.Println()
	
	// 测试用例3
	s3 := "barfoofoobarthefoobarman"
	words3 := []string{"bar", "foo", "the"}
	expected3 := []int{6, 9, 12}
	result3 := findSubstring(s3, words3)
	fmt.Printf("测试用例3: s='%s', words=%v\n", s3, words3)
	fmt.Printf("期望结果: %v\n", expected3)
	fmt.Printf("实际结果: %v\n", result3)
	fmt.Printf("测试结果: %s\n", map[bool]string{true: "通过", false: "失败"}[isEqual(result3, expected3)])
	fmt.Println()
	
	// 边界情况测试
	s4 := "a"
	words4 := []string{"a"}
	expected4 := []int{0}
	result4 := findSubstring(s4, words4)
	fmt.Printf("边界测试: s='%s', words=%v\n", s4, words4)
	fmt.Printf("期望结果: %v\n", expected4)
	fmt.Printf("实际结果: %v\n", result4)
	fmt.Printf("测试结果: %s\n", map[bool]string{true: "通过", false: "失败"}[isEqual(result4, expected4)])
	fmt.Println()
	
	// 空字符串测试
	s5 := ""
	words5 := []string{"a"}
	expected5 := []int{}
	result5 := findSubstring(s5, words5)
	fmt.Printf("空字符串测试: s='%s', words=%v\n", s5, words5)
	fmt.Printf("期望结果: %v\n", expected5)
	fmt.Printf("实际结果: %v\n", result5)
	fmt.Printf("测试结果: %s\n", map[bool]string{true: "通过", false: "失败"}[isEqual(result5, expected5)])
}
