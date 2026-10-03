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
    private int best;

    /**
     * 124. 二叉树中的最大路径和
     * 后序递归：dfs(node) 返回「以 node 为起点、向下走的最大贡献值」
     * （贡献为负就当作 0，即不选这条分支）；
     * 同时把「左贡献 + 节点值 + 右贡献」当作以 node 为最高点的路径和，更新全局答案。
     */
    public int maxPathSum(TreeNode root) {
        best = Integer.MIN_VALUE;
        dfs(root);
        return best;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = Math.max(dfs(node.left), 0);
        int right = Math.max(dfs(node.right), 0);
        best = Math.max(best, node.val + left + right);
        return node.val + Math.max(left, right);
    }
}
