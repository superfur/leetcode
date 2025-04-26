# 2132. 用邮票贴满网格图

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的二进制矩阵&nbsp;<code>grid</code>&nbsp;，每个格子要么为&nbsp;<code>0</code>&nbsp;（空）要么为&nbsp;<code>1</code>&nbsp;（被占据）。</p>

<p>给你邮票的尺寸为&nbsp;<code>stampHeight x stampWidth</code>&nbsp;。我们想将邮票贴进二进制矩阵中，且满足以下&nbsp;<strong>限制</strong>&nbsp;和&nbsp;<strong>要求</strong>&nbsp;：</p>

<ol>
	<li>覆盖所有 <strong>空</strong>&nbsp;格子。</li>
	<li>不覆盖任何 <strong>被占据&nbsp;</strong>的格子。</li>
	<li>我们可以放入任意数目的邮票。</li>
	<li>邮票可以相互有 <strong>重叠</strong>&nbsp;部分。</li>
	<li>邮票不允许 <strong>旋转</strong>&nbsp;。</li>
	<li>邮票必须完全在矩阵 <strong>内</strong>&nbsp;。</li>
</ol>

<p>如果在满足上述要求的前提下，可以放入邮票，请返回&nbsp;<code>true</code>&nbsp;，否则返回<i>&nbsp;</i><code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/ex1.png" style="width: 180px; height: 237px;"></p>

<pre><b>输入：</b>grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
<b>输出：</b>true
<b>解释：</b>我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/ex2.png" style="width: 170px; height: 179px;"></p>

<pre><b>输入：</b>grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 
<b>输出：</b>false 
<b>解释：</b>没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[r].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>grid[r][c]</code> 要么是&nbsp;<code>0</code>&nbsp;，要么是&nbsp;<code>1</code> 。</li>
	<li><code>1 &lt;= stampHeight, stampWidth &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 矩阵
- 前缀和

## 提示

1. We can check if every empty cell is a part of a consecutive row of empty cells that has a width of at least stampWidth as well as a consecutive column of empty cells that has a height of at least stampHeight.
2. We can prove that this condition is sufficient and necessary to fit the stamps while following the given restrictions and requirements.
3. For each row, find every consecutive row of empty cells, and mark all the cells where the consecutive row is at least stampWidth wide. Do the same for the columns with stampHeight. Then, you can check if every cell is marked twice.

## 示例

```
[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
4
3
[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
2
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool possibleToStamp(vector<vector<int>>& grid, int stampHeight, int stampWidth) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean possibleToStamp(int[][] grid, int stampHeight, int stampWidth) {
        
    }
}
```

### Python

```python
class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        
```

### C

```c
bool possibleToStamp(int** grid, int gridSize, int* gridColSize, int stampHeight, int stampWidth) {
    
}
```

### C#

```csharp
public class Solution {
    public bool PossibleToStamp(int[][] grid, int stampHeight, int stampWidth) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} stampHeight
 * @param {number} stampWidth
 * @return {boolean}
 */
var possibleToStamp = function(grid, stampHeight, stampWidth) {
    
};
```

### TypeScript

```typescript
function possibleToStamp(grid: number[][], stampHeight: number, stampWidth: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $stampHeight
     * @param Integer $stampWidth
     * @return Boolean
     */
    function possibleToStamp($grid, $stampHeight, $stampWidth) {
        
    }
}
```

### Swift

```swift
class Solution {
    func possibleToStamp(_ grid: [[Int]], _ stampHeight: Int, _ stampWidth: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun possibleToStamp(grid: Array<IntArray>, stampHeight: Int, stampWidth: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool possibleToStamp(List<List<int>> grid, int stampHeight, int stampWidth) {
    
  }
}
```

### Go

```golang
func possibleToStamp(grid [][]int, stampHeight int, stampWidth int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} stamp_height
# @param {Integer} stamp_width
# @return {Boolean}
def possible_to_stamp(grid, stamp_height, stamp_width)
    
end
```

### Scala

```scala
object Solution {
    def possibleToStamp(grid: Array[Array[Int]], stampHeight: Int, stampWidth: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn possible_to_stamp(grid: Vec<Vec<i32>>, stamp_height: i32, stamp_width: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (possible-to-stamp grid stampHeight stampWidth)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec possible_to_stamp(Grid :: [[integer()]], StampHeight :: integer(), StampWidth :: integer()) -> boolean().
possible_to_stamp(Grid, StampHeight, StampWidth) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec possible_to_stamp(grid :: [[integer]], stamp_height :: integer, stamp_width :: integer) :: boolean
  def possible_to_stamp(grid, stamp_height, stamp_width) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func possibleToStamp(grid: Array<Array<Int64>>, stampHeight: Int64, stampWidth: Int64): Bool {

    }
}
```

