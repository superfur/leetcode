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
     * 117. 填充每个节点的下一个右侧节点指针 II
     * 普通二叉树，不能像完美二叉树那样直接假设子节点都存在，
     * 但同样可以做到 O(1) 额外空间：用一个 dummy 节点作为
     * "下一层"链表的临时尾巴，沿着当前层的 next 链遍历，
     * 把每个节点存在的 left/right 依次接到 dummy 链的末尾；
     * 当前层走完后，下一层的头就是 dummy.next。
     */
    public Node connect(Node root) {
        Node node = root;
        while (node != null) {
            Node dummy = new Node();
            Node tail = dummy;
            while (node != null) {
                if (node.left != null) {
                    tail.next = node.left;
                    tail = tail.next;
                }
                if (node.right != null) {
                    tail.next = node.right;
                    tail = tail.next;
                }
                node = node.next;
            }
            node = dummy.next;
        }
        return root;
    }
}
