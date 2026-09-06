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
    private int[] postorder;
    private java.util.Map<Integer, Integer> indexOf;
    private int postIdx;

    /**
     * 106. 从中序与后序遍历序列构造二叉树
     * 后序的最后一个元素永远是当前子树的根；在中序里找到这个根的位置，
     * 左边是左子树的中序、右边是右子树的中序。
     * 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
     * 用一个从末尾向前推进的 postIdx 指针避免对 postorder 做切片；
     * 因为指针从后往前走，必须先递归构建右子树、再构建左子树。
     */
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.postorder = postorder;
        this.indexOf = new java.util.HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            indexOf.put(inorder[i], i);
        }
        this.postIdx = postorder.length - 1;
        return build(0, inorder.length - 1);
    }

    private TreeNode build(int inLeft, int inRight) {
        if (inLeft > inRight) {
            return null;
        }
        int rootVal = postorder[postIdx--];
        int mid = indexOf.get(rootVal);
        TreeNode root = new TreeNode(rootVal);
        root.right = build(mid + 1, inRight);
        root.left = build(inLeft, mid - 1);
        return root;
    }
}
