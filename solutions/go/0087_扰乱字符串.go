package main

// 87. 扰乱字符串
// 回溯枚举分割点 i：要么 s1[:i]/s1[i:] 与 s2[:i]/s2[i:] 同步扰乱，
// 要么 s1[:i]/s1[i:] 与 s2[n-i:]/s2[:n-i]（交换）同步扰乱。
// 剪枝：字符计数不等直接返回 false；用 map 记忆化。
func isScramble(s1 string, s2 string) bool {
	type pair struct{ a, b string }
	memo := make(map[pair]bool)

	var dfs func(a, b string) bool
	dfs = func(a, b string) bool {
		if v, ok := memo[pair{a, b}]; ok {
			return v
		}
		if a == b {
			memo[pair{a, b}] = true
			return true
		}
		// 字符计数剪枝
		var cnt [26]int
		for i := 0; i < len(a); i++ {
			cnt[a[i]-'a']++
			cnt[b[i]-'a']--
		}
		if cnt != [26]int{} {
			memo[pair{a, b}] = false
			return false
		}
		n := len(a)
		for i := 1; i < n; i++ {
			// 不交换
			if dfs(a[:i], b[:i]) && dfs(a[i:], b[i:]) {
				memo[pair{a, b}] = true
				return true
			}
			// 交换
			if dfs(a[:i], b[n-i:]) && dfs(a[i:], b[:n-i]) {
				memo[pair{a, b}] = true
				return true
			}
		}
		memo[pair{a, b}] = false
		return false
	}

	return dfs(s1, s2)
}