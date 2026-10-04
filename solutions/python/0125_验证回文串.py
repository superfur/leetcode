class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        125. 验证回文串
        双指针：左右两端向中间走，跳过非字母数字字符，
        其余字符忽略大小写后逐个比较，不一致就不是回文。
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("a", True),
        (".,", True),
        ("ab_a", True),
        ("a.", True),
        (".a", True),
        ("ab.", False),
    ]
    solution = Solution()
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.isPalindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (s={s!r}, got={result}, expected={expected})")
