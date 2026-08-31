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

/// 101. 对称二叉树
/// 递归判断两棵子树是否互为镜像：值相同，且 t1 的左子树与 t2 的右子树
/// 互为镜像、t1 的右子树与 t2 的左子树互为镜像。
pub fn is_symmetric(root: Link) -> bool {
    fn is_mirror(t1: &Link, t2: &Link) -> bool {
        match (t1, t2) {
            (None, None) => true,
            (Some(a), Some(b)) => {
                a.borrow().val == b.borrow().val
                    && is_mirror(&a.borrow().left, &b.borrow().right)
                    && is_mirror(&a.borrow().right, &b.borrow().left)
            }
            _ => false,
        }
    }

    match &root {
        None => true,
        Some(n) => is_mirror(&n.borrow().left, &n.borrow().right),
    }
}

impl Solution {
    pub fn is_symmetric(root: Link) -> bool {
        is_symmetric(root)
    }
}
