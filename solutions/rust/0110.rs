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

/// 110. 平衡二叉树
/// 自底向上后序遍历，一趟同时算高度和判平衡：
/// 用 -1 作为“已经不平衡”的哨兵值向上传播，一旦子树出现
/// 不平衡或左右高度差超过 1，就不再继续计算，直接短路返回。
pub fn is_balanced(root: Link) -> bool {
    fn height(node: &Link) -> i32 {
        match node {
            None => 0,
            Some(n) => {
                let left = height(&n.borrow().left);
                if left == -1 {
                    return -1;
                }
                let right = height(&n.borrow().right);
                if right == -1 || (left - right).abs() > 1 {
                    return -1;
                }
                1 + left.max(right)
            }
        }
    }

    height(&root) != -1
}

impl Solution {
    pub fn is_balanced(root: Link) -> bool {
        is_balanced(root)
    }
}
