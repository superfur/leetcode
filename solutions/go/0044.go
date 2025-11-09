func isMatch(s string, p string) bool {
	i, j := 0, 0           // i: s 的指针，j: p 的指针
	starIdx := -1          // 记录最近出现的 '*' 在模式中的位置
	match := 0             // 记录当匹配失败回溯时，s 中的匹配起点
	m, n := len(s), len(p) // 字符串和模式的长度

	for i < m {
		if j < n && (p[j] == s[i] || p[j] == '?') {
			// 字符相同或模式为 '?'，双指针同时前进
			i++
			j++
		} else if j < n && p[j] == '*' {
			// 记录 '*' 的位置，并尝试让 '*' 匹配空串
			starIdx = j
			match = i
			j++
		} else if starIdx != -1 {
			// 模式当前字符无法匹配，但之前出现过 '*'
			// 回溯：让 '*' 多匹配一个字符
			j = starIdx + 1
			match++
			i = match
		} else {
			return false
		}
	}

	// s 已经匹配完，p 剩余的字符必须全部为 '*'
	for j < n && p[j] == '*' {
		j++
	}

	return j == n
}