/**
 * 105. 从前序与中序遍历序列构造二叉树
 * 前序的第一个元素永远是当前子树的根；在中序里找到这个根的位置，
 * 左边就是左子树的中序、右边是右子树的中序。
 * 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
 * 用一个全局推进的 preIdx 指针避免对 preorder 做切片，
 * 只在中序区间 [inLeft, inRight] 上递归划分左右子树。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function buildTree(preorder: number[], inorder: number[]): TNode | null {
    const indexOf = new Map<number, number>();
    inorder.forEach((val, i) => indexOf.set(val, i));
    let preIdx = 0;

    const build = (inLeft: number, inRight: number): TNode | null => {
        if (inLeft > inRight) return null;
        const rootVal = preorder[preIdx++];
        const mid = indexOf.get(rootVal)!;
        const root: TNode = { val: rootVal, left: null, right: null };
        root.left = build(inLeft, mid - 1);
        root.right = build(mid + 1, inRight);
        return root;
    };

    return build(0, inorder.length - 1);
}

export default buildTree;
