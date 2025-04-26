# 3033. 修改矩阵

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>m x n</code> 的整数矩阵 <code>matrix</code> ，新建一个下标从 <strong>0</strong> 开始、名为 <code>answer</code> 的矩阵。使 <code>answer</code> 与 <code>matrix</code> 相等，接着将其中每个值为 <code>-1</code> 的元素替换为所在列的 <strong>最大</strong> 元素。</p>

<p>返回矩阵 <code>answer</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/24/matrix1.png" style="width: 491px; height: 161px;" />
<pre>
<strong>输入：</strong>matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
<strong>输出：</strong>[[1,2,9],[4,8,6],[7,8,9]]
<strong>解释：</strong>上图显示了发生替换的元素（蓝色区域）。
- 将单元格 [1][1] 中的值替换为列 1 中的最大值 8 。
- 将单元格 [0][2] 中的值替换为列 2 中的最大值 9 。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/24/matrix2.png" style="width: 411px; height: 111px;" />
<pre>
<strong>输入：</strong>matrix = [[3,-1],[5,2]]
<strong>输出：</strong>[[3,2],[5,2]]
<strong>解释：</strong>上图显示了发生替换的元素（蓝色区域）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 50</code></li>
	<li><code>-1 &lt;= matrix[i][j] &lt;= 100</code></li>
	<li>测试用例中生成的输入满足每列至少包含一个非负整数。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 示例

```
[[1,2,-1],[4,-1,6],[7,8,9]]
[[3,-1],[5,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> modifiedMatrix(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** modifiedMatrix(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] ModifiedMatrix(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var modifiedMatrix = function(matrix) {
    
};
```

### TypeScript

```typescript
function modifiedMatrix(matrix: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function modifiedMatrix($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func modifiedMatrix(_ matrix: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun modifiedMatrix(matrix: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> modifiedMatrix(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func modifiedMatrix(matrix [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer[][]}
def modified_matrix(matrix)
    
end
```

### Scala

```scala
object Solution {
    def modifiedMatrix(matrix: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn modified_matrix(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (modified-matrix matrix)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec modified_matrix(Matrix :: [[integer()]]) -> [[integer()]].
modified_matrix(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec modified_matrix(matrix :: [[integer]]) :: [[integer]]
  def modified_matrix(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func modifiedMatrix(matrix: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

