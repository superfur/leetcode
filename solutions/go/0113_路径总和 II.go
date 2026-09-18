package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 113. 路径总和 II
// 回溯：沿途把节点值压入 path，到叶子节点时若剩余目标值
// 正好归零就把 path 的一份拷贝收进结果；不管是否匹配，
// 递归返回前都要把刚压入的节点值弹出，恢复现场再试下一分支。
func pathSum(root *TreeNode, targetSum int) [][]int {
	result := [][]int{}
	path := []int{}

	var dfs func(node *TreeNode, remaining int)
	dfs = func(node *TreeNode, remaining int) {
		if node == nil {
			return
		}
		path = append(path, node.Val)
		remaining -= node.Val
		if node.Left == nil && node.Right == nil && remaining == 0 {
			cp := make([]int, len(path))
			copy(cp, path)
			result = append(result, cp)
		} else {
			dfs(node.Left, remaining)
			dfs(node.Right, remaining)
		}
		path = path[:len(path)-1]
	}

	dfs(root, targetSum)
	return result
}
