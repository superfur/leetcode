from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        122. 买卖股票的最佳时机 II
        贪心：可以无限次交易，所以只要今天比昨天贵，
        就把这一段差价赚到手（等价于把每个上涨区间的涨幅都累加起来）。
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ]
    solution = Solution()
    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (prices={prices}, got={result}, expected={expected})")
