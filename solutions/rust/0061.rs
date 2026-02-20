/*
 * 旋转链表（LeetCode 61）
 *
 * 将链表向右旋转 k 个位置。ListNode 由 LeetCode 提供。
 *
 * 时间复杂度: O(n)
 * 空间复杂度: O(n)，用于暂存节点值后重建链表（也可用双指针做到 O(1)，但 Rust 借位较繁琐）
 */
impl Solution {
    pub fn rotate_right(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let vals = Self::list_to_vec(head);
        if vals.is_empty() || vals.len() == 1 {
            return Self::vec_to_list(&vals);
        }

        let n = vals.len();
        let k = (k as usize) % n;
        if k == 0 {
            return Self::vec_to_list(&vals);
        }

        let mut rotated = vals[n - k..].to_vec();
        rotated.extend_from_slice(&vals[..n - k]);
        Self::vec_to_list(&rotated)
    }

    fn list_to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut v = Vec::new();
        while let Some(node) = head {
            v.push(node.val);
            head = node.next;
        }
        v
    }

    fn vec_to_list(v: &[i32]) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: None });
        let mut cur = &mut dummy;
        for &val in v {
            cur.next = Some(Box::new(ListNode { val, next: None }));
            cur = cur.next.as_mut().unwrap();
        }
        dummy.next
    }
}
