# 1975. 最大方阵和

## 题目描述

<p>给你一个&nbsp;<code>n x n</code>&nbsp;的整数方阵&nbsp;<code>matrix</code>&nbsp;。你可以执行以下操作&nbsp;<strong>任意次</strong>&nbsp;：</p>

<ul>
	<li>选择&nbsp;<code>matrix</code>&nbsp;中&nbsp;<strong>相邻</strong>&nbsp;两个元素，并将它们都 <strong>乘以</strong>&nbsp;<code>-1</code>&nbsp;。</li>
</ul>

<p>如果两个元素有 <strong>公共边</strong>&nbsp;，那么它们就是 <strong>相邻</strong>&nbsp;的。</p>

<p>你的目的是 <strong>最大化</strong>&nbsp;方阵元素的和。请你在执行以上操作之后，返回方阵的&nbsp;<strong>最大</strong>&nbsp;和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png" style="width: 401px; height: 81px;">
<pre><b>输入：</b>matrix = [[1,-1],[-1,1]]
<b>输出：</b>4
<b>解释：</b>我们可以执行以下操作使和等于 4 ：
- 将第一行的 2 个元素乘以 -1 。
- 将第一列的 2 个元素乘以 -1 。
</pre>

<p><strong>示例&nbsp;2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png" style="width: 321px; height: 121px;">
<pre><b>输入：</b>matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
<b>输出：</b>16
<b>解释：</b>我们可以执行以下操作使和等于 16 ：
- 将第二行的最后 2 个元素乘以 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 250</code></li>
	<li><code>-10<sup>5</sup> &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 矩阵

## 提示

1. Try to use the operation so that each row has only one negative number.
2. If you have only one negative element you cannot convert it to positive.

## 示例

```
[[1,-1],[-1,1]]
[[1,2,3],[-1,-2,-3],[1,2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxMatrixSum(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
```

### C

```c
long long maxMatrixSum(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxMatrixSum(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function(matrix) {
    
};
```

### TypeScript

```typescript
function maxMatrixSum(matrix: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function maxMatrixSum($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxMatrixSum(_ matrix: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxMatrixSum(matrix: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxMatrixSum(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func maxMatrixSum(matrix [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer}
def max_matrix_sum(matrix)
    
end
```

### Scala

```scala
object Solution {
    def maxMatrixSum(matrix: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-matrix-sum matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_matrix_sum(Matrix :: [[integer()]]) -> integer().
max_matrix_sum(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_matrix_sum(matrix :: [[integer]]) :: integer
  def max_matrix_sum(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxMatrixSum(matrix: Array<Array<Int64>>): Int64 {

    }
}
```

