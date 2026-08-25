/// 93. 复原 IP 地址
/// 回溯：依次切出长度 1~3 的一段作为一个 IP 段，
/// 段值需在 0~255 之间且不能有前导 0（除了单独的 "0"）；
/// 切出 4 段且恰好用完所有字符时才是一个合法答案。
pub fn restore_ip_addresses(s: String) -> Vec<String> {
    let bytes = s.as_bytes();
    let n = bytes.len();
    let mut result: Vec<String> = Vec::new();
    let mut segments: Vec<String> = Vec::new();

    fn backtrack(bytes: &[u8], start: usize, segments: &mut Vec<String>, result: &mut Vec<String>) {
        let n = bytes.len();
        if segments.len() == 4 {
            if start == n {
                result.push(segments.join("."));
            }
            return;
        }
        if n - start > (4 - segments.len()) * 3 {
            return;
        }
        for length in 1..=3 {
            if start + length > n {
                break;
            }
            let segment = std::str::from_utf8(&bytes[start..start + length]).unwrap();
            if length > 1 && segment.starts_with('0') {
                break;
            }
            let val: u32 = segment.parse().unwrap();
            if val > 255 {
                break;
            }
            segments.push(segment.to_string());
            backtrack(bytes, start + length, segments, result);
            segments.pop();
        }
    }

    backtrack(bytes, 0, &mut segments, &mut result);
    result
}

impl Solution {
    pub fn restore_ip_addresses(s: String) -> Vec<String> {
        restore_ip_addresses(s)
    }
}
