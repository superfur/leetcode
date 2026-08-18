public class Solution {
    /**
     * 89. 格雷编码
     * 经典公式：gray(i) = i ^ (i >> 1)。
     */
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        int size = 1 << n;
        for (int i = 0; i < size; i++) {
            result.add(i ^ (i >> 1));
        }
        return result;
    }
}