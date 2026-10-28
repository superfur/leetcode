package main

// Definition for a Node.
// type Node struct {
//     Val int
//     Next *Node
//     Random *Node
// }

// 138. 随机链表的复制
// 哈希表 + 两遍遍历：
// 第一遍只复制节点的 Val，建立「原节点 -> 克隆节点」的映射；
// 第二遍再通过映射给每个克隆节点接上 Next 和 Random（指向 nil 时 map 查询返回 nil，正好是想要的值）。
// 哈希表保证同一个原节点只会有一个克隆体，所以 Random 指向的共享节点不会被复制多份。
// 时间 O(n)，空间 O(n)。
func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}

	clones := map[*Node]*Node{}
	for cur := head; cur != nil; cur = cur.Next {
		clones[cur] = &Node{Val: cur.Val}
	}
	for cur := head; cur != nil; cur = cur.Next {
		clones[cur].Next = clones[cur.Next]
		clones[cur].Random = clones[cur.Random]
	}
	return clones[head]
}
