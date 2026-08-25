// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
use std::cell::RefCell;
use std::rc::Rc;

/// 94. 二叉树的中序遍历
/// 迭代：用栈模拟递归——一路把左子树压栈到底，
/// 弹出访问后转向右子树，重复直到栈空且当前节点为空。
pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut result = Vec::new();
    let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
    let mut node = root;
    while node.is_some() || !stack.is_empty() {
        while let Some(n) = node {
            node = n.borrow().left.clone();
            stack.push(n);
        }
        let n = stack.pop().unwrap();
        result.push(n.borrow().val);
        node = n.borrow().right.clone();
    }
    result
}

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        inorder_traversal(root)
    }
}
