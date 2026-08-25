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
     * 94. 二叉树的中序遍历
     * 迭代：用栈模拟递归——一路把左子树压栈到底，
     * 弹出访问后转向右子树，重复直到栈空且当前节点为空。
     */
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new java.util.ArrayList<>();
        java.util.Deque<TreeNode> stack = new java.util.ArrayDeque<>();
        TreeNode node = root;
        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            result.add(node.val);
            node = node.right;
        }
        return result;
    }
}
