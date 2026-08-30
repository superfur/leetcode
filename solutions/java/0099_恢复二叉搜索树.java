/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    /**
     * 99. 恢复二叉搜索树
     * 中序遍历（迭代，栈）应严格递增；用 prev 记录上一个访问节点，
     * 每次出现 prev.val > cur.val 就是一次"逆序对"：
     * 第一次出现记录 (prev, cur) 为 first/second 候选；
     * 若又出现第二次逆序（两个交换节点不相邻），把 second 更新为这次的 cur。
     * 最后交换 first 和 second 的值即可恢复。
     */
    public void recoverTree(TreeNode root) {
        java.util.Deque<TreeNode> stack = new java.util.ArrayDeque<>();
        TreeNode prev = null, first = null, second = null;
        TreeNode node = root;

        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            if (prev != null && prev.val > node.val) {
                if (first == null) {
                    first = prev;
                }
                second = node;
            }
            prev = node;
            node = node.right;
        }

        if (first != null && second != null) {
            int tmp = first.val;
            first.val = second.val;
            second.val = tmp;
        }
    }
}
