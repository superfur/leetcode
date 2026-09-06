/**
 * 106. 从中序与后序遍历序列构造二叉树
 * 后序的最后一个元素永远是当前子树的根；在中序里找到这个根的位置，
 * 左边是左子树的中序、右边是右子树的中序。
 * 用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
 * 用一个从末尾向前推进的 postIdx 指针避免对 postorder 做切片；
 * 因为指针从后往前走，必须先递归构建右子树、再构建左子树。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function buildTree(inorder: number[], postorder: number[]): TNode | null {
    const indexOf = new Map<number, number>();
    inorder.forEach((val, i) => indexOf.set(val, i));
    let postIdx = postorder.length - 1;

    const build = (inLeft: number, inRight: number): TNode | null => {
        if (inLeft > inRight) return null;
        const rootVal = postorder[postIdx--];
        const mid = indexOf.get(rootVal)!;
        const root: TNode = { val: rootVal, left: null, right: null };
        root.right = build(mid + 1, inRight);
        root.left = build(inLeft, mid - 1);
        return root;
    };

    return build(0, inorder.length - 1);
}

export default buildTree;
