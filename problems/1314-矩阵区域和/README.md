# 1314. 矩阵区域和

## 题目描述

<p>给你一个 <code>m x n</code> 的矩阵 <code>mat</code> 和一个整数 <code>k</code> ，请你返回一个矩阵 <code>answer</code> ，其中每个 <code>answer[i][j]</code> 是所有满足下述条件的元素 <code>mat[r][c]</code> 的和： </p>

<ul>
	<li><code>i - k <= r <= i + k, </code></li>
	<li><code>j - k <= c <= j + k</code> 且</li>
	<li><code>(r, c)</code> 在矩阵内。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>输出：</strong>[[12,21,16],[27,45,33],[24,39,28]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
<strong>输出：</strong>[[45,45,45],[45,45,45],[45,45,45]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 <= m, n, k <= 100</code></li>
	<li><code>1 <= mat[i][j] <= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 前缀和

## 提示

1. How to calculate the required sum for a cell (i,j) fast ?
2. Use the concept of cumulative sum array.
3. Create a cumulative sum matrix where dp[i][j] is the sum of all cells in the rectangle from (0,0) to (i,j), use inclusion-exclusion idea.

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
1
[[1,2,3],[4,5,6],[7,8,9]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] matrixBlockSum(int[][] mat, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixBlockSum(int** mat, int matSize, int* matColSize, int k, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] MatrixBlockSum(int[][] mat, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[][]}
 */
var matrixBlockSum = function(mat, k) {
    
};
```

### TypeScript

```typescript
function matrixBlockSum(mat: number[][], k: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Integer[][]
     */
    function matrixBlockSum($mat, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func matrixBlockSum(_ mat: [[Int]], _ k: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun matrixBlockSum(mat: Array<IntArray>, k: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> matrixBlockSum(List<List<int>> mat, int k) {
    
  }
}
```

### Go

```golang
func matrixBlockSum(mat [][]int, k int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer} k
# @return {Integer[][]}
def matrix_block_sum(mat, k)
    
end
```

### Scala

```scala
object Solution {
    def matrixBlockSum(mat: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn matrix_block_sum(mat: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (matrix-block-sum mat k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec matrix_block_sum(Mat :: [[integer()]], K :: integer()) -> [[integer()]].
matrix_block_sum(Mat, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec matrix_block_sum(mat :: [[integer]], k :: integer) :: [[integer]]
  def matrix_block_sum(mat, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func matrixBlockSum(mat: Array<Array<Int64>>, k: Int64): Array<Array<Int64>> {

    }
}
```

