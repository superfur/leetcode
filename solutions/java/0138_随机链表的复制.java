/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    /**
     * 138. 随机链表的复制
     * 哈希表 + 两遍遍历：
     * 第一遍只复制节点的 val，建立「原节点 -> 克隆节点」的映射；
     * 第二遍再通过映射给每个克隆节点接上 next 和 random（HashMap.get(null) 返回 null，正好是想要的值）。
     * 哈希表保证同一个原节点只会有一个克隆体，所以 random 指向的共享节点不会被复制多份。
     * 时间 O(n)，空间 O(n)。
     */
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }

        Map<Node, Node> clones = new HashMap<>();
        for (Node cur = head; cur != null; cur = cur.next) {
            clones.put(cur, new Node(cur.val));
        }
        for (Node cur = head; cur != null; cur = cur.next) {
            clones.get(cur).next = clones.get(cur.next);
            clones.get(cur).random = clones.get(cur.random);
        }
        return clones.get(head);
    }
}
