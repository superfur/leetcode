package main

// Definition for a Node.
// type Node struct {
//     Val int
//     Neighbors []*Node
// }

// 133. 克隆图
// BFS 遍历原图，用 map 记录「原节点 -> 克隆节点」：
// 遇到还没克隆的邻居就新建克隆并入队，
// 然后把邻居对应的克隆节点挂到当前节点的克隆体的 Neighbors 上。
// map 同时起到「已访问」的作用，所以环不会死循环。
func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}

	clones := map[*Node]*Node{node: {Val: node.Val}}
	queue := []*Node{node}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, nb := range cur.Neighbors {
			if _, ok := clones[nb]; !ok {
				clones[nb] = &Node{Val: nb.Val}
				queue = append(queue, nb)
			}
			clones[cur].Neighbors = append(clones[cur].Neighbors, clones[nb])
		}
	}
	return clones[node]
}
