impl Solution {
    /// 123. 买卖股票的最佳时机 III
    /// 最多两笔交易：维护四个状态 buy1/sell1/buy2/sell2，
    /// 分别表示第一次买入后、第一次卖出后、第二次买入后、第二次卖出后的最大收益。
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut buy1 = i32::MIN;
        let mut buy2 = i32::MIN;
        let mut sell1 = 0;
        let mut sell2 = 0;
        for price in prices {
            buy1 = buy1.max(-price);
            sell1 = sell1.max(buy1 + price);
            buy2 = buy2.max(sell1 - price);
            sell2 = sell2.max(buy2 + price);
        }
        sell2
    }
}
