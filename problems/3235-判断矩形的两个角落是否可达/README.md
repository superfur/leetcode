# 3235. 判断矩形的两个角落是否可达

## 题目描述

<p>给你两个正整数&nbsp;<code>xCorner</code> 和&nbsp;<code>yCorner</code>&nbsp;和一个二维整数数组&nbsp;<code>circles</code>&nbsp;，其中&nbsp;<code>circles[i] = [x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub>]</code>&nbsp;表示一个圆心在&nbsp;<code>(x<sub>i</sub>, y<sub>i</sub>)</code>&nbsp;半径为&nbsp;<code>r<sub>i</sub></code>&nbsp;的圆。</p>

<p>坐标平面内有一个左下角在原点，右上角在&nbsp;<code>(xCorner, yCorner)</code>&nbsp;的矩形。你需要判断是否存在一条从左下角到右上角的路径满足：路径&nbsp;<strong>完全</strong>&nbsp;在矩形内部，<strong>不会</strong>&nbsp;触碰或者经过 <strong>任何</strong>&nbsp;圆的内部和边界，同时&nbsp;<strong>只</strong> 在起点和终点接触到矩形。</p>

<p>如果存在这样的路径，请你返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>X = 3, Y = 4, circles = [[2,1,1]]</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/18/example2circle1.png" style="width: 346px; height: 264px;" /></p>

<p>黑色曲线表示一条从&nbsp;<code>(0, 0)</code>&nbsp;到&nbsp;<code>(3, 4)</code>&nbsp;的路径。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>X = 3, Y = 3, circles = [[1,1,2]]</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/18/example1circle.png" style="width: 346px; height: 264px;" /></p>

<p>不存在从&nbsp;<code>(0, 0)</code> 到&nbsp;<code>(3, 3)</code>&nbsp;的路径。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>X = 3, Y = 3, circles = [[2,1,1],[1,2,1]]</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><b>解释：</b></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/18/example0circle.png" style="width: 346px; height: 264px;" /></p>

<p>不存在从&nbsp;<code>(0, 0)</code>&nbsp;到&nbsp;<code>(3, 3)</code>&nbsp;的路径。</p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">X = 4, Y = 4, circles = [[5,5,1]]</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/04/rectangles.png" style="width: 346px; height: 264px;" /></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= xCorner, yCorner&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= circles.length &lt;= 1000</code></li>
	<li><code>circles[i].length == 3</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 几何
- 数组
- 数学

## 提示

1. Create a graph with <code>n + 4</code> vertices.
2. Vertices 0 to <code>n - 1</code> represent the circles, vertex <code>n</code> represents upper edge, vertex <code>n + 1</code> represents right edge, vertex <code>n + 2</code> represents lower edge, and vertex <code>n + 3</code> represents left edge.
3. Add an edge between these vertices if they intersect or touch.
4. Answer will be <code>false</code> when any of two sides left-right, left-bottom, right-top or top-bottom are reachable using the edges.

## 示例

```
3
4
[[2,1,1]]
3
3
[[1,1,2]]
3
3
[[2,1,1],[1,2,1]]
4
4
[[5,5,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canReachCorner(int xCorner, int yCorner, vector<vector<int>>& circles) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canReachCorner(int xCorner, int yCorner, int[][] circles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canReachCorner(self, xCorner, yCorner, circles):
        """
        :type xCorner: int
        :type yCorner: int
        :type circles: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        
```

### C

```c
bool canReachCorner(int xCorner, int yCorner, int** circles, int circlesSize, int* circlesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanReachCorner(int xCorner, int yCorner, int[][] circles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} xCorner
 * @param {number} yCorner
 * @param {number[][]} circles
 * @return {boolean}
 */
var canReachCorner = function(xCorner, yCorner, circles) {
    
};
```

### TypeScript

```typescript
function canReachCorner(xCorner: number, yCorner: number, circles: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $xCorner
     * @param Integer $yCorner
     * @param Integer[][] $circles
     * @return Boolean
     */
    function canReachCorner($xCorner, $yCorner, $circles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canReachCorner(_ xCorner: Int, _ yCorner: Int, _ circles: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canReachCorner(xCorner: Int, yCorner: Int, circles: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canReachCorner(int xCorner, int yCorner, List<List<int>> circles) {
    
  }
}
```

### Go

```golang
func canReachCorner(xCorner int, yCorner int, circles [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} x_corner
# @param {Integer} y_corner
# @param {Integer[][]} circles
# @return {Boolean}
def can_reach_corner(x_corner, y_corner, circles)
    
end
```

### Scala

```scala
object Solution {
    def canReachCorner(xCorner: Int, yCorner: Int, circles: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_reach_corner(x_corner: i32, y_corner: i32, circles: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-reach-corner xCorner yCorner circles)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec can_reach_corner(XCorner :: integer(), YCorner :: integer(), Circles :: [[integer()]]) -> boolean().
can_reach_corner(XCorner, YCorner, Circles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_reach_corner(x_corner :: integer, y_corner :: integer, circles :: [[integer]]) :: boolean
  def can_reach_corner(x_corner, y_corner, circles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canReachCorner(xCorner: Int64, yCorner: Int64, circles: Array<Array<Int64>>): Bool {

    }
}
```

