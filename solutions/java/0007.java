public class Solution {
    public int reverse(int x) {
        long result = 0;  // 使用 long 来避免中间计算溢出
        
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        
        // 检查结果是否在 int 范围内
        if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) {
            return 0;
        }
        
        return (int) result;
    }
}