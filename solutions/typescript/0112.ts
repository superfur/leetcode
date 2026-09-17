/**
 * 112. 路径总和
 * 递归：空树直接不存在路径；到达叶子节点时判断剩余目标值
 * 是否正好等于该叶子的值；否则把目标值减去当前节点值，
 * 分别在左右子树里继续找。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function hasPathSum(root: TNode | null, targetSum: number): boolean {
    if (!root) return false;
    if (!root.left && !root.right) return root.val === targetSum;
    const remaining = targetSum - root.val;
    return hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining);
}

export default hasPathSum;
