/**
 * 108. 将有序数组转换为二叉搜索树
 * 每次取区间中点作为根（自然保证左右子树节点数最多差 1，即高度平衡），
 * 左半区间递归建左子树，右半区间递归建右子树。
 * 答案不唯一，只要是高度平衡的 BST 即可。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function sortedArrayToBST(nums: number[]): TNode | null {
    const build = (left: number, right: number): TNode | null => {
        if (left > right) return null;
        const mid = Math.floor((left + right) / 2);
        return {
            val: nums[mid],
            left: build(left, mid - 1),
            right: build(mid + 1, right),
        };
    };

    return build(0, nums.length - 1);
}

export default sortedArrayToBST;
