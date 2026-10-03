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
    /// 124. 二叉树中的最大路径和
    /// 后序递归：dfs(node) 返回「以 node 为起点、向下走的最大贡献值」
    /// （贡献为负就当作 0，即不选这条分支）；
    /// 同时把「左贡献 + 节点值 + 右贡献」当作以 node 为最高点的路径和，更新全局答案。
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Link, best: &mut i32) -> i32 {
            match node {
                None => 0,
                Some(rc) => {
                    let (val, left, right) = {
                        let n = rc.borrow();
                        (n.val, n.left.clone(), n.right.clone())
                    };
                    let l = dfs(&left, best).max(0);
                    let r = dfs(&right, best).max(0);
                    *best = (*best).max(val + l + r);
                    val + l.max(r)
                }
            }
        }

        let mut best = i32::MIN;
        dfs(&root, &mut best);
        best
    }
}
