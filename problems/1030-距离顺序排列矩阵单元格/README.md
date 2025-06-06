# 1030. 距离顺序排列矩阵单元格

## 题目描述

<p>给定四个整数 <code>rows</code>&nbsp;,&nbsp; &nbsp;<code>cols</code> ,&nbsp; <code>rCenter</code> 和 <code>cCenter</code> 。有一个&nbsp;<code>rows x cols</code>&nbsp;的矩阵，你在单元格上的坐标是&nbsp;<code>(rCenter, cCenter)</code> 。</p>

<p>返回矩阵中的所有单元格的坐标，并按与<em>&nbsp;</em><code>(rCenter, cCenter)</code><em>&nbsp;</em>的 <strong>距离</strong> 从最小到最大的顺序排。你可以按 <strong>任何</strong> 满足此条件的顺序返回答案。</p>

<p>单元格<code>(r1, c1)</code> 和 <code>(r2, c2)</code> 之间的距离为<code>|r1 - r2| + |c1 - c2|</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>rows = 1, cols = 2, rCenter = 0, cCenter = 0
<strong>输出：</strong>[[0,0],[0,1]]
<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>rows = 2, cols = 2, rCenter = 0, cCenter = 1
<strong>输出：</strong>[[0,1],[0,0],[1,1],[1,0]]
<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rows = 2, cols = 3, rCenter = 1, cCenter = 2
<strong>输出：</strong>[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rows, cols &lt;= 100</code></li>
	<li><code>0 &lt;= rCenter &lt; rows</code></li>
	<li><code>0 &lt;= cCenter &lt; cols</code></li>
</ul>


## 难度

Easy

## 标签

- 几何
- 数组
- 数学
- 矩阵
- 排序

## 示例

```
1
2
0
0
2
2
0
1
2
3
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        
    }
}
```

### Python

```python
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** allCellsDistOrder(int rows, int cols, int rCenter, int cCenter, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] AllCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} rows
 * @param {number} cols
 * @param {number} rCenter
 * @param {number} cCenter
 * @return {number[][]}
 */
var allCellsDistOrder = function(rows, cols, rCenter, cCenter) {
    
};
```

### TypeScript

```typescript
function allCellsDistOrder(rows: number, cols: number, rCenter: number, cCenter: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $rows
     * @param Integer $cols
     * @param Integer $rCenter
     * @param Integer $cCenter
     * @return Integer[][]
     */
    function allCellsDistOrder($rows, $cols, $rCenter, $cCenter) {
        
    }
}
```

### Swift

```swift
class Solution {
    func allCellsDistOrder(_ rows: Int, _ cols: Int, _ rCenter: Int, _ cCenter: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
    
  }
}
```

### Go

```golang
func allCellsDistOrder(rows int, cols int, rCenter int, cCenter int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} rows
# @param {Integer} cols
# @param {Integer} r_center
# @param {Integer} c_center
# @return {Integer[][]}
def all_cells_dist_order(rows, cols, r_center, c_center)
    
end
```

### Scala

```scala
object Solution {
    def allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn all_cells_dist_order(rows: i32, cols: i32, r_center: i32, c_center: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (all-cells-dist-order rows cols rCenter cCenter)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec all_cells_dist_order(Rows :: integer(), Cols :: integer(), RCenter :: integer(), CCenter :: integer()) -> [[integer()]].
all_cells_dist_order(Rows, Cols, RCenter, CCenter) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec all_cells_dist_order(rows :: integer, cols :: integer, r_center :: integer, c_center :: integer) :: [[integer]]
  def all_cells_dist_order(rows, cols, r_center, c_center) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func allCellsDistOrder(rows: Int64, cols: Int64, rCenter: Int64, cCenter: Int64): Array<Array<Int64>> {

    }
}
```

