class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            if char in char_map:
                left = max(char_map[char] + 1, left)
            char_map[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
