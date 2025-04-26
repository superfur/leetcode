# 1263. 推箱子

## 题目描述

<p>「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。</p>

<p>游戏地图用大小为&nbsp;<code>m x n</code>&nbsp;的网格 <code>grid</code> 表示，其中每个元素可以是墙、地板或者是箱子。</p>

<p>现在你将作为玩家参与游戏，按规则将箱子&nbsp;<code>'B'</code>&nbsp;移动到目标位置&nbsp;<code>'T'</code> ：</p>

<ul>
	<li>玩家用字符&nbsp;<code>'S'</code>&nbsp;表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。</li>
	<li>地板用字符&nbsp;<code>'.'</code>&nbsp;表示，意味着可以自由行走。</li>
	<li>墙用字符&nbsp;<code>'#'</code>&nbsp;表示，意味着障碍物，不能通行。&nbsp;</li>
	<li>箱子仅有一个，用字符&nbsp;<code>'B'</code>&nbsp;表示。相应地，网格上有一个目标位置&nbsp;<code>'T'</code>。</li>
	<li>玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。</li>
	<li>玩家无法越过箱子。</li>
</ul>

<p>返回将箱子推到目标位置的最小 <strong>推动</strong> 次数，如果无法做到，请返回&nbsp;<code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/sample_1_1620.png" style="height: 335px; width: 500px;" /></strong></p>

<pre>
<strong>输入：</strong>grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
&nbsp;            ["#",".",".","B",".","#"],
&nbsp;            ["#",".","#","#",".","#"],
&nbsp;            ["#",".",".",".","S","#"],
&nbsp;            ["#","#","#","#","#","#"]]
<strong>输出：</strong>3
<strong>解释：</strong>我们只需要返回推箱子的次数。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
&nbsp;            ["#",".",".","B",".","#"],
&nbsp;            ["#","#","#","#",".","#"],
&nbsp;            ["#",".",".",".","S","#"],
&nbsp;            ["#","#","#","#","#","#"]]
<strong>输出：</strong>-1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [["#","#","#","#","#","#"],
&nbsp;            ["#","T",".",".","#","#"],
&nbsp;            ["#",".","#","B",".","#"],
&nbsp;            ["#",".",".",".",".","#"],
&nbsp;            ["#",".",".",".","S","#"],
&nbsp;            ["#","#","#","#","#","#"]]
<strong>输出：</strong>5
<strong>解释：</strong>向下、向左、向左、向上再向上。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 20</code></li>
	<li><code>grid</code> 仅包含字符&nbsp;<code>'.'</code>, <code>'#'</code>,&nbsp; <code>'S'</code> , <code>'T'</code>, 以及&nbsp;<code>'B'</code>。</li>
	<li><code>grid</code>&nbsp;中&nbsp;<code>'S'</code>, <code>'B'</code>&nbsp;和&nbsp;<code>'T'</code>&nbsp;各只能出现一个。</li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 数组
- 矩阵
- 堆（优先队列）

## 提示

1. We represent the search state as (player_row, player_col, box_row, box_col).
2. You need to count only the number of pushes. Then inside of your BFS check if the box could be pushed (in any direction) given the current position of the player.

## 示例

```
[["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
[["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#","#","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
[["#","#","#","#","#","#"],["#","T",".",".","#","#"],["#",".","#","B",".","#"],["#",".",".",".",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minPushBox(vector<vector<char>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minPushBox(char[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
```

### C

```c
int minPushBox(char** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinPushBox(char[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var minPushBox = function(grid) {
    
};
```

### TypeScript

```typescript
function minPushBox(grid: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function minPushBox($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minPushBox(_ grid: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minPushBox(grid: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minPushBox(List<List<String>> grid) {
    
  }
}
```

### Go

```golang
func minPushBox(grid [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} grid
# @return {Integer}
def min_push_box(grid)
    
end
```

### Scala

```scala
object Solution {
    def minPushBox(grid: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_push_box(grid: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-push-box grid)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_push_box(Grid :: [[char()]]) -> integer().
min_push_box(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_push_box(grid :: [[char]]) :: integer
  def min_push_box(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minPushBox(grid: Array<Array<Rune>>): Int64 {

    }
}
```

