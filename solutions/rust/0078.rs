/// 78. 子集
/// 回溯枚举所有子集（幂集），数组元素互不相同
pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut result: Vec<Vec<i32>> = Vec::new();
    let mut path: Vec<i32> = Vec::new();

    fn dfs(start: usize, nums: &[i32], path: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        result.push(path.clone());
        for i in start..nums.len() {
            path.push(nums[i]);
            dfs(i + 1, nums, path, result);
            path.pop();
        }
    }

    dfs(0, &nums, &mut path, &mut result);
    result
}

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        subsets(nums)
    }
}