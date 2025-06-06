# 850. 矩形面积 II

## 题目描述

<p>给你一个轴对齐的二维数组&nbsp;<code>rectangles</code>&nbsp;。 对于&nbsp;<code>rectangle[i] = [x1, y1, x2, y2]</code>，其中&nbsp;<code>(x<sub>i1</sub>, y<sub>i1</sub>)</code>&nbsp;是该矩形 <strong>左下角</strong> 的坐标，<meta charset="UTF-8" />&nbsp;<code>(x<sub>i2</sub>, y<sub>i2</sub>)</code>&nbsp;是该矩形&nbsp;<strong>右上角</strong> 的坐标。</p>

<p>计算平面中所有&nbsp;<code>rectangles</code>&nbsp;所覆盖的 <strong>总面积 </strong>。任何被两个或多个矩形覆盖的区域应只计算 <strong>一次</strong> 。</p>

<p>返回<em> <strong>总面积</strong> </em>。因为答案可能太大，返回<meta charset="UTF-8" />&nbsp;<code>10<sup>9</sup>&nbsp;+ 7</code> 的&nbsp;<strong>模</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png" style="height: 360px; width: 480px;" /></p>

<pre>
<strong>输入：</strong>rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
<strong>输出：</strong>6
<strong>解释：</strong>如图所示，三个矩形覆盖了总面积为 6 的区域。
从(1,1)到(2,2)，绿色矩形和红色矩形重叠。
从(1,0)到(2,3)，三个矩形都重叠。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>rectangles = [[0,0,1000000000,1000000000]]
<strong>输出：</strong>49
<strong>解释：</strong>答案是 10<sup>18</sup> 对 (10<sup>9</sup> + 7) 取模的结果， 即 49 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 200</code></li>
	<li><code>rectanges[i].length = 4</code><meta charset="UTF-8" /></li>
	<li><code>0 &lt;= x<sub>i1</sub>, y<sub>i1</sub>, x<sub>i2</sub>, y<sub>i2</sub>&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>x<sub>i1&nbsp;</sub>&lt;= x<sub>i2</sub></code></li>
	<li><code>y<sub>i1&nbsp;</sub>&lt;= y<sub>i2</sub></code></li>
	<li>所有矩阵面积不为 0。</li>
</ul>


## 难度

Hard

## 标签

- 线段树
- 数组
- 有序集合
- 扫描线

## 示例

```
[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
[[0,0,1000000000,1000000000]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        
    }
};
```

### Java

```java
class Solution {
    public int rectangleArea(int[][] rectangles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
```

### C

```c
int rectangleArea(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int RectangleArea(int[][] rectangles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var rectangleArea = function(rectangles) {
    
};
```

### TypeScript

```typescript
function rectangleArea(rectangles: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function rectangleArea($rectangles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rectangleArea(_ rectangles: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rectangleArea(rectangles: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int rectangleArea(List<List<int>> rectangles) {
    
  }
}
```

### Go

```golang
func rectangleArea(rectangles [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} rectangles
# @return {Integer}
def rectangle_area(rectangles)
    
end
```

### Scala

```scala
object Solution {
    def rectangleArea(rectangles: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rectangle_area(rectangles: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (rectangle-area rectangles)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec rectangle_area(Rectangles :: [[integer()]]) -> integer().
rectangle_area(Rectangles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rectangle_area(rectangles :: [[integer]]) :: integer
  def rectangle_area(rectangles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rectangleArea(rectangles: Array<Array<Int64>>): Int64 {

    }
}
```

