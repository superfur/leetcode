/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    /**
     * 133. 克隆图
     * BFS 遍历原图，用 HashMap 记录「原节点 -> 克隆节点」：
     * 遇到还没克隆的邻居就新建克隆并入队，
     * 然后把邻居对应的克隆节点挂到当前节点的克隆体的 neighbors 上。
     * HashMap 同时起到「已访问」的作用，所以环不会死循环。
     */
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        Map<Node, Node> clones = new HashMap<>();
        clones.put(node, new Node(node.val));
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(node);
        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            for (Node nb : cur.neighbors) {
                if (!clones.containsKey(nb)) {
                    clones.put(nb, new Node(nb.val));
                    queue.add(nb);
                }
                clones.get(cur).neighbors.add(clones.get(nb));
            }
        }
        return clones.get(node);
    }
}
