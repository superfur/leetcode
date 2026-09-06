package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 106. 从中序与后序遍历序列构造二叉树
// 后序的最后一个元素永远是当前子树的根；在中序里找到这个根的位置，
// 左边是左子树的中序、右边是右子树的中序。
// 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
// 用一个从末尾向前推进的 postIdx 指针避免对 postorder 做切片；
// 因为指针从后往前走，必须先递归构建右子树、再构建左子树。
func buildTree(inorder []int, postorder []int) *TreeNode {
	indexOf := make(map[int]int, len(inorder))
	for i, val := range inorder {
		indexOf[val] = i
	}
	postIdx := len(postorder) - 1

	var build func(inLeft, inRight int) *TreeNode
	build = func(inLeft, inRight int) *TreeNode {
		if inLeft > inRight {
			return nil
		}
		rootVal := postorder[postIdx]
		postIdx--
		mid := indexOf[rootVal]
		root := &TreeNode{Val: rootVal}
		root.Right = build(mid+1, inRight)
		root.Left = build(inLeft, mid-1)
		return root
	}

	return build(0, len(inorder)-1)
}
