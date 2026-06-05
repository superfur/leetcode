package com.leetcode;

public class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;
        long left = 1, right = x / 2;
        while (left <= right) {
            long mid = (left + right) / 2;
            long sq = mid * mid;
            if (sq == x) return (int) mid;
            else if (sq < x) left = mid + 1;
            else right = mid - 1;
        }
        return (int) right;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] cases = {{4, 2}, {8, 2}, {0, 0}, {1, 1}, {9, 3}};
        for (int[] tc : cases) {
            int result = sol.mySqrt(tc[0]);
            String ok = result == tc[1] ? "PASS" : "FAIL";
            System.out.printf("mySqrt(%d) = %d, expected %d: %s%n", tc[0], result, tc[1], ok);
        }
        // 大数测试
        int big = sol.mySqrt(2147395600);
        System.out.printf("mySqrt(2147395600) = %d, expected 46340: %s%n", big, big == 46340 ? "PASS" : "FAIL");
    }
}
