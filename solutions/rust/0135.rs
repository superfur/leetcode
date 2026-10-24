impl Solution {
    /// 135. 分发糖果
    /// 两遍贪心，把「左邻居」和「右邻居」两个约束拆开分别满足：
    /// - 从左往右：ratings[i] > ratings[i - 1] 时 candies[i] = candies[i - 1] + 1，保证比左邻居高的孩子糖更多；
    /// - 从右往左：ratings[i] > ratings[i + 1] 时 candies[i] = max(candies[i], candies[i + 1] + 1)，
    ///   取 max 是为了不破坏第一遍已经满足的左侧约束。
    /// 两个方向各自都取最小值，叠加后总和即最少糖果数。
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        let mut candies = vec![1i32; n];
        for i in 1..n {
            if ratings[i] > ratings[i - 1] {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for i in (0..n - 1).rev() {
            if ratings[i] > ratings[i + 1] {
                candies[i] = candies[i].max(candies[i + 1] + 1);
            }
        }
        candies.iter().sum()
    }
}
