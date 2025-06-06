# 3025. 人员站位的方案数 I

## 题目描述

<p>给你一个&nbsp;&nbsp;<code>n x 2</code>&nbsp;的二维数组 <code>points</code>&nbsp;，它表示二维平面上的一些点坐标，其中&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;。</p>

<p>&nbsp;</p>

<p>计算点对&nbsp;<code>(A, B)</code>&nbsp;的数量，其中</p>

<ul>
	<li><code>A</code> 在 <code>B</code> 的左上角，并且</li>
	<li>它们形成的长方形中（或直线上）没有其它点（<strong>包括边界</strong>）。</li>
</ul>

<p>返回数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>points = [[1,1],[2,2],[3,3]]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2024/01/04/example1alicebob.png" style="width: 427px; height: 350px;" /></p>

<p>没有办法选择&nbsp;<code>A</code> 和&nbsp;<code>B</code>，使得&nbsp;<code>A</code>&nbsp;在&nbsp;<code>B</code>&nbsp;的左上角。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">points = [[6,2],[4,4],[2,6]]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p><img height="365" src="https://assets.leetcode.com/uploads/2024/06/25/t2.jpg" width="1321" /></p>

<ul>
	<li>左边的是点对&nbsp;<code>(points[1], points[0])</code>，其中&nbsp;<code>points[1]</code>&nbsp;在&nbsp;<code>points[0]</code>&nbsp;的左上角，并且形成的长方形内部是空的。</li>
	<li>中间的是点对&nbsp;<code>(points[2], points[1])</code>，和左边的一样是合法的点对。</li>
	<li>右边的是点对 <code>(points[2], points[0])</code>，其中 <code>points[2]</code> 在 <code>points[0]</code>&nbsp;的左上角，但&nbsp;<code>points[1]</code>&nbsp;在长方形内部，所以不是一个合法的点对。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">points = [[3,1],[1,3],[1,1]]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2024/06/25/t3.jpg" style="width: 1269px; height: 350px;" /></p>

<ul>
	<li>左边的是点对 <code>(points[2], points[0])</code>，其中&nbsp;<code>points[2]</code>&nbsp;在&nbsp;<code>points[0]</code>&nbsp;的左上角并且在它们形成的直线上没有其它点。注意两个点形成一条线的情况是合法的。</li>
	<li>中间的是点对 <code>(points[1], points[2])</code>，和左边一样也是合法的点对。</li>
	<li>右边的是点对 <code>(points[1], points[0])</code>，它不是合法的点对，因为&nbsp;<code>points[2]</code>&nbsp;在长方形的边上。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 50</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= points[i][0], points[i][1] &lt;= 50</code></li>
	<li><code>points[i]</code>&nbsp;点对两两不同。</li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数组
- 数学
- 枚举
- 排序

## 提示

1. We can enumerate all the upper-left and lower-right corners.
2. If the upper-left corner is <code>(x1, y1)</code> and lower-right corner is <code>(x2, y2)</code>, check that there is no point <code>(x, y)</code> such that <code>x1 <= x <= x2</code> and <code>y2 <= y <= y1</code>.

## 示例

```
[[1,1],[2,2],[3,3]]
[[6,2],[4,4],[2,6]]
[[3,1],[1,3],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfPairs(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
```

### C

```c
int numberOfPairs(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfPairs(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfPairs = function(points) {
    
};
```

### TypeScript

```typescript
function numberOfPairs(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function numberOfPairs($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPairs(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPairs(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPairs(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func numberOfPairs(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def number_of_pairs(points)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPairs(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_pairs(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-pairs points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_pairs(Points :: [[integer()]]) -> integer().
number_of_pairs(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(points :: [[integer]]) :: integer
  def number_of_pairs(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPairs(points: Array<Array<Int64>>): Int64 {

    }
}
```

