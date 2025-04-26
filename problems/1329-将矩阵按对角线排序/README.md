# 1329. 将矩阵按对角线排序

## 题目描述

<p><strong>矩阵对角线</strong> 是一条从矩阵最上面行或者最左侧列中的某个元素开始的对角线，沿右下方向一直到矩阵末尾的元素。例如，矩阵 <code>mat</code> 有 <code>6</code> 行 <code>3</code> 列，从 <code>mat[2][0]</code> 开始的 <strong>矩阵对角线</strong> 将会经过 <code>mat[2][0]</code>、<code>mat[3][1]</code> 和 <code>mat[4][2]</code> 。</p>

<p>给你一个 <code>m * n</code> 的整数矩阵 <code>mat</code> ，请你将同一条 <strong>矩阵对角线 </strong>上的元素按升序排序后，返回排好序的矩阵。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/25/1482_example_1_2.png" style="height: 198px; width: 500px;" /></p>

<pre>
<strong>输入：</strong>mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
<strong>输出：</strong>[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
<strong>输出：</strong>[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 <= m, n <= 100</code></li>
	<li><code>1 <= mat[i][j] <= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 排序

## 提示

1. Use a data structure to store all values of each diagonal.
2. How to index the data structure with the id of the diagonal?
3. All cells in the same diagonal (i,j) have the same difference so we can get the diagonal of a cell using the difference i-j.

## 示例

```
[[3,3,1,1],[2,2,1,2],[1,1,1,2]]
[[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] diagonalSort(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** diagonalSort(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] DiagonalSort(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var diagonalSort = function(mat) {
    
};
```

### TypeScript

```typescript
function diagonalSort(mat: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[][]
     */
    function diagonalSort($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func diagonalSort(_ mat: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun diagonalSort(mat: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> diagonalSort(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func diagonalSort(mat [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer[][]}
def diagonal_sort(mat)
    
end
```

### Scala

```scala
object Solution {
    def diagonalSort(mat: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn diagonal_sort(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (diagonal-sort mat)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec diagonal_sort(Mat :: [[integer()]]) -> [[integer()]].
diagonal_sort(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec diagonal_sort(mat :: [[integer]]) :: [[integer]]
  def diagonal_sort(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func diagonalSort(mat: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

