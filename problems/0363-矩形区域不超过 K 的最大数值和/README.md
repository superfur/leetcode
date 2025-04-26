# 363. 矩形区域不超过 K 的最大数值和

## 题目描述

<p>给你一个 <code>m x n</code> 的矩阵 <code>matrix</code> 和一个整数 <code>k</code> ，找出并返回矩阵内部矩形区域的不超过 <code>k</code> 的最大数值和。</p>

<p>题目数据保证总会存在一个数值和不超过 <code>k</code> 的矩形区域。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg" style="width: 255px; height: 176px;" />
<pre>
<strong>输入：</strong>matrix = [[1,0,1],[0,-2,3]], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>蓝色边框圈出来的矩形区域 <code>[[0, 1], [-2, 3]]</code> 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[2,2,-1]], k = 3
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 100</code></li>
	<li><code>-100 <= matrix[i][j] <= 100</code></li>
	<li><code>-10<sup>5</sup> <= k <= 10<sup>5</sup></code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>如果行数远大于列数，该如何设计解决方案？</p>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 矩阵
- 有序集合
- 前缀和

## 示例

```
[[1,0,1],[0,-2,3]]
2
[[2,2,-1]]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
```

### C

```c
int maxSumSubmatrix(int** matrix, int matrixSize, int* matrixColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSumSubmatrix(int[][] matrix, int k) {
        
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
var maxSumSubmatrix = function(matrix, k) {
    
};
```

### TypeScript

```typescript
function maxSumSubmatrix(matrix: number[][], k: number): number {
    
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
    function maxSumSubmatrix($matrix, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSumSubmatrix(_ matrix: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSumSubmatrix(matrix: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSumSubmatrix(List<List<int>> matrix, int k) {
    
  }
}
```

### Go

```golang
func maxSumSubmatrix(matrix [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @param {Integer} k
# @return {Integer}
def max_sum_submatrix(matrix, k)
    
end
```

### Scala

```scala
object Solution {
    def maxSumSubmatrix(matrix: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum_submatrix(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum-submatrix matrix k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum_submatrix(Matrix :: [[integer()]], K :: integer()) -> integer().
max_sum_submatrix(Matrix, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum_submatrix(matrix :: [[integer]], k :: integer) :: integer
  def max_sum_submatrix(matrix, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSumSubmatrix(matrix: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

