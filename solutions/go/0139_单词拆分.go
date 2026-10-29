package main

// 139. 单词拆分
// dp[i] 表示 s 的前 i 个字符能否被拆成字典里的单词（dp[0] = true）。
// 对每个 i 枚举「最后一个单词」的起点 j：dp[j] 为真且 s[j:i] 在字典里，则 dp[i] 为真。
// 字典里最长的单词长度为 maxLen，所以 j 只需要从 i - maxLen 开始往后枚举，
// 用 map 判断单词是否存在。时间 O(n * maxLen * maxLen)。
func wordBreak(s string, wordDict []string) bool {
	words := make(map[string]bool, len(wordDict))
	maxLen := 0
	for _, w := range wordDict {
		words[w] = true
		if len(w) > maxLen {
			maxLen = len(w)
		}
	}

	n := len(s)
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i <= n; i++ {
		start := i - maxLen
		if start < 0 {
			start = 0
		}
		for j := start; j < i; j++ {
			if dp[j] && words[s[j:i]] {
				dp[i] = true
				break
			}
		}
	}
	return dp[n]
}
