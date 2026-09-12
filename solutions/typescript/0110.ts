/**
 * 110. 平衡二叉树
 * 自底向上后序遍历，一趟同时算高度和判平衡：
 * 用 -1 作为"已经不平衡"的哨兵值向上传播，一旦子树出现
 * 不平衡或左右高度差超过 1，就不再继续计算，直接短路返回。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function isBalanced(root: TNode | null): boolean {
    const height = (node: TNode | null): number => {
        if (!node) return 0;
        const left = height(node.left);
        if (left === -1) return -1;
        const right = height(node.right);
        if (right === -1 || Math.abs(left - right) > 1) return -1;
        return 1 + Math.max(left, right);
    };

    return height(root) !== -1;
}

export default isBalanced;
