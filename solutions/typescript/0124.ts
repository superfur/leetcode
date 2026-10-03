/**
 * 124. 二叉树中的最大路径和
 * 后序递归：dfs(node) 返回「以 node 为起点、向下走的最大贡献值」
 * （贡献为负就当作 0，即不选这条分支）；
 * 同时把「左贡献 + 节点值 + 右贡献」当作以 node 为最高点的路径和，更新全局答案。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function maxPathSum(root: TNode | null): number {
    let best = -Infinity;

    const dfs = (node: TNode | null): number => {
        if (!node) return 0;
        const left = Math.max(dfs(node.left), 0);
        const right = Math.max(dfs(node.right), 0);
        best = Math.max(best, node.val + left + right);
        return node.val + Math.max(left, right);
    };

    dfs(root);
    return best;
}

export default maxPathSum;
