class Solution {
    /**
     * 119. 杨辉三角 II
     * 只用一个长度为 rowIndex+1 的数组原地滚动更新：
     * 每处理一行就从右往左把 row[j] 加上 row[j-1]（右往左是关键，
     * 避免用本行已经更新过的值覆盖还没处理的旧值）。
     */
    public List<Integer> getRow(int rowIndex) {
        Integer[] row = new Integer[rowIndex + 1];
        java.util.Arrays.fill(row, 1);
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i - 1; j > 0; j--) {
                row[j] += row[j - 1];
            }
        }
        return java.util.Arrays.asList(row);
    }
}
