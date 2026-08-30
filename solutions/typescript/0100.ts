/**
 * 100. 相同的树
 * 递归：两个节点同时为空则相同；一空一非空或值不同则不同；
 * 否则要求左子树和右子树都分别相同。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function isSameTree(p: TNode | null, q: TNode | null): boolean {
    if (!p && !q) return true;
    if (!p || !q) return false;
    if (p.val !== q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

export default isSameTree;
