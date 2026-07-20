package main

// 76. 最小覆盖子串
// 滑动窗口 + 频率计数，时间复杂度 O(m+n)
func minWindow(s string, t string) string {
	if len(t) == 0 || len(s) == 0 {
		return ""
	}

	need := make(map[byte]int)
	for i := 0; i < len(t); i++ {
		need[t[i]]++
	}

	required := len(need)
	formed := 0
	left := 0
	bestLeft := 0
	bestLength := len(s) + 1
	windowCount := make(map[byte]int)

	for right := 0; right < len(s); right++ {
		c := s[right]
		windowCount[c]++

		if want, ok := need[c]; ok && windowCount[c] == want {
			formed++
		}

		for formed == required && left <= right {
			currentLength := right - left + 1
			if currentLength < bestLength {
				bestLength = currentLength
				bestLeft = left
			}

			leftChar := s[left]
			windowCount[leftChar]--
			if want, ok := need[leftChar]; ok && windowCount[leftChar] < want {
				formed--
			}
			left++
		}
	}

	if bestLength == len(s)+1 {
		return ""
	}
	return s[bestLeft : bestLeft+bestLength]
}
