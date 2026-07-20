/// 76. 最小覆盖子串
/// 滑动窗口 + 频率计数，时间复杂度 O(m+n)
pub fn min_window(s: &str, t: &str) -> String {
    if s.is_empty() || t.is_empty() {
        return String::new();
    }

    let s_bytes = s.as_bytes();
    let t_bytes = t.as_bytes();

    let mut need = [0usize; 128];
    let mut required = 0usize;
    for &b in t_bytes {
        if need[b as usize] == 0 {
            required += 1;
        }
        need[b as usize] += 1;
    }

    let mut window = [0usize; 128];
    let mut formed = 0usize;
    let mut left = 0usize;
    let mut best_left = 0usize;
    let mut best_length = usize::MAX;

    for right in 0..s_bytes.len() {
        let c = s_bytes[right] as usize;
        window[c] += 1;
        if need[c] > 0 && window[c] == need[c] {
            formed += 1;
        }

        while formed == required {
            let current_length = right - left + 1;
            if current_length < best_length {
                best_length = current_length;
                best_left = left;
            }

            let lc = s_bytes[left] as usize;
            window[lc] -= 1;
            if need[lc] > 0 && window[lc] < need[lc] {
                formed -= 1;
            }
            left += 1;
        }
    }

    if best_length == usize::MAX {
        return String::new();
    }
    s[best_left..best_left + best_length].to_string()
}

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        min_window(&s, &t)
    }
}