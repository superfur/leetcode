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

/// 98. 验证二叉搜索树
/// 区间递归：每个节点携带一个开区间 (low, high)，其值必须落在区间内；
/// 向左递归时收紧上界为当前值，向右递归时收紧下界为当前值。
pub fn is_valid_bst(root: Link) -> bool {
    fn validate(node: &Link, low: i64, high: i64) -> bool {
        match node {
            None => true,
            Some(n) => {
                let v = n.borrow().val as i64;
                if !(v > low && v < high) {
                    return false;
                }
                validate(&n.borrow().left, low, v) && validate(&n.borrow().right, v, high)
            }
        }
    }

    validate(&root, i64::MIN, i64::MAX)
}

impl Solution {
    pub fn is_valid_bst(root: Link) -> bool {
        is_valid_bst(root)
    }
}
