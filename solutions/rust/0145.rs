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

/// 145. 二叉树的后序遍历
/// 后序是 左 → 右 → 根，它的逆序恰好是 根 → 右 → 左，
/// 而后者就是前序遍历把左右孩子的入栈顺序对调（先压左、后压右）。
/// 所以用显式栈按 根 → 右 → 左 收集值，最后整体反转即可。
/// 不依赖递归深度，时间 O(n)，空间 O(h)（结果数组除外）。
pub fn postorder_traversal(root: Link) -> Vec<i32> {
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
        if let Some(l) = left {
            stack.push(l);
        }
        if let Some(r) = right {
            stack.push(r);
        }
    }
    res.reverse();
    res
}

impl Solution {
    pub fn postorder_traversal(root: Link) -> Vec<i32> {
        postorder_traversal(root)
    }
}
