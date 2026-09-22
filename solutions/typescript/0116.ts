/**
 * 116. 填充每个节点的下一个右侧节点指针
 * O(1) 额外空间：利用已经连好的上一层 next 指针去连接下一层——
 * leftmost 指向当前层最左节点，用 head 沿着当前层的 next 链
 * 往右走，每一步把 head.left.next 接到 head.right，
 * 再把 head.right.next 接到 head.next.left（如果 head.next 存在）；
 * 走完当前层后，leftmost 下移一层，重复直到最底层（叶子层没有子节点）。
 * 这是完美二叉树，所以只要 leftmost.left 存在就说明还有下一层。
 *
 * 注：_Node 类型由 LeetCode 平台注入，本文件用 untyped NNode 接口避免冲突。
 */

interface NNode { val: number; left: NNode | null; right: NNode | null; next: NNode | null }

function connect(root: NNode | null): NNode | null {
    let leftmost = root;
    while (leftmost && leftmost.left) {
        let head: NNode | null = leftmost;
        while (head) {
            head.left!.next = head.right;
            if (head.next) {
                head.right!.next = head.next.left;
            }
            head = head.next;
        }
        leftmost = leftmost.left;
    }
    return root;
}

export default connect;
