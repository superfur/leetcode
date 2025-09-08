use std::collections::HashMap;

impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        if s.is_empty() || words.is_empty() {
            return vec![];
        }
        
        let word_len = words[0].len();
        let total_len = words.len() * word_len;
        let mut result = Vec::new();
        
        // 创建words的计数映射
        let mut word_count = HashMap::new();
        for word in &words {
            *word_count.entry(word.as_str()).or_insert(0) += 1;
        }
        
        // 使用滑动窗口优化：只需要检查 word_len 个不同的起始位置
        for start in 0..word_len {
            if start + total_len > s.len() {
                break;
            }
            
            let mut current_count = HashMap::new();
            let mut matched = 0;
            let mut left = start;
            
            // 初始化窗口
            for i in 0..words.len() {
                let word_start = start + i * word_len;
                let word_end = word_start + word_len;
                
                if word_end > s.len() {
                    break;
                }
                
                let word = &s[word_start..word_end];
                
                if word_count.contains_key(word) {
                    *current_count.entry(word).or_insert(0) += 1;
                    if current_count[word] <= word_count[word] {
                        matched += 1;
                    }
                }
            }
            
            if matched == words.len() {
                result.push(start as i32);
            }
            
            // 滑动窗口
            while left + total_len + word_len <= s.len() {
                // 移除左边的单词
                let left_word = &s[left..left + word_len];
                if word_count.contains_key(left_word) {
                    if current_count[left_word] <= word_count[left_word] {
                        matched -= 1;
                    }
                    *current_count.get_mut(left_word).unwrap() -= 1;
                }
                
                // 添加右边的单词
                let right_start = left + total_len;
                let right_word = &s[right_start..right_start + word_len];
                if word_count.contains_key(right_word) {
                    *current_count.entry(right_word).or_insert(0) += 1;
                    if current_count[right_word] <= word_count[right_word] {
                        matched += 1;
                    }
                }
                
                left += word_len;
                
                if matched == words.len() {
                    result.push(left as i32);
                }
            }
        }
        
        result
    }
}