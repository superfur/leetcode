# 1958. 检查操作是否合法

## 题目描述

<p>给你一个下标从&nbsp;<strong>0</strong>&nbsp;开始的&nbsp;<code>8 x 8</code> 网格&nbsp;<code>board</code>&nbsp;，其中&nbsp;<code>board[r][c]</code>&nbsp;表示游戏棋盘上的格子&nbsp;<code>(r, c)</code>&nbsp;。棋盘上空格用&nbsp;<code>'.'</code>&nbsp;表示，白色格子用&nbsp;<code>'W'</code>&nbsp;表示，黑色格子用&nbsp;<code>'B'</code>&nbsp;表示。</p>

<p>游戏中每次操作步骤为：选择一个空格子，将它变成你正在执行的颜色（要么白色，要么黑色）。但是，<strong>合法 </strong>操作必须满足：涂色后这个格子是 <strong>好线段的一个端点</strong>&nbsp;（好线段可以是水平的，竖直的或者是对角线）。</p>

<p><strong>好线段</strong>&nbsp;指的是一个包含 <strong>三个或者更多格子（包含端点格子）</strong>的线段，线段两个端点格子为 <strong>同一种颜色</strong>&nbsp;，且中间剩余格子的颜色都为 <strong>另一种颜色</strong>&nbsp;（线段上不能有任何空格子）。你可以在下图找到好线段的例子：</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/22/goodlines5.png" style="width: 500px; height: 312px;" />
<p>给你两个整数&nbsp;<code>rMove</code> 和&nbsp;<code>cMove</code>&nbsp;以及一个字符&nbsp;<code>color</code>&nbsp;，表示你正在执行操作的颜色（白或者黑），如果将格子&nbsp;<code>(rMove, cMove)</code>&nbsp;变成颜色&nbsp;<code>color</code>&nbsp;后，是一个&nbsp;<strong>合法</strong>&nbsp;操作，那么返回&nbsp;<code>true</code>&nbsp;，如果不是合法操作返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/07/10/grid11.png" style="width: 350px; height: 350px;" /></p>

<pre>
<b>输入：</b>board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
<b>输出：</b>true
<b>解释：</b>'.'，'W' 和 'B' 分别用颜色蓝色，白色和黑色表示。格子 (rMove, cMove) 用 'X' 标记。
以选中格子为端点的两个好线段在上图中用红色矩形标注出来了。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/07/10/grid2.png" style="width: 350px; height: 351px;" /></p>

<pre>
<b>输入：</b>board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
<b>输出：</b>false
<b>解释：</b>虽然选中格子涂色后，棋盘上产生了好线段，但选中格子是作为中间格子，没有产生以选中格子为端点的好线段。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>board.length == board[r].length == 8</code></li>
	<li><code>0 &lt;= rMove, cMove &lt; 8</code></li>
	<li><code>board[rMove][cMove] == '.'</code></li>
	<li><code>color</code>&nbsp;要么是&nbsp;<code>'B'</code> 要么是&nbsp;<code>'W'</code>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 枚举
- 矩阵

## 提示

1. For each line starting at the given cell check if it's a good line
2. To do that iterate over all directions horizontal, vertical, and diagonals then check good lines naively

## 示例

```
[[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]
4
3
"B"
[[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]]
4
4
"W"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkMove(vector<vector<char>>& board, int rMove, int cMove, char color) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkMove(char[][] board, int rMove, int cMove, char color) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        
```

### C

```c
bool checkMove(char** board, int boardSize, int* boardColSize, int rMove, int cMove, char color) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckMove(char[][] board, int rMove, int cMove, char color) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} board
 * @param {number} rMove
 * @param {number} cMove
 * @param {character} color
 * @return {boolean}
 */
var checkMove = function(board, rMove, cMove, color) {
    
};
```

### TypeScript

```typescript
function checkMove(board: string[][], rMove: number, cMove: number, color: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $board
     * @param Integer $rMove
     * @param Integer $cMove
     * @param String $color
     * @return Boolean
     */
    function checkMove($board, $rMove, $cMove, $color) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkMove(_ board: [[Character]], _ rMove: Int, _ cMove: Int, _ color: Character) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkMove(board: Array<CharArray>, rMove: Int, cMove: Int, color: Char): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkMove(List<List<String>> board, int rMove, int cMove, String color) {
    
  }
}
```

### Go

```golang
func checkMove(board [][]byte, rMove int, cMove int, color byte) bool {
    
}
```

### Ruby

```ruby
# @param {Character[][]} board
# @param {Integer} r_move
# @param {Integer} c_move
# @param {Character} color
# @return {Boolean}
def check_move(board, r_move, c_move, color)
    
end
```

### Scala

```scala
object Solution {
    def checkMove(board: Array[Array[Char]], rMove: Int, cMove: Int, color: Char): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_move(board: Vec<Vec<char>>, r_move: i32, c_move: i32, color: char) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-move board rMove cMove color)
  (-> (listof (listof char?)) exact-integer? exact-integer? char? boolean?)
  )
```

### Erlang

```erlang
-spec check_move(Board :: [[char()]], RMove :: integer(), CMove :: integer(), Color :: char()) -> boolean().
check_move(Board, RMove, CMove, Color) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_move(board :: [[char]], r_move :: integer, c_move :: integer, color :: char) :: boolean
  def check_move(board, r_move, c_move, color) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkMove(board: Array<Array<Rune>>, rMove: Int64, cMove: Int64, color: Rune): Bool {

    }
}
```

