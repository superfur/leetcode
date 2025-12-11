import java.util.*;

class Solution {
    /**
     * 字母异位词分组 - 哈希表 + 字符计数（优化版）
     * 
     * 时间复杂度: O(n * k)，其中 n 是字符串数组长度，k 是字符串的最大长度
     *   - 遍历 n 个字符串，每个字符串需要 O(k) 时间统计字符
     *   - 相比排序方案的 O(n * k * log k)，去掉了 log k 因子
     * 空间复杂度: O(n * k)，用于存储哈希表和结果
     * 
     * 思路:
     * 1. 字母异位词的特征：包含相同的字母及其出现次数，只是顺序不同
     * 2. 使用字符计数代替排序：统计每个字符出现的次数，生成唯一键
     * 3. 由于只包含小写字母，使用固定大小的计数数组（26个元素）
     * 4. 将计数数组转为字符串作为 Map 的键
     * 5. 最后将 Map 的所有值（分组）转为 List 返回
     * 
     * 优化点:
     * - 避免了排序操作（O(k log k) → O(k)）
     * - 使用固定大小的计数数组，空间开销固定为 O(26) = O(1)
     * 
     * 示例:
     * - "eat" → [1,0,0,0,1,0,...,1,0,...] → "1#0#0#0#1#0#...#1#..."
     * - "tea" → [1,0,0,0,1,0,...,1,0,...] → "1#0#0#0#1#0#...#1#..."
     * - "ate" → [1,0,0,0,1,0,...,1,0,...] → "1#0#0#0#1#0#...#1#..."
     * - 它们生成相同的键，被分到同一组
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        // 使用 Map 存储分组，键是字符计数的字符串表示，值是该组的字符串列表
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            // 统计每个字符出现的次数（26个小写字母）
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            
            // 将计数数组转为字符串作为键
            // 使用 # 分隔避免歧义，例如 [1,11] 和 [11,1] 应该不同
            StringBuilder keyBuilder = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                if (i > 0) {
                    keyBuilder.append('#');
                }
                keyBuilder.append(count[i]);
            }
            String key = keyBuilder.toString();
            
            // 使用 computeIfAbsent 简化代码：如果键不存在则创建新列表，然后添加字符串
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        
        // 将所有分组转为 List 返回
        return new ArrayList<>(map.values());
    }
}