package main

import "strconv"

// 93. 复原 IP 地址
// 回溯：依次切出长度 1~3 的一段作为一个 IP 段，
// 段值需在 0~255 之间且不能有前导 0（除了单独的 "0"）；
// 切出 4 段且恰好用完所有字符时才是一个合法答案。
func restoreIpAddresses(s string) []string {
	n := len(s)
	var result []string
	var segments []string

	var backtrack func(start int)
	backtrack = func(start int) {
		if len(segments) == 4 {
			if start == n {
				result = append(result, segments[0]+"."+segments[1]+"."+segments[2]+"."+segments[3])
			}
			return
		}
		if n-start > (4-len(segments))*3 {
			return
		}
		for length := 1; length <= 3 && start+length <= n; length++ {
			segment := s[start : start+length]
			if length > 1 && segment[0] == '0' {
				break
			}
			val, _ := strconv.Atoi(segment)
			if val > 255 {
				break
			}
			segments = append(segments, segment)
			backtrack(start + length)
			segments = segments[:len(segments)-1]
		}
	}

	backtrack(0)
	return result
}
