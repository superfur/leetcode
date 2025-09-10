import java.util.*;

class Solution {
    /**
     * 找到字符串s中所有串联子串的起始位置
     * 
     * 思路：
     * 1. 使用滑动窗口遍历字符串s
     * 2. 对于每个窗口，检查是否包含words中的所有字符串
     * 3. 使用HashMap记录words中每个字符串的出现次数
     * 4. 维护当前窗口中的字符串计数
     * 
     * 时间复杂度：O(n * m)，其中n是s的长度，m是words的长度
     * 空间复杂度：O(m)
     */
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        
        // 边界情况处理
        if (s == null || s.length() == 0 || words == null || words.length == 0 || words[0].length() == 0) {
            return result;
        }
        
        int wordLen = words[0].length();  // 每个单词的长度
        int wordCount = words.length;     // 单词数量
        int totalLen = wordLen * wordCount;  // 目标子串的总长度
        
        // 如果s长度小于目标长度，直接返回空数组
        if (s.length() < totalLen) {
            return result;
        }
        
        // 统计words中每个字符串的出现次数
        Map<String, Integer> wordFreq = new HashMap<>();
        for (String word : words) {
            wordFreq.put(word, wordFreq.getOrDefault(word, 0) + 1);
        }
        
        // 只需要检查前wordLen个起始位置
        // 因为后续位置会被前面的滑动窗口覆盖
        for (int i = 0; i < wordLen; i++) {
            int left = i;
            int right = i;
            Map<String, Integer> currentFreq = new HashMap<>();  // 当前窗口中的字符串计数
            
            // 滑动窗口遍历
            while (right + wordLen <= s.length()) {
                // 获取当前单词
                String currentWord = s.substring(right, right + wordLen);
                right += wordLen;
                
                // 如果当前单词不在words中，重置窗口
                if (!wordFreq.containsKey(currentWord)) {
                    currentFreq.clear();
                    left = right;
                } else {
                    currentFreq.put(currentWord, currentFreq.getOrDefault(currentWord, 0) + 1);
                    
                    // 如果当前单词出现次数超过words中的次数，移动左边界
                    while (currentFreq.get(currentWord) > wordFreq.get(currentWord)) {
                        String leftWord = s.substring(left, left + wordLen);
                        currentFreq.put(leftWord, currentFreq.get(leftWord) - 1);
                        left += wordLen;
                    }
                    
                    // 如果窗口大小等于words的总长度，找到一个有效子串
                    if (right - left == totalLen) {
                        result.add(left);
                    }
                }
            }
        }
        
        return result;
    }
}