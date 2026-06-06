package com.leetcode;

public class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int tmp = a + b;
            a = b;
            b = tmp;
        }
        return b;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] cases = {{1, 1}, {2, 2}, {3, 3}, {5, 8}, {10, 89}, {45, 1836311903}};
        for (int[] tc : cases) {
            int result = sol.climbStairs(tc[0]);
            String ok = result == tc[1] ? "PASS" : "FAIL";
            System.out.printf("climbStairs(%d) = %d, expected %d: %s%n", tc[0], result, tc[1], ok);
        }
    }
}
