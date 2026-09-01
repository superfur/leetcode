/**
 * 102. 二叉树的层序遍历
 * BFS：队列每轮先记录当前层的节点数 size，
 * 依次弹出 size 个节点收集值、把它们的子节点入队，
 * 这一轮就是完整的一层。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function levelOrder(root: TNode | null): number[][] {
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
    return result;
}

export default levelOrder;
