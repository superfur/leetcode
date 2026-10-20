/**
 * 133. 克隆图
 * BFS 遍历原图，用 Map 记录「原节点 -> 克隆节点」：
 * 遇到还没克隆的邻居就新建克隆并入队，
 * 然后把邻居对应的克隆节点挂到当前节点的克隆体的 neighbors 上。
 * Map 同时起到「已访问」的作用，所以环不会死循环。
 *
 * 注：_Node 类型由 LeetCode 平台注入，本文件用 untyped GNode 接口避免冲突。
 */

interface GNode { val: number; neighbors: GNode[] }

function cloneGraph(node: GNode | null): GNode | null {
    if (!node) return null;

    const clones = new Map<GNode, GNode>();
    clones.set(node, { val: node.val, neighbors: [] });
    const queue: GNode[] = [node];

    for (let head = 0; head < queue.length; head++) {
        const cur = queue[head];
        for (const nb of cur.neighbors) {
            if (!clones.has(nb)) {
                clones.set(nb, { val: nb.val, neighbors: [] });
                queue.push(nb);
            }
            clones.get(cur)!.neighbors.push(clones.get(nb)!);
        }
    }
    return clones.get(node)!;
}

export default cloneGraph;
