/**
 * 145. 二叉树的后序遍历
 * 后序是 左 → 右 → 根，它的逆序恰好是 根 → 右 → 左，
 * 而后者就是前序遍历把左右孩子的入栈顺序对调（先压左、后压右）。
 * 所以用显式栈按 根 → 右 → 左 收集值，最后整体反转即可。
 * 不依赖递归深度，时间 O(n)，空间 O(h)（结果数组除外）。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function postorderTraversal(root: TNode | null): number[] {
    const res: number[] = [];
    const stack: TNode[] = root ? [root] : [];
    while (stack.length > 0) {
        const node = stack.pop()!;
        res.push(node.val);
        if (node.left) stack.push(node.left);
        if (node.right) stack.push(node.right);
    }
    return res.reverse();
}

export default postorderTraversal;
