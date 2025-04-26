# 764. 最大加号标志

## 题目描述

<p>在一个 <code>n x n</code> 的矩阵&nbsp;<code>grid</code>&nbsp;中，除了在数组&nbsp;<code>mines</code>&nbsp;中给出的元素为&nbsp;<code>0</code>，其他每个元素都为&nbsp;<code>1</code>。<code>mines[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>表示&nbsp;<code>grid[x<sub>i</sub>][y<sub>i</sub>] == 0</code></p>

<p>返回 <em>&nbsp;</em><code>grid</code><em> 中包含&nbsp;<code>1</code>&nbsp;的最大的 <strong>轴对齐</strong> 加号标志的阶数</em> 。如果未找到加号标志，则返回 <code>0</code> 。</p>

<p>一个&nbsp;<code>k</code>&nbsp;阶由&nbsp;<em><code>1</code></em>&nbsp;组成的 <strong>“轴对称”加号标志</strong> 具有中心网格&nbsp;<code>grid[r][c] == 1</code>&nbsp;，以及4个从中心向上、向下、向左、向右延伸，长度为&nbsp;<code>k-1</code>，由&nbsp;<code>1</code>&nbsp;组成的臂。注意，只有加号标志的所有网格要求为 <code>1</code> ，别的网格可能为 <code>0</code> 也可能为 <code>1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg" /></p>

<pre>
<strong>输入:</strong> n = 5, mines = [[4, 2]]
<strong>输出:</strong> 2
<strong>解释: </strong>在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/13/plus2-grid.jpg" /></p>

<pre>
<strong>输入:</strong> n = 1, mines = [[0, 0]]
<strong>输出:</strong> 0
<strong>解释: </strong>没有加号标志，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= mines.length &lt;= 5000</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt; n</code></li>
	<li>每一对&nbsp;<code>(x<sub>i</sub>, y<sub>i</sub>)</code>&nbsp;都 <strong>不重复</strong>​​​​​​​</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. For each direction such as "left", find left[r][c] = the number of 1s you will see before a zero starting at r, c and walking left.  You can find this in N^2 time with a dp.  The largest plus sign at r, c is just the minimum of left[r][c], up[r][c] etc.

## 示例

```
5
[[4,2]]
1
[[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        
    }
};
```

### Java

```java
class Solution {
    public int orderOfLargestPlusSign(int n, int[][] mines) {
        
    }
}
```

### Python

```python
class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
```

### C

```c
int orderOfLargestPlusSign(int n, int** mines, int minesSize, int* minesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int OrderOfLargestPlusSign(int n, int[][] mines) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} mines
 * @return {number}
 */
var orderOfLargestPlusSign = function(n, mines) {
    
};
```

### TypeScript

```typescript
function orderOfLargestPlusSign(n: number, mines: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $mines
     * @return Integer
     */
    function orderOfLargestPlusSign($n, $mines) {
        
    }
}
```

### Swift

```swift
class Solution {
    func orderOfLargestPlusSign(_ n: Int, _ mines: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun orderOfLargestPlusSign(n: Int, mines: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int orderOfLargestPlusSign(int n, List<List<int>> mines) {
    
  }
}
```

### Go

```golang
func orderOfLargestPlusSign(n int, mines [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} mines
# @return {Integer}
def order_of_largest_plus_sign(n, mines)
    
end
```

### Scala

```scala
object Solution {
    def orderOfLargestPlusSign(n: Int, mines: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn order_of_largest_plus_sign(n: i32, mines: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (order-of-largest-plus-sign n mines)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec order_of_largest_plus_sign(N :: integer(), Mines :: [[integer()]]) -> integer().
order_of_largest_plus_sign(N, Mines) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec order_of_largest_plus_sign(n :: integer, mines :: [[integer]]) :: integer
  def order_of_largest_plus_sign(n, mines) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func orderOfLargestPlusSign(n: Int64, mines: Array<Array<Int64>>): Int64 {

    }
}
```

