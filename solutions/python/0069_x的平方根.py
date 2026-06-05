class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

if __name__ == "__main__":
    test_cases = [
        (4, 2),
        (8, 2),
        (0, 0),
        (1, 1),
        (9, 3),
        (2147395600, 46340),
    ]
    sol = Solution()
    for x, expected in test_cases:
        result = sol.mySqrt(x)
        ok = result == expected
        print(f"mySqrt({x}) = {result}, expected {expected}: {'PASS' if ok else 'FAIL'}")
