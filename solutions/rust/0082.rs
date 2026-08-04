/// 82. 删除排序链表中的重复元素 II
/// 删除所有出现重复的数字节点，只保留出现一次的。
/// 由于 Rust Box 链表难以同时维护 prev 引用和修改 prev.next，
/// 这里走"提取值→过滤→重建"路线：单次扫描利用链表已排序的特性，
/// 判断 vals[i] 是否与左右邻居相等，相等则丢弃。
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
    // 1. 提取所有值
    let mut vals: Vec<i32> = Vec::new();
    let mut curr = head;
    while let Some(node) = curr {
        vals.push(node.val);
        curr = node.next;
    }

    // 2. 链表已排序，vals[i] 需保留当且仅当它不等于左右邻居
    let n = vals.len();
    let mut keep: Vec<i32> = Vec::with_capacity(n);
    for i in 0..n {
        let prev_dup = i > 0 && vals[i - 1] == vals[i];
        let next_dup = i + 1 < n && vals[i + 1] == vals[i];
        if !prev_dup && !next_dup {
            keep.push(vals[i]);
        }
    }

    // 3. 重建链表
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