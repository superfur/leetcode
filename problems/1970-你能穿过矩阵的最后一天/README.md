# 1970. 你能穿过矩阵的最后一天

## 题目描述

<p>给你一个下标从 <strong>1</strong>&nbsp;开始的二进制矩阵，其中&nbsp;<code>0</code>&nbsp;表示陆地，<code>1</code>&nbsp;表示水域。同时给你&nbsp;<code>row</code> 和&nbsp;<code>col</code>&nbsp;分别表示矩阵中行和列的数目。</p>

<p>一开始在第&nbsp;<code>0</code>&nbsp;天，<strong>整个</strong>&nbsp;矩阵都是&nbsp;<strong>陆地</strong>&nbsp;。但每一天都会有一块新陆地被&nbsp;<strong>水</strong>&nbsp;淹没变成水域。给你一个下标从&nbsp;<strong>1</strong>&nbsp;开始的二维数组&nbsp;<code>cells</code>&nbsp;，其中&nbsp;<code>cells[i] = [r<sub>i</sub>, c<sub>i</sub>]</code>&nbsp;表示在第&nbsp;<code>i</code>&nbsp;天，第&nbsp;<code>r<sub>i</sub></code>&nbsp;行&nbsp;<code>c<sub>i</sub></code>&nbsp;列（下标都是从 <strong>1</strong>&nbsp;开始）的陆地会变成 <strong>水域</strong>&nbsp;（也就是 <code>0</code>&nbsp;变成 <code>1</code>&nbsp;）。</p>

<p>你想知道从矩阵最 <strong>上面</strong>&nbsp;一行走到最 <strong>下面</strong>&nbsp;一行，且只经过陆地格子的 <strong>最后一天</strong>&nbsp;是哪一天。你可以从最上面一行的&nbsp;<strong>任意</strong>&nbsp;格子出发，到达最下面一行的&nbsp;<strong>任意</strong>&nbsp;格子。你只能沿着&nbsp;<strong>四个</strong>&nbsp;基本方向移动（也就是上下左右）。</p>

<p>请返回只经过陆地格子能从最 <strong>上面</strong>&nbsp;一行走到最 <strong>下面</strong>&nbsp;一行的 <strong>最后一天</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/1.png" style="width: 624px; height: 162px;">
<pre><b>输入：</b>row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
<b>输出：</b>2
<b>解释：</b>上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 2 天。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/2.png" style="width: 504px; height: 178px;">
<pre><b>输入：</b>row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
<b>输出：</b>1
<b>解释：</b>上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 1 天。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/3.png" style="width: 666px; height: 167px;">
<pre><b>输入：</b>row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
<b>输出：</b>3
<b>解释：</b>上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 3 天。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= row, col &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>4 &lt;= row * col &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>cells.length == row * col</code></li>
	<li><code>1 &lt;= r<sub>i</sub> &lt;= row</code></li>
	<li><code>1 &lt;= c<sub>i</sub> &lt;= col</code></li>
	<li><code>cells</code>&nbsp;中的所有格子坐标都是 <strong>唯一</strong>&nbsp;的。</li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 二分查找
- 矩阵

## 提示

1. What graph algorithm allows us to find whether a path exists?
2. Can we use binary search to help us solve the problem?

## 示例

```
2
2
[[1,1],[2,1],[1,2],[2,2]]
2
2
[[1,1],[1,2],[2,1],[2,2]]
3
3
[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        
    }
};
```

### Java

```java
class Solution {
    public int latestDayToCross(int row, int col, int[][] cells) {
        
    }
}
```

### Python

```python
class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
```

### C

```c
int latestDayToCross(int row, int col, int** cells, int cellsSize, int* cellsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LatestDayToCross(int row, int col, int[][] cells) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} row
 * @param {number} col
 * @param {number[][]} cells
 * @return {number}
 */
var latestDayToCross = function(row, col, cells) {
    
};
```

### TypeScript

```typescript
function latestDayToCross(row: number, col: number, cells: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $row
     * @param Integer $col
     * @param Integer[][] $cells
     * @return Integer
     */
    function latestDayToCross($row, $col, $cells) {
        
    }
}
```

### Swift

```swift
class Solution {
    func latestDayToCross(_ row: Int, _ col: Int, _ cells: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun latestDayToCross(row: Int, col: Int, cells: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int latestDayToCross(int row, int col, List<List<int>> cells) {
    
  }
}
```

### Go

```golang
func latestDayToCross(row int, col int, cells [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} row
# @param {Integer} col
# @param {Integer[][]} cells
# @return {Integer}
def latest_day_to_cross(row, col, cells)
    
end
```

### Scala

```scala
object Solution {
    def latestDayToCross(row: Int, col: Int, cells: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (latest-day-to-cross row col cells)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec latest_day_to_cross(Row :: integer(), Col :: integer(), Cells :: [[integer()]]) -> integer().
latest_day_to_cross(Row, Col, Cells) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec latest_day_to_cross(row :: integer, col :: integer, cells :: [[integer]]) :: integer
  def latest_day_to_cross(row, col, cells) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func latestDayToCross(row: Int64, col: Int64, cells: Array<Array<Int64>>): Int64 {

    }
}
```

