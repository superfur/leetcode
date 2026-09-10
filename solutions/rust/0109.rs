// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
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

/// 109. 有序链表转换二叉搜索树
/// 先把链表一次性摊平成数组（O(n)），之后就是 108 题的做法：
/// 取区间中点为根递归划分左右子树，天然保证高度平衡。
pub fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Link {
    let mut values = Vec::new();
    let mut node = head;
    while let Some(n) = node {
        values.push(n.val);
        node = n.next;
    }

    fn build(values: &[i32], left: i32, right: i32) -> Link {
        if left > right {
            return None;
        }
        let mid = (left + right) / 2;
        let l = build(values, left, mid - 1);
        let r = build(values, mid + 1, right);
        Some(Rc::new(RefCell::new(TreeNode {
            val: values[mid as usize],
            left: l,
            right: r,
        })))
    }

    build(&values, 0, values.len() as i32 - 1)
}

impl Solution {
    pub fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Link {
        sorted_list_to_bst(head)
    }
}
