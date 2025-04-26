# 688. 骑士在棋盘上的概率

## 题目描述

<p>在一个&nbsp;<code>n x n</code>&nbsp;的国际象棋棋盘上，一个骑士从单元格 <code>(row, column)</code>&nbsp;开始，并尝试进行 <code>k</code> 次移动。行和列是 <strong>从 0 开始</strong> 的，所以左上单元格是 <code>(0,0)</code> ，右下单元格是 <code>(n - 1, n - 1)</code> 。</p>

<p>象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/knight.png" style="height: 300px; width: 300px;" /></p>

<p>每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。</p>

<p>骑士继续移动，直到它走了 <code>k</code> 步或离开了棋盘。</p>

<p>返回 <em>骑士在棋盘停止移动后仍留在棋盘上的概率</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> n = 3, k = 2, row = 0, column = 0
<strong>输出:</strong> 0.0625
<strong>解释:</strong> 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> n = 1, k = 0, row = 0, column = 0
<strong>输出:</strong> 1.00000
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 25</code></li>
	<li><code>0 &lt;= k &lt;= 100</code></li>
	<li><code>0 &lt;= row, column &lt;= n - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 示例

```
3
2
0
0
1
0
0
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        
    }
};
```

### Java

```java
class Solution {
    public double knightProbability(int n, int k, int row, int column) {
        
    }
}
```

### Python

```python
class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
```

### C

```c
double knightProbability(int n, int k, int row, int column) {
    
}
```

### C#

```csharp
public class Solution {
    public double KnightProbability(int n, int k, int row, int column) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} row
 * @param {number} column
 * @return {number}
 */
var knightProbability = function(n, k, row, column) {
    
};
```

### TypeScript

```typescript
function knightProbability(n: number, k: number, row: number, column: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $row
     * @param Integer $column
     * @return Float
     */
    function knightProbability($n, $k, $row, $column) {
        
    }
}
```

### Swift

```swift
class Solution {
    func knightProbability(_ n: Int, _ k: Int, _ row: Int, _ column: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun knightProbability(n: Int, k: Int, row: Int, column: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double knightProbability(int n, int k, int row, int column) {
    
  }
}
```

### Go

```golang
func knightProbability(n int, k int, row int, column int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @param {Integer} row
# @param {Integer} column
# @return {Float}
def knight_probability(n, k, row, column)
    
end
```

### Scala

```scala
object Solution {
    def knightProbability(n: Int, k: Int, row: Int, column: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn knight_probability(n: i32, k: i32, row: i32, column: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (knight-probability n k row column)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec knight_probability(N :: integer(), K :: integer(), Row :: integer(), Column :: integer()) -> float().
knight_probability(N, K, Row, Column) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec knight_probability(n :: integer, k :: integer, row :: integer, column :: integer) :: float
  def knight_probability(n, k, row, column) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func knightProbability(n: Int64, k: Int64, row: Int64, column: Int64): Float64 {

    }
}
```

