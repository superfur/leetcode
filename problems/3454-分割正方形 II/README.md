# 3454. 分割正方形 II

## 题目描述

<p>给你一个二维整数数组 <code>squares</code>&nbsp;，其中&nbsp;<code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code> 表示一个与 x 轴平行的正方形的左下角坐标和正方形的边长。</p>

<p>找到一个<strong>最小的</strong> y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 <strong>等于</strong> 该线以下正方形的总面积。</p>

<p>答案如果与实际答案的误差在 <code>10<sup>-5</sup></code> 以内，将视为正确答案。</p>

<p><strong>注意</strong>：正方形&nbsp;<strong>可能会&nbsp;</strong>重叠。重叠区域只&nbsp;<strong>统计一次&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">squares = [[0,0,1],[2,2,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1.00000</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1739609602-zhNmeC-4065example1drawio.png" style="width: 269px; height: 203px;" /></p>

<p>任何在 <code>y = 1</code> 和 <code>y = 2</code> 之间的水平线都会有 1 平方单位的面积在其上方，1 平方单位的面积在其下方。最小的 y 坐标是 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">squares = [[0,0,2],[1,1,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1.00000</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1739609605-ezeVgk-4065example2drawio.png" style="width: 269px; height: 203px;" /></p>

<p>由于蓝色正方形和红色正方形有重叠区域且重叠区域只统计一次。所以直线&nbsp;<code>y = 1</code>&nbsp;将正方形分割成两部分且面积相等。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= squares.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code></li>
	<li><code>squares[i].length == 3</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li>所有正方形的总面积不超过 <code>10<sup>15</sup></code>。</li>
</ul>


## 难度

Hard

## 标签

- 线段树
- 数组
- 二分查找
- 扫描线

## 提示

1. Use a line sweep and a segment tree.
2. The line must lie in one of the squares.

## 示例

```
[[0,0,1],[2,2,1]]
[[0,0,2],[1,1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        
    }
};
```

### Java

```java
class Solution {
    public double separateSquares(int[][] squares) {
        
    }
}
```

### Python

```python
class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
```

### C

```c
double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double SeparateSquares(int[][] squares) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} squares
 * @return {number}
 */
var separateSquares = function(squares) {
    
};
```

### TypeScript

```typescript
function separateSquares(squares: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $squares
     * @return Float
     */
    function separateSquares($squares) {
        
    }
}
```

### Swift

```swift
class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun separateSquares(squares: Array<IntArray>): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double separateSquares(List<List<int>> squares) {
    
  }
}
```

### Go

```golang
func separateSquares(squares [][]int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} squares
# @return {Float}
def separate_squares(squares)
    
end
```

### Scala

```scala
object Solution {
    def separateSquares(squares: Array[Array[Int]]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (separate-squares squares)
  (-> (listof (listof exact-integer?)) flonum?)
  )
```

### Erlang

```erlang
-spec separate_squares(Squares :: [[integer()]]) -> float().
separate_squares(Squares) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec separate_squares(squares :: [[integer]]) :: float
  def separate_squares(squares) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func separateSquares(squares: Array<Array<Int64>>): Float64 {

    }
}
```

