impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::new();
        }
        let mut prefix = strs[0].clone();
        for i in 1..strs.len() {
            while !strs[i].starts_with(&prefix) {
                prefix = prefix.chars().take(prefix.len() - 1).collect();
            }
        }
        prefix
    }
}