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

/// 111. 二叉树的最小深度
/// 最小深度要求到最近的“叶子节点”，所以只有一个子节点的节点
/// 不能直接取 min(0, 子树深度)——必须沿着那个唯一的非空子节点继续走。
/// 只有左右子节点都为空（真正的叶子）时深度才是 1。
pub fn min_depth(root: Link) -> i32 {
    match root {
        None => 0,
        Some(node) => {
            let (left, right) = {
                let n = node.borrow();
                (n.left.clone(), n.right.clone())
            };
            match (left, right) {
                (None, right) => 1 + min_depth(right),
                (left, None) => 1 + min_depth(left),
                (left, right) => 1 + min_depth(left).min(min_depth(right)),
            }
        }
    }
}

impl Solution {
    pub fn min_depth(root: Link) -> i32 {
        min_depth(root)
    }
}
