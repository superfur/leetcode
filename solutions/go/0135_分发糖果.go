package main

// 135. 分发糖果
// 两遍贪心，把「左邻居」和「右邻居」两个约束拆开分别满足：
// - 从左往右：ratings[i] > ratings[i-1] 时 candies[i] = candies[i-1] + 1，保证比左邻居高的孩子糖更多；
// - 从右往左：ratings[i] > ratings[i+1] 时 candies[i] = max(candies[i], candies[i+1] + 1)，
//   取 max 是为了不破坏第一遍已经满足的左侧约束。
// 两个方向各自都取最小值，叠加后总和即最少糖果数。
func candy(ratings []int) int {
	n := len(ratings)
	candies := make([]int, n)
	for i := range candies {
		candies[i] = 1
	}
	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i-1] {
			candies[i] = candies[i-1] + 1
		}
	}
	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] && candies[i+1]+1 > candies[i] {
			candies[i] = candies[i+1] + 1
		}
	}
	total := 0
	for _, c := range candies {
		total += c
	}
	return total
}
