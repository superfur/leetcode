class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
            if result > MAX_INT:
                return MAX_INT if sign == 1 else MIN_INT
        return result * sign