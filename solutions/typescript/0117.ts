/**
 * 117. 填充每个节点的下一个右侧节点指针 II
 * 普通二叉树，不能像完美二叉树那样直接假设子节点都存在，
 * 但同样可以做到 O(1) 额外空间：用一个 dummy 节点作为
 * "下一层"链表的临时尾巴，沿着当前层的 next 链遍历，
 * 把每个节点存在的 left/right 依次接到 dummy 链的末尾；
 * 当前层走完后，下一层的头就是 dummy.next。
 *
 * 注：_Node 类型由 LeetCode 平台注入，本文件用 untyped NNode 接口避免冲突。
 */

interface NNode { val: number; left: NNode | null; right: NNode | null; next: NNode | null }

function connect(root: NNode | null): NNode | null {
    let node = root;
    while (node) {
        const dummy: NNode = { val: 0, left: null, right: null, next: null };
        let tail = dummy;
        while (node) {
            if (node.left) {
                tail.next = node.left;
                tail = tail.next;
            }
            if (node.right) {
                tail.next = node.right;
                tail = tail.next;
            }
            node = node.next;
        }
        node = dummy.next;
    }
    return root;
}

export default connect;
