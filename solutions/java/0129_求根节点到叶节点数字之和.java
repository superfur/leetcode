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
     * 129. 求根节点到叶节点数字之和
     * DFS 往下传「根到当前节点已经拼出的数字」（cur * 10 + val），
     * 走到叶子节点时这个数字就是一条完整路径代表的数，累加进答案。
     */
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int cur) {
        if (node == null) {
            return 0;
        }
        cur = cur * 10 + node.val;
        if (node.left == null && node.right == null) {
            return cur;
        }
        return dfs(node.left, cur) + dfs(node.right, cur);
    }
}
