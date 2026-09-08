/**
 * 107. 二叉树的层序遍历 II
 * 与普通层序遍历（102 题）完全相同的 BFS，
 * 只是最后把层的顺序整体反转，变成从叶子层到根层。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function levelOrderBottom(root: TNode | null): number[][] {
    if (!root) return [];
    const result: number[][] = [];
    let queue: TNode[] = [root];
    while (queue.length) {
        const level: number[] = [];
        const next: TNode[] = [];
        for (const node of queue) {
            level.push(node.val);
            if (node.left) next.push(node.left);
            if (node.right) next.push(node.right);
        }
        result.push(level);
        queue = next;
    }
    return result.reverse();
}

export default levelOrderBottom;
