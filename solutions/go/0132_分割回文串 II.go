package main

// 132. 分割回文串 II
// 先用区间 DP 预处理 isPal[i][j]（s[i..j] 是否回文）；
// 再令 dp[i] 为 s[0..i] 的最少分割次数：
// 若 s[0..i] 本身是回文则为 0，否则枚举最后一段回文 s[j+1..i]，取 dp[j] + 1 的最小值。
// 时间 O(n^2)。
func minCut(s string) int {
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

	dp := make([]int, n)
	for i := 0; i < n; i++ {
		if isPal[0][i] {
			dp[i] = 0
			continue
		}
		best := i
		for j := 0; j < i; j++ {
			if isPal[j+1][i] && dp[j]+1 < best {
				best = dp[j] + 1
			}
		}
		dp[i] = best
	}
	return dp[n-1]
}
