/**
 * 144. 二叉树的前序遍历
 * 迭代 + 显式栈：弹出节点就记录它的值（根），再先压右孩子、后压左孩子，
 * 这样下一次弹出的就是左孩子，顺序为 根 → 左 → 右。
 * 不依赖递归深度，时间 O(n)，空间 O(h)。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function preorderTraversal(root: TNode | null): number[] {
    const res: number[] = [];
    const stack: TNode[] = root ? [root] : [];
    while (stack.length > 0) {
        const node = stack.pop()!;
        res.push(node.val);
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);
    }
    return res;
}

export default preorderTraversal;
