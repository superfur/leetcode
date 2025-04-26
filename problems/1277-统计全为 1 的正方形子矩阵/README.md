# 1277. 统计全为 1 的正方形子矩阵

## 题目描述

<p>给你一个&nbsp;<code>m * n</code>&nbsp;的矩阵，矩阵中的元素不是 <code>0</code> 就是 <code>1</code>，请你统计并返回其中完全由 <code>1</code> 组成的 <strong>正方形</strong> 子矩阵的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>matrix =
[
&nbsp; [0,1,1,1],
&nbsp; [1,1,1,1],
&nbsp; [0,1,1,1]
]
<strong>输出：</strong>15
<strong>解释：</strong> 
边长为 1 的正方形有 <strong>10</strong> 个。
边长为 2 的正方形有 <strong>4</strong> 个。
边长为 3 的正方形有 <strong>1</strong> 个。
正方形的总数 = 10 + 4 + 1 = <strong>15</strong>.
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
<strong>输出：</strong>7
<strong>解释：</strong>
边长为 1 的正方形有 <strong>6</strong> 个。 
边长为 2 的正方形有 <strong>1</strong> 个。
正方形的总数 = 6 + 1 = <strong>7</strong>.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 300</code></li>
	<li><code>1 &lt;= arr[0].length&nbsp;&lt;= 300</code></li>
	<li><code>0 &lt;= arr[i][j] &lt;= 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Create an additive table that counts the sum of elements of submatrix with the superior corner at (0,0).
2. Loop over all subsquares in O(n^3) and check if the sum make the whole array to be ones, if it checks then add 1 to the answer.

## 示例

```
[[0,1,1,1],[1,1,1,1],[0,1,1,1]]
[[1,0,1],[1,1,0],[1,1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSquares(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
```

### C

```c
int countSquares(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSquares(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
    
};
```

### TypeScript

```typescript
function countSquares(matrix: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function countSquares($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSquares(_ matrix: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSquares(matrix: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSquares(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func countSquares(matrix [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer}
def count_squares(matrix)
    
end
```

### Scala

```scala
object Solution {
    def countSquares(matrix: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_squares(matrix: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-squares matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_squares(Matrix :: [[integer()]]) -> integer().
count_squares(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_squares(matrix :: [[integer]]) :: integer
  def count_squares(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSquares(matrix: Array<Array<Int64>>): Int64 {

    }
}
```

