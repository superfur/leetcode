# 566. 重塑矩阵

## 题目描述

<p>在 MATLAB 中，有一个非常有用的函数 <code>reshape</code> ，它可以将一个&nbsp;<code>m x n</code> 矩阵重塑为另一个大小不同（<code>r x c</code>）的新矩阵，但保留其原始数据。</p>

<p>给你一个由二维数组 <code>mat</code> 表示的&nbsp;<code>m x n</code> 矩阵，以及两个正整数 <code>r</code> 和 <code>c</code> ，分别表示想要的重构的矩阵的行数和列数。</p>

<p>重构后的矩阵需要将原始矩阵的所有元素以相同的<strong> 行遍历顺序 </strong>填充。</p>

<p>如果具有给定参数的 <code>reshape</code> 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg" style="width: 613px; height: 173px;" />
<pre>
<strong>输入：</strong>mat = [[1,2],[3,4]], r = 1, c = 4
<strong>输出：</strong>[[1,2,3,4]]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg" style="width: 453px; height: 173px;" />
<pre>
<strong>输入：</strong>mat = [[1,2],[3,4]], r = 2, c = 4
<strong>输出：</strong>[[1,2],[3,4]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-1000 &lt;= mat[i][j] &lt;= 1000</code></li>
	<li><code>1 &lt;= r, c &lt;= 300</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵
- 模拟

## 提示

1. Do you know how 2d matrix is stored in 1d memory? Try to map 2-dimensions into one.
2. M[i][j]=M[n*i+j] , where n is the number of cols. 
This is the one way of converting 2-d indices into one 1-d index.  
Now, how will you convert 1-d index into 2-d indices?
3. Try to use division and modulus to convert 1-d index into 2-d indices.
4. M[i] =>  M[i/n][i%n] Will it result in right mapping? Take some example and check this formula.

## 示例

```
[[1,2],[3,4]]
1
4
[[1,2],[3,4]]
2
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] MatrixReshape(int[][] mat, int r, int c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
    
};
```

### TypeScript

```typescript
function matrixReshape(mat: number[][], r: number, c: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $r
     * @param Integer $c
     * @return Integer[][]
     */
    function matrixReshape($mat, $r, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func matrixReshape(_ mat: [[Int]], _ r: Int, _ c: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun matrixReshape(mat: Array<IntArray>, r: Int, c: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> matrixReshape(List<List<int>> mat, int r, int c) {
    
  }
}
```

### Go

```golang
func matrixReshape(mat [][]int, r int, c int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer} r
# @param {Integer} c
# @return {Integer[][]}
def matrix_reshape(mat, r, c)
    
end
```

### Scala

```scala
object Solution {
    def matrixReshape(mat: Array[Array[Int]], r: Int, c: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn matrix_reshape(mat: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (matrix-reshape mat r c)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec matrix_reshape(Mat :: [[integer()]], R :: integer(), C :: integer()) -> [[integer()]].
matrix_reshape(Mat, R, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec matrix_reshape(mat :: [[integer]], r :: integer, c :: integer) :: [[integer]]
  def matrix_reshape(mat, r, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func matrixReshape(mat: Array<Array<Int64>>, r: Int64, c: Int64): Array<Array<Int64>> {

    }
}
```

