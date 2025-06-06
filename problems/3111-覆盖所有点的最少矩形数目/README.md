# 3111. 覆盖所有点的最少矩形数目

## 题目描述

<p>给你一个二维整数数组&nbsp;<code>point</code>&nbsp;，其中&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;表示二维平面内的一个点。同时给你一个整数&nbsp;<code>w</code>&nbsp;。你需要用矩形&nbsp;<strong>覆盖所有</strong>&nbsp;点。</p>

<p>每个矩形的左下角在某个点&nbsp;<code>(x<sub>1</sub>, 0)</code>&nbsp;处，且右上角在某个点&nbsp;<code>(x<sub>2</sub>, y<sub>2</sub>)</code>&nbsp;处，其中&nbsp;<code>x<sub>1</sub> &lt;= x<sub>2</sub></code>&nbsp;且&nbsp;<code>y<sub>2</sub> &gt;= 0</code>&nbsp;，同时对于每个矩形都&nbsp;<strong>必须</strong>&nbsp;满足&nbsp;<code>x<sub>2</sub> - x<sub>1</sub> &lt;= w</code>&nbsp;。</p>

<p>如果一个点在矩形内或者在边上，我们说这个点被矩形覆盖了。</p>

<p>请你在确保每个点都 <strong>至少</strong>&nbsp;被一个矩形覆盖的前提下，<strong>最少</strong>&nbsp;需要多少个矩形。</p>

<p><strong>注意：</strong>一个点可以被多个矩形覆盖。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/04/screenshot-from-2024-03-04-20-33-05.png" style="width: 205px; height: 300px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p style=""><span class="example-io" style="font-size: 8.75px;"><b>输入：</b></span><span class="example-io" style="font-size: 0.85rem; font-family: Menlo, sans-serif;">points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1</span></p>

<p style=""><span class="example-io" style="font-size: 8.75px;"><b>输出：</b></span><span class="example-io" style="font-size: 0.85rem; font-family: Menlo, sans-serif;">2</span></p>

<p style="font-size: 0.875rem;"><strong>解释：</strong></p>

<p style="font-size: 0.875rem;">上图展示了一种可行的矩形放置方案：</p>

<ul style="font-size: 0.875rem;">
	<li>一个矩形的左下角在&nbsp;<code>(1, 0)</code>&nbsp;，右上角在&nbsp;<code>(2, 8)</code>&nbsp;。</li>
	<li>一个矩形的左下角在&nbsp;<code>(3, 0)</code>&nbsp;，右上角在&nbsp;<code>(4, 8)</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/04/screenshot-from-2024-03-04-18-59-12.png" style="width: 260px; height: 250px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p style=""><span class="example-io" style="font-size: 8.75px;"><b>输入：</b></span><span class="example-io" style="font-size: 0.85rem; font-family: Menlo, sans-serif;">points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2</span></p>

<p style=""><span class="example-io" style="font-size: 8.75px;"><b>输出：</b></span><span class="example-io" style="font-size: 0.85rem; font-family: Menlo, sans-serif;">3</span></p>

<p style="font-size: 0.875rem;"><b>解释：</b></p>

<p style="font-size: 0.875rem;">上图展示了一种可行的矩形放置方案：</p>

<ul style="font-size: 0.875rem;">
	<li>一个矩形的左下角在&nbsp;<code>(0, 0)</code>&nbsp;，右上角在&nbsp;<code>(2, 2)</code>&nbsp;。</li>
	<li>一个矩形的左下角在&nbsp;<code>(3, 0)</code>&nbsp;，右上角在&nbsp;<code>(5, 5)</code>&nbsp;。</li>
	<li>一个矩形的左下角在&nbsp;<code>(6, 0)</code>&nbsp;，右上角在&nbsp;<code>(6, 6)</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/04/screenshot-from-2024-03-04-20-24-03.png" style="height: 150px; width: 127px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p style=""><span class="example-io" style="font-size: 8.75px;"><b>输入：</b></span><span class="example-io" style="font-size: 0.85rem; font-family: Menlo, sans-serif;">points = [[2,3],[1,2]], w = 0</span></p>

<p style=""><span class="example-io" style="font-size: 8.75px;"><b>输出：</b></span><span class="example-io" style="font-size: 0.85rem; font-family: Menlo, sans-serif;">2</span></p>

<p style="font-size: 0.875rem;"><strong>解释：</strong></p>

<p style="font-size: 0.875rem;">上图展示了一种可行的矩形放置方案：</p>

<ul style="font-size: 0.875rem;">
	<li>一个矩形的左下角在&nbsp;<code>(1, 0)</code>&nbsp;，右上角在&nbsp;<code>(1, 2)</code>&nbsp;。</li>
	<li>一个矩形的左下角在&nbsp;<code>(2, 0)</code>&nbsp;，右上角在&nbsp;<code>(2, 3)</code>&nbsp;。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub> == points[i][0] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= y<sub>i</sub> == points[i][1] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= w &lt;= 10<sup>9</sup></code></li>
	<li>所有点坐标&nbsp;<code>(x<sub>i</sub>, y<sub>i</sub>)</code>&nbsp;互不相同。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. The <code>y</code> values don't matter; only the <code>x</code> values matter.
2. Sort all the points by <code>x<sub>i</sub></code>.
3. Each time, select the smallest <code>x</code> value, <code>x<sub>0</sub></code>, from the unselected points, and then select all the points with <code>x</code> values not larger than <code>x<sub>0</sub> + w</code>.

## 示例

```
[[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]
1
[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
2
[[2,3],[1,2]]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minRectanglesToCoverPoints(vector<vector<int>>& points, int w) {
        
    }
};
```

### Java

```java
class Solution {
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        
```

### C

```c
int minRectanglesToCoverPoints(int** points, int pointsSize, int* pointsColSize, int w) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinRectanglesToCoverPoints(int[][] points, int w) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @param {number} w
 * @return {number}
 */
var minRectanglesToCoverPoints = function(points, w) {
    
};
```

### TypeScript

```typescript
function minRectanglesToCoverPoints(points: number[][], w: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $w
     * @return Integer
     */
    function minRectanglesToCoverPoints($points, $w) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minRectanglesToCoverPoints(_ points: [[Int]], _ w: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minRectanglesToCoverPoints(points: Array<IntArray>, w: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minRectanglesToCoverPoints(List<List<int>> points, int w) {
    
  }
}
```

### Go

```golang
func minRectanglesToCoverPoints(points [][]int, w int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @param {Integer} w
# @return {Integer}
def min_rectangles_to_cover_points(points, w)
    
end
```

### Scala

```scala
object Solution {
    def minRectanglesToCoverPoints(points: Array[Array[Int]], w: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_rectangles_to_cover_points(points: Vec<Vec<i32>>, w: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-rectangles-to-cover-points points w)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_rectangles_to_cover_points(Points :: [[integer()]], W :: integer()) -> integer().
min_rectangles_to_cover_points(Points, W) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_rectangles_to_cover_points(points :: [[integer]], w :: integer) :: integer
  def min_rectangles_to_cover_points(points, w) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minRectanglesToCoverPoints(points: Array<Array<Int64>>, w: Int64): Int64 {

    }
}
```

