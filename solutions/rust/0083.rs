/// 83. 删除排序链表中的重复元素
/// 链表已排序，提取所有值后去重相邻重复，再重建链表即可。
/// （与 82 题相同的 Rust 实现套路，避开 Box prev.next 改写难题。）
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     fn new(val: i32) -> Self {
//         ListNode { val, next: None }
//     }
// }

pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut vals: Vec<i32> = Vec::new();
    let mut curr = head;
    while let Some(node) = curr {
        vals.push(node.val);
        curr = node.next;
    }

    let mut keep: Vec<i32> = Vec::with_capacity(vals.len());
    for &v in &vals {
        if keep.last() != Some(&v) {
            keep.push(v);
        }
    }

    let mut new_head: Option<Box<ListNode>> = None;
    for &v in keep.iter().rev() {
        new_head = Some(Box::new(ListNode { val: v, next: new_head }));
    }
    new_head
}

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        delete_duplicates(head)
    }
}