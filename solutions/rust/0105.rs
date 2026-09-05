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

/// 105. 从前序与中序遍历序列构造二叉树
/// 前序的第一个元素永远是当前子树的根；在中序里找到这个根的位置，
/// 左边就是左子树的中序、右边是右子树的中序。
/// 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
/// 用一个全局推进的 pre_idx 指针避免对 preorder 做切片，
/// 只在中序区间 [in_left, in_right] 上递归划分左右子树。
pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Link {
    let index_of: HashMap<i32, usize> = inorder.iter().enumerate().map(|(i, &v)| (v, i)).collect();
    let mut pre_idx = 0usize;

    fn build(preorder: &[i32], index_of: &HashMap<i32, usize>, pre_idx: &mut usize, in_left: i32, in_right: i32) -> Link {
        if in_left > in_right {
            return None;
        }
        let root_val = preorder[*pre_idx];
        *pre_idx += 1;
        let mid = index_of[&root_val] as i32;
        let left = build(preorder, index_of, pre_idx, in_left, mid - 1);
        let right = build(preorder, index_of, pre_idx, mid + 1, in_right);
        Some(Rc::new(RefCell::new(TreeNode { val: root_val, left, right })))
    }

    build(&preorder, &index_of, &mut pre_idx, 0, inorder.len() as i32 - 1)
}

impl Solution {
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Link {
        build_tree(preorder, inorder)
    }
}
