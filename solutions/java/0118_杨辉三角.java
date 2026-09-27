class Solution {
    /**
     * 118. 杨辉三角
     * 逐行生成：每行首尾都是 1，中间第 j 个数等于上一行第 j-1 和第 j 个数之和。
     */
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new java.util.ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new java.util.ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    row.add(1);
                } else {
                    row.add(result.get(i - 1).get(j - 1) + result.get(i - 1).get(j));
                }
            }
            result.add(row);
        }
        return result;
    }
}
