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
     * 95. 不同的二叉搜索树 II
     * 区间递归：generate(start, end) 枚举 [start, end] 内每个值作为根，
     * 左子树取 generate(start, root-1)，右子树取 generate(root+1, end)，
     * 两两组合得到该区间内所有可能的 BST。
     */
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) {
            return new java.util.ArrayList<>();
        }
        return generate(1, n);
    }

    private List<TreeNode> generate(int start, int end) {
        List<TreeNode> result = new java.util.ArrayList<>();
        if (start > end) {
            result.add(null);
            return result;
        }
        for (int rootVal = start; rootVal <= end; rootVal++) {
            List<TreeNode> lefts = generate(start, rootVal - 1);
            List<TreeNode> rights = generate(rootVal + 1, end);
            for (TreeNode left : lefts) {
                for (TreeNode right : rights) {
                    result.add(new TreeNode(rootVal, left, right));
                }
            }
        }
        return result;
    }
}
