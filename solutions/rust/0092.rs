/// 92. 反转链表 II
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

/// Box 链表原地摘取/头插较繁琐，改用与 86 同套路：
/// 提取全部值 → 反转 [left, right) 区间 → 重建链表。
pub fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {
    let mut vals: Vec<i32> = Vec::new();
    let mut curr = head;
    while let Some(node) = curr {
        vals.push(node.val);
        curr = node.next;
    }

    let (l, r) = ((left - 1) as usize, (right - 1) as usize);
    vals[l..=r].reverse();

    let mut new_head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {
        new_head = Some(Box::new(ListNode { val: v, next: new_head }));
    }
    new_head
}

impl Solution {
    pub fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {
        reverse_between(head, left, right)
    }
}
