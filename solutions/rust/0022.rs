impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut result = Vec::new();
        let mut current = String::new();
        Self::generate(n, 0, 0, &mut current, &mut result);
        result
    }

    fn generate(n: i32, left: i32, right: i32, current: &mut String, result: &mut Vec<String>) {
        if current.len() == n as usize * 2 {
            result.push(current.clone());
            return;
        }
        if left < n {
            current.push('(');
            Self::generate(n, left + 1, right, current, result);
            current.pop();
        }
        if right < left {
            current.push(')');
            Self::generate(n, left, right + 1, current, result);
            current.pop();
        }
    }
}