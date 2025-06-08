class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        is_negative = x < 0
        reversed = int(str(abs(x))[::-1])
        result = -reversed if is_negative else reversed
        return result if MIN_INT <= result <= MAX_INT else 0