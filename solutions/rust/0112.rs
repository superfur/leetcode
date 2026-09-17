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

/// 112. 路径总和
/// 递归：空树直接不存在路径；到达叶子节点时判断剩余目标值
/// 是否正好等于该叶子的值；否则把目标值减去当前节点值，
/// 分别在左右子树里继续找。
pub fn has_path_sum(root: Link, target_sum: i32) -> bool {
    match root {
        None => false,
        Some(node) => {
            let (val, left, right) = {
                let n = node.borrow();
                (n.val, n.left.clone(), n.right.clone())
            };
            let remaining = target_sum - val;
            if left.is_none() && right.is_none() {
                return remaining == 0;
            }
            has_path_sum(left, remaining) || has_path_sum(right, remaining)
        }
    }
}

impl Solution {
    pub fn has_path_sum(root: Link, target_sum: i32) -> bool {
        has_path_sum(root, target_sum)
    }
}
