class Solution {
    /**
     * 149. 直线上最多的点数
     * 固定一个点 i 作为「基准点」，统计它与后面每个点 j 连线的斜率，斜率相同的点与 i 共线。
     * 为了避免浮点误差，不直接除，而是把方向向量 (dx, dy) 除以 gcd 约成最简，
     * 再统一符号（dx < 0，或 dx == 0 且 dy < 0 时整体取反），同一斜率就对应唯一的 (dx, dy)。
     * 坐标范围 [-10^4, 10^4]，所以 dx ∈ [0, 2*10^4]、dy ∈ [-2*10^4, 2*10^4]，
     * 用 dx * 100003L + dy 编成一个整数当哈希键。
     * 只需统计 j > i 的点：共线的点集里编号最小的点作基准时就能数全，不用重复计算。
     * 基准点自己算一个，所以答案为 max(同斜率计数) + 1。
     * 时间 O(n^2 log C)，空间 O(n)。
     */
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n <= 2) {
            return n;
        }
        int best = 1;
        for (int i = 0; i < n; i++) {
            if (best >= n - i) {
                break; // 剩下的点不够超过当前答案了
            }
            java.util.Map<Long, Integer> slopes = new java.util.HashMap<>();
            for (int j = i + 1; j < n; j++) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                int g = gcd(dx, dy);
                dx /= g;
                dy /= g;
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }
                long key = dx * 100003L + dy;
                int cnt = slopes.merge(key, 1, Integer::sum);
                best = Math.max(best, cnt + 1);
            }
        }
        return best;
    }

    private int gcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
