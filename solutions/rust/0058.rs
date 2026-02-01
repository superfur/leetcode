impl Solution {
    /*
     * 最后一个单词的长度
     *
     * 时间复杂度: O(n)，其中 n 为字符串长度
     * 空间复杂度: O(1)
     *
     * 思路: 从字符串末尾向前遍历
     * 1. 跳过末尾的空格
     * 2. 从非空格字符开始计数，直到遇到空格或到达字符串开头
     *
     * 示例:
     * s = "   fly me   to   the moon  " -> 4 (moon)
     */
    pub fn length_of_last_word(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut i = bytes.len();

        // 跳过末尾空格
        while i > 0 && bytes[i - 1] == b' ' {
            i -= 1;
        }

        let start = i;

        // 统计最后一个单词的长度
        while i > 0 && bytes[i - 1] != b' ' {
            i -= 1;
        }

        (start - i) as i32
    }
}
