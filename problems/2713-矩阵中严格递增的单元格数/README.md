# 2713. 矩阵中严格递增的单元格数

## 题目描述

<p>给你一个下标从 <strong>1</strong> 开始、大小为 <code>m x n</code> 的整数矩阵 <code>mat</code>，你可以选择任一单元格作为 <strong>起始单元格</strong> 。</p>

<p>从起始单元格出发，你可以移动到 <strong>同一行或同一列</strong> 中的任何其他单元格，但前提是目标单元格的值<strong> 严格大于 </strong>当前单元格的值。</p>

<p>你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。</p>

<p>请你找出从某个单元开始访问矩阵所能访问的 <strong>单元格的最大数量</strong> 。</p>

<p>返回一个表示可访问单元格最大数量的整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/23/diag1drawio.png" style="width: 200px; height: 176px;"></strong></p>

<pre><strong>输入：</strong>mat = [[3,1],[3,4]]
<strong>输出：</strong>2
<strong>解释：</strong>上图展示了从第 1 行、第 2 列的单元格开始，可以访问 2 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 2 个单元格，因此答案是 2 。 
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/23/diag3drawio.png" style="width: 200px; height: 176px;"></strong></p>

<pre><strong>输入：</strong>mat = [[1,1],[1,1]]
<strong>输出：</strong>1
<strong>解释：</strong>由于目标单元格必须严格大于当前单元格，在本示例中只能访问 1 个单元格。 
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/23/diag4drawio.png" style="width: 350px; height: 250px;"></strong></p>

<pre><strong>输入：</strong>mat = [[3,1,6],[-9,5,7]]
<strong>输出：</strong>4
<strong>解释：</strong>上图展示了从第 2 行、第 1 列的单元格开始，可以访问 4 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 4 个单元格，因此答案是 4 。  
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length&nbsp;</code></li>
	<li><code>n == mat[i].length&nbsp;</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 数组
- 哈希表
- 二分查找
- 动态规划
- 矩阵
- 有序集合
- 排序

## 提示

1. We can try to build the answer in a bottom-up fashion, starting from the smallest values and increasing to the larger values.
2. Going through the values in sorted order, we can store the maximum path we have seen so far for a row/column.
3. When we are at a cell, we check its row and column to find out the best previous smaller value that we’ve got so far, and we use it to increment the current value of the row and column.

## 示例

```
[[3,1],[3,4]]
[[1,1],[1,1]]
[[3,1,6],[-9,5,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxIncreasingCells(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxIncreasingCells(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxIncreasingCells(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        
```

### C

```c
int maxIncreasingCells(int** mat, int matSize, int* matColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxIncreasingCells(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var maxIncreasingCells = function(mat) {
    
};
```

### TypeScript

```typescript
function maxIncreasingCells(mat: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function maxIncreasingCells($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxIncreasingCells(_ mat: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxIncreasingCells(mat: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxIncreasingCells(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func maxIncreasingCells(mat [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer}
def max_increasing_cells(mat)
    
end
```

### Scala

```scala
object Solution {
    def maxIncreasingCells(mat: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_increasing_cells(mat: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-increasing-cells mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_increasing_cells(Mat :: [[integer()]]) -> integer().
max_increasing_cells(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_increasing_cells(mat :: [[integer]]) :: integer
  def max_increasing_cells(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxIncreasingCells(mat: Array<Array<Int64>>): Int64 {

    }
}
```

