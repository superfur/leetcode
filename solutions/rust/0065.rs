impl Solution {
    pub fn is_number(s: String) -> bool {
        let s = s.trim();
        if s.is_empty() {
            return false;
        }
        let mut seen_digit = false;
        let mut seen_dot = false;
        let mut seen_exp = false;
        let chars: Vec<char> = s.chars().collect();
        for i in 0..chars.len() {
            let ch = chars[i];
            if ch == '+' || ch == '-' {
                if i > 0 && chars[i - 1] != 'e' && chars[i - 1] != 'E' {
                    return false;
                }
            } else if ch == '.' {
                if seen_dot || seen_exp {
                    return false;
                }
                seen_dot = true;
            } else if ch == 'e' || ch == 'E' {
                if seen_exp || !seen_digit {
                    return false;
                }
                seen_exp = true;
                seen_digit = false;
            } else if ch.is_ascii_digit() {
                seen_digit = true;
            } else {
                return false;
            }
        }
        seen_digit
    }
}
