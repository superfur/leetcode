# 1791. 找出星型图的中心节点

## 题目描述

<p>有一个无向的 <strong>星型</strong> 图，由 <code>n</code> 个编号从 <code>1</code> 到 <code>n</code> 的节点组成。星型图有一个 <strong>中心</strong> 节点，并且恰有 <code>n - 1</code> 条边将中心节点与其他每个节点连接起来。</p>

<p>给你一个二维整数数组 <code>edges</code> ，其中 <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示在节点 <code>u<sub>i</sub></code> 和 <code>v<sub>i</sub></code> 之间存在一条边。请你找出并返回 <code>edges</code> 所表示星型图的中心节点。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/14/star_graph.png" style="width: 331px; height: 321px;" />
<pre>
<strong>输入：</strong>edges = [[1,2],[2,3],[4,2]]
<strong>输出：</strong>2
<strong>解释：</strong>如上图所示，节点 2 与其他每个节点都相连，所以节点 2 是中心节点。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>edges = [[1,2],[5,1],[1,3],[1,4]]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= n <= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 <= u<sub>i,</sub> v<sub>i</sub> <= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li>题目数据给出的 <code>edges</code> 表示一个有效的星型图</li>
</ul>


## 难度

Easy

## 标签

- 图

## 提示

1. The center is the only node that has more than one edge.
2. The center is also connected to all other nodes.
3. Any two edges must have a common node, which is the center.

## 示例

```
[[1,2],[2,3],[4,2]]
[[1,2],[5,1],[1,3],[1,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int findCenter(int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
```

### C

```c
int findCenter(int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindCenter(int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function(edges) {
    
};
```

### TypeScript

```typescript
function findCenter(edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function findCenter($edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findCenter(_ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findCenter(edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findCenter(List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func findCenter(edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} edges
# @return {Integer}
def find_center(edges)
    
end
```

### Scala

```scala
object Solution {
    def findCenter(edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_center(edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-center edges)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_center(Edges :: [[integer()]]) -> integer().
find_center(Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_center(edges :: [[integer]]) :: integer
  def find_center(edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findCenter(edges: Array<Array<Int64>>): Int64 {

    }
}
```

