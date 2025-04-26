# 1632. 矩阵转换后的秩

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的矩阵 <code>matrix</code>&nbsp;，请你返回一个新的矩阵<em>&nbsp;</em><code>answer</code>&nbsp;，其中<em>&nbsp;</em><code>answer[row][col]</code>&nbsp;是&nbsp;<code>matrix[row][col]</code>&nbsp;的秩。</p>

<p>每个元素的&nbsp;<b>秩</b>&nbsp;是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：</p>

<ul>
	<li>秩是从 1 开始的一个整数。</li>
	<li>如果两个元素&nbsp;<code>p</code> 和&nbsp;<code>q</code>&nbsp;在 <strong>同一行</strong>&nbsp;或者 <strong>同一列</strong>&nbsp;，那么：
	<ul>
		<li>如果&nbsp;<code>p &lt; q</code> ，那么&nbsp;<code>rank(p) &lt; rank(q)</code></li>
		<li>如果&nbsp;<code>p == q</code>&nbsp;，那么&nbsp;<code>rank(p) == rank(q)</code></li>
		<li>如果&nbsp;<code>p &gt; q</code>&nbsp;，那么&nbsp;<code>rank(p) &gt; rank(q)</code></li>
	</ul>
	</li>
	<li><b>秩</b>&nbsp;需要越 <strong>小</strong>&nbsp;越好。</li>
</ul>

<p>题目保证按照上面规则&nbsp;<code>answer</code>&nbsp;数组是唯一的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/rank1.jpg" style="width: 442px; height: 162px;" />
<pre>
<b>输入：</b>matrix = [[1,2],[3,4]]
<b>输出：</b>[[1,2],[2,3]]
<strong>解释：</strong>
matrix[0][0] 的秩为 1 ，因为它是所在行和列的最小整数。
matrix[0][1] 的秩为 2 ，因为 matrix[0][1] &gt; matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][0] 的秩为 2 ，因为 matrix[1][0] &gt; matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][1] 的秩为 3 ，因为 matrix[1][1] &gt; matrix[0][1]， matrix[1][1] &gt; matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的秩都为 2 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/rank2.jpg" style="width: 442px; height: 162px;" />
<pre>
<b>输入：</b>matrix = [[7,7],[7,7]]
<b>输出：</b>[[1,1],[1,1]]
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/rank3.jpg" style="width: 601px; height: 322px;" />
<pre>
<b>输入：</b>matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
<b>输出：</b>[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[row][col] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 并查集
- 图
- 拓扑排序
- 数组
- 矩阵
- 排序

## 提示

1. Sort the cells by value and process them in increasing order.
2. The rank of a cell is the maximum rank in its row and column plus one.
3. Handle the equal cells by treating them as components using a union-find data structure.

## 示例

```
[[1,2],[3,4]]
[[7,7],[7,7]]
[[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] matrixRankTransform(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixRankTransform(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] MatrixRankTransform(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var matrixRankTransform = function(matrix) {
    
};
```

### TypeScript

```typescript
function matrixRankTransform(matrix: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function matrixRankTransform($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func matrixRankTransform(_ matrix: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun matrixRankTransform(matrix: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> matrixRankTransform(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func matrixRankTransform(matrix [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer[][]}
def matrix_rank_transform(matrix)
    
end
```

### Scala

```scala
object Solution {
    def matrixRankTransform(matrix: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn matrix_rank_transform(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (matrix-rank-transform matrix)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec matrix_rank_transform(Matrix :: [[integer()]]) -> [[integer()]].
matrix_rank_transform(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec matrix_rank_transform(matrix :: [[integer]]) :: [[integer]]
  def matrix_rank_transform(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func matrixRankTransform(matrix: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

