# 面试题 04.08. 首个共同祖先

## 题目描述

<p>设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。</p>

<p>例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]</p>

<pre>
    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4
</pre>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>输出：</strong>3
<strong>解释：</strong>节点 5 和节点 1 的最近公共祖先是节点 3。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>输出：</strong>5
<strong>解释：</strong>节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。</pre>

<p><strong>提示：</strong></p>

<pre>
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。</pre>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 二叉树

## 提示

1. 小心！你的算法处理只有一个节点的情况吗？会发生什么事？你可能要微调返回值。
2. 如果每个节点都有一个到其父节点的链接，我们可以利用9.2节问题2.7的方法。然而，面试官可能不会让我们作出这样的假设。
3. 第一个共同的祖先是最深的节点，这样p和q都是后代。想想你要如何识别这个节点。
4. 你如何弄清p是否为节点n的后代？
5. 从根节点开始。你能确定根是第一个共同祖先吗？如果不是，你能分辨出第一个共同祖先在根节点的哪一边吗？
6. 尝试递归方法。检查p和q是否为左子树和右子树的后代。如果它们是不同的树的后代，那么当前节点是第一个共同的祖先。如果它们是同一子树的后代，则该子树保存第一个共同祖先。现在，你该如何有效地实现它呢？
7. 在更简单的算法中，我们有一个方法表明x是n的后代，另一个方法是递归查找第一个共同的祖先。这样是在子树中反复搜索相同的元素。我们应该将其合并成一个firstCommonAncestor方法。那么什么样的返回值会给我们需要的信息？
8. firstCommonAncestor函数可以返回第一个共同的祖先（如果p和q都包含在树里），如果p在树上而q不在，返回p；如果q在树上而p不在，返回q；否则，返回空。

## 示例

```
[3,5,1,6,2,0,8,null,null,7,4]
5
1
[3,5,1,6,2,0,8,null,null,7,4]
5
4
```

## 示例代码

### C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {

    }
};
```

### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

    }
}
```

### Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
```

### Python3

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
```

### C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q){

}

```

### C#

```csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

    }
}
```

### JavaScript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {

};
```

### Go

```golang
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func lowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {

}
```

### Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)

end
```

