package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 105. 从前序与中序遍历序列构造二叉树
// 前序的第一个元素永远是当前子树的根；在中序里找到这个根的位置，
// 左边就是左子树的中序、右边是右子树的中序。
// 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
// 用一个全局推进的 preIdx 指针避免对 preorder 做切片，
// 只在中序区间 [inLeft, inRight] 上递归划分左右子树。
func buildTree(preorder []int, inorder []int) *TreeNode {
	indexOf := make(map[int]int, len(inorder))
	for i, val := range inorder {
		indexOf[val] = i
	}
	preIdx := 0

	var build func(inLeft, inRight int) *TreeNode
	build = func(inLeft, inRight int) *TreeNode {
		if inLeft > inRight {
			return nil
		}
		rootVal := preorder[preIdx]
		preIdx++
		mid := indexOf[rootVal]
		root := &TreeNode{Val: rootVal}
		root.Left = build(inLeft, mid-1)
		root.Right = build(mid+1, inRight)
		return root
	}

	return build(0, len(inorder)-1)
}
