impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.is_empty() {
            return 0;
        }
        if haystack.is_empty() {
            return -1;
        }
        let haystack_len = haystack.len();
        let needle_len = needle.len();
        
        // 如果haystack长度小于needle长度，直接返回-1
        if haystack_len < needle_len {
            return -1;
        }
        
        for i in 0..haystack_len - needle_len + 1 {
            if haystack[i..i + needle_len] == needle {
                return i as i32;
            }
        }
        -1
    }
}