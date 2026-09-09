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

/// 108. 将有序数组转换为二叉搜索树
/// 每次取区间中点作为根（自然保证左右子树节点数最多差 1，即高度平衡），
/// 左半区间递归建左子树，右半区间递归建右子树。
/// 答案不唯一，只要是高度平衡的 BST 即可。
pub fn sorted_array_to_bst(nums: Vec<i32>) -> Link {
    fn build(nums: &[i32], left: i32, right: i32) -> Link {
        if left > right {
            return None;
        }
        let mid = (left + right) / 2;
        let l = build(nums, left, mid - 1);
        let r = build(nums, mid + 1, right);
        Some(Rc::new(RefCell::new(TreeNode {
            val: nums[mid as usize],
            left: l,
            right: r,
        })))
    }

    build(&nums, 0, nums.len() as i32 - 1)
}

impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Link {
        sorted_array_to_bst(nums)
    }
}
