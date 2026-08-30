/**
 * 98. 验证二叉搜索树
 * 区间递归：每个节点携带一个开区间 (low, high)，其值必须落在区间内；
 * 向左递归时收紧上界为当前值，向右递归时收紧下界为当前值。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function isValidBST(root: TNode | null): boolean {
    const validate = (node: TNode | null, low: number, high: number): boolean => {
        if (!node) return true;
        if (!(node.val > low && node.val < high)) return false;
        return validate(node.left, low, node.val) && validate(node.right, node.val, high);
    };

    return validate(root, -Infinity, Infinity);
}

export default isValidBST;
