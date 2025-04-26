# 885. 螺旋矩阵 III

## 题目描述

<p>在 <code>rows x cols</code> 的网格上，你从单元格 <code>(rStart, cStart)</code> 面朝东面开始。网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。</p>

<p>你需要以顺时针按螺旋状行走，访问此网格中的每个位置。每当移动到网格的边界之外时，需要继续在网格之外行走（但稍后可能会返回到网格边界）。</p>

<p>最终，我们到过网格的所有&nbsp;<code>rows x cols</code>&nbsp;个空间。</p>

<p>按照访问顺序返回表示网格位置的坐标列表。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png" style="width: 174px; height: 99px;" />
<pre>
<strong>输入：</strong>rows = 1, cols = 4, rStart = 0, cStart = 0
<strong>输出：</strong>[[0,0],[0,1],[0,2],[0,3]]
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png" style="width: 202px; height: 142px;" />
<pre>
<strong>输入：</strong>rows = 5, cols = 6, rStart = 1, cStart = 4
<strong>输出：</strong>[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rows, cols &lt;= 100</code></li>
	<li><code>0 &lt;= rStart &lt; rows</code></li>
	<li><code>0 &lt;= cStart &lt; cols</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 模拟

## 示例

```
1
4
0
0
5
6
1
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        
    }
}
```

### Python

```python
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** spiralMatrixIII(int rows, int cols, int rStart, int cStart, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] SpiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} rows
 * @param {number} cols
 * @param {number} rStart
 * @param {number} cStart
 * @return {number[][]}
 */
var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    
};
```

### TypeScript

```typescript
function spiralMatrixIII(rows: number, cols: number, rStart: number, cStart: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $rows
     * @param Integer $cols
     * @param Integer $rStart
     * @param Integer $cStart
     * @return Integer[][]
     */
    function spiralMatrixIII($rows, $cols, $rStart, $cStart) {
        
    }
}
```

### Swift

```swift
class Solution {
    func spiralMatrixIII(_ rows: Int, _ cols: Int, _ rStart: Int, _ cStart: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
    
  }
}
```

### Go

```golang
func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} rows
# @param {Integer} cols
# @param {Integer} r_start
# @param {Integer} c_start
# @return {Integer[][]}
def spiral_matrix_iii(rows, cols, r_start, c_start)
    
end
```

### Scala

```scala
object Solution {
    def spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn spiral_matrix_iii(rows: i32, cols: i32, r_start: i32, c_start: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (spiral-matrix-iii rows cols rStart cStart)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec spiral_matrix_iii(Rows :: integer(), Cols :: integer(), RStart :: integer(), CStart :: integer()) -> [[integer()]].
spiral_matrix_iii(Rows, Cols, RStart, CStart) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec spiral_matrix_iii(rows :: integer, cols :: integer, r_start :: integer, c_start :: integer) :: [[integer]]
  def spiral_matrix_iii(rows, cols, r_start, c_start) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func spiralMatrixIII(rows: Int64, cols: Int64, rStart: Int64, cStart: Int64): Array<Array<Int64>> {

    }
}
```

