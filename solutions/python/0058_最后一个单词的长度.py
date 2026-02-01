def 最后一个单词的长度(s: str) -> int:
    """
    最后一个单词的长度

    时间复杂度: O(n)，其中 n 为字符串长度
    空间复杂度: O(1)

    思路: 从字符串末尾向前遍历
    1. 跳过末尾的空格
    2. 从非空格字符开始计数，直到遇到空格或到达字符串开头

    示例: s = "   fly me   to   the moon  " -> 4 (moon)
    """
    i = len(s) - 1

    # 跳过末尾空格
    while i >= 0 and s[i] == " ":
        i -= 1

    length = 0
    # 统计最后一个单词的长度
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        {"input": "Hello World", "expected": 5},
        {"input": "   fly me   to   the moon  ", "expected": 4},
        {"input": "luffy is still joyboy", "expected": 6},
    ]
    for i, test_case in enumerate(test_cases, 1):
        s, expected = test_case["input"], test_case["expected"]
        result = 最后一个单词的长度(s)
        status = "通过" if result == expected else "失败"
        print(f"测试用例 {i}: {status} (输入: {s!r}, 期望: {expected}, 实际: {result})")
