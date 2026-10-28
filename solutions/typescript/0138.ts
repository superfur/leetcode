/**
 * 138. 随机链表的复制
 * 哈希表 + 两遍遍历：
 * 第一遍只复制节点的 val，建立「原节点 -> 克隆节点」的映射；
 * 第二遍再通过映射给每个克隆节点接上 next 和 random（指向 null 就保持 null）。
 * 哈希表保证同一个原节点只会有一个克隆体，所以 random 指向的共享节点不会被复制多份。
 * 时间 O(n)，空间 O(n)。
 *
 * 注：_Node 类型由 LeetCode 平台注入，本文件用 untyped RNode 接口避免冲突。
 */

interface RNode { val: number; next: RNode | null; random: RNode | null }

function copyRandomList(head: RNode | null): RNode | null {
    if (!head) return null;

    const clones = new Map<RNode, RNode>();
    for (let cur: RNode | null = head; cur; cur = cur.next) {
        clones.set(cur, { val: cur.val, next: null, random: null });
    }
    for (let cur: RNode | null = head; cur; cur = cur.next) {
        const clone = clones.get(cur)!;
        clone.next = cur.next ? clones.get(cur.next)! : null;
        clone.random = cur.random ? clones.get(cur.random)! : null;
    }
    return clones.get(head)!;
}

export default copyRandomList;
