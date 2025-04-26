# 2359. 找到离给定两个节点最近的节点

## 题目描述

<p>给你一个 <code>n</code>&nbsp;个节点的 <strong>有向图</strong>&nbsp;，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，每个节点 <strong>至多</strong>&nbsp;有一条出边。</p>

<p>有向图用大小为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>edges</code>&nbsp;表示，表示节点&nbsp;<code>i</code>&nbsp;有一条有向边指向&nbsp;<code>edges[i]</code>&nbsp;。如果节点&nbsp;<code>i</code>&nbsp;没有出边，那么&nbsp;<code>edges[i] == -1</code>&nbsp;。</p>

<p>同时给你两个节点&nbsp;<code>node1</code> 和&nbsp;<code>node2</code>&nbsp;。</p>

<p>请你返回一个从 <code>node1</code>&nbsp;和 <code>node2</code>&nbsp;都能到达节点的编号，使节点 <code>node1</code>&nbsp;和节点 <code>node2</code>&nbsp;到这个节点的距离 <b>较大值最小化</b>。如果有多个答案，请返回 <strong>最小</strong>&nbsp;的节点编号。如果答案不存在，返回 <code>-1</code>&nbsp;。</p>

<p>注意&nbsp;<code>edges</code>&nbsp;可能包含环。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-2.png" style="width: 321px; height: 161px;"></p>

<pre><b>输入：</b>edges = [2,2,3,-1], node1 = 0, node2 = 1
<b>输出：</b>2
<b>解释：</b>从节点 0 到节点 2 的距离为 1 ，从节点 1 到节点 2 的距离为 1 。
两个距离的较大值为 1 。我们无法得到一个比 1 更小的较大值，所以我们返回节点 2 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-4.png" style="width: 195px; height: 161px;"></p>

<pre><b>输入：</b>edges = [1,2,-1], node1 = 0, node2 = 2
<b>输出：</b>2
<b>解释：</b>节点 0 到节点 2 的距离为 2 ，节点 2 到它自己的距离为 0 。
两个距离的较大值为 2 。我们无法得到一个比 2 更小的较大值，所以我们返回节点 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-1 &lt;= edges[i] &lt; n</code></li>
	<li><code>edges[i] != i</code></li>
	<li><code>0 &lt;= node1, node2 &lt; n</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 图

## 提示

1. How can you find the shortest distance from one node to all nodes in the graph?
2. Use BFS to find the shortest distance from both node1 and node2 to all nodes in the graph. Then iterate over all nodes, and find the node with the minimum max distance.

## 示例

```
[2,2,3,-1]
0
1
[1,2,-1]
0
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        
    }
};
```

### Java

```java
class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
```

### C

```c
int closestMeetingNode(int* edges, int edgesSize, int node1, int node2) {
    
}
```

### C#

```csharp
public class Solution {
    public int ClosestMeetingNode(int[] edges, int node1, int node2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode = function(edges, node1, node2) {
    
};
```

### TypeScript

```typescript
function closestMeetingNode(edges: number[], node1: number, node2: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $edges
     * @param Integer $node1
     * @param Integer $node2
     * @return Integer
     */
    function closestMeetingNode($edges, $node1, $node2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closestMeetingNode(_ edges: [Int], _ node1: Int, _ node2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closestMeetingNode(edges: IntArray, node1: Int, node2: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int closestMeetingNode(List<int> edges, int node1, int node2) {
    
  }
}
```

### Go

```golang
func closestMeetingNode(edges []int, node1 int, node2 int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} edges
# @param {Integer} node1
# @param {Integer} node2
# @return {Integer}
def closest_meeting_node(edges, node1, node2)
    
end
```

### Scala

```scala
object Solution {
    def closestMeetingNode(edges: Array[Int], node1: Int, node2: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (closest-meeting-node edges node1 node2)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec closest_meeting_node(Edges :: [integer()], Node1 :: integer(), Node2 :: integer()) -> integer().
closest_meeting_node(Edges, Node1, Node2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec closest_meeting_node(edges :: [integer], node1 :: integer, node2 :: integer) :: integer
  def closest_meeting_node(edges, node1, node2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closestMeetingNode(edges: Array<Int64>, node1: Int64, node2: Int64): Int64 {

    }
}
```

