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

/// 102. 二叉树的层序遍历
/// BFS：队列每轮先记录当前层的节点数 size，
/// 依次弹出 size 个节点收集值、把它们的子节点入队，
/// 这一轮就是完整的一层。
pub fn level_order(root: Link) -> Vec<Vec<i32>> {
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

    result
}

impl Solution {
    pub fn level_order(root: Link) -> Vec<Vec<i32>> {
        level_order(root)
    }
}
