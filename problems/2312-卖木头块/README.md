# 2312. 卖木头块

## 题目描述

<p>给你两个整数&nbsp;<code>m</code> 和&nbsp;<code>n</code>&nbsp;，分别表示一块矩形木块的高和宽。同时给你一个二维整数数组&nbsp;<code>prices</code>&nbsp;，其中&nbsp;<code>prices[i] = [h<sub>i</sub>, w<sub>i</sub>, price<sub>i</sub>]</code>&nbsp;表示你可以以&nbsp;<code>price<sub>i</sub></code>&nbsp;元的价格卖一块高为&nbsp;<code>h<sub>i</sub></code>&nbsp;宽为&nbsp;<code>w<sub>i</sub></code>&nbsp;的矩形木块。</p>

<p>每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：</p>

<ul>
	<li>沿垂直方向按高度 <strong>完全</strong> 切割木块，或</li>
	<li>沿水平方向按宽度 <strong>完全</strong> 切割木块</li>
</ul>

<p>在将一块木块切成若干小木块后，你可以根据 <code>prices</code>&nbsp;卖木块。你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。你 <strong>不能</strong>&nbsp;旋转切好后木块来交换它的高度值和宽度值。</p>

<p>请你返回切割一块大小为<em>&nbsp;</em><code>m x n</code><em> </em>的木块后，能得到的&nbsp;<strong>最多</strong>&nbsp;钱数。</p>

<p>注意你可以切割木块任意次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/04/27/ex1.png" style="width: 239px; height: 150px;" /></p>

<pre>
<b>输入：</b>m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
<b>输出：</b>19
<b>解释：</b>上图展示了一个可行的方案。包括：
- 2 块 2 x 2 的小木块，售出 2 * 7 = 14 元。
- 1 块 2 x 1 的小木块，售出 1 * 3 = 3 元。
- 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
总共售出 14 + 3 + 2 = 19 元。
19 元是最多能得到的钱数。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/04/27/ex2new.png" style="width: 250px; height: 175px;" /></p>

<pre>
<b>输入：</b>m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
<b>输出：</b>32
<b>解释：</b>上图展示了一个可行的方案。包括：
- 3 块 3 x 2 的小木块，售出 3 * 10 = 30 元。
- 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
总共售出 30 + 2 = 32 元。
32 元是最多能得到的钱数。
注意我们不能旋转 1 x 4 的木块来得到 4 x 1 的木块。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= prices.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>prices[i].length == 3</code></li>
	<li><code>1 &lt;= h<sub>i</sub> &lt;= m</code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= n</code></li>
	<li><code>1 &lt;= price<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>所有&nbsp;<code>(h<sub>i</sub>, w<sub>i</sub>)</code> <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 数组
- 动态规划

## 提示

1. Note down the different actions that can be done on a piece of wood with dimensions m x n. What do you notice?
2. If possible, we could sell the m x n piece. We could also cut the piece vertically creating two pieces of size m x n1 and m x n2 where n1 + n2 = n, or horizontally creating two pieces of size m1 x n and m2 x n where m1 + m2 = m.
3. Notice that cutting a piece breaks the problem down into smaller subproblems, and selling the piece when available is also a case that terminates the process. Thus, we can use DP to efficiently solve this.

## 示例

```
3
5
[[1,4,2],[2,2,7],[2,1,3]]
4
6
[[3,2,10],[1,4,2],[4,1,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long sellingWood(int m, int n, vector<vector<int>>& prices) {
        
    }
};
```

### Java

```java
class Solution {
    public long sellingWood(int m, int n, int[][] prices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        
```

### C

```c
long long sellingWood(int m, int n, int** prices, int pricesSize, int* pricesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long SellingWood(int m, int n, int[][] prices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} prices
 * @return {number}
 */
var sellingWood = function(m, n, prices) {
    
};
```

### TypeScript

```typescript
function sellingWood(m: number, n: number, prices: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $prices
     * @return Integer
     */
    function sellingWood($m, $n, $prices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sellingWood(_ m: Int, _ n: Int, _ prices: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sellingWood(m: Int, n: Int, prices: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int sellingWood(int m, int n, List<List<int>> prices) {
    
  }
}
```

### Go

```golang
func sellingWood(m int, n int, prices [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} prices
# @return {Integer}
def selling_wood(m, n, prices)
    
end
```

### Scala

```scala
object Solution {
    def sellingWood(m: Int, n: Int, prices: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn selling_wood(m: i32, n: i32, prices: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (selling-wood m n prices)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec selling_wood(M :: integer(), N :: integer(), Prices :: [[integer()]]) -> integer().
selling_wood(M, N, Prices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec selling_wood(m :: integer, n :: integer, prices :: [[integer]]) :: integer
  def selling_wood(m, n, prices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sellingWood(m: Int64, n: Int64, prices: Array<Array<Int64>>): Int64 {

    }
}
```

