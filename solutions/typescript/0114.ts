/**
 * 114. 二叉树展开为链表
 * O(1) 额外空间：从根开始，若当前节点有左子树，
 * 就在左子树里一路往右找到最右节点（也就是左子树先序遍历的最后一个节点），
 * 把当前节点原来的右子树接到这个最右节点的 right 上，
 * 再把左子树整体搬到右边、左指针置空。
 * 这样处理完当前节点后，沿着 right 指针继续处理下一个节点，
 * 整体顺序正好等于先序遍历。
 *
 * 注：TreeNode 类型由 LeetCode 平台注入，本文件用 untyped TNode 接口避免冲突。
 */

interface TNode { val: number; left: TNode | null; right: TNode | null }

function flatten(root: TNode | null): void {
    let node = root;
    while (node) {
        if (node.left) {
            let predecessor = node.left;
            while (predecessor.right) {
                predecessor = predecessor.right;
            }
            predecessor.right = node.right;
            node.right = node.left;
            node.left = null;
        }
        node = node.right;
    }
}

export default flatten;
