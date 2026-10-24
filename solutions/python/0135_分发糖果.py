import random
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        135. 分发糖果
        两遍贪心，把「左邻居」和「右邻居」两个约束拆开分别满足：
        - 从左往右：ratings[i] > ratings[i - 1] 时 candies[i] = candies[i - 1] + 1，保证比左邻居高的孩子糖更多；
        - 从右往左：ratings[i] > ratings[i + 1] 时 candies[i] = max(candies[i], candies[i + 1] + 1)，
          取 max 是为了不破坏第一遍已经满足的左侧约束。
        两个方向各自都取最小值，叠加后总和即最少糖果数。
        """
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


def brute_force(ratings: List[int]) -> int:
    n = len(ratings)
    candies = [1] * n
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
                changed = True
            if i < n - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
                changed = True
    return sum(candies)


if __name__ == "__main__":
    test_cases = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1], 1),
        ([2, 2, 2], 3),
        ([1, 2, 3, 4, 5], 15),
        ([5, 4, 3, 2, 1], 15),
        ([1, 3, 2, 2, 1], 7),
        ([1, 2, 87, 87, 87, 2, 1], 13),
        (list(range(20000)), 20000 * 20001 // 2),
        ([7] * 20000, 20000),
    ]
    solution = Solution()
    for i, (ratings, expected) in enumerate(test_cases, 1):
        result = solution.candy(ratings)
        status = "PASS" if result == expected else "FAIL"
        shown = ratings if len(ratings) <= 10 else f"(len={len(ratings)})"
        print(f"测试用例 {i}: {status} (ratings={shown}, got={result}, expected={expected})")

    random.seed(135)
    mismatches = 0
    for _ in range(500):
        ratings = [random.randint(0, 5) for _ in range(random.randint(1, 12))]
        if solution.candy(ratings) != brute_force(ratings):
            mismatches += 1
            print(f"随机对拍不一致: ratings={ratings}")
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if mismatches == 0 else 'FAIL'} (500 个随机小数组与迭代松弛法对拍，不一致 {mismatches} 个)")
