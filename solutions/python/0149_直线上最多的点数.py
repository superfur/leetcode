import random
from math import gcd
from typing import Dict, List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        149. 直线上最多的点数
        固定一个点 i 作为「基准点」，统计它与后面每个点 j 连线的斜率，斜率相同的点与 i 共线。
        为了避免浮点误差，不直接除，而是把方向向量 (dx, dy) 除以 gcd 约成最简，
        再统一符号（dx < 0，或 dx == 0 且 dy < 0 时整体取反），同一斜率就对应唯一的 (dx, dy)。
        坐标范围 [-10^4, 10^4]，所以 dx ∈ [0, 2*10^4]、dy ∈ [-2*10^4, 2*10^4]，
        用 dx * 100003 + dy 编成一个整数当哈希键。
        只需统计 j > i 的点：共线的点集里编号最小的点作基准时就能数全，不用重复计算。
        基准点自己算一个，所以答案为 max(同斜率计数) + 1。
        时间 O(n^2 log C)，空间 O(n)。
        """
        n = len(points)
        if n <= 2:
            return n
        best = 1
        for i in range(n):
            if best >= n - i:
                break  # 剩下的点不够超过当前答案了
            xi, yi = points[i]
            slopes: Dict[int, int] = {}
            for j in range(i + 1, n):
                dx, dy = points[j][0] - xi, points[j][1] - yi
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                key = dx * 100003 + dy
                cnt = slopes.get(key, 0) + 1
                slopes[key] = cnt
                if cnt + 1 > best:
                    best = cnt + 1
        return best


def brute_force(points: List[List[int]]) -> int:
    n = len(points)
    if n <= 2:
        return n
    best = 2
    for i in range(n):
        for j in range(i + 1, n):
            dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
            cnt = sum(
                1 for k in range(n)
                if dx * (points[k][1] - points[i][1]) == dy * (points[k][0] - points[i][0])
            )
            best = max(best, cnt)
    return best


if __name__ == "__main__":
    test_cases = [
        ([[1, 1], [2, 2], [3, 3]], 3),
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
        ([[0, 0]], 1),
        ([[0, 0], [1, 1]], 2),
        ([[0, 0], [0, 5], [0, -3], [1, 1]], 3),  # 竖直线
        ([[0, 0], [5, 0], [-3, 0], [1, 1]], 3),  # 水平线
        ([[0, 0], [1, 1], [-1, -1], [2, 2], [1, -1]], 4),
        ([[-10000, -10000], [10000, 10000], [0, 0], [10000, -10000]], 3),  # 坐标极值
        ([[0, 0], [10000, 9999], [9999, 9998]], 2),  # 斜率 9999/10000 与 9998/9999 非常接近，浮点比较容易误判
        ([[1, 1], [1, 1 + 1], [2, 1], [2, 2]], 2),
    ]
    solution = Solution()
    for i, (points, expected) in enumerate(test_cases, 1):
        result = solution.maxPoints(points)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (points={points}, got={result}, expected={expected})")

    # 规模：300 个点，全部共线 / 随机
    line = [[k, 2 * k - 7] for k in range(300)]
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if solution.maxPoints(line) == 300 else 'FAIL'} (300 个点全部共线)")
    random.seed(149)
    rand_pts = list({(random.randint(-10000, 10000), random.randint(-10000, 10000)) for _ in range(300)})
    rand_pts = [list(p) for p in rand_pts]
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if solution.maxPoints(rand_pts) == brute_force(rand_pts) else 'FAIL'} (300 个随机点，与暴力解一致)")

    mismatches = 0
    for _ in range(1000):
        span = random.choice([2, 3, 5, 10])  # 小坐标范围，容易出现大量共线 / 重叠斜率
        cells = [(x, y) for x in range(-span, span + 1) for y in range(-span, span + 1)]
        pts = [list(p) for p in random.sample(cells, random.randint(1, min(len(cells), 25)))]
        if solution.maxPoints(pts) != brute_force(pts):
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 3}: {'PASS' if mismatches == 0 else 'FAIL'} (1000 组小范围随机点集与叉积暴力解对拍，不一致 {mismatches} 组)")
