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

/// 99. 恢复二叉搜索树
/// 中序遍历（迭代，栈）应严格递增；用 prev 记录上一个访问节点，
/// 每次出现 prev.val > cur.val 就是一次“逆序对”：
/// 第一次出现记录 (prev, cur) 为 first/second 候选；
/// 若又出现第二次逆序（两个交换节点不相邻），把 second 更新为这次的 cur。
/// 最后交换 first 和 second 的值即可恢复。
pub fn recover_tree(root: &mut Link) {
    let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
    let mut prev: Link = None;
    let mut first: Link = None;
    let mut second: Link = None;
    let mut node = root.clone();

    while node.is_some() || !stack.is_empty() {
        while let Some(n) = node {
            node = n.borrow().left.clone();
            stack.push(n);
        }
        let n = stack.pop().unwrap();
        if let Some(p) = &prev {
            if p.borrow().val > n.borrow().val {
                if first.is_none() {
                    first = Some(p.clone());
                }
                second = Some(n.clone());
            }
        }
        prev = Some(n.clone());
        node = n.borrow().right.clone();
    }

    if let (Some(f), Some(s)) = (first, second) {
        let tmp = f.borrow().val;
        f.borrow_mut().val = s.borrow().val;
        s.borrow_mut().val = tmp;
    }
}

impl Solution {
    pub fn recover_tree(root: &mut Link) {
        recover_tree(root)
    }
}
