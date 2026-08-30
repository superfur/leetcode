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

/// 100. 相同的树
/// 递归：两个节点同时为空则相同；一空一非空或值不同则不同；
/// 否则要求左子树和右子树都分别相同。
pub fn is_same_tree(p: Link, q: Link) -> bool {
    match (p, q) {
        (None, None) => true,
        (Some(a), Some(b)) => {
            a.borrow().val == b.borrow().val
                && is_same_tree(a.borrow().left.clone(), b.borrow().left.clone())
                && is_same_tree(a.borrow().right.clone(), b.borrow().right.clone())
        }
        _ => false,
    }
}

impl Solution {
    pub fn is_same_tree(p: Link, q: Link) -> bool {
        is_same_tree(p, q)
    }
}
