/// 87. 扰乱字符串
/// 回溯枚举分割点 i：要么 s1[..i]/s1[i..] 与 s2[..i]/s2[i..] 同步扰乱，
/// 要么 s1[..i]/s1[i..] 与 s2[n-i..]/s2[..n-i]（交换）同步扰乱。
/// 剪枝：字符计数不等直接返回 false；用 HashMap<(s1, s2), bool> 记忆化。
use std::collections::HashMap;

pub fn is_scramble(s1: String, s2: String) -> bool {
    let mut memo: HashMap<(String, String), bool> = HashMap::new();
    dfs(&s1, &s2, &mut memo)
}

fn dfs(a: &str, b: &str, memo: &mut HashMap<(String, String), bool>) -> bool {
    let key = (a.to_string(), b.to_string());
    if let Some(&v) = memo.get(&key) {
        return v;
    }
    if a == b {
        memo.insert(key, true);
        return true;
    }
    // 字符计数剪枝
    let mut cnt = [0i32; 26];
    for (ca, cb) in a.bytes().zip(b.bytes()) {
        cnt[(ca - b'a') as usize] += 1;
        cnt[(cb - b'a') as usize] -= 1;
    }
    if cnt.iter().any(|&x| x != 0) {
        memo.insert(key, false);
        return false;
    }
    let n = a.len();
    for i in 1..n {
        // 不交换
        if dfs(&a[..i], &b[..i], memo) && dfs(&a[i..], &b[i..], memo) {
            memo.insert(key, true);
            return true;
        }
        // 交换
        if dfs(&a[..i], &b[n - i..], memo) && dfs(&a[i..], &b[..n - i], memo) {
            memo.insert(key, true);
            return true;
        }
    }
    memo.insert(key, false);
    false
}

impl Solution {
    pub fn is_scramble(s1: String, s2: String) -> bool {
        is_scramble(s1, s2)
    }
}