impl Solution {
    /// 134. 加油站
    /// 贪心一趟扫描：
    /// - total 累加所有 gas[i] - cost[i]，total < 0 说明总油量不够绕一圈，直接 -1；
    /// - tank 是从当前候选起点出发的油箱余量，一旦变负，说明从候选起点到 i 的任何一站
    ///   出发都走不到 i + 1，于是候选起点改成 i + 1，tank 清零。
    /// 扫完后 total >= 0，则最后的候选起点就是唯一解。
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let mut total = 0;
        let mut tank = 0;
        let mut start = 0;
        for i in 0..gas.len() {
            let diff = gas[i] - cost[i];
            total += diff;
            tank += diff;
            if tank < 0 {
                start = i as i32 + 1;
                tank = 0;
            }
        }
        if total < 0 {
            -1
        } else {
            start
        }
    }
}
