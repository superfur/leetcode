// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
use std::cell::RefCell;
use std::rc::Rc;

type Link = Option<Rc<RefCell<TreeNode>>>;

/// 113. 路径总和 II
/// 回溯：沿途把节点值压入 path，到叶子节点时若剩余目标值
/// 正好归零就把 path 的一份拷贝收进结果；不管是否匹配，
/// 递归返回前都要把刚压入的节点值弹出，恢复现场再试下一分支。
pub fn path_sum(root: Link, target_sum: i32) -> Vec<Vec<i32>> {
    let mut result = Vec::new();
    let mut path = Vec::new();

    fn dfs(node: &Link, remaining: i32, path: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        let node = match node {
            None => return,
            Some(n) => n,
        };
        let (val, left, right) = {
            let n = node.borrow();
            (n.val, n.left.clone(), n.right.clone())
        };
        path.push(val);
        let remaining = remaining - val;
        if left.is_none() && right.is_none() && remaining == 0 {
            result.push(path.clone());
        } else {
            dfs(&left, remaining, path, result);
            dfs(&right, remaining, path, result);
        }
        path.pop();
    }

    dfs(&root, target_sum, &mut path, &mut result);
    result
}

impl Solution {
    pub fn path_sum(root: Link, target_sum: i32) -> Vec<Vec<i32>> {
        path_sum(root, target_sum)
    }
}
