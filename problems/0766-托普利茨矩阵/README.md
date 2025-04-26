# 766. 托普利茨矩阵

## 题目描述

<p>给你一个 <code>m x n</code> 的矩阵 <code>matrix</code> 。如果这个矩阵是托普利茨矩阵，返回 <code>true</code> ；否则，返回<em> </em><code>false</code><em> 。</em></p>

<p>如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是<em> </em><strong>托普利茨矩阵</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
<strong>输出：</strong>true
<strong>解释：</strong>
在上述矩阵中, 其对角线为: 
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。 
各条对角线上的所有元素均相同, 因此答案是 True 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>输入：</strong>matrix = [[1,2],[2,2]]
<strong>输出：</strong>false
<strong>解释：</strong>
对角线 "[1, 2]" 上的元素不同。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 20</code></li>
	<li><code>0 <= matrix[i][j] <= 99</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong></p>

<ul>
	<li>如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？</li>
	<li>如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Check whether each value is equal to the value of it's top-left neighbor.

## 示例

```
[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
[[1,2],[2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
```

### C

```c
bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsToeplitzMatrix(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function(matrix) {
    
};
```

### TypeScript

```typescript
function isToeplitzMatrix(matrix: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Boolean
     */
    function isToeplitzMatrix($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isToeplitzMatrix(matrix: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isToeplitzMatrix(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func isToeplitzMatrix(matrix [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Boolean}
def is_toeplitz_matrix(matrix)
    
end
```

### Scala

```scala
object Solution {
    def isToeplitzMatrix(matrix: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_toeplitz_matrix(matrix: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-toeplitz-matrix matrix)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec is_toeplitz_matrix(Matrix :: [[integer()]]) -> boolean().
is_toeplitz_matrix(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_toeplitz_matrix(matrix :: [[integer]]) :: boolean
  def is_toeplitz_matrix(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isToeplitzMatrix(matrix: Array<Array<Int64>>): Bool {

    }
}
```

