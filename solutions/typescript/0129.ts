/**
 * 129. 求根节点到叶节点数字之和
 * DFS 往下传「根到当前节点已经拼出的数字」（cur * 10 + val），
 * 走到叶子节点时这个数字就是一条完整路径代表的数，累加进答案。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function sumNumbers(root: TNode | null): number {
    const dfs = (node: TNode | null, cur: number): number => {
        if (!node) return 0;
        cur = cur * 10 + node.val;
        if (!node.left && !node.right) return cur;
        return dfs(node.left, cur) + dfs(node.right, cur);
    };
    return dfs(root, 0);
}

export default sumNumbers;
