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

/// 104. 二叉树的最大深度
/// 递归：空树深度为 0，否则为左右子树深度的较大值加 1。
pub fn max_depth(root: Link) -> i32 {
    match root {
        None => 0,
        Some(node) => {
            let (left, right) = {
                let n = node.borrow();
                (n.left.clone(), n.right.clone())
            };
            1 + max_depth(left).max(max_depth(right))
        }
    }
}

impl Solution {
    pub fn max_depth(root: Link) -> i32 {
        max_depth(root)
    }
}
