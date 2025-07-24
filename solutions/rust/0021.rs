impl Solution {
    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>
    ) -> Option<Box<ListNode>> {
        match (list1.as_mut(), list2.as_mut()) {
            (None, _) => list2,
            (_, None) => list1,
            (Some(l1), Some(l2)) => {
                if l1.val < l2.val {
                    let next = l1.next.take();
                    l1.next = Self::merge_two_lists(next, list2);
                    list1
                } else {
                    let next = l2.next.take();
                    l2.next = Self::merge_two_lists(list1, next);
                    list2
                }
            }
        }
    }
}