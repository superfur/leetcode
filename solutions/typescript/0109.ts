/**
 * 109. 有序链表转换二叉搜索树
 * 先把链表一次性摊平成数组（O(n)），之后就是 108 题的做法：
 * 取区间中点为根递归划分左右子树，天然保证高度平衡。
 *
 * 注：ListNode / TreeNode 类型由 LeetCode 平台注入，本文件用 untyped
 * LNode / TNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }
interface TNode { val: number; left: TNode | null; right: TNode | null }

function sortedListToBST(head: LNode | null): TNode | null {
    const values: number[] = [];
    let node = head;
    while (node) {
        values.push(node.val);
        node = node.next;
    }

    const build = (left: number, right: number): TNode | null => {
        if (left > right) return null;
        const mid = Math.floor((left + right) / 2);
        return {
            val: values[mid],
            left: build(left, mid - 1),
            right: build(mid + 1, right),
        };
    };

    return build(0, values.length - 1);
}

export default sortedListToBST;
