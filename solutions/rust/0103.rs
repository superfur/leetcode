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

/// 103. 二叉树的锯齿形层序遍历
/// 与普通层序遍历（BFS）相同，只是奇数层（从 0 计数的第 1、3、5... 层）
/// 收集完之后把这一层的结果反转即可。
pub fn zigzag_level_order(root: Link) -> Vec<Vec<i32>> {
    let mut result = Vec::new();
    let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
    if let Some(r) = root {
        queue.push_back(r);
    }
    let mut left_to_right = true;

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
        if !left_to_right {
            level.reverse();
        }
        result.push(level);
        left_to_right = !left_to_right;
    }

    result
}

impl Solution {
    pub fn zigzag_level_order(root: Link) -> Vec<Vec<i32>> {
        zigzag_level_order(root)
    }
}
