/**
 * 101. 对称二叉树
 * 递归判断两棵子树是否互为镜像：值相同，且 t1 的左子树与 t2 的右子树
 * 互为镜像、t1 的右子树与 t2 的左子树互为镜像。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function isSymmetric(root: TNode | null): boolean {
    const isMirror = (t1: TNode | null, t2: TNode | null): boolean => {
        if (!t1 && !t2) return true;
        if (!t1 || !t2) return false;
        if (t1.val !== t2.val) return false;
        return isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left);
    };

    return !root || isMirror(root.left, root.right);
}

export default isSymmetric;
