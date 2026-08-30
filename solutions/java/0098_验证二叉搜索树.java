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
     * 98. 验证二叉搜索树
     * 区间递归：每个节点携带一个开区间 (low, high)，其值必须落在区间内；
     * 向左递归时收紧上界为当前值，向右递归时收紧下界为当前值。
     */
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean validate(TreeNode node, long low, long high) {
        if (node == null) {
            return true;
        }
        if (!(node.val > low && node.val < high)) {
            return false;
        }
        return validate(node.left, low, node.val) && validate(node.right, node.val, high);
    }
}
