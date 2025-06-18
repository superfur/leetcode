impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let m = s.len();
        let n = p.len();

        let mut dp = vec![vec![false; n + 1]; m + 1];
        dp[0][0] = true;

        for i in 0..=m {
            for j in 1..=n {
                if p.chars().nth(j - 1).unwrap() == '*' {
                    dp[i][j] = dp[i][j - 2] || (i > 0 && (s.chars().nth(i - 1).unwrap() == p.chars().nth(j - 2).unwrap() || p.chars().nth(j - 2).unwrap() == '.') && dp[i - 1][j]);
                } else {
                    dp[i][j] = i > 0 && (s.chars().nth(i - 1).unwrap() == p.chars().nth(j - 1).unwrap() || p.chars().nth(j - 1).unwrap() == '.') && dp[i - 1][j - 1];
                }
            }
        }
        dp[m][n]
    }
}