/**
 * 104. 二叉树的最大深度
 * 递归：空树深度为 0，否则为左右子树深度的较大值加 1。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function maxDepth(root: TNode | null): number {
    if (!root) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

export default maxDepth;
