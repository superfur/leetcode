class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 8),
        (10, 89),
        (45, 1836311903),
    ]
    sol = Solution()
    for n, expected in test_cases:
        result = sol.climbStairs(n)
        ok = result == expected
        print(f"climbStairs({n}) = {result}, expected {expected}: {'PASS' if ok else 'FAIL'}")
