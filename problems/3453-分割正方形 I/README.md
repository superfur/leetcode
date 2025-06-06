# 3453. 分割正方形 I

## 题目描述

<p>给你一个二维整数数组 <code>squares</code>&nbsp;，其中&nbsp;<code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code> 表示一个与 x 轴平行的正方形的左下角坐标和正方形的边长。</p>

<p>找到一个<strong>最小的</strong> y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 <strong>等于</strong> 该线以下正方形的总面积。</p>

<p>答案如果与实际答案的误差在 <code>10<sup>-5</sup></code> 以内，将视为正确答案。</p>

<p><strong>注意</strong>：正方形&nbsp;<strong>可能会&nbsp;</strong>重叠。重叠区域应该被&nbsp;<strong>多次计数&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">squares = [[0,0,1],[2,2,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1.00000</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1739609465-UaFzhk-4062example1drawio.png" style="width: 378px; height: 352px;" /></p>

<p>任何在 <code>y = 1</code> 和 <code>y = 2</code> 之间的水平线都会有 1 平方单位的面积在其上方，1 平方单位的面积在其下方。最小的 y 坐标是 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">squares = [[0,0,2],[1,1,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1.16667</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1739609527-TWqefZ-4062example2drawio.png" style="width: 378px; height: 352px;" /></p>

<p>面积如下：</p>

<ul>
	<li>线下的面积：<code>7/6 * 2 (红色) + 1/6 (蓝色) = 15/6 = 2.5</code>。</li>
	<li>线上的面积：<code>5/6 * 2 (红色) + 5/6 (蓝色) = 15/6 = 2.5</code>。</li>
</ul>

<p>由于线以上和线以下的面积相等，输出为 <code>7/6 = 1.16667</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= squares.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code></li>
	<li><code>squares[i].length == 3</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li>所有正方形的总面积不超过 <code>10<sup>12</sup></code>。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Binary search on the answer.

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

