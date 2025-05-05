use std::collections::HashMap;
use std::cmp::max;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut char_map = HashMap::new();
        let mut max_length = 0;
        let mut left = 0;

        for (right, char) in s.chars().enumerate() {
            if char_map.contains_key(&char) {
                left = max(char_map[&char] + 1, left);
            }
            char_map.insert(char, right);
            max_length = max(max_length, right - left + 1);
        }
        max_length as i32
    }
}