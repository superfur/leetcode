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
     * 107. 二叉树的层序遍历 II
     * 与普通层序遍历（102 题）完全相同的 BFS，
     * 只是最后把层的顺序整体反转，变成从叶子层到根层。
     */
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        java.util.LinkedList<List<Integer>> result = new java.util.LinkedList<>();
        if (root == null) {
            return result;
        }
        java.util.Deque<TreeNode> queue = new java.util.ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new java.util.ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            result.addFirst(level);
        }
        return result;
    }
}
