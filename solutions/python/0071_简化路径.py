class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)


if __name__ == "__main__":
    test_cases = [
        {"input": "/home/", "expected": "/home"},
        {"input": "/home//foo/", "expected": "/home/foo"},
        {"input": "/home/user/Documents/../Pictures", "expected": "/home/user/Pictures"},
        {"input": "/../", "expected": "/"},
        {"input": "/.../a/../b/c/../d/./", "expected": "/.../b/d"},
    ]
    for i, tc in enumerate(test_cases, 1):
        result = Solution().simplifyPath(tc["input"])
        status = "PASS" if result == tc["expected"] else "FAIL"
        print(f"测试用例 {i}: {status} (got={result}, expected={tc['expected']})")
