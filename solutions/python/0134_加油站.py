from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        134. 加油站
        贪心一趟扫描：
        - total 累加所有 gas[i] - cost[i]，total < 0 说明总油量不够绕一圈，直接 -1；
        - tank 是从当前候选起点出发的油箱余量，一旦变负，说明从候选起点到 i 的任何一站
          出发都走不到 i + 1，于是候选起点改成 i + 1，tank 清零。
        扫完后 total >= 0，则最后的候选起点就是唯一解。
        """
        total = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5], [4], 0),
        ([2], [2], 0),
        ([2], [3], -1),
        ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
        ([3, 1, 1], [1, 2, 2], 0),
        ([1, 2, 3], [1, 2, 3], 0),
    ]
    solution = Solution()
    for i, (gas, cost, expected) in enumerate(test_cases, 1):
        result = solution.canCompleteCircuit(gas, cost)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (gas={gas}, cost={cost}, got={result}, expected={expected})")
