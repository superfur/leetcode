#!/usr/bin/env python3
"""
LeetCode 30. 串联所有单词的子串 - 测试文件
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'solutions', 'python'))

# 直接导入模块
sys.path.append(os.path.join(os.path.dirname(__file__), 'solutions', 'python'))
exec(open(os.path.join(os.path.dirname(__file__), 'solutions', 'python', '0030.py')).read())

def test_findSubstring():
    solution = Solution()
    
    # 测试用例1
    s1 = "barfoothefoobarman"
    words1 = ["foo","bar"]
    expected1 = [0, 9]
    result1 = solution.findSubstring(s1, words1)
    print(f"测试用例1: s='{s1}', words={words1}")
    print(f"期望结果: {expected1}")
    print(f"实际结果: {result1}")
    print(f"测试结果: {'通过' if sorted(result1) == sorted(expected1) else '失败'}")
    print()
    
    # 测试用例2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word","good","best","word"]
    expected2 = []
    result2 = solution.findSubstring(s2, words2)
    print(f"测试用例2: s='{s2}', words={words2}")
    print(f"期望结果: {expected2}")
    print(f"实际结果: {result2}")
    print(f"测试结果: {'通过' if result2 == expected2 else '失败'}")
    print()
    
    # 测试用例3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar","foo","the"]
    expected3 = [6, 9, 12]
    result3 = solution.findSubstring(s3, words3)
    print(f"测试用例3: s='{s3}', words={words3}")
    print(f"期望结果: {expected3}")
    print(f"实际结果: {result3}")
    print(f"测试结果: {'通过' if sorted(result3) == sorted(expected3) else '失败'}")
    print()
    
    # 边界情况测试
    s4 = "a"
    words4 = ["a"]
    expected4 = [0]
    result4 = solution.findSubstring(s4, words4)
    print(f"边界测试: s='{s4}', words={words4}")
    print(f"期望结果: {expected4}")
    print(f"实际结果: {result4}")
    print(f"测试结果: {'通过' if result4 == expected4 else '失败'}")
    print()
    
    # 空字符串测试
    s5 = ""
    words5 = ["a"]
    expected5 = []
    result5 = solution.findSubstring(s5, words5)
    print(f"空字符串测试: s='{s5}', words={words5}")
    print(f"期望结果: {expected5}")
    print(f"实际结果: {result5}")
    print(f"测试结果: {'通过' if result5 == expected5 else '失败'}")

if __name__ == "__main__":
    test_findSubstring()
