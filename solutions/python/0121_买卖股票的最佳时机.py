from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        121. 买卖股票的最佳时机
        一次遍历：维护"目前为止见过的最低价" min_price，
        每天用当前价减去 min_price 更新可能的最大利润，
        再用当前价刷新 min_price。
        """
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]
    solution = Solution()
    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (prices={prices}, got={result}, expected={expected})")
