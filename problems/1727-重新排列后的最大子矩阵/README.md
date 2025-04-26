# 1727. 重新排列后的最大子矩阵

## 题目描述

<p>给你一个二进制矩阵 <code>matrix</code> ，它的大小为 <code>m x n</code> ，你可以将 <code>matrix</code> 中的 <strong>列</strong> 按任意顺序重新排列。</p>

<p>请你返回最优方案下将 <code>matrix</code> 重新排列后，全是 <code>1</code> 的子矩阵面积。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/screenshot-2020-12-30-at-40536-pm.png" style="width: 300px; height: 144px;" /></strong></p>

<pre>
<b>输入：</b>matrix = [[0,0,1],[1,1,1],[1,0,1]]
<b>输出：</b>4
<b>解释：</b>你可以按照上图方式重新排列矩阵的每一列。
最大的全 1 子矩阵是上图中加粗的部分，面积为 4 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/screenshot-2020-12-30-at-40852-pm.png" style="width: 500px; height: 62px;" /></p>

<pre>
<b>输入：</b>matrix = [[1,0,1,0,1]]
<b>输出：</b>3
<b>解释：</b>你可以按照上图方式重新排列矩阵的每一列。
最大的全 1 子矩阵是上图中加粗的部分，面积为 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>matrix = [[1,1,0],[1,0,1]]
<b>输出：</b>2
<b>解释：</b>由于你只能整列整列重新排布，所以没有比面积为 2 更大的全 1 子矩形。</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>matrix = [[0,0],[0,0]]
<b>输出：</b>0
<b>解释：</b>由于矩阵中没有 1 ，没有任何全 1 的子矩阵，所以面积为 0 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m * n <= 10<sup>5</sup></code></li>
	<li><code>matrix[i][j]</code> 要么是 <code>0</code> ，要么是 <code>1</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 矩阵
- 排序

## 提示

1. For each column, find the number of consecutive ones ending at each position.
2. For each row, sort the cumulative ones in non-increasing order and "fit" the largest submatrix.

## 示例

```
[[0,0,1],[1,1,1],[1,0,1]]
[[1,0,1,0,1]]
[[1,1,0],[1,0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestSubmatrix(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
```

### C

```c
int largestSubmatrix(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestSubmatrix(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var largestSubmatrix = function(matrix) {
    
};
```

### TypeScript

```typescript
function largestSubmatrix(matrix: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function largestSubmatrix($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestSubmatrix(_ matrix: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestSubmatrix(matrix: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestSubmatrix(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func largestSubmatrix(matrix [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer}
def largest_submatrix(matrix)
    
end
```

### Scala

```scala
object Solution {
    def largestSubmatrix(matrix: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-submatrix matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_submatrix(Matrix :: [[integer()]]) -> integer().
largest_submatrix(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_submatrix(matrix :: [[integer]]) :: integer
  def largest_submatrix(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestSubmatrix(matrix: Array<Array<Int64>>): Int64 {

    }
}
```

