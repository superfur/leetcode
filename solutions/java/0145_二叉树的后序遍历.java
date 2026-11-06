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
     * 145. 二叉树的后序遍历
     * 后序是 左 → 右 → 根，它的逆序恰好是 根 → 右 → 左，
     * 而后者就是前序遍历把左右孩子的入栈顺序对调（先压左、后压右）。
     * 所以用显式栈按 根 → 右 → 左 收集值，最后整体反转即可。
     * 不依赖递归深度，时间 O(n)，空间 O(h)（结果数组除外）。
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new java.util.ArrayList<>();
        if (root == null) {
            return res;
        }
        java.util.Deque<TreeNode> stack = new java.util.ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            res.add(node.val);
            if (node.left != null) {
                stack.push(node.left);
            }
            if (node.right != null) {
                stack.push(node.right);
            }
        }
        java.util.Collections.reverse(res);
        return res;
    }
}
