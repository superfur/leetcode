import random
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        137. 只出现一次的数字 II
        逐位统计：出现三次的数，每一位上的 1 的个数一定是 3 的倍数，
        所以把所有数在第 i 位上的 1 加起来对 3 取模，余数就是答案在第 i 位的值。
        Python 的整数没有固定位宽，统计完 32 位后，如果符号位（第 31 位）是 1，
        要减去 2^32 还原成负数。时间 O(32n)，空间 O(1)。
        """
        result = 0
        for i in range(32):
            ones = sum((x >> i) & 1 for x in nums)
            if ones % 3:
                result |= 1 << i
        if result >= 1 << 31:
            result -= 1 << 32
        return result


if __name__ == "__main__":
    INT_MIN, INT_MAX = -(2 ** 31), 2 ** 31 - 1
    test_cases = [
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
        ([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2], -4),
        ([INT_MIN, INT_MIN, INT_MIN, 7], 7),
        ([INT_MAX, INT_MAX, INT_MAX, INT_MIN], INT_MIN),
        ([-1, -1, -1, 5], 5),
        ([-1, -1, -1, INT_MAX], INT_MAX),
        ([42], 42),
        ([-42], -42),
    ]
    solution = Solution()
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.singleNumber(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (nums={nums}, got={result}, expected={expected})")

    random.seed(137)
    mismatches = 0
    for _ in range(300):
        k = random.randint(0, 200)
        pool = random.sample(range(INT_MIN, INT_MAX + 1), k + 1) if k < 50 else [random.randint(INT_MIN, INT_MAX) for _ in range(k + 1)]
        pool = list(dict.fromkeys(pool))
        single, rest = pool[0], pool[1:]
        arr = rest * 3 + [single]
        random.shuffle(arr)
        if solution.singleNumber(arr) != single:
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if mismatches == 0 else 'FAIL'} (300 组随机全范围 int32 数据，不一致 {mismatches} 组)")

    big = list(range(1, 10001))
    arr = big * 3 + [-31337]
    random.shuffle(arr)
    r = solution.singleNumber(arr)
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if r == -31337 else 'FAIL'} (n={len(arr)}, got={r}, expected=-31337)")
