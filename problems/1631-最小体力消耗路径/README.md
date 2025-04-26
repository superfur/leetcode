# 1631. 最小体力消耗路径

## 题目描述

<p>你准备参加一场远足活动。给你一个二维 <code>rows x columns</code> 的地图 <code>heights</code> ，其中 <code>heights[row][col]</code> 表示格子 <code>(row, col)</code> 的高度。一开始你在最左上角的格子 <code>(0, 0)</code> ，且你希望去最右下角的格子 <code>(rows-1, columns-1)</code> （注意下标从 <strong>0</strong> 开始编号）。你每次可以往 <strong>上</strong>，<strong>下</strong>，<strong>左</strong>，<strong>右</strong> 四个方向之一移动，你想要找到耗费 <strong>体力</strong> 最小的一条路径。</p>

<p>一条路径耗费的 <strong>体力值</strong> 是路径上相邻格子之间 <strong>高度差绝对值</strong> 的 <strong>最大值</strong> 决定的。</p>

<p>请你返回从左上角走到右下角的最小<strong> 体力消耗值</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/ex1.png" style="width: 300px; height: 300px;" /></p>

<pre>
<b>输入：</b>heights = [[1,2,2],[3,8,2],[5,3,5]]
<b>输出：</b>2
<b>解释：</b>路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/ex2.png" style="width: 300px; height: 300px;" /></p>

<pre>
<b>输入：</b>heights = [[1,2,3],[3,8,4],[5,3,5]]
<b>输出：</b>1
<b>解释：</b>路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/ex3.png" style="width: 300px; height: 300px;" />
<pre>
<b>输入：</b>heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
<b>输出：</b>0
<b>解释：</b>上图所示路径不需要消耗任何体力。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rows == heights.length</code></li>
	<li><code>columns == heights[i].length</code></li>
	<li><code>1 <= rows, columns <= 100</code></li>
	<li><code>1 <= heights[i][j] <= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 二分查找
- 矩阵
- 堆（优先队列）

## 提示

1. Consider the grid as a graph, where adjacent cells have an edge with cost of the difference between the cells.
2. If you are given threshold k, check if it is possible to go from (0, 0) to (n-1, m-1) using only edges of ≤ k cost.
3. Binary search the k value.

## 示例

```
[[1,2,2],[3,8,2],[5,3,5]]
[[1,2,3],[3,8,4],[5,3,5]]
[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumEffortPath(int[][] heights) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
```

### C

```c
int minimumEffortPath(int** heights, int heightsSize, int* heightsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumEffortPath(int[][] heights) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} heights
 * @return {number}
 */
var minimumEffortPath = function(heights) {
    
};
```

### TypeScript

```typescript
function minimumEffortPath(heights: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $heights
     * @return Integer
     */
    function minimumEffortPath($heights) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumEffortPath(_ heights: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumEffortPath(heights: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumEffortPath(List<List<int>> heights) {
    
  }
}
```

### Go

```golang
func minimumEffortPath(heights [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} heights
# @return {Integer}
def minimum_effort_path(heights)
    
end
```

### Scala

```scala
object Solution {
    def minimumEffortPath(heights: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-effort-path heights)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_effort_path(Heights :: [[integer()]]) -> integer().
minimum_effort_path(Heights) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_effort_path(heights :: [[integer]]) :: integer
  def minimum_effort_path(heights) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumEffortPath(heights: Array<Array<Int64>>): Int64 {

    }
}
```

