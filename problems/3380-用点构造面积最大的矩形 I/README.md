# 3380. 用点构造面积最大的矩形 I

## 题目描述

<p>给你一个数组 <code>points</code>，其中 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示无限平面上一点的坐标。</p>

<p>你的任务是找出满足以下条件的矩形可能的&nbsp;<strong>最大&nbsp;</strong>面积：</p>

<ul>
	<li>矩形的四个顶点必须是数组中的&nbsp;<strong>四个&nbsp;</strong>点。</li>
	<li>矩形的内部或边界上&nbsp;<strong>不能&nbsp;</strong>包含任何其他点。</li>
	<li>矩形的边与坐标轴&nbsp;<strong>平行&nbsp;</strong>。</li>
</ul>

<p>返回可以获得的&nbsp;<strong>最大面积&nbsp;</strong>，如果无法形成这样的矩形，则返回 -1。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3]]</span></p>

<p><strong>输出：</strong>4</p>

<p><strong>解释：</strong></p>

<p><strong class="example"><img alt="示例 1 图示" src="https://assets.leetcode.com/uploads/2024/11/02/example1.png" style="width: 229px; height: 228px;" /></strong></p>

<p>我们可以用这 4 个点作为顶点构成一个矩形，并且矩形内部或边界上没有其他点。因此，最大面积为 4 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3],[2,2]]</span></p>

<p><strong>输出：</strong>-1</p>

<p><strong>解释：</strong></p>

<p><strong class="example"><img alt="示例 2 图示" src="https://assets.leetcode.com/uploads/2024/11/02/example2.png" style="width: 229px; height: 228px;" /></strong></p>

<p>唯一一组可能构成矩形的点为 <code>[1,1], [1,3], [3,1]</code> 和 <code>[3,3]</code>，但点 <code>[2,2]</code> 总是位于矩形内部。因此，返回 -1 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]</span></p>

<p><strong>输出：</strong>2</p>

<p><strong>解释：</strong></p>

<p><strong class="example"><img alt="示例 3 图示" src="https://assets.leetcode.com/uploads/2024/11/02/example3.png" style="width: 229px; height: 228px;" /></strong></p>

<p>点 <code>[1,3], [1,2], [3,2], [3,3]</code>&nbsp;可以构成面积最大的矩形，面积为 2。此外，点 <code>[1,1], [1,2], [3,1], [3,2]</code> 也可以构成一个符合题目要求的矩形，面积相同。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 10</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 100</code></li>
	<li>给定的所有点都是 <strong>唯一</strong> 的。</li>
</ul>


## 难度

Medium

## 标签

- 树状数组
- 线段树
- 几何
- 数组
- 数学
- 枚举
- 排序

## 提示

1. If <code>(x1, y1)</code> and <code>(x2, y2)</code> are two opposite corners of a rectangle, then the other two would be <code>(x1, y2)</code> and <code>(x2, y1)</code>.
2. Fix two points and find the other two using a set data structure.
3. After determining the rectangle, iterate through the array of points to ensure no point lies on the rectangle’s border or within its interior.

## 示例

```
[[1,1],[1,3],[3,1],[3,3]]
[[1,1],[1,3],[3,1],[3,3],[2,2]]
[[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxRectangleArea(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxRectangleArea(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        
```

### C

```c
int maxRectangleArea(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxRectangleArea(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxRectangleArea = function(points) {
    
};
```

### TypeScript

```typescript
function maxRectangleArea(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxRectangleArea($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxRectangleArea(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxRectangleArea(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxRectangleArea(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func maxRectangleArea(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def max_rectangle_area(points)
    
end
```

### Scala

```scala
object Solution {
    def maxRectangleArea(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_rectangle_area(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-rectangle-area points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_rectangle_area(Points :: [[integer()]]) -> integer().
max_rectangle_area(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_rectangle_area(points :: [[integer]]) :: integer
  def max_rectangle_area(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxRectangleArea(points: Array<Array<Int64>>): Int64 {

    }
}
```

