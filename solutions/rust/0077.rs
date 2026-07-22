/// 77. 组合
/// 回溯 + 剪枝，返回 [1, n] 中所有 k 个数的组合
pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
    let mut result: Vec<Vec<i32>> = Vec::new();
    let mut path: Vec<i32> = Vec::with_capacity(k as usize);

    fn dfs(start: i32, n: i32, k: i32, path: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        if path.len() as i32 == k {
            result.push(path.clone());
            return;
        }
        let upper = n - (k - path.len() as i32) + 1;
        for i in start..=upper {
            path.push(i);
            dfs(i + 1, n, k, path, result);
            path.pop();
        }
    }

    dfs(1, n, k, &mut path, &mut result);
    result
}

impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        combine(n, k)
    }
}
