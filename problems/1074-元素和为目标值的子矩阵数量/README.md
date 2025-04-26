# 1074. 元素和为目标值的子矩阵数量

## 题目描述

<p>给出矩阵&nbsp;<code>matrix</code>&nbsp;和目标值&nbsp;<code>target</code>，返回元素总和等于目标值的非空子矩阵的数量。</p>

<p>子矩阵&nbsp;<code>x1, y1, x2, y2</code>&nbsp;是满足 <code>x1 &lt;= x &lt;= x2</code>&nbsp;且&nbsp;<code>y1 &lt;= y &lt;= y2</code>&nbsp;的所有单元&nbsp;<code>matrix[x][y]</code>&nbsp;的集合。</p>

<p>如果&nbsp;<code>(x1, y1, x2, y2)</code> 和&nbsp;<code>(x1', y1', x2', y2')</code>&nbsp;两个子矩阵中部分坐标不同（如：<code>x1 != x1'</code>），那么这两个子矩阵也不同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/mate1.jpg" style="width: 242px; height: 242px;" /></p>

<pre>
<strong>输入：</strong>matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
<strong>输出：</strong>4
<strong>解释：</strong>四个只含 0 的 1x1 子矩阵。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[1,-1],[-1,1]], target = 0
<strong>输出：</strong>5
<strong>解释：</strong>两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[904]], target = 0
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong><strong>提示：</strong></strong></p>

<ul>
	<li><code>1 &lt;= matrix.length &lt;= 100</code></li>
	<li><code>1 &lt;= matrix[0].length &lt;= 100</code></li>
	<li><code>-1000 &lt;= matrix[i][j] &lt;= 1000</code></li>
	<li><code>-10^8 &lt;= target &lt;= 10^8</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 矩阵
- 前缀和

## 提示

1. Using a 2D prefix sum, we can query the sum of any submatrix in O(1) time.
Now for each (r1, r2), we can find the largest sum of a submatrix that uses every row in [r1, r2] in linear time using a sliding window.

## 示例

```
[[0,1,0],[1,1,1],[0,1,0]]
0
[[1,-1],[-1,1]]
0
[[904]]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
```

### C

```c
int numSubmatrixSumTarget(int** matrix, int matrixSize, int* matrixColSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {number}
 */
var numSubmatrixSumTarget = function(matrix, target) {
    
};
```

### TypeScript

```typescript
function numSubmatrixSumTarget(matrix: number[][], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Integer
     */
    function numSubmatrixSumTarget($matrix, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSubmatrixSumTarget(_ matrix: [[Int]], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSubmatrixSumTarget(matrix: Array<IntArray>, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSubmatrixSumTarget(List<List<int>> matrix, int target) {
    
  }
}
```

### Go

```golang
func numSubmatrixSumTarget(matrix [][]int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Integer}
def num_submatrix_sum_target(matrix, target)
    
end
```

### Scala

```scala
object Solution {
    def numSubmatrixSumTarget(matrix: Array[Array[Int]], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-submatrix-sum-target matrix target)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_submatrix_sum_target(Matrix :: [[integer()]], Target :: integer()) -> integer().
num_submatrix_sum_target(Matrix, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_submatrix_sum_target(matrix :: [[integer]], target :: integer) :: integer
  def num_submatrix_sum_target(matrix, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSubmatrixSumTarget(matrix: Array<Array<Int64>>, target: Int64): Int64 {

    }
}
```

