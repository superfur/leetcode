use std::collections::{HashMap, HashSet};

impl Solution {
    /// 140. 单词拆分 II
    /// 记忆化回溯：dfs(start) 返回后缀 s[start..] 的所有拆分句子。
    /// 枚举第一个单词 s[start..end]（长度不超过字典最长单词），在字典里就把它拼到 dfs(end) 的每个句子前面；
    /// start == n 时返回 [""]，表示「恰好拆完」，拼接时据此决定要不要加空格。
    /// 按起点缓存结果，相同的后缀不会被重复展开（题目保证只有小写字母，按字节切片是安全的）。
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        fn dfs(
            start: usize,
            s: &str,
            words: &HashSet<&str>,
            max_len: usize,
            memo: &mut HashMap<usize, Vec<String>>,
        ) -> Vec<String> {
            let n = s.len();
            if start == n {
                return vec![String::new()];
            }
            if let Some(cached) = memo.get(&start) {
                return cached.clone();
            }

            let mut res = Vec::new();
            for end in (start + 1)..=n.min(start + max_len) {
                let word = &s[start..end];
                if words.contains(word) {
                    for tail in dfs(end, s, words, max_len, memo) {
                        if tail.is_empty() {
                            res.push(word.to_string());
                        } else {
                            res.push(format!("{} {}", word, tail));
                        }
                    }
                }
            }
            memo.insert(start, res.clone());
            res
        }

        let words: HashSet<&str> = word_dict.iter().map(|w| w.as_str()).collect();
        let max_len = word_dict.iter().map(|w| w.len()).max().unwrap_or(0);
        let mut memo = HashMap::new();
        dfs(0, &s, &words, max_len, &mut memo)
    }
}
