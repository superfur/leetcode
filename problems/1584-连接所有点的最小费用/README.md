# 1584. 连接所有点的最小费用

## 题目描述

<p>给你一个<code>points</code>&nbsp;数组，表示 2D 平面上的一些点，其中&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;。</p>

<p>连接点&nbsp;<code>[x<sub>i</sub>, y<sub>i</sub>]</code> 和点&nbsp;<code>[x<sub>j</sub>, y<sub>j</sub>]</code>&nbsp;的费用为它们之间的 <strong>曼哈顿距离</strong>&nbsp;：<code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>&nbsp;，其中&nbsp;<code>|val|</code>&nbsp;表示&nbsp;<code>val</code>&nbsp;的绝对值。</p>

<p>请你返回将所有点连接的最小总费用。只有任意两点之间 <strong>有且仅有</strong>&nbsp;一条简单路径时，才认为所有点都已连接。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="height:268px; width:214px; background:#e5e5e5" /></p>

<pre>
<strong>输入：</strong>points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
<strong>输出：</strong>20
<strong>解释：
</strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="height:268px; width:214px; background:#e5e5e5" />
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[3,12],[-2,5],[-4,1]]
<strong>输出：</strong>18
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>points = [[0,0],[1,1],[1,0],[-1,1]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>points = [[-1000000,-1000000],[1000000,1000000]]
<strong>输出：</strong>4000000
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>points = [[0,0]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 1000</code></li>
	<li><code>-10<sup>6</sup>&nbsp;&lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>所有点&nbsp;<code>(x<sub>i</sub>, y<sub>i</sub>)</code>&nbsp;两两不同。</li>
</ul>


## 难度

Medium

## 标签

- 并查集
- 图
- 数组
- 最小生成树

## 提示

1. Connect each pair of points with a weighted edge, the weight being the manhattan distance between those points.
2. The problem is now the cost of minimum spanning tree in graph with above edges.

## 示例

```
[[0,0],[2,2],[3,10],[5,2],[7,0]]
[[3,12],[-2,5],[-4,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
```

### C

```c
int minCostConnectPoints(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCostConnectPoints(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function(points) {
    
};
```

### TypeScript

```typescript
function minCostConnectPoints(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minCostConnectPoints($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCostConnectPoints(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCostConnectPoints(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCostConnectPoints(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func minCostConnectPoints(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def min_cost_connect_points(points)
    
end
```

### Scala

```scala
object Solution {
    def minCostConnectPoints(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost-connect-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost_connect_points(Points :: [[integer()]]) -> integer().
min_cost_connect_points(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost_connect_points(points :: [[integer]]) :: integer
  def min_cost_connect_points(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCostConnectPoints(points: Array<Array<Int64>>): Int64 {

    }
}
```

