package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 108. 将有序数组转换为二叉搜索树
// 每次取区间中点作为根（自然保证左右子树节点数最多差 1，即高度平衡），
// 左半区间递归建左子树，右半区间递归建右子树。
// 答案不唯一，只要是高度平衡的 BST 即可。
func sortedArrayToBST(nums []int) *TreeNode {
	var build func(left, right int) *TreeNode
	build = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}
		mid := (left + right) / 2
		root := &TreeNode{Val: nums[mid]}
		root.Left = build(left, mid-1)
		root.Right = build(mid+1, right)
		return root
	}

	return build(0, len(nums)-1)
}
