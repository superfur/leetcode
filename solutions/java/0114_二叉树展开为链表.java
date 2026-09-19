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
     * 114. 二叉树展开为链表
     * O(1) 额外空间：从根开始，若当前节点有左子树，
     * 就在左子树里一路往右找到最右节点（也就是左子树先序遍历的最后一个节点），
     * 把当前节点原来的右子树接到这个最右节点的 right 上，
     * 再把左子树整体搬到右边、左指针置空。
     * 这样处理完当前节点后，沿着 right 指针继续处理下一个节点，
     * 整体顺序正好等于先序遍历。
     */
    public void flatten(TreeNode root) {
        TreeNode node = root;
        while (node != null) {
            if (node.left != null) {
                TreeNode predecessor = node.left;
                while (predecessor.right != null) {
                    predecessor = predecessor.right;
                }
                predecessor.right = node.right;
                node.right = node.left;
                node.left = null;
            }
            node = node.right;
        }
    }
}
