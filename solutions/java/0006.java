class Solution {
    /**
     * 将字符串按照 Z 字形排列后按行读取
     * @param s 输入字符串
     * @param numRows Z 字形的行数
     * @return 按行读取后的字符串
     */
    public String convert(String s, int numRows) {
        // 如果只有一行，直接返回原字符串
        if (numRows == 1) {
            return s;
        }

        // 创建存储每行字符的字符串数组
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int curRow = 0;
        boolean goingDown = false;

        // 遍历字符串中的每个字符
        for (char c : s.toCharArray()) {
            // 将字符添加到当前行
            rows[curRow].append(c);

            // 在到达顶部或底部时改变方向
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }

            // 根据方向更新当前行
            curRow += goingDown ? 1 : -1;
        }

        // 将所有行连接起来
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }
}