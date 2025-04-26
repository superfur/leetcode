# 1377. T 秒后青蛙的位置

## 题目描述

<p>给你一棵由 <code>n</code> 个顶点组成的无向树，顶点编号从 <code>1</code> 到 <code>n</code>。青蛙从 <strong>顶点 1</strong> 开始起跳。规则如下：</p>

<ul>
	<li>在一秒内，青蛙从它所在的当前顶点跳到另一个 <strong>未访问</strong> 过的顶点（如果它们直接相连）。</li>
	<li>青蛙无法跳回已经访问过的顶点。</li>
	<li>如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。</li>
	<li>如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。</li>
</ul>

<p>无向树的边用数组 <code>edges</code> 描述，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 意味着存在一条直接连通 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 两个顶点的边。</p>

<p>返回青蛙在 <em><code>t</code></em> 秒后位于目标顶点 <em><code>target</code> </em>上的概率。与实际答案相差不超过 <code>10<sup>-5</sup></code> 的结果将被视为正确答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/12/21/frog1.jpg" /></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
<strong>输出：</strong>0.16666666666666666 
<strong>解释：</strong>上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 <strong>1 秒</strong> 有 1/3 的概率跳到顶点 2 ，然后第 <strong>2 秒</strong> 有 1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。 
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/12/21/frog2.jpg" /></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
<strong>输出：</strong>0.3333333333333333
<strong>解释：</strong>上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 <strong>1 秒</strong> 后跳到顶点 7 。 
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub>&nbsp;&lt;= n</code></li>
	<li><code>1 &lt;= t &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 图

## 提示

1. Use a variation of DFS with parameters 'curent_vertex' and 'current_time'.
2. Update the probability considering to jump to one of the children vertices.

## 示例

```
7
[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
2
4
7
[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
1
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double frogPosition(int n, vector<vector<int>>& edges, int t, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public double frogPosition(int n, int[][] edges, int t, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
```

### C

```c
double frogPosition(int n, int** edges, int edgesSize, int* edgesColSize, int t, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public double FrogPosition(int n, int[][] edges, int t, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} t
 * @param {number} target
 * @return {number}
 */
var frogPosition = function(n, edges, t, target) {
    
};
```

### TypeScript

```typescript
function frogPosition(n: number, edges: number[][], t: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $t
     * @param Integer $target
     * @return Float
     */
    function frogPosition($n, $edges, $t, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func frogPosition(_ n: Int, _ edges: [[Int]], _ t: Int, _ target: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun frogPosition(n: Int, edges: Array<IntArray>, t: Int, target: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double frogPosition(int n, List<List<int>> edges, int t, int target) {
    
  }
}
```

### Go

```golang
func frogPosition(n int, edges [][]int, t int, target int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} t
# @param {Integer} target
# @return {Float}
def frog_position(n, edges, t, target)
    
end
```

### Scala

```scala
object Solution {
    def frogPosition(n: Int, edges: Array[Array[Int]], t: Int, target: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn frog_position(n: i32, edges: Vec<Vec<i32>>, t: i32, target: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (frog-position n edges t target)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec frog_position(N :: integer(), Edges :: [[integer()]], T :: integer(), Target :: integer()) -> float().
frog_position(N, Edges, T, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec frog_position(n :: integer, edges :: [[integer]], t :: integer, target :: integer) :: float
  def frog_position(n, edges, t, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func frogPosition(n: Int64, edges: Array<Array<Int64>>, t: Int64, target: Int64): Float64 {

    }
}
```

