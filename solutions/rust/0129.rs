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

impl Solution {
    /// 129. 求根节点到叶节点数字之和
    /// DFS 往下传「根到当前节点已经拼出的数字」（cur * 10 + val），
    /// 走到叶子节点时这个数字就是一条完整路径代表的数，累加进答案。
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Link, cur: i32) -> i32 {
            match node {
                None => 0,
                Some(rc) => {
                    let (val, left, right) = {
                        let n = rc.borrow();
                        (n.val, n.left.clone(), n.right.clone())
                    };
                    let cur = cur * 10 + val;
                    if left.is_none() && right.is_none() {
                        return cur;
                    }
                    dfs(&left, cur) + dfs(&right, cur)
                }
            }
        }
        dfs(&root, 0)
    }
}
