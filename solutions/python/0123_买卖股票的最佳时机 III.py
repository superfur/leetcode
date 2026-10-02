from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        123. 买卖股票的最佳时机 III
        最多两笔交易：维护四个状态 buy1/sell1/buy2/sell2，
        分别表示第一次买入后、第一次卖出后、第二次买入后、第二次卖出后的最大收益。
        """
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2


if __name__ == "__main__":
    test_cases = [
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
    ]
    solution = Solution()
    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (prices={prices}, got={result}, expected={expected})")
