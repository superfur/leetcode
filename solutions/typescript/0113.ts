/**
 * 113. 路径总和 II
 * 回溯：沿途把节点值压入 path，到叶子节点时若剩余目标值
 * 正好归零就把 path 的一份拷贝收进结果；不管是否匹配，
 * 递归返回前都要把刚压入的节点值弹出，恢复现场再试下一分支。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function pathSum(root: TNode | null, targetSum: number): number[][] {
    const result: number[][] = [];
    const path: number[] = [];

    const dfs = (node: TNode | null, remaining: number): void => {
        if (!node) return;
        path.push(node.val);
        remaining -= node.val;
        if (!node.left && !node.right && remaining === 0) {
            result.push([...path]);
        } else {
            dfs(node.left, remaining);
            dfs(node.right, remaining);
        }
        path.pop();
    };

    dfs(root, targetSum);
    return result;
}

export default pathSum;
