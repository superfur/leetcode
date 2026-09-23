package main

// Definition for a Node.
// type Node struct {
// 	Val   int
// 	Left  *Node
// 	Right *Node
// 	Next  *Node
// }

// 117. 填充每个节点的下一个右侧节点指针 II
// 普通二叉树，不能像完美二叉树那样直接假设子节点都存在，
// 但同样可以做到 O(1) 额外空间：用一个 dummy 节点作为
// “下一层”链表的临时尾巴，沿着当前层的 next 链遍历，
// 把每个节点存在的 Left/Right 依次接到 dummy 链的末尾；
// 当前层走完后，下一层的头就是 dummy.Next。
func connect(root *Node) *Node {
	node := root
	for node != nil {
		dummy := &Node{}
		tail := dummy
		for node != nil {
			if node.Left != nil {
				tail.Next = node.Left
				tail = tail.Next
			}
			if node.Right != nil {
				tail.Next = node.Right
				tail = tail.Next
			}
			node = node.Next
		}
		node = dummy.Next
	}
	return root
}
