/**
 * 111. 二叉树的最小深度
 * 最小深度要求到最近的"叶子节点"，所以只有一个子节点的节点
 * 不能直接取 min(0, 子树深度)——必须沿着那个唯一的非空子节点继续走。
 * 只有左右子节点都为空（真正的叶子）时深度才是 1。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function minDepth(root: TNode | null): number {
    if (!root) return 0;
    if (!root.left) return 1 + minDepth(root.right);
    if (!root.right) return 1 + minDepth(root.left);
    return 1 + Math.min(minDepth(root.left), minDepth(root.right));
}

export default minDepth;
