# 812. 最大三角形面积

## 题目描述

<p>给你一个由 <strong>X-Y</strong> 平面上的点组成的数组 <code>points</code> ，其中 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 。从其中取任意三个不同的点组成三角形，返回能组成的最大三角形的面积。与真实值误差在 <code>10<sup>-5</sup></code> 内的答案将会视为正确答案<strong>。</strong></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height: 369px; width: 450px;" />
<pre>
<strong>输入：</strong>points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>输出：</strong>2.00000
<strong>解释：</strong>输入中的 5 个点如上图所示，红色的三角形面积最大。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,0],[0,0],[0,1]]
<strong>输出：</strong>0.50000
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code></li>
	<li><code>-50 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 50</code></li>
	<li>给出的所有点 <strong>互不相同</strong></li>
</ul>


## 难度

Easy

## 标签

- 几何
- 数组
- 数学

## 示例

```
[[0,0],[0,1],[1,0],[0,2],[2,0]]
[[1,0],[0,0],[0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public double largestTriangleArea(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
```

### C

```c
double largestTriangleArea(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double LargestTriangleArea(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var largestTriangleArea = function(points) {
    
};
```

### TypeScript

```typescript
function largestTriangleArea(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Float
     */
    function largestTriangleArea($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestTriangleArea(_ points: [[Int]]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestTriangleArea(points: Array<IntArray>): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double largestTriangleArea(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func largestTriangleArea(points [][]int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Float}
def largest_triangle_area(points)
    
end
```

### Scala

```scala
object Solution {
    def largestTriangleArea(points: Array[Array[Int]]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-triangle-area points)
  (-> (listof (listof exact-integer?)) flonum?)
  )
```

### Erlang

```erlang
-spec largest_triangle_area(Points :: [[integer()]]) -> float().
largest_triangle_area(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_triangle_area(points :: [[integer]]) :: float
  def largest_triangle_area(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestTriangleArea(points: Array<Array<Int64>>): Float64 {

    }
}
```

