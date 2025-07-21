class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for char in s:
            if char in map:
                stack.append(char)
            else:
                if not stack or map[stack.pop()] != char:
                    return False
        return not stack