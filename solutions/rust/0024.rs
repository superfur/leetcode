// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return head;
        }
        
        let mut dummy = ListNode::new(0);
        let mut prev = &mut dummy;
        let mut current = head;·
        
        while let Some(mut curr) = current {
            if let Some(mut next) = curr.next.take() {
                // 保存 next 的下一个节点
                let next_next = next.next.take();
                
                // 交换当前节点和下一个节点
                next.next = Some(curr);
                prev.next = Some(next);
                
                // 移动到下一对·
                prev = prev.next.as_mut().unwrap().next.as_mut().unwrap();
                current = next_next;
            } else {
                // 如果只有一个节点，直接添加
                prev.next = Some(curr);
                break;
            }
        }
        
        dummy.next
    }
}