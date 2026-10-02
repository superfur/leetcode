/**
 * 123. 买卖股票的最佳时机 III
 * 最多两笔交易：维护四个状态 buy1/sell1/buy2/sell2，
 * 分别表示第一次买入后、第一次卖出后、第二次买入后、第二次卖出后的最大收益。
 */
function maxProfit(prices: number[]): number {
    let buy1 = -Infinity;
    let sell1 = 0;
    let buy2 = -Infinity;
    let sell2 = 0;
    for (const price of prices) {
        buy1 = Math.max(buy1, -price);
        sell1 = Math.max(sell1, buy1 + price);
        buy2 = Math.max(buy2, sell1 - price);
        sell2 = Math.max(sell2, buy2 + price);
    }
    return sell2;
}

export default maxProfit;
