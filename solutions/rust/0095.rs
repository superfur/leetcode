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

/// 95. 不同的二叉搜索树 II
/// 区间递归：generate(start, end) 枚举 [start, end] 内每个值作为根，
/// 左子树取 generate(start, root-1)，右子树取 generate(root+1, end)，
/// 两两组合得到该区间内所有可能的 BST。
pub fn generate_trees(n: i32) -> Vec<Link> {
    if n == 0 {
        return Vec::new();
    }

    fn generate(start: i32, end: i32) -> Vec<Link> {
        if start > end {
            return vec![None];
        }
        let mut result = Vec::new();
        for root_val in start..=end {
            let lefts = generate(start, root_val - 1);
            let rights = generate(root_val + 1, end);
            for left in &lefts {
                for right in &rights {
                    result.push(Some(Rc::new(RefCell::new(TreeNode {
                        val: root_val,
                        left: left.clone(),
                        right: right.clone(),
                    }))));
                }
            }
        }
        result
    }

    generate(1, n)
}

impl Solution {
    pub fn generate_trees(n: i32) -> Vec<Link> {
        generate_trees(n)
    }
}
