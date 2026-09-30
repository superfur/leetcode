impl Solution {
    /// 122. 买卖股票的最佳时机 II
    /// 贪心：可以无限次交易，所以只要今天比昨天贵，
    /// 就把这一段差价赚到手（等价于把每个上涨区间的涨幅都累加起来）。
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        for i in 1..prices.len() {
            if prices[i] > prices[i - 1] {
                profit += prices[i] - prices[i - 1];
            }
        }
        profit
    }
}
