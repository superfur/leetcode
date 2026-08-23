/// 91. 解码方法
/// 动态规划：dp[i] 表示 s[..i] 的解码方法数。
/// 单字符有效（非 '0'）时可从 dp[i-1] 转移；
/// 双字符在 10~26 之间时可从 dp[i-2] 转移。
/// 用两个变量滚动即可，无需数组。
pub fn num_decodings(s: String) -> i32 {
    let bytes = s.as_bytes();
    let n = bytes.len();
    let mut prev2: i32 = 1;
    let mut prev1: i32 = if bytes[0] != b'0' { 1 } else { 0 };

    for i in 2..=n {
        let mut cur = 0;
        if bytes[i - 1] != b'0' {
            cur += prev1;
        }
        let two_digit = (bytes[i - 2] - b'0') as i32 * 10 + (bytes[i - 1] - b'0') as i32;
        if (10..=26).contains(&two_digit) {
            cur += prev2;
        }
        prev2 = prev1;
        prev1 = cur;
    }

    prev1
}

impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        num_decodings(s)
    }
}
