# 2360. 图中的最长环

## 题目描述

<p>给你一个 <code>n</code>&nbsp;个节点的 <b>有向图</b>&nbsp;，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，其中每个节点&nbsp;<strong>至多</strong>&nbsp;有一条出边。</p>

<p>图用一个大小为 <code>n</code>&nbsp;下标从<strong>&nbsp;0</strong>&nbsp;开始的数组&nbsp;<code>edges</code>&nbsp;表示，节点 <code>i</code>&nbsp;到节点&nbsp;<code>edges[i]</code>&nbsp;之间有一条有向边。如果节点&nbsp;<code>i</code>&nbsp;没有出边，那么&nbsp;<code>edges[i] == -1</code>&nbsp;。</p>

<p>请你返回图中的 <strong>最长</strong>&nbsp;环，如果没有任何环，请返回 <code>-1</code>&nbsp;。</p>

<p>一个环指的是起点和终点是 <strong>同一个</strong>&nbsp;节点的路径。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/08/graph4drawio-5.png" style="width: 335px; height: 191px;" /></p>

<pre>
<b>输入：</b>edges = [3,3,4,2,3]
<b>输出去：</b>3
<b>解释：</b>图中的最长环是：2 -&gt; 4 -&gt; 3 -&gt; 2 。
这个环的长度为 3 ，所以返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-1.png" style="width: 171px; height: 161px;" /></p>

<pre>
<b>输入：</b>edges = [2,-1,3,1]
<b>输出：</b>-1
<b>解释：</b>图中没有任何环。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-1 &lt;= edges[i] &lt; n</code></li>
	<li><code>edges[i] != i</code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 拓扑排序

## 提示

1. How many cycles can each node at most be part of?
2. Each node can be part of at most one cycle. Start from each node and find the cycle that it is part of if there is any. Save the already visited nodes to not repeat visiting the same cycle multiple times.

## 示例

```
[3,3,4,2,3]
[2,-1,3,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestCycle(vector<int>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestCycle(int[] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
```

### C

```c
int longestCycle(int* edges, int edgesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestCycle(int[] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function(edges) {
    
};
```

### TypeScript

```typescript
function longestCycle(edges: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $edges
     * @return Integer
     */
    function longestCycle($edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestCycle(_ edges: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestCycle(edges: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestCycle(List<int> edges) {
    
  }
}
```

### Go

```golang
func longestCycle(edges []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} edges
# @return {Integer}
def longest_cycle(edges)
    
end
```

### Scala

```scala
object Solution {
    def longestCycle(edges: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_cycle(edges: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-cycle edges)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_cycle(Edges :: [integer()]) -> integer().
longest_cycle(Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_cycle(edges :: [integer]) :: integer
  def longest_cycle(edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestCycle(edges: Array<Int64>): Int64 {

    }
}
```

