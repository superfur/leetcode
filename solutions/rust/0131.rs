impl Solution {
    /// 131. 分割回文串
    /// 先用区间 DP 预处理 is_pal[i][j]（s[i..j] 是否回文），
    /// 再回溯：从位置 start 开始，枚举每个能切出回文前缀 s[start..end] 的位置，
    /// 选中后递归处理 end + 1，走到字符串末尾就收集一个方案。
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut is_pal = vec![vec![true; n]; n];
        for i in (0..n).rev() {
            for j in (i + 1)..n {
                is_pal[i][j] = bytes[i] == bytes[j] && (j - i < 2 || is_pal[i + 1][j - 1]);
            }
        }

        fn back(
            start: usize,
            s: &str,
            is_pal: &Vec<Vec<bool>>,
            path: &mut Vec<String>,
            res: &mut Vec<Vec<String>>,
        ) {
            if start == s.len() {
                res.push(path.clone());
                return;
            }
            for end in start..s.len() {
                if is_pal[start][end] {
                    path.push(s[start..=end].to_string());
                    back(end + 1, s, is_pal, path, res);
                    path.pop();
                }
            }
        }

        let mut res = Vec::new();
        let mut path = Vec::new();
        back(0, &s, &is_pal, &mut path, &mut res);
        res
    }
}
