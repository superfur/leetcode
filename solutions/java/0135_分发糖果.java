class Solution {
    /**
     * 135. 分发糖果
     * 两遍贪心，把「左邻居」和「右邻居」两个约束拆开分别满足：
     * - 从左往右：ratings[i] > ratings[i - 1] 时 candies[i] = candies[i - 1] + 1，保证比左邻居高的孩子糖更多；
     * - 从右往左：ratings[i] > ratings[i + 1] 时 candies[i] = max(candies[i], candies[i + 1] + 1)，
     *   取 max 是为了不破坏第一遍已经满足的左侧约束。
     * 两个方向各自都取最小值，叠加后总和即最少糖果数。
     */
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
        }
        int total = 0;
        for (int c : candies) {
            total += c;
        }
        return total;
    }
}
