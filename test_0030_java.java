/**
 * LeetCode 30. 串联所有单词的子串 - Java测试文件
 */

import java.util.*;

public class Test0030 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // 测试用例1
        String s1 = "barfoothefoobarman";
        String[] words1 = {"foo", "bar"};
        List<Integer> expected1 = Arrays.asList(0, 9);
        List<Integer> result1 = solution.findSubstring(s1, words1);
        System.out.println("测试用例1: s='" + s1 + "', words=" + Arrays.toString(words1));
        System.out.println("期望结果: " + expected1);
        System.out.println("实际结果: " + result1);
        System.out.println("测试结果: " + (isEqual(result1, expected1) ? "通过" : "失败"));
        System.out.println();
        
        // 测试用例2
        String s2 = "wordgoodgoodgoodbestword";
        String[] words2 = {"word", "good", "best", "word"};
        List<Integer> expected2 = new ArrayList<>();
        List<Integer> result2 = solution.findSubstring(s2, words2);
        System.out.println("测试用例2: s='" + s2 + "', words=" + Arrays.toString(words2));
        System.out.println("期望结果: " + expected2);
        System.out.println("实际结果: " + result2);
        System.out.println("测试结果: " + (isEqual(result2, expected2) ? "通过" : "失败"));
        System.out.println();
        
        // 测试用例3
        String s3 = "barfoofoobarthefoobarman";
        String[] words3 = {"bar", "foo", "the"};
        List<Integer> expected3 = Arrays.asList(6, 9, 12);
        List<Integer> result3 = solution.findSubstring(s3, words3);
        System.out.println("测试用例3: s='" + s3 + "', words=" + Arrays.toString(words3));
        System.out.println("期望结果: " + expected3);
        System.out.println("实际结果: " + result3);
        System.out.println("测试结果: " + (isEqual(result3, expected3) ? "通过" : "失败"));
        System.out.println();
        
        // 边界情况测试
        String s4 = "a";
        String[] words4 = {"a"};
        List<Integer> expected4 = Arrays.asList(0);
        List<Integer> result4 = solution.findSubstring(s4, words4);
        System.out.println("边界测试: s='" + s4 + "', words=" + Arrays.toString(words4));
        System.out.println("期望结果: " + expected4);
        System.out.println("实际结果: " + result4);
        System.out.println("测试结果: " + (isEqual(result4, expected4) ? "通过" : "失败"));
        System.out.println();
        
        // 空字符串测试
        String s5 = "";
        String[] words5 = {"a"};
        List<Integer> expected5 = new ArrayList<>();
        List<Integer> result5 = solution.findSubstring(s5, words5);
        System.out.println("空字符串测试: s='" + s5 + "', words=" + Arrays.toString(words5));
        System.out.println("期望结果: " + expected5);
        System.out.println("实际结果: " + result5);
        System.out.println("测试结果: " + (isEqual(result5, expected5) ? "通过" : "失败"));
    }
    
    /**
     * 比较两个List是否相等（忽略顺序）
     */
    private static boolean isEqual(List<Integer> list1, List<Integer> list2) {
        if (list1.size() != list2.size()) {
            return false;
        }
        Collections.sort(list1);
        Collections.sort(list2);
        return list1.equals(list2);
    }
}
