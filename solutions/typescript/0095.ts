/**
 * 95. 不同的二叉搜索树 II
 * 区间递归：generate(start, end) 枚举 [start, end] 内每个值作为根，
 * 左子树取 generate(start, root-1)，右子树取 generate(root+1, end)，
 * 两两组合得到该区间内所有可能的 BST。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function generateTrees(n: number): (TNode | null)[] {
    if (n === 0) return [];

    const generate = (start: number, end: number): (TNode | null)[] => {
        if (start > end) return [null];
        const result: (TNode | null)[] = [];
        for (let rootVal = start; rootVal <= end; rootVal++) {
            const lefts = generate(start, rootVal - 1);
            const rights = generate(rootVal + 1, end);
            for (const left of lefts) {
                for (const right of rights) {
                    result.push({ val: rootVal, left, right });
                }
            }
        }
        return result;
    };

    return generate(1, n);
}

export default generateTrees;
