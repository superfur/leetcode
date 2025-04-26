# 782. 变为棋盘

## 题目描述

<p>一个&nbsp;<code>n x n</code>&nbsp;的二维网络&nbsp;<code>board</code>&nbsp;仅由&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;组成&nbsp;。每次移动，你能交换任意两列或是两行的位置。</p>

<p>返回 <em>将这个矩阵变为<strong>&nbsp; “棋盘”&nbsp;&nbsp;</strong>所需的最小移动次数&nbsp;</em>。如果不存在可行的变换，输出 <code>-1</code>。</p>

<p><strong>“棋盘”</strong> 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/29/chessboard1-grid.jpg" style="height: 145px; width: 500px;" /></p>

<pre>
<strong>输入:</strong> board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
<strong>输出:</strong> 2
<strong>解释:</strong>一种可行的变换方式如下，从左到右：
第一次移动交换了第一列和第二列。
第二次移动交换了第二行和第三行。
</pre>

<p><strong>示例 2:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/29/chessboard2-grid.jpg" /></p>

<pre>
<strong>输入:</strong> board = [[0, 1], [1, 0]]
<strong>输出:</strong> 0
<strong>解释: </strong>注意左上角的格值为0时也是合法的棋盘，也是合法的棋盘.
</pre>

<p><strong>示例 3:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/29/chessboard3-grid.jpg" /></p>

<pre>
<strong>输入:</strong> board = [[1, 0], [1, 0]]
<strong>输出:</strong> -1
<strong>解释: </strong>任意的变换都不能使这个输入变为合法的棋盘。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 30</code></li>
	<li><code>board[i][j]</code>&nbsp;将只包含&nbsp;<code>0</code>或&nbsp;<code>1</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 数学
- 矩阵

## 示例

```
[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
[[0,1],[1,0]]
[[1,0],[1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public int movesToChessboard(int[][] board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        
```

### C

```c
int movesToChessboard(int** board, int boardSize, int* boardColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MovesToChessboard(int[][] board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} board
 * @return {number}
 */
var movesToChessboard = function(board) {
    
};
```

### TypeScript

```typescript
function movesToChessboard(board: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function movesToChessboard($board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func movesToChessboard(_ board: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun movesToChessboard(board: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int movesToChessboard(List<List<int>> board) {
    
  }
}
```

### Go

```golang
func movesToChessboard(board [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} board
# @return {Integer}
def moves_to_chessboard(board)
    
end
```

### Scala

```scala
object Solution {
    def movesToChessboard(board: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn moves_to_chessboard(board: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (moves-to-chessboard board)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec moves_to_chessboard(Board :: [[integer()]]) -> integer().
moves_to_chessboard(Board) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec moves_to_chessboard(board :: [[integer]]) :: integer
  def moves_to_chessboard(board) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func movesToChessboard(board: Array<Array<Int64>>): Int64 {

    }
}
```

