/**
 * 103. 二叉树的锯齿形层序遍历
 * 与普通层序遍历（BFS）相同，只是奇数层（从 0 计数的第 1、3、5... 层）
 * 收集完之后把这一层的结果反转即可。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function zigzagLevelOrder(root: TNode | null): number[][] {
    if (!root) return [];
    const result: number[][] = [];
    let queue: TNode[] = [root];
    let leftToRight = true;
    while (queue.length) {
        const level: number[] = [];
        const next: TNode[] = [];
        for (const node of queue) {
            level.push(node.val);
            if (node.left) next.push(node.left);
            if (node.right) next.push(node.right);
        }
        if (!leftToRight) level.reverse();
        result.push(level);
        queue = next;
        leftToRight = !leftToRight;
    }
    return result;
}

export default zigzagLevelOrder;
