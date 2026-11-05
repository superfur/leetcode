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
     * 144. 二叉树的前序遍历
     * 迭代 + 显式栈：弹出节点就记录它的值（根），再先压右孩子、后压左孩子，
     * 这样下一次弹出的就是左孩子，顺序为 根 → 左 → 右。
     * 不依赖递归深度，时间 O(n)，空间 O(h)。
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new java.util.ArrayList<>();
        if (root == null) {
            return res;
        }
        java.util.Deque<TreeNode> stack = new java.util.ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            res.add(node.val);
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        return res;
    }
}
