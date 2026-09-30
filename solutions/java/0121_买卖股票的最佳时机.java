class Solution {
    /**
     * 121. 买卖股票的最佳时机
     * 一次遍历：维护"目前为止见过的最低价" minPrice，
     * 每天用当前价减去 minPrice 更新可能的最大利润，
     * 再用当前价刷新 minPrice。
     */
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfitSoFar = 0;
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfitSoFar) {
                maxProfitSoFar = price - minPrice;
            }
        }
        return maxProfitSoFar;
    }
}
