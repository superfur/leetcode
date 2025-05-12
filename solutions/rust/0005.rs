impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let s = s.as_bytes();
        let n = s.len();
        if n <= 1 {
            return String::from_utf8(s.to_vec()).unwrap();
        }
        let mut max_len = 1;
        let mut begin = 0;
        let mut dp = vec![vec![false; n]; n];
        for i in 0..n {
            dp[i][i] = true;
        }
        for j in 1..n {
            for i in 0..j {
                if s[i] != s[j] {
                    dp[i][j] = false;
                } else {
                    if j - i < 3 {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                    if dp[i][j] && j - i + 1 > max_len {
                        max_len = j - i + 1;
                        begin = i;
                    }
                }
            }
        }
        String::from_utf8(s[begin..begin + max_len].to_vec()).unwrap()
    }
}