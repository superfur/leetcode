# 面试题 16.13. 平分正方形

## 题目描述

<p>给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。</p>

<p>每个正方形的数据<code>square</code>包含3个数值，正方形的左下顶点坐标<code>[X,Y] = [square[0],square[1]]</code>，以及正方形的边长<code>square[2]</code>。所求直线穿过两个正方形会形成4个交点，请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点）。2个端点坐标<code>[X<sub>1</sub>,Y<sub>1</sub>]</code>和<code>[X<sub>2</sub>,Y<sub>2</sub>]</code>的返回格式为<code>{X<sub>1</sub>,Y<sub>1</sub>,X<sub>2</sub>,Y<sub>2</sub>}</code>，要求若<code>X<sub>1</sub> != X<sub>2</sub></code>，需保证<code>X<sub>1</sub> &lt; X<sub>2</sub></code>，否则需保证<code>Y<sub>1</sub> &lt;= Y<sub>2</sub></code>。</p>

<p>若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
square1 = {-1, -1, 2}
square2 = {0, -1, 2}
<strong>输出：</strong> {-1,0,2,0}
<strong>解释：</strong> 直线 y = 0 能将两个正方形同时分为等面积的两部分，返回的两线段端点为[-1,0]和[2,0]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>square.length == 3</code></li>
	<li><code>square[2] &gt; 0</code></li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数学

## 提示

1. 画一个正方形和一些把它切成两半的线。这些线位于哪里？
2. 任何把正方形切成两半的直线都穿过正方形的中心。那你怎么才能找到一条把两个正方形切成两半的线呢？
3. 要将两个正方形切成两半，这条线必须穿过这两个正方形的中心。
4. 给定一条直线（斜率和y轴截距），你能找到它与另一条直线的交点吗?

## 示例

```
[-1,1,3]
[0,0,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<double> cutSquares(vector<int>& square1, vector<int>& square2) {
        
    }
};
```

### Java

```java
class Solution {
    public double[] cutSquares(int[] square1, int[] square2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def cutSquares(self, square1, square2):
        """
        :type square1: List[int]
        :type square2: List[int]
        :rtype: List[float]
        """
        
```

### Python3

```python3
class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* cutSquares(int* square1, int square1Size, int* square2, int square2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double[] CutSquares(int[] square1, int[] square2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} square1
 * @param {number[]} square2
 * @return {number[]}
 */
var cutSquares = function(square1, square2) {
    
};
```

### TypeScript

```typescript
function cutSquares(square1: number[], square2: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $square1
     * @param Integer[] $square2
     * @return Float[]
     */
    function cutSquares($square1, $square2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func cutSquares(_ square1: [Int], _ square2: [Int]) -> [Double] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun cutSquares(square1: IntArray, square2: IntArray): DoubleArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<double> cutSquares(List<int> square1, List<int> square2) {
    
  }
}
```

### Go

```golang
func cutSquares(square1 []int, square2 []int) []float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} square1
# @param {Integer[]} square2
# @return {Float[]}
def cut_squares(square1, square2)
    
end
```

### Scala

```scala
object Solution {
    def cutSquares(square1: Array[Int], square2: Array[Int]): Array[Double] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn cut_squares(square1: Vec<i32>, square2: Vec<i32>) -> Vec<f64> {
        
    }
}
```

### Racket

```racket
(define/contract (cut-squares square1 square2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof flonum?))
  )
```

### Erlang

```erlang
-spec cut_squares(Square1 :: [integer()], Square2 :: [integer()]) -> [float()].
cut_squares(Square1, Square2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec cut_squares(square1 :: [integer], square2 :: [integer]) :: [float]
  def cut_squares(square1, square2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func cutSquares(square1: Array<Int64>, square2: Array<Int64>): Array<Float64> {

    }
}
```

