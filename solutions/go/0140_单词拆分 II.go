package main

// 140. 单词拆分 II
// 记忆化回溯：dfs(start) 返回后缀 s[start:] 的所有拆分句子。
// 枚举第一个单词 s[start:end]（长度不超过字典最长单词），在字典里就把它拼到 dfs(end) 的每个句子前面；
// start == n 时返回 [""]，表示「恰好拆完」，拼接时据此决定要不要加空格。
// 按起点缓存结果，相同的后缀不会被重复展开。
func wordBreak(s string, wordDict []string) []string {
	words := make(map[string]bool, len(wordDict))
	maxLen := 0
	for _, w := range wordDict {
		words[w] = true
		if len(w) > maxLen {
			maxLen = len(w)
		}
	}
	n := len(s)
	memo := map[int][]string{}

	var dfs func(start int) []string
	dfs = func(start int) []string {
		if start == n {
			return []string{""}
		}
		if cached, ok := memo[start]; ok {
			return cached
		}
		res := []string{}
		for end := start + 1; end <= n && end <= start+maxLen; end++ {
			word := s[start:end]
			if !words[word] {
				continue
			}
			for _, tail := range dfs(end) {
				if tail == "" {
					res = append(res, word)
				} else {
					res = append(res, word+" "+tail)
				}
			}
		}
		memo[start] = res
		return res
	}

	return dfs(0)
}
