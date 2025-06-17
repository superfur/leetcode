class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        original = x
        while x > 0:
            reversed = reversed * 10 + x % 10
            x = x // 10
        return reversed == original