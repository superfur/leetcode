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
    private int[] preorder;
    private java.util.Map<Integer, Integer> indexOf;
    private int preIdx;

    /**
     * 105. 从前序与中序遍历序列构造二叉树
     * 前序的第一个元素永远是当前子树的根；在中序里找到这个根的位置，
     * 左边就是左子树的中序、右边是右子树的中序。
     * 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
     * 用一个全局推进的 preIdx 指针避免对 preorder 做切片，
     * 只在中序区间 [inLeft, inRight] 上递归划分左右子树。
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.indexOf = new java.util.HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            indexOf.put(inorder[i], i);
        }
        this.preIdx = 0;
        return build(0, inorder.length - 1);
    }

    private TreeNode build(int inLeft, int inRight) {
        if (inLeft > inRight) {
            return null;
        }
        int rootVal = preorder[preIdx++];
        int mid = indexOf.get(rootVal);
        TreeNode root = new TreeNode(rootVal);
        root.left = build(inLeft, mid - 1);
        root.right = build(mid + 1, inRight);
        return root;
    }
}
