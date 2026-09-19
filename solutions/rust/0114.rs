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

/// 114. 二叉树展开为链表
/// O(1) 额外空间：从根开始，若当前节点有左子树，
/// 就在左子树里一路往右找到最右节点（也就是左子树先序遍历的最后一个节点），
/// 把当前节点原来的右子树接到这个最右节点的 right 上，
/// 再把左子树整体搬到右边、左指针置空。
/// 这样处理完当前节点后，沿着 right 指针继续处理下一个节点，
/// 整体顺序正好等于先序遍历。
pub fn flatten(root: &mut Link) {
    let mut node = root.clone();
    while let Some(n) = node {
        let left = n.borrow().left.clone();
        if let Some(left_node) = left {
            let mut predecessor = left_node.clone();
            loop {
                let next = predecessor.borrow().right.clone();
                match next {
                    Some(p) => predecessor = p,
                    None => break,
                }
            }
            let right = n.borrow().right.clone();
            predecessor.borrow_mut().right = right;
            n.borrow_mut().right = Some(left_node);
            n.borrow_mut().left = None;
        }
        node = n.borrow().right.clone();
    }
}

impl Solution {
    pub fn flatten(root: &mut Link) {
        flatten(root)
    }
}
