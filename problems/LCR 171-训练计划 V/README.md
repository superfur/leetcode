# LCR 171. 训练计划 V

## 题目描述

<p>某教练同时带教两位学员，分别以链表 <code>l1</code>、<code>l2</code> 记录了两套核心肌群训练计划，节点值为训练项目编号。两套计划仅有前半部分热身项目不同，后续正式训练项目相同。请设计一个程序找出并返回第一个正式训练项目编号。如果两个链表不存在相交节点，返回 <code>null</code> 。</p>

<p>如下面的两个链表<strong>：</strong></p>

<p><a href="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png" target="_blank"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png" /></a></p>

<p>在节点 <code>c1</code> 开始相交。</p>

<p>输入说明：</p>

<p><code>intersectVal</code> - 相交的起始节点的值。如果不存在相交节点，这一值为 0</p>

<p><code>l1</code> - 第一个训练计划链表</p>

<p><code>l2</code> - 第二个训练计划链表</p>

<p><code>skip1</code> - 在 <code>l1</code> 中（从头节点开始）跳到交叉节点的节点数</p>

<p><code>skip2</code> - 在 <code>l2</code> 中（从头节点开始）跳到交叉节点的节点数</p>

<p>程序将根据这些输入创建链式数据结构，并将两个头节点 <code>head1</code> 和 <code>head2</code> 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被视作正确答案 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png" target="_blank"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_1.png" /></a></p>

<pre>
<strong>输入：</strong>intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
<strong>输出：</strong>Reference of the node with value = 8
<strong>解释：</strong>第一个正式训练项目编号为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;2：</strong></p>

<p><a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png" target="_blank"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_2.png" /></a></p>

<pre>
<strong>输入：</strong>intersectVal&nbsp;= 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
<strong>输出：</strong>Reference of the node with value = 2
<strong>解释：</strong>第一个正式训练项目编号为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;3：</strong></p>

<p><a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png" target="_blank"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png" /></a></p>

<pre>
<strong>输入：</strong>intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
<strong>输出：</strong>null
<strong>解释：</strong>两套计划完全不同，返回 null。从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
</pre>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li>如果两个链表没有交点，返回 <code>null</code>.</li>
	<li>在返回结果后，两个链表仍须保持原有的结构。</li>
	<li>可假定整个链表结构中没有循环。</li>
	<li>程序尽量满足 O(<em>n</em>) 时间复杂度，且仅用 O(<em>1</em>) 内存。</li>
	<li>本题与主站 160 题相同：<a href="https://leetcode-cn.com/problems/intersection-of-two-linked-lists/">https://leetcode-cn.com/problems/intersection-of-two-linked-lists/</a></li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 哈希表
- 链表
- 双指针

## 示例

```
8
[3,7,2,8,9,5,1]
[4,6,8,9,5,1]
3
2
```

## 示例代码

### C++

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
    }
};
```

### Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
class Solution {
    ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
    }
}
```

### Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
```

### Python3

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
```

### C

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    
}
```

### C#

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        
    }
}
```

### JavaScript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    
};
```

### Go

```golang
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    
}
```

