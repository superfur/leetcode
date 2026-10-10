use std::collections::HashSet;

impl Solution {
    /// 127. 单词接龙
    /// BFS：从 beginWord 出发，每次把某一位换成 a~z，命中字典的单词就入队，
    /// 并立刻从字典里删掉（等价于标记已访问）。
    /// 第一次碰到 endWord 时的步数（按单词个数计，起点算 1）就是答案。
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        let mut words: HashSet<String> = word_list.into_iter().collect();
        if !words.contains(&end_word) {
            return 0;
        }

        words.remove(&begin_word);
        let mut level: Vec<String> = vec![begin_word];
        let mut steps = 1;

        while !level.is_empty() {
            let mut next: Vec<String> = Vec::new();
            for word in &level {
                let mut chars: Vec<u8> = word.bytes().collect();
                for i in 0..chars.len() {
                    let orig = chars[i];
                    for c in b'a'..=b'z' {
                        if c == orig {
                            continue;
                        }
                        chars[i] = c;
                        let nw = String::from_utf8(chars.clone()).unwrap();
                        if words.contains(&nw) {
                            if nw == end_word {
                                return steps + 1;
                            }
                            words.remove(&nw);
                            next.push(nw);
                        }
                    }
                    chars[i] = orig;
                }
            }
            level = next;
            steps += 1;
        }
        0
    }
}
