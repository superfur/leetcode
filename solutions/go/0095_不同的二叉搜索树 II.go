package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 95. 不同的二叉搜索树 II
// 区间递归：generate(start, end) 枚举 [start, end] 内每个值作为根，
// 左子树取 generate(start, root-1)，右子树取 generate(root+1, end)，
// 两两组合得到该区间内所有可能的 BST。
func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return []*TreeNode{}
	}

	var generate func(start, end int) []*TreeNode
	generate = func(start, end int) []*TreeNode {
		if start > end {
			return []*TreeNode{nil}
		}
		result := []*TreeNode{}
		for rootVal := start; rootVal <= end; rootVal++ {
			lefts := generate(start, rootVal-1)
			rights := generate(rootVal+1, end)
			for _, left := range lefts {
				for _, right := range rights {
					result = append(result, &TreeNode{Val: rootVal, Left: left, Right: right})
				}
			}
		}
		return result
	}

	return generate(1, n)
}
