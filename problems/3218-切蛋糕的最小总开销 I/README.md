# 3218. 切蛋糕的最小总开销 I

## 题目描述

<p>有一个&nbsp;<code>m x n</code>&nbsp;大小的矩形蛋糕，需要切成&nbsp;<code>1 x 1</code>&nbsp;的小块。</p>

<p>给你整数&nbsp;<code>m</code>&nbsp;，<code>n</code>&nbsp;和两个数组：</p>

<ul>
	<li><code>horizontalCut</code> 的大小为&nbsp;<code>m - 1</code>&nbsp;，其中&nbsp;<code>horizontalCut[i]</code>&nbsp;表示沿着水平线 <code>i</code>&nbsp;切蛋糕的开销。</li>
	<li><code>verticalCut</code> 的大小为&nbsp;<code>n - 1</code>&nbsp;，其中&nbsp;<code>verticalCut[j]</code>&nbsp;表示沿着垂直线&nbsp;<code>j</code>&nbsp;切蛋糕的开销。</li>
</ul>

<p>一次操作中，你可以选择任意不是&nbsp;<code>1 x 1</code>&nbsp;大小的矩形蛋糕并执行以下操作之一：</p>

<ol>
	<li>沿着水平线&nbsp;<code>i</code>&nbsp;切开蛋糕，开销为&nbsp;<code>horizontalCut[i]</code>&nbsp;。</li>
	<li>沿着垂直线&nbsp;<code>j</code>&nbsp;切开蛋糕，开销为&nbsp;<code>verticalCut[j]</code>&nbsp;。</li>
</ol>

<p>每次操作后，这块蛋糕都被切成两个独立的小蛋糕。</p>

<p>每次操作的开销都为最开始对应切割线的开销，并且不会改变。</p>

<p>请你返回将蛋糕全部切成&nbsp;<code>1 x 1</code>&nbsp;的蛋糕块的&nbsp;<strong>最小</strong>&nbsp;总开销。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]</span></p>

<p><span class="example-io"><b>输出：</b>13</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/04/ezgifcom-animated-gif-maker-1.gif" style="width: 280px; height: 320px;" /></p>

<ul>
	<li>沿着垂直线 0 切开蛋糕，开销为 5 。</li>
	<li>沿着水平线 0 切开&nbsp;<code>3 x 1</code>&nbsp;的蛋糕块，开销为 1 。</li>
	<li>沿着水平线 0 切开 <code>3 x 1</code>&nbsp;的蛋糕块，开销为 1 。</li>
	<li>沿着水平线 1 切开 <code>2 x 1</code>&nbsp;的蛋糕块，开销为 3 。</li>
	<li>沿着水平线 1 切开 <code>2 x 1</code>&nbsp;的蛋糕块，开销为 3 。</li>
</ul>

<p>总开销为&nbsp;<code>5 + 1 + 1 + 3 + 3 = 13</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>m = 2, n = 2, horizontalCut = [7], verticalCut = [4]</span></p>

<p><span class="example-io"><b>输出：</b>15</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>沿着水平线 0 切开蛋糕，开销为 7 。</li>
	<li>沿着垂直线 0 切开&nbsp;<code>1 x 2</code>&nbsp;的蛋糕块，开销为 4 。</li>
	<li>沿着垂直线 0 切开&nbsp;<code>1 x 2</code>&nbsp;的蛋糕块，开销为 4 。</li>
</ul>

<p>总开销为&nbsp;<code>7 + 4 + 4 = 15</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 20</code></li>
	<li><code>horizontalCut.length == m - 1</code></li>
	<li><code>verticalCut.length == n - 1</code></li>
	<li><code>1 &lt;= horizontalCut[i], verticalCut[i] &lt;= 10<sup>3</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划
- 排序

## 提示

1. The intended solution uses Dynamic Programming.
2. Let <code>dp[sx][sy][tx][ty]</code> denote the minimum cost to cut the rectangle into <code>1 x 1</code> pieces.
3. Iterate on the row or column on which you will perform the next cut, after the cut, the current rectangle will be decomposed into two sub-rectangles.

## 示例

```
3
2
[1,3]
[5]
2
2
[7]
[4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumCost(int m, int n, vector<int>& horizontalCut, vector<int>& verticalCut) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
```

### C

```c
int minimumCost(int m, int n, int* horizontalCut, int horizontalCutSize, int* verticalCut, int verticalCutSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[]} horizontalCut
 * @param {number[]} verticalCut
 * @return {number}
 */
var minimumCost = function(m, n, horizontalCut, verticalCut) {
    
};
```

### TypeScript

```typescript
function minimumCost(m: number, n: number, horizontalCut: number[], verticalCut: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[] $horizontalCut
     * @param Integer[] $verticalCut
     * @return Integer
     */
    function minimumCost($m, $n, $horizontalCut, $verticalCut) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ m: Int, _ n: Int, _ horizontalCut: [Int], _ verticalCut: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(m: Int, n: Int, horizontalCut: IntArray, verticalCut: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(int m, int n, List<int> horizontalCut, List<int> verticalCut) {
    
  }
}
```

### Go

```golang
func minimumCost(m int, n int, horizontalCut []int, verticalCut []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} horizontal_cut
# @param {Integer[]} vertical_cut
# @return {Integer}
def minimum_cost(m, n, horizontal_cut, vertical_cut)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(m: Int, n: Int, horizontalCut: Array[Int], verticalCut: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(m: i32, n: i32, horizontal_cut: Vec<i32>, vertical_cut: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost m n horizontalCut verticalCut)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(M :: integer(), N :: integer(), HorizontalCut :: [integer()], VerticalCut :: [integer()]) -> integer().
minimum_cost(M, N, HorizontalCut, VerticalCut) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(m :: integer, n :: integer, horizontal_cut :: [integer], vertical_cut :: [integer]) :: integer
  def minimum_cost(m, n, horizontal_cut, vertical_cut) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(m: Int64, n: Int64, horizontalCut: Array<Int64>, verticalCut: Array<Int64>): Int64 {

    }
}
```

