impl Solution {
    /// 121. 买卖股票的最佳时机
    /// 一次遍历：维护“目前为止见过的最低价” min_price，
    /// 每天用当前价减去 min_price 更新可能的最大利润，
    /// 再用当前价刷新 min_price。
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price = i32::MAX;
        let mut max_profit_so_far = 0;
        for price in prices {
            if price < min_price {
                min_price = price;
            } else if price - min_price > max_profit_so_far {
                max_profit_so_far = price - min_price;
            }
        }
        max_profit_so_far
    }
}
