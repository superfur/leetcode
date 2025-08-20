// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

impl Solution {
    /// K 个一组反转链表
    /// 
    /// 算法思路：
    /// 1. 使用递归方法，每次处理 k 个节点
    /// 2. 先检查是否有足够的节点进行反转
    /// 3. 如果有足够的节点，反转前 k 个节点
    /// 4. 递归处理剩余的节点
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if k <= 1 {
            return head;
        }
        
        let mut head = head;
        let mut current = &mut head;
        
        // 检查是否有足够的节点进行反转
        let mut count = 0;
        let mut temp = current.as_ref();
        while let Some(node) = temp {
            count += 1;
            if count >= k {
                break;
            }
            temp = node.next.as_ref();
        }
        
        // 如果节点数不足 k 个，直接返回
        if count < k {
            return head;
        }
        
        // 反转前 k 个节点
        let mut prev: Option<Box<ListNode>> = None;
        let mut current_node = current.take();
        
        for _ in 0..k {
            if let Some(mut node) = current_node {
                let next = node.next.take();
                node.next = prev;
                prev = Some(node);
                current_node = next;
            }
        }
        
        // 递归处理剩余的节点
        if let Some(mut reversed_head) = prev {
            let remaining = Self::reverse_k_group(current_node, k);
            
            // 找到反转后链表的尾节点，将剩余节点连接到尾部
            let mut tail = &mut reversed_head;
            while let Some(ref next) = tail.next {
                tail = tail.next.as_mut().unwrap();
            }
            tail.next = remaining;
            
            Some(reversed_head)
        } else {
            None
        }
    }
}