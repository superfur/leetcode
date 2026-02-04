public class Solution {
    /**
     * 最后一个单词的长度
     *
     * 时间复杂度: O(n)，其中 n 为字符串长度
     * 空间复杂度: O(1)
     *
     * 思路: 从字符串末尾向前遍历
     * 1. 跳过末尾的空格
     * 2. 从非空格字符开始计数，直到遇到空格或到达字符串开头
     *
     * 示例: s = "   fly me   to   the moon  " -> 4 (moon)
     */
    public Object 最后一个单词的长度(Object... args) {
        String s = (String) args[0];
        return lengthOfLastWord(s);
    }

    /**
     * LeetCode 标准接口: lengthOfLastWord
     */
    public int lengthOfLastWord(String s) {
        int i = s.length() - 1;

        // 跳过末尾空格
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        int len = 0;
        // 统计最后一个单词的长度
        while (i >= 0 && s.charAt(i) != ' ') {
            len++;
            i--;
        }

        return len;
    }
}
