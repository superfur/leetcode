package main

// Definition for singly-linked list.
// type ListNode struct {
//     Val int
//     Next *ListNode
// }

// 148. 排序链表
// 自底向上的归并排序，满足进阶要求：O(n log n) 时间、O(1) 额外空间（没有递归栈）。
// 先数出长度 n，然后让子链表长度 step 依次取 1, 2, 4, ...：
// 每一轮从头扫描，每次切出相邻的两段各 step 个节点，合并后接到已处理部分的末尾。
// 合并时 `<=` 优先取左段，保证排序稳定。
func sortList(head *ListNode) *ListNode {
	n := 0
	for node := head; node != nil; node = node.Next {
		n++
	}

	dummy := &ListNode{Next: head}
	for step := 1; step < n; step *= 2 {
		prev, cur := dummy, dummy.Next
		for cur != nil {
			left := cur
			right := cutList(left, step)
			cur = cutList(right, step)
			prev = mergeList(left, right, prev)
		}
	}
	return dummy.Next
}

// cutList 从 head 开始保留 n 个节点，断开并返回剩余部分的头。
func cutList(head *ListNode, n int) *ListNode {
	for head != nil && n > 1 {
		head = head.Next
		n--
	}
	if head == nil {
		return nil
	}
	rest := head.Next
	head.Next = nil
	return rest
}

// mergeList 把有序链表 a、b 合并接到 tail 后面，返回合并后的最后一个节点。
func mergeList(a, b, tail *ListNode) *ListNode {
	for a != nil && b != nil {
		if a.Val <= b.Val {
			tail.Next = a
			a = a.Next
		} else {
			tail.Next = b
			b = b.Next
		}
		tail = tail.Next
	}
	if a != nil {
		tail.Next = a
	} else {
		tail.Next = b
	}
	for tail.Next != nil {
		tail = tail.Next
	}
	return tail
}
