from typing import List, Optional


# LeetCode 会提供 ListNode，本地运行用下面定义
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    旋转链表：将链表向右旋转 k 个位置。O(n) 时间，O(1) 空间。
    """
    if not head or not head.next or k == 0:
        return head

    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1
    k = k % n
    if k == 0:
        return head

    slow = fast = head
    for _ in range(k):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next

    new_head = slow.next
    slow.next = None
    tail.next = head
    return new_head


def 旋转链表(*args, **kwargs):
    """args: (head, k) 或 kwargs: head=..., k=..."""
    if args and len(args) >= 2:
        head, k = args[0], args[1]
    elif "head" in kwargs and "k" in kwargs:
        head, k = kwargs["head"], kwargs["k"]
    else:
        return None
    return rotate_right(head, k)


class Solution:
    """LeetCode 驱动需要的 Solution 类"""

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return rotate_right(head, k)


def _list_to_nodes(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def _nodes_to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    head = _list_to_nodes([1, 2, 3, 4, 5])
    got = rotate_right(head, 2)
    print("旋转链表 [1,2,3,4,5] k=2:", _nodes_to_list(got))
