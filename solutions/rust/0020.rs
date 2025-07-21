use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        let map: HashMap<char, char> = HashMap::from([
            ('(', ')'),
            ('{', '}'),
            ('[', ']')
        ]);
        for c in s.chars() {
            if map.contains_key(&c) {
                stack.push(c);
            } else if stack.len() > 0 && map[&stack[stack.len() - 1]] == c {
                stack.pop();
            } else {
                return false;
            }
        }
        stack.is_empty()
    }
}