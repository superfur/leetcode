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
     * 102. 二叉树的层序遍历
     * BFS：队列每轮先记录当前层的节点数 size，
     * 依次弹出 size 个节点收集值、把它们的子节点入队，
     * 这一轮就是完整的一层。
     */
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new java.util.ArrayList<>();
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
            result.add(level);
        }
        return result;
    }
}
