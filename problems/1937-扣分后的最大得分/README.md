# 1937. 扣分后的最大得分

## 题目描述

<p>给你一个 <code>m x n</code> 的整数矩阵 <code>points</code> （下标从 <strong>0</strong> 开始）。一开始你的得分为 <code>0</code> ，你想最大化从矩阵中得到的分数。</p>

<p>你的得分方式为：<strong>每一行</strong> 中选取一个格子，选中坐标为 <code>(r, c)</code> 的格子会给你的总得分 <strong>增加</strong> <code>points[r][c]</code> 。</p>

<p>然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。对于相邻行 <code>r</code> 和 <code>r + 1</code> （其中 <code>0 <= r < m - 1</code>），选中坐标为 <code>(r, c<sub>1</sub>)</code> 和 <code>(r + 1, c<sub>2</sub>)</code> 的格子，你的总得分 <b>减少</b> <code>abs(c<sub>1</sub> - c<sub>2</sub>)</code> 。</p>

<p>请你返回你能得到的 <strong>最大</strong> 得分。</p>

<p><code>abs(x)</code> 定义为：</p>

<ul>
	<li>如果 <code>x >= 0</code> ，那么值为 <code>x</code> 。</li>
	<li>如果 <code>x < 0</code> ，那么值为 <code>-x</code> 。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png" style="width: 300px; height: 300px;" />
<pre>
<b>输入：</b>points = [[1,2,3],[1,5,1],[3,1,1]]
<b>输出：</b>9
<strong>解释：</strong>
蓝色格子是最优方案选中的格子，坐标分别为 (0, 2)，(1, 1) 和 (2, 0) 。
你的总得分增加 3 + 5 + 3 = 11 。
但是你的总得分需要扣除 abs(2 - 1) + abs(1 - 0) = 2 。
你的最终得分为 11 - 2 = 9 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png" style="width: 200px; height: 299px;" />
<pre>
<b>输入：</b>points = [[1,5],[2,3],[4,2]]
<b>输出：</b>11
<strong>解释：</strong>
蓝色格子是最优方案选中的格子，坐标分别为 (0, 1)，(1, 1) 和 (2, 0) 。
你的总得分增加 5 + 3 + 4 = 12 。
但是你的总得分需要扣除 abs(1 - 1) + abs(1 - 0) = 1 。
你的最终得分为 12 - 1 = 11 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == points.length</code></li>
	<li><code>n == points[r].length</code></li>
	<li><code>1 <= m, n <= 10<sup>5</sup></code></li>
	<li><code>1 <= m * n <= 10<sup>5</sup></code></li>
	<li><code>0 <= points[r][c] <= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Try using dynamic programming.
2. dp[i][j] is the maximum number of points you can have if points[i][j] is the most recent cell you picked.

## 示例

```
[[1,2,3],[1,5,1],[3,1,1]]
[[1,5],[2,3],[4,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxPoints(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
```

### C

```c
long long maxPoints(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxPoints(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxPoints = function(points) {
    
};
```

### TypeScript

```typescript
function maxPoints(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxPoints($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPoints(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPoints(points: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPoints(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func maxPoints(points [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def max_points(points)
    
end
```

### Scala

```scala
object Solution {
    def maxPoints(points: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_points(Points :: [[integer()]]) -> integer().
max_points(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_points(points :: [[integer]]) :: integer
  def max_points(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPoints(points: Array<Array<Int64>>): Int64 {

    }
}
```

