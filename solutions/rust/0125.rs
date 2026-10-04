impl Solution {
    /// 125. 验证回文串
    /// 双指针：左右两端向中间走，跳过非字母数字字符，
    /// 其余字符忽略大小写后逐个比较，不一致就不是回文。
    /// 注：下标用 isize，因为 right 可能被跳到 0 之后再减 1，用 usize 会下溢。
    pub fn is_palindrome(s: String) -> bool {
        let bytes = s.as_bytes();
        let (mut left, mut right) = (0isize, bytes.len() as isize - 1);
        while left < right {
            while left < right && !bytes[left as usize].is_ascii_alphanumeric() {
                left += 1;
            }
            while left < right && !bytes[right as usize].is_ascii_alphanumeric() {
                right -= 1;
            }
            if bytes[left as usize].to_ascii_lowercase() != bytes[right as usize].to_ascii_lowercase() {
                return false;
            }
            left += 1;
            right -= 1;
        }
        true
    }
}
