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
     * 103. 二叉树的锯齿形层序遍历
     * 与普通层序遍历（BFS）相同，只是奇数层（从 0 计数的第 1、3、5... 层）
     * 收集完之后把这一层的结果反转即可。
     */
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new java.util.ArrayList<>();
        if (root == null) {
            return result;
        }
        java.util.Deque<TreeNode> queue = new java.util.ArrayDeque<>();
        queue.offer(root);
        boolean leftToRight = true;
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
            if (!leftToRight) {
                java.util.Collections.reverse(level);
            }
            result.add(level);
            leftToRight = !leftToRight;
        }
        return result;
    }
}
