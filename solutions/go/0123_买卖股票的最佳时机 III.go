package main

import "math"

// 123. 买卖股票的最佳时机 III
// 最多两笔交易：维护四个状态 buy1/sell1/buy2/sell2，
// 分别表示第一次买入后、第一次卖出后、第二次买入后、第二次卖出后的最大收益。
func maxProfit(prices []int) int {
	buy1, buy2 := math.MinInt64, math.MinInt64
	sell1, sell2 := 0, 0
	for _, price := range prices {
		if -price > buy1 {
			buy1 = -price
		}
		if buy1+price > sell1 {
			sell1 = buy1 + price
		}
		if sell1-price > buy2 {
			buy2 = sell1 - price
		}
		if buy2+price > sell2 {
			sell2 = buy2 + price
		}
	}
	return sell2
}
