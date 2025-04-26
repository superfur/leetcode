# 3047. 求交集区域内的最大正方形面积

## 题目描述

<p>在二维平面上存在 <code>n</code> 个矩形。给你两个下标从 <strong>0</strong> 开始的二维整数数组 <code>bottomLeft</code> 和 <code>topRight</code>，两个数组的大小都是 <code>n x 2</code> ，其中 <code>bottomLeft[i]</code> 和 <code>topRight[i]</code> 分别代表第 <code>i</code> 个矩形的<strong> 左下角 </strong>和 <strong>右上角 </strong>坐标。</p>

<p>我们定义 <strong>向右 </strong>的方向为 x 轴正半轴（<strong>x 坐标增加</strong>），<strong>向左 </strong>的方向为 x 轴负半轴（<strong>x 坐标减少</strong>）。同样地，定义 <strong>向上 </strong>的方向为 y 轴正半轴（<strong>y 坐标增加</strong>）<strong>，向下 </strong>的方向为 y 轴负半轴（<strong>y 坐标减少</strong>）。</p>

<p>你可以选择一个区域，该区域由两个矩形的 <strong>交集</strong>&nbsp;形成。你需要找出能够放入该区域 <strong>内 </strong>的<strong> 最大 </strong>正方形面积，并选择最优解。</p>

<p>返回能够放入交集区域的正方形的 <strong>最大 </strong>可能面积，如果矩形之间不存在任何交集区域，则返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/05/example12.png" style="width: 443px; height: 364px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;" />
<pre>
<strong>输入：</strong>bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
<strong>输出：</strong>1
<strong>解释：</strong>边长为 1 的正方形可以放入矩形 0 和矩形 1 的交集区域，或矩形 1 和矩形 2 的交集区域。因此最大面积是边长 * 边长，即 1 * 1 = 1。
可以证明，边长更大的正方形无法放入任何交集区域。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 445px; height: 365px;" />
<pre>
<strong>输入：</strong>bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]
<strong>输出：</strong>1
<strong>解释：</strong>边长为 1 的正方形可以放入矩形 0 和矩形 1，矩形 1 和矩形 2，或所有三个矩形的交集区域。因此最大面积是边长 * 边长，即 1 * 1 = 1。
可以证明，边长更大的正方形无法放入任何交集区域。
请注意，区域可以由多于两个矩形的交集构成。
</pre>

<p><strong class="example">示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample3.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 444px; height: 364px;" />
<pre>
<strong>输入：</strong>bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]
<strong>输出：</strong>0
<strong>解释：</strong>不存在相交的矩形，因此，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == bottomLeft.length == topRight.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>3</sup></code></li>
	<li><code>bottomLeft[i].length == topRight[i].length == 2</code></li>
	<li><code>1 &lt;= bottomLeft[i][0], bottomLeft[i][1] &lt;= 10<sup>7</sup></code></li>
	<li><code>1 &lt;= topRight[i][0], topRight[i][1] &lt;= 10<sup>7</sup></code></li>
	<li><code>bottomLeft[i][0] &lt; topRight[i][0]</code></li>
	<li><code>bottomLeft[i][1] &lt; topRight[i][1]</code></li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数组
- 数学

## 提示

1. Brute Force the intersection area of each pair of rectangles.
2. Two rectangles will not overlap when the bottom left x coordinate of one rectangle is greater than the top right x coordinate of the other rectangle. The same is true for the y coordinate.
3. The intersection area (if any) is also a rectangle. Find its corners.

## 示例

```
[[1,1],[2,2],[3,1]]
[[3,3],[4,4],[6,6]]
[[1,1],[1,3],[1,5]]
[[5,5],[5,7],[5,9]]
[[1,1],[2,2],[1,2]]
[[3,3],[4,4],[3,4]]
[[1,1],[3,3],[3,1]]
[[2,2],[4,4],[4,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        
    }
};
```

### Java

```java
class Solution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
```

### C

```c
long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize, int** topRight, int topRightSize, int* topRightColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} bottomLeft
 * @param {number[][]} topRight
 * @return {number}
 */
var largestSquareArea = function(bottomLeft, topRight) {
    
};
```

### TypeScript

```typescript
function largestSquareArea(bottomLeft: number[][], topRight: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $bottomLeft
     * @param Integer[][] $topRight
     * @return Integer
     */
    function largestSquareArea($bottomLeft, $topRight) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestSquareArea(_ bottomLeft: [[Int]], _ topRight: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestSquareArea(bottomLeft: Array<IntArray>, topRight: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestSquareArea(List<List<int>> bottomLeft, List<List<int>> topRight) {
    
  }
}
```

### Go

```golang
func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} bottom_left
# @param {Integer[][]} top_right
# @return {Integer}
def largest_square_area(bottom_left, top_right)
    
end
```

### Scala

```scala
object Solution {
    def largestSquareArea(bottomLeft: Array[Array[Int]], topRight: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>, top_right: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-square-area bottomLeft topRight)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_square_area(BottomLeft :: [[integer()]], TopRight :: [[integer()]]) -> integer().
largest_square_area(BottomLeft, TopRight) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_square_area(bottom_left :: [[integer]], top_right :: [[integer]]) :: integer
  def largest_square_area(bottom_left, top_right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestSquareArea(bottomLeft: Array<Array<Int64>>, topRight: Array<Array<Int64>>): Int64 {

    }
}
```

