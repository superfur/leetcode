// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

type Link = Option<Rc<RefCell<TreeNode>>>;

/// 106. 从中序与后序遍历序列构造二叉树
/// 后序的最后一个元素永远是当前子树的根；在中序里找到这个根的位置，
/// 左边是左子树的中序、右边是右子树的中序。
/// 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
/// 用一个从末尾向前推进的 post_idx 指针避免对 postorder 做切片；
/// 因为指针从后往前走，必须先递归构建右子树、再构建左子树。
pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Link {
    let index_of: HashMap<i32, usize> = inorder.iter().enumerate().map(|(i, &v)| (v, i)).collect();
    let mut post_idx = postorder.len() as i32 - 1;

    fn build(postorder: &[i32], index_of: &HashMap<i32, usize>, post_idx: &mut i32, in_left: i32, in_right: i32) -> Link {
        if in_left > in_right {
            return None;
        }
        let root_val = postorder[*post_idx as usize];
        *post_idx -= 1;
        let mid = index_of[&root_val] as i32;
        let right = build(postorder, index_of, post_idx, mid + 1, in_right);
        let left = build(postorder, index_of, post_idx, in_left, mid - 1);
        Some(Rc::new(RefCell::new(TreeNode { val: root_val, left, right })))
    }

    build(&postorder, &index_of, &mut post_idx, 0, inorder.len() as i32 - 1)
}

impl Solution {
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Link {
        build_tree(inorder, postorder)
    }
}
