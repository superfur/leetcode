# 999. 可以被一步捕获的棋子数

## 题目描述

<p>给定一个&nbsp;<code>8 x 8</code> 的棋盘，<strong>只有一个</strong> 白色的车，用字符 <code>'R'</code> 表示。棋盘上还可能存在白色的象&nbsp;<code>'B'</code>&nbsp;以及黑色的卒&nbsp;<code>'p'</code>。空方块用字符 <code>'.'</code>&nbsp;表示。</p>

<p>车可以按水平或竖直方向（上，下，左，右）移动任意个方格直到它遇到另一个棋子或棋盘的边界。如果它能够在一次移动中移动到棋子的方格，则能够 <strong>吃掉</strong> 棋子。</p>

<p>注意：车不能穿过其它棋子，比如象和卒。这意味着如果有其它棋子挡住了路径，车就不能够吃掉棋子。</p>

<p>返回白车 <strong>攻击</strong>&nbsp;范围内 <strong>兵的数量</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_1_improved.PNG" style="height: 305px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong>输出：</strong>3
<strong>解释：
</strong>在本例中，车能够吃掉所有的卒。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_2_improved.PNG" style="height: 306px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong>输出：</strong>0
<strong>解释：
</strong>象阻止了车吃掉任何卒。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_3_improved.PNG" style="height: 305px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong>输出：</strong>3
<strong>解释： </strong>
车可以吃掉位置 b5，d6 和 f5 的卒。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>board.length == 8</code></li>
	<li><code>board[i].length == 8</code></li>
	<li><code>board[i][j]</code> 可以是&nbsp;<code>'R'</code>，<code>'.'</code>，<code>'B'</code>&nbsp;或&nbsp;<code>'p'</code></li>
	<li>只有一个格子上存在&nbsp;<code>board[i][j] == 'R'</code></li>
</ol>


## 难度

Easy

## 标签

- 数组
- 矩阵
- 模拟

## 示例

```
[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public int numRookCaptures(char[][] board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
```

### C

```c
int numRookCaptures(char** board, int boardSize, int* boardColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumRookCaptures(char[][] board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} board
 * @return {number}
 */
var numRookCaptures = function(board) {
    
};
```

### TypeScript

```typescript
function numRookCaptures(board: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $board
     * @return Integer
     */
    function numRookCaptures($board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numRookCaptures(_ board: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numRookCaptures(board: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numRookCaptures(List<List<String>> board) {
    
  }
}
```

### Go

```golang
func numRookCaptures(board [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} board
# @return {Integer}
def num_rook_captures(board)
    
end
```

### Scala

```scala
object Solution {
    def numRookCaptures(board: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_rook_captures(board: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-rook-captures board)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_rook_captures(Board :: [[char()]]) -> integer().
num_rook_captures(Board) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_rook_captures(board :: [[char]]) :: integer
  def num_rook_captures(board) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numRookCaptures(board: Array<Array<Rune>>): Int64 {

    }
}
```

