/**
 * 99. 恢复二叉搜索树
 * 中序遍历（迭代，栈）应严格递增；用 prev 记录上一个访问节点，
 * 每次出现 prev.val > cur.val 就是一次"逆序对"：
 * 第一次出现记录 (prev, cur) 为 first/second 候选；
 * 若又出现第二次逆序（两个交换节点不相邻），把 second 更新为这次的 cur。
 * 最后交换 first 和 second 的值即可恢复。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function recoverTree(root: TNode | null): void {
    const stack: TNode[] = [];
    let prev: TNode | null = null;
    let first: TNode | null = null;
    let second: TNode | null = null;
    let node = root;

    while (node || stack.length) {
        while (node) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop()!;
        if (prev && prev.val > node.val) {
            if (!first) first = prev;
            second = node;
        }
        prev = node;
        node = node.right;
    }

    if (first && second) {
        const tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
}

export default recoverTree;
