/// 96. 不同的二叉搜索树
/// 动态规划（卡特兰数）：dp[i] 表示 i 个节点能组成的 BST 数量。
/// 以 k 为根时，左子树用 k-1 个节点、右子树用 i-k 个节点，
/// dp[i] = sum(dp[k-1] * dp[i-k]) for k in 1..i。
pub fn num_trees(n: i32) -> i32 {
    let n = n as usize;
    let mut dp = vec![0i64; n + 1];
    dp[0] = 1;
    for i in 1..=n {
        for k in 1..=i {
            dp[i] += dp[k - 1] * dp[i - k];
        }
    }
    dp[n] as i32
}

impl Solution {
    pub fn num_trees(n: i32) -> i32 {
        num_trees(n)
    }
}
