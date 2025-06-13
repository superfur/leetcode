public class Solution {
    public int myAtoi(String s) {
        int MAX_INT = Integer.MAX_VALUE;
        int MIN_INT = Integer.MIN_VALUE;
        s = s.trim();
        if (s.isEmpty()) return 0;
        int sign = 1;
        int i = 0;
        if (s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = s.charAt(i) == '-' ? -1 : 1;
            i++;
        }
        long result = 0;  // 使用long来避免中间计算溢出
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i) - '0');
            if (sign == 1 && result > MAX_INT) {
                return MAX_INT;
            }
            if (sign == -1 && result > -(long)MIN_INT) {
                return MIN_INT;
            }
            i++;
        }
        return (int)(result * sign);
    }
}