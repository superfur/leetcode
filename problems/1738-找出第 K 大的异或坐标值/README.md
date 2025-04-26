# 1738. 找出第 K 大的异或坐标值

## 题目描述

<p>给你一个二维矩阵 <code>matrix</code> 和一个整数 <code>k</code> ，矩阵大小为&nbsp;<code>m x n</code> 由非负整数组成。</p>

<p>矩阵中坐标 <code>(a, b)</code> 的 <strong>目标值</strong>&nbsp;可以通过对所有元素 <code>matrix[i][j]</code>&nbsp;执行异或运算得到，其中&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code> 满足 <code>0 &lt;= i &lt;= a &lt; m</code> 且 <code>0 &lt;= j &lt;= b &lt; n</code>（<strong>下标从 0 开始计数</strong>）。</p>

<p>请你找出&nbsp;<code>matrix</code> 的所有坐标中第 <code>k</code> 大的目标值（<strong><code>k</code> 的值从 1 开始计数</strong>）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[5,2],[1,6]], k = 1
<strong>输出：</strong>7
<strong>解释：</strong>坐标 (0,1) 的目标值是 5 XOR 2 = 7 ，为最大的目标值。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[5,2],[1,6]], k = 2
<strong>输出：</strong>5
<strong>解释：</strong>坐标 (0,0) 的目标值是 5 = 5 ，为第 2 大的目标值。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[5,2],[1,6]], k = 3
<strong>输出：</strong>4
<strong>解释：</strong>坐标 (1,0) 的目标值是 5 XOR 1 = 4 ，为第 3 大的目标值。</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[5,2],[1,6]], k = 4
<strong>输出：</strong>0
<strong>解释：</strong>坐标 (1,1) 的目标值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的目标值。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>0 &lt;= matrix[i][j] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= m * n</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 分治
- 矩阵
- 前缀和
- 快速选择
- 排序
- 堆（优先队列）

## 提示

1. Use a 2D prefix sum to precalculate the xor-sum of the upper left submatrix.

## 示例

```
[[5,2],[1,6]]
1
[[5,2],[1,6]]
2
[[5,2],[1,6]]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kthLargestValue(int[][] matrix, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
```

### C

```c
int kthLargestValue(int** matrix, int matrixSize, int* matrixColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KthLargestValue(int[][] matrix, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthLargestValue = function(matrix, k) {
    
};
```

### TypeScript

```typescript
function kthLargestValue(matrix: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function kthLargestValue($matrix, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthLargestValue(_ matrix: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthLargestValue(matrix: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kthLargestValue(List<List<int>> matrix, int k) {
    
  }
}
```

### Go

```golang
func kthLargestValue(matrix [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @param {Integer} k
# @return {Integer}
def kth_largest_value(matrix, k)
    
end
```

### Scala

```scala
object Solution {
    def kthLargestValue(matrix: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_largest_value(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (kth-largest-value matrix k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec kth_largest_value(Matrix :: [[integer()]], K :: integer()) -> integer().
kth_largest_value(Matrix, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_largest_value(matrix :: [[integer]], k :: integer) :: integer
  def kth_largest_value(matrix, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthLargestValue(matrix: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

