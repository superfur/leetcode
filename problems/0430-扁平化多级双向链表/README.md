# 430. 扁平化多级双向链表

## 题目描述

<p>你会得到一个双链表，其中包含的节点有一个下一个指针、一个前一个指针和一个额外的 <strong>子指针</strong> 。这个子指针可能指向一个单独的双向链表，也包含这些特殊的节点。这些子列表可以有一个或多个自己的子列表，以此类推，以生成如下面的示例所示的 <strong>多层数据结构</strong> 。</p>

<p>给定链表的头节点&nbsp;<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">head</span></span></font></font>&nbsp;，将链表 <strong>扁平化</strong> ，以便所有节点都出现在单层双链表中。让 <code>curr</code> 是一个带有子列表的节点。子列表中的节点应该出现在<strong>扁平化列表</strong>中的&nbsp;<code>curr</code> <strong>之后</strong> 和&nbsp;<code>curr.next</code>&nbsp;<strong>之前</strong> 。</p>

<p>返回 <em>扁平列表的 <code>head</code>&nbsp;。列表中的节点必须将其 <strong>所有</strong> 子指针设置为&nbsp;<code>null</code>&nbsp;。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/11/09/flatten11.jpg" style="height:339px; width:700px" /></p>

<pre>
<strong>输入：</strong>head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
<strong>输出：</strong>[1,2,3,7,8,11,12,9,10,4,5,6]
<strong>解释：</strong>输入的多级列表如上图所示。
扁平化后的链表如下图：
<img src="https://assets.leetcode.com/uploads/2021/11/09/flatten12.jpg" style="height:69px; width:1000px" />
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/11/09/flatten2.1jpg" style="height:200px; width:200px" /></p>

<pre>
<strong>输入：</strong>head = [1,2,null,3]
<strong>输出：</strong>[1,3,2]
<strong>解释：</strong>输入的多级列表如上图所示。
扁平化后的链表如下图：
<img src="https://assets.leetcode.com/uploads/2021/11/24/list.jpg" style="height:87px; width:300px" />
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = []
<strong>输出：</strong>[]
<strong>说明：</strong>输入中可能存在空列表。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>节点数目不超过 <code>1000</code></li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>如何表示测试用例中的多级链表？</strong></p>

<p>以 <strong>示例 1</strong> 为例：</p>

<pre>
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL</pre>

<p>序列化其中的每一级之后：</p>

<pre>
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
</pre>

<p>为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。</p>

<pre>
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
</pre>

<p>合并所有序列化结果，并去除末尾的 null 。</p>

<pre>
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
</pre>

<ul>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 链表
- 双向链表

## 示例

```
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
[1,2,null,3]
[]
```

## 示例代码

### C++

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        
    }
};
```

### Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        
    }
}
```

### Python

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
```

### Python3

```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
```

### C#

```csharp
/*
// Definition for a Node.
public class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
}
*/

public class Solution {
    public Node Flatten(Node head) {
        
    }
}
```

### JavaScript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var flatten = function(head) {
    
};
```

### TypeScript

```typescript
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     prev: _Node | null
 *     next: _Node | null
 *     child: _Node | null
 *     
 *     constructor(val?: number, prev? : _Node, next? : _Node, child? : _Node) {
 *         this.val = (val===undefined ? 0 : val);
 *         this.prev = (prev===undefined ? null : prev);
 *         this.next = (next===undefined ? null : next);
 *         this.child = (child===undefined ? null : child);
 *     }
 * }
 */


function flatten(head: _Node | null): _Node | null {

};
```

### PHP

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val = null;
 *     public $prev = null;
 *     public $next = null;
 *     public $child = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->prev = null;
 *         $this->next = null;
 *         $this->child = null;
 *     }
 * }
 */

class Solution {
    /**
     * @param Node $head
     * @return Node
     */
    function flatten($head) {
        
    }
}
```

### Swift

```swift
/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var prev: Node?
 *     public var next: Node?
 *     public var child: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.prev = nil
 *         self.next = nil
 *         self.child  = nil
 *     }
 * }
 */

class Solution {
    func flatten(_ head: Node?) -> Node? {
        
    }
}
```

### Kotlin

```kotlin
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var prev: Node? = null
 *     var next: Node? = null
 *     var child: Node? = null
 * }
 */

class Solution {
    fun flatten(root: Node?): Node? {
        
    }
}
```

### Go

```golang
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Prev *Node
 *     Next *Node
 *     Child *Node
 * }
 */

func flatten(root *Node) *Node {
    
}
```

### Ruby

```ruby
# Definition for a Node.
# class Node
#     attr_accessor :val, :prev, :next, :child
#     def initialize(val=nil, prev=nil, next_=nil, child=nil)
#         @val = val
#         @prev = prev
#         @next = next_
#         @child = child
#     end
# end

# @param {Node} root
# @return {Node}
def flatten(root)
    
end
```

### Scala

```scala
/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var prev: Node = null
 *   var next: Node = null
 *   var child: Node = null
 * }
 */

object Solution {
    def flatten(head: Node): Node = {
    	
    }
}
```

