package main

// 131. 分割回文串
// 先用区间 DP 预处理 isPal[i][j]（s[i..j] 是否回文），
// 再回溯：从位置 start 开始，枚举每个能切出回文前缀 s[start..end] 的位置，
// 选中后递归处理 end + 1，走到字符串末尾就收集一个方案。
func partition(s string) [][]string {
	n := len(s)
	isPal := make([][]bool, n)
	for i := range isPal {
		isPal[i] = make([]bool, n)
		for j := range isPal[i] {
			isPal[i][j] = true
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			isPal[i][j] = s[i] == s[j] && isPal[i+1][j-1]
		}
	}

	res := [][]string{}
	path := []string{}

	var back func(start int)
	back = func(start int) {
		if start == n {
			cp := make([]string, len(path))
			copy(cp, path)
			res = append(res, cp)
			return
		}
		for end := start; end < n; end++ {
			if isPal[start][end] {
				path = append(path, s[start:end+1])
				back(end + 1)
				path = path[:len(path)-1]
			}
		}
	}

	back(0)
	return res
}
