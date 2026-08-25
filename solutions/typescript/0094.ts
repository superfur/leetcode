/**
 * 94. 二叉树的中序遍历
 * 迭代：用栈模拟递归——一路把左子树压栈到底，
 * 弹出访问后转向右子树，重复直到栈空且当前节点为空。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function inorderTraversal(root: TNode | null): number[] {
    const result: number[] = [];
    const stack: TNode[] = [];
    let node = root;
    while (node || stack.length) {
        while (node) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop()!;
        result.push(node.val);
        node = node.right;
    }
    return result;
}

export default inorderTraversal;
