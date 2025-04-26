# 419. 棋盘上的战舰

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的矩阵 <code>board</code> 表示棋盘，其中，每个单元格可以是一艘战舰 <code>'X'</code> 或者是一个空位 <code>'.'</code> ，返回在棋盘 <code>board</code> 上放置的 <strong>舰队</strong> 的数量。</p>

<p><strong>舰队</strong> 只能水平或者垂直放置在 <code>board</code> 上。换句话说，舰队只能按 <code>1 x k</code>（<code>1</code> 行，<code>k</code> 列）或 <code>k x 1</code>（<code>k</code> 行，<code>1</code> 列）的形状放置，其中 <code>k</code> 可以是任意大小。两个舰队之间至少有一个水平或垂直的空格分隔 （即没有相邻的舰队）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1719200420-KKnzye-image.png" style="width: 333px; height: 333px;" />
<pre>
<strong>输入：</strong>board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>board = [["."]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> 是 <code>'.'</code> 或 <code>'X'</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以实现一次扫描算法，并只使用<strong> </strong><code>O(1)</code><strong> </strong>额外空间，并且不修改 <code>board</code> 的值来解决这个问题吗？</p>


## 难度

Medium

## 标签

- 深度优先搜索
- 数组
- 矩阵

## 示例

```
[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
[["."]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public int countBattleships(char[][] board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
```

### C

```c
int countBattleships(char** board, int boardSize, int* boardColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountBattleships(char[][] board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} board
 * @return {number}
 */
var countBattleships = function(board) {
    
};
```

### TypeScript

```typescript
function countBattleships(board: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $board
     * @return Integer
     */
    function countBattleships($board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countBattleships(_ board: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countBattleships(board: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countBattleships(List<List<String>> board) {
    
  }
}
```

### Go

```golang
func countBattleships(board [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} board
# @return {Integer}
def count_battleships(board)
    
end
```

### Scala

```scala
object Solution {
    def countBattleships(board: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_battleships(board: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-battleships board)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_battleships(Board :: [[char()]]) -> integer().
count_battleships(Board) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_battleships(board :: [[char]]) :: integer
  def count_battleships(board) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countBattleships(board: Array<Array<Rune>>): Int64 {

    }
}
```

