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

/// 144. 二叉树的前序遍历
/// 迭代 + 显式栈：弹出节点就记录它的值（根），再先压右孩子、后压左孩子，
/// 这样下一次弹出的就是左孩子，顺序为 根 → 左 → 右。
/// 不依赖递归深度，时间 O(n)，空间 O(h)。
pub fn preorder_traversal(root: Link) -> Vec<i32> {
    let mut res = Vec::new();
    let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
    if let Some(node) = root {
        stack.push(node);
    }
    while let Some(node) = stack.pop() {
        let (val, left, right) = {
            let n = node.borrow();
            (n.val, n.left.clone(), n.right.clone())
        };
        res.push(val);
        if let Some(r) = right {
            stack.push(r);
        }
        if let Some(l) = left {
            stack.push(l);
        }
    }
    res
}

impl Solution {
    pub fn preorder_traversal(root: Link) -> Vec<i32> {
        preorder_traversal(root)
    }
}
