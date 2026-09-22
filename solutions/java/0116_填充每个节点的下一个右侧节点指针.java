/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    /**
     * 116. 填充每个节点的下一个右侧节点指针
     * O(1) 额外空间：利用已经连好的上一层 next 指针去连接下一层——
     * leftmost 指向当前层最左节点，用 head 沿着当前层的 next 链
     * 往右走，每一步把 head.left.next 接到 head.right，
     * 再把 head.right.next 接到 head.next.left（如果 head.next 存在）；
     * 走完当前层后，leftmost 下移一层，重复直到最底层（叶子层没有子节点）。
     * 这是完美二叉树，所以只要 leftmost.left 存在就说明还有下一层。
     */
    public Node connect(Node root) {
        Node leftmost = root;
        while (leftmost != null && leftmost.left != null) {
            Node head = leftmost;
            while (head != null) {
                head.left.next = head.right;
                if (head.next != null) {
                    head.right.next = head.next.left;
                }
                head = head.next;
            }
            leftmost = leftmost.left;
        }
        return root;
    }
}
