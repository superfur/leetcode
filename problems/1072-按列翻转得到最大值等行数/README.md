# 1072. 按列翻转得到最大值等行数

## 题目描述

<p>给定&nbsp;<code>m x n</code>&nbsp;矩阵&nbsp;<code>matrix</code>&nbsp;。</p>

<p>你可以从中选出任意数量的列并翻转其上的&nbsp;<strong>每个&nbsp;</strong>单元格。（即翻转后，单元格的值从 <code>0</code> 变成 <code>1</code>，或者从 <code>1</code> 变为 <code>0</code> 。）</p>

<p>返回 <em>经过一些翻转后，行内所有值都相等的最大行数</em>&nbsp;。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[0,1],[1,1]]
<strong>输出：</strong>1
<strong>解释：</strong>不进行翻转，有 1 行所有值都相等。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[0,1],[1,0]]
<strong>输出：</strong>2
<strong>解释：</strong>翻转第一列的值之后，这两行都由相等的值组成。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[0,0,0],[0,0,1],[1,1,0]]
<strong>输出：</strong>2
<strong>解释：</strong>翻转前两列的值之后，后两行由相等的值组成。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>matrix[i][j] == 0</code> 或&nbsp;<code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 矩阵

## 提示

1. Flipping a subset of columns is like doing a bitwise XOR of some number K onto each row.  We want rows X with X ^ K = all 0s or all 1s.  This is the same as X = X^K ^K = (all 0s or all 1s) ^ K, so we want to count rows that have opposite bits set.  For example, if K = 1, then we count rows X = (00000...001, or 1111....110).

## 示例

```
[[0,1],[1,1]]
[[0,1],[1,0]]
[[0,0,0],[0,0,1],[1,1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
```

### C

```c
int maxEqualRowsAfterFlips(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxEqualRowsAfterFlips(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxEqualRowsAfterFlips = function(matrix) {
    
};
```

### TypeScript

```typescript
function maxEqualRowsAfterFlips(matrix: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function maxEqualRowsAfterFlips($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxEqualRowsAfterFlips(_ matrix: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxEqualRowsAfterFlips(matrix: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxEqualRowsAfterFlips(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func maxEqualRowsAfterFlips(matrix [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer}
def max_equal_rows_after_flips(matrix)
    
end
```

### Scala

```scala
object Solution {
    def maxEqualRowsAfterFlips(matrix: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_equal_rows_after_flips(matrix: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-equal-rows-after-flips matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_equal_rows_after_flips(Matrix :: [[integer()]]) -> integer().
max_equal_rows_after_flips(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_equal_rows_after_flips(matrix :: [[integer]]) :: integer
  def max_equal_rows_after_flips(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxEqualRowsAfterFlips(matrix: Array<Array<Int64>>): Int64 {

    }
}
```

