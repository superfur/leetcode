# 2374. 边积分最高的节点

## 题目描述

<p>给你一个有向图，图中有 <code>n</code> 个节点，节点编号从 <code>0</code> 到 <code>n - 1</code> ，其中每个节点都 <strong>恰有一条</strong> 出边。</p>

<p>图由一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>edges</code> 表示，其中 <code>edges[i]</code> 表示存在一条从节点 <code>i</code> 到节点 <code>edges[i]</code> 的 <strong>有向</strong> 边。</p>

<p>节点 <code>i</code> 的 <strong>边积分</strong> 定义为：所有存在一条指向节点 <code>i</code> 的边的节点的 <strong>编号</strong> 总和。</p>

<p>返回 <strong>边积分</strong> 最高的节点。如果多个节点的 <strong>边积分</strong> 相同，返回编号 <strong>最小</strong> 的那个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/06/20/image-20220620195403-1.png" style="width: 450px; height: 260px;">
<pre><strong>输入：</strong>edges = [1,0,0,0,0,7,7,5]
<strong>输出：</strong>7
<strong>解释：</strong>
- 节点 1、2、3 和 4 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 + 3 + 4 = 10 。
- 节点 0 有一条指向节点 1 的边，节点 1 的边积分等于 0 。
- 节点 7 有一条指向节点 5 的边，节点 5 的边积分等于 7 。
- 节点 5 和 6 都有指向节点 7 的边，节点 7 的边积分等于 5 + 6 = 11 。
节点 7 的边积分最高，所以返回 7 。
</pre>

<p><strong>示例 2：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/06/20/image-20220620200212-3.png" style="width: 150px; height: 155px;">
<pre><strong>输入：</strong>edges = [2,0,0,2]
<strong>输出：</strong>0
<strong>解释：
</strong>- 节点 1 和 2 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 = 3 。
- 节点 0 和 3 都有指向节点 2 的边，节点 2 的边积分等于 0 + 3 = 3 。
节点 0 和 2 的边积分都是 3 。由于节点 0 的编号更小，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges[i] &lt; n</code></li>
	<li><code>edges[i] != i</code></li>
</ul>


## 难度

Medium

## 标签

- 图
- 哈希表

## 提示

1. Create an array arr where arr[i] is the edge score for node i.
2. How does the edge score for node edges[i] change? It increases by i.
3. The edge score may not fit within a standard 32-bit integer.

## 示例

```
[1,0,0,0,0,7,7,5]
[2,0,0,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int edgeScore(vector<int>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int edgeScore(int[] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
```

### C

```c
int edgeScore(int* edges, int edgesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int EdgeScore(int[] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} edges
 * @return {number}
 */
var edgeScore = function(edges) {
    
};
```

### TypeScript

```typescript
function edgeScore(edges: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $edges
     * @return Integer
     */
    function edgeScore($edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func edgeScore(_ edges: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun edgeScore(edges: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int edgeScore(List<int> edges) {
    
  }
}
```

### Go

```golang
func edgeScore(edges []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} edges
# @return {Integer}
def edge_score(edges)
    
end
```

### Scala

```scala
object Solution {
    def edgeScore(edges: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn edge_score(edges: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (edge-score edges)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec edge_score(Edges :: [integer()]) -> integer().
edge_score(Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec edge_score(edges :: [integer]) :: integer
  def edge_score(edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func edgeScore(edges: Array<Int64>): Int64 {

    }
}
```

