class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            current = roman_map[s[i]]
            next = roman_map[s[i + 1]] if i + 1 < len(s) else 0
            if next and current < next:
                result -= current
            else:
                result += current
        return result