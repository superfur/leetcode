package main

// Definition for a Node.
// type Node struct {
// 	Val   int
// 	Left  *Node
// 	Right *Node
// 	Next  *Node
// }

// 116. 填充每个节点的下一个右侧节点指针
// O(1) 额外空间：利用已经连好的上一层 next 指针去连接下一层——
// leftmost 指向当前层最左节点，用 head 沿着当前层的 next 链
// 往右走，每一步把 head.Left.Next 接到 head.Right，
// 再把 head.Right.Next 接到 head.Next.Left（如果 head.Next 存在）；
// 走完当前层后，leftmost 下移一层，重复直到最底层（叶子层没有子节点）。
// 这是完美二叉树，所以只要 leftmost.Left 存在就说明还有下一层。
func connect(root *Node) *Node {
	leftmost := root
	for leftmost != nil && leftmost.Left != nil {
		head := leftmost
		for head != nil {
			head.Left.Next = head.Right
			if head.Next != nil {
				head.Right.Next = head.Next.Left
			}
			head = head.Next
		}
		leftmost = leftmost.Left
	}
	return root
}
