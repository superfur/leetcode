impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut fast: *mut ListNode = &mut *dummy;
        let mut slow: *mut ListNode = &mut *dummy;

        // fast 先走 n 步
        for _ in 0..n {
            unsafe {
                fast = match (*fast).next.as_mut() {
                    Some(node) => &mut **node,
                    None => return dummy.next,
                };
            }
        }

        // fast 再走到末尾，slow 同步前进
        unsafe {
            while (*fast).next.is_some() {
                fast = (*fast).next.as_mut().map(|node| &mut **node).unwrap();
                slow = (*slow).next.as_mut().map(|node| &mut **node).unwrap();
            }
            // 删除 slow.next
            let next = (*slow).next.as_mut().and_then(|node| node.next.take());
            (*slow).next = next;
        }

        dummy.next
    }
}

