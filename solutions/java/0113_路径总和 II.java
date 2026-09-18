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
    private final List<List<Integer>> result = new java.util.ArrayList<>();
    private final java.util.Deque<Integer> path = new java.util.ArrayDeque<>();

    /**
     * 113. 路径总和 II
     * 回溯：沿途把节点值压入 path，到叶子节点时若剩余目标值
     * 正好归零就把 path 的一份拷贝收进结果；不管是否匹配，
     * 递归返回前都要把刚压入的节点值弹出，恢复现场再试下一分支。
     */
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        dfs(root, targetSum);
        return result;
    }

    private void dfs(TreeNode node, int remaining) {
        if (node == null) {
            return;
        }
        path.addLast(node.val);
        remaining -= node.val;
        if (node.left == null && node.right == null && remaining == 0) {
            result.add(new java.util.ArrayList<>(path));
        } else {
            dfs(node.left, remaining);
            dfs(node.right, remaining);
        }
        path.removeLast();
    }
}
