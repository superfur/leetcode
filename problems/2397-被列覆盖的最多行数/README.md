# 2397. 被列覆盖的最多行数

## 题目描述

<p>给你一个下标从 <strong>0 </strong>开始、大小为 <code>m x n</code> 的二进制矩阵 <code>matrix</code> ；另给你一个整数 <code>numSelect</code>，表示你必须从 <code>matrix</code> 中选择的 <strong>不同</strong> 列的数量。</p>

<p>如果一行中所有的 <code>1</code> 都被你选中的列所覆盖，则认为这一行被 <strong>覆盖</strong> 了。</p>

<p><strong>形式上</strong>，假设 <code>s = {c<sub>1</sub>, c<sub>2</sub>, ...., c<sub>numSelect</sub>}</code> 是你选择的列的集合。对于矩阵中的某一行 <code>row</code> ，如果满足下述条件，则认为这一行被集合 <code>s</code> <strong>覆盖</strong>：</p>

<ul>
	<li>对于满足 <code>matrix[row][col] == 1</code> 的每个单元格 <code>matrix[row][col]</code>（<code>0 &lt;= col &lt;= n - 1</code>），<code>col</code> 均存在于 <code>s</code> 中，或者</li>
	<li><code>row</code> 中 <strong>不存在</strong> 值为 <code>1</code> 的单元格。</li>
</ul>

<p>你需要从矩阵中选出 <code>numSelect</code> 个列，使集合覆盖的行数最大化。</p>

<p>返回一个整数，表示可以由 <code>numSelect</code> 列构成的集合 <strong>覆盖</strong> 的 <strong>最大行数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2022/07/14/rowscovered.png" style="width: 250px; height: 417px;" /></strong></p>

<pre>
<b>输入：</b>matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2
<b>输出：</b>3
<strong>解释：</strong>
图示中显示了一种覆盖 3 行的可行办法。
选择 s = {0, 2} 。
- 第 0 行被覆盖，因为其中没有出现 1 。
- 第 1 行被覆盖，因为值为 1 的两列（即 0 和 2）均存在于 s 中。
- 第 2 行未被覆盖，因为 matrix[2][1] == 1 但是 1 未存在于 s 中。
- 第 3 行被覆盖，因为 matrix[2][2] == 1 且 2 存在于 s 中。
因此，可以覆盖 3 行。
另外 s = {1, 2} 也可以覆盖 3 行，但可以证明无法覆盖更多行。</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2022/07/14/rowscovered2.png" style="width: 83px; height: 247px;" /></strong></p>

<pre>
<b>输入：</b>matrix = [[1],[0]], numSelect = 1
<b>输出：</b>2
<strong>解释：</strong>
选择唯一的一列，两行都被覆盖了，因为整个矩阵都被覆盖了。
所以我们返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 12</code></li>
	<li><code>matrix[i][j]</code> 要么是 <code>0</code> 要么是 <code>1</code></li>
	<li><code>1 &lt;= numSelect&nbsp;&lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 回溯
- 枚举
- 矩阵

## 提示

1. Try a brute-force approach.
2. Iterate through all possible sets of exactly <code>cols</code> columns.
3. For each valid set, check how many rows are covered, and return the maximum.

## 示例

```
[[0,0,0],[1,0,1],[0,1,1],[0,0,1]]
2
[[1],[0]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumRows(vector<vector<int>>& matrix, int numSelect) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumRows(int[][] matrix, int numSelect) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumRows(self, matrix, numSelect):
        """
        :type matrix: List[List[int]]
        :type numSelect: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        
```

### C

```c
int maximumRows(int** matrix, int matrixSize, int* matrixColSize, int numSelect) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumRows(int[][] matrix, int numSelect) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} numSelect
 * @return {number}
 */
var maximumRows = function(matrix, numSelect) {
    
};
```

### TypeScript

```typescript
function maximumRows(matrix: number[][], numSelect: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $numSelect
     * @return Integer
     */
    function maximumRows($matrix, $numSelect) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumRows(_ matrix: [[Int]], _ numSelect: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumRows(matrix: Array<IntArray>, numSelect: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumRows(List<List<int>> matrix, int numSelect) {
    
  }
}
```

### Go

```golang
func maximumRows(matrix [][]int, numSelect int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @param {Integer} num_select
# @return {Integer}
def maximum_rows(matrix, num_select)
    
end
```

### Scala

```scala
object Solution {
    def maximumRows(matrix: Array[Array[Int]], numSelect: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_rows(matrix: Vec<Vec<i32>>, num_select: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-rows matrix numSelect)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_rows(Matrix :: [[integer()]], NumSelect :: integer()) -> integer().
maximum_rows(Matrix, NumSelect) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_rows(matrix :: [[integer]], num_select :: integer) :: integer
  def maximum_rows(matrix, num_select) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumRows(matrix: Array<Array<Int64>>, numSelect: Int64): Int64 {

    }
}
```

