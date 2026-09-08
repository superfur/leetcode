// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

type Link = Option<Rc<RefCell<TreeNode>>>;

/// 107. 二叉树的层序遍历 II
/// 与普通层序遍历（102 题）完全相同的 BFS，
/// 只是最后把层的顺序整体反转，变成从叶子层到根层。
pub fn level_order_bottom(root: Link) -> Vec<Vec<i32>> {
    let mut result = Vec::new();
    let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
    if let Some(r) = root {
        queue.push_back(r);
    }

    while !queue.is_empty() {
        let size = queue.len();
        let mut level = Vec::with_capacity(size);
        for _ in 0..size {
            let node = queue.pop_front().unwrap();
            let (val, left, right) = {
                let n = node.borrow();
                (n.val, n.left.clone(), n.right.clone())
            };
            level.push(val);
            if let Some(left) = left {
                queue.push_back(left);
            }
            if let Some(right) = right {
                queue.push_back(right);
            }
        }
        result.push(level);
    }

    result.reverse();
    result
}

impl Solution {
    pub fn level_order_bottom(root: Link) -> Vec<Vec<i32>> {
        level_order_bottom(root)
    }
}
