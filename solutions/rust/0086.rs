/// 86. 分隔链表
/// Box 链表 prev.next 改写复杂，与 82/83 同套路：提取值 → 分区 → 重建链表。
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

pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
    // 1. 提取所有值
    let mut vals: Vec<i32> = Vec::new();
    let mut curr = head;
    while let Some(node) = curr {
        vals.push(node.val);
        curr = node.next;
    }

    // 2. 稳定分区：先 < x，再 >= x
    let mut small: Vec<i32> = Vec::new();
    let mut large: Vec<i32> = Vec::new();
    for v in vals {
        if v < x {
            small.push(v);
        } else {
            large.push(v);
        }
    }
    small.extend(large);

    // 3. 重建链表
    let mut new_head: Option<Box<ListNode>> = None;
    for &v in small.iter().rev() {
        new_head = Some(Box::new(ListNode { val: v, next: new_head }));
    }
    new_head
}

impl Solution {
    pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        partition(head, x)
    }
}