use std::collections::HashSet;

impl Solution {
    /// 139. 单词拆分
    /// dp[i] 表示 s 的前 i 个字符能否被拆成字典里的单词（dp[0] = true）。
    /// 对每个 i 枚举「最后一个单词」的起点 j：dp[j] 为真且 s[j..i] 在字典里，则 dp[i] 为真。
    /// 字典里最长的单词长度为 max_len，所以 j 只需要从 i - max_len 开始往后枚举，
    /// 用集合判断单词是否存在（题目保证只有小写字母，按字节切片是安全的）。
    /// 时间 O(n * max_len * max_len)。
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let words: HashSet<&str> = word_dict.iter().map(|w| w.as_str()).collect();
        let max_len = word_dict.iter().map(|w| w.len()).max().unwrap_or(0);

        let n = s.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;
        for i in 1..=n {
            let start = i.saturating_sub(max_len);
            for j in start..i {
                if dp[j] && words.contains(&s[j..i]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        dp[n]
    }
}
