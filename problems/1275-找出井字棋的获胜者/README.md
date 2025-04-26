# 1275. 找出井字棋的获胜者

## 题目描述

<p><strong>井字棋&nbsp;</strong>是由两个玩家<i>&nbsp;</i><code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;在&nbsp;<code>3 x 3</code>&nbsp;的棋盘上进行的游戏。井字棋游戏的规则如下：</p>

<ul>
	<li>玩家轮流将棋子放在空方格 (<code>' '</code>) 上。</li>
	<li>第一个玩家 <code>A</code> 总是用&nbsp;<code>'X'</code> 作为棋子，而第二个玩家 <code>B</code> 总是用 <code>'O'</code> 作为棋子。</li>
	<li><code>'X'</code> 和 <code>'O'</code> 只能放在空方格中，而不能放在已经被占用的方格上。</li>
	<li>只要有 <strong>3</strong> 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。</li>
	<li>如果所有方块都放满棋子（不为空），游戏也会结束。</li>
	<li>游戏结束后，棋子无法再进行任何移动。</li>
</ul>

<p>给你一个数组 <code>moves</code>，其中 <code>moves[i] = [row<sub>i</sub>, col<sub>i</sub>]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;次移动在&nbsp;<code>grid[row<sub>i</sub>][col<sub>i</sub>]</code>。如果游戏存在获胜者（<code>A</code> 或 <code>B</code>），就返回该游戏的获胜者；如果游戏以平局结束，则返回 <code>"Draw"</code>；如果仍会有行动（游戏未结束），则返回 <code>"Pending"</code>。</p>

<p>你可以假设&nbsp;<code>moves</code>&nbsp;都 <strong>有效</strong>（遵循 <strong>井字棋</strong> 规则），网格最初是空的，<code>A</code> 将先行动。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/22/xo1-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
<strong>输出：</strong>"A"
<strong>解释：</strong>"A" 获胜，他总是先走。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/22/xo2-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
<strong>输出：</strong>"B"
<strong>解释：</strong>"B" 获胜。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/22/xo3-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
<strong>输出：</strong>"Draw"
<strong>解释：</strong>由于没有办法再行动，游戏以平局结束。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= moves.length &lt;= 9</code></li>
	<li><code>moves[i].length == 2</code></li>
	<li><code>0 &lt;= moves[i][j] &lt;= 2</code></li>
	<li><code>moves</code>&nbsp;里没有重复的元素。</li>
	<li><code>moves</code> 遵循井字棋的规则。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 矩阵
- 模拟

## 提示

1. It's straightforward to check if A or B won or not, check for each row/column/diag if all the three are the same.
2. Then if no one wins, the game is a draw iff the board is full, i.e. moves.length = 9 otherwise is pending.

## 示例

```
[[0,0],[2,0],[1,1],[2,1],[2,2]]
[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        
    }
};
```

### Java

```java
class Solution {
    public String tictactoe(int[][] moves) {
        
    }
}
```

### Python

```python
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
```

### C

```c
char* tictactoe(int** moves, int movesSize, int* movesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string Tictactoe(int[][] moves) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function(moves) {
    
};
```

### TypeScript

```typescript
function tictactoe(moves: number[][]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $moves
     * @return String
     */
    function tictactoe($moves) {
        
    }
}
```

### Swift

```swift
class Solution {
    func tictactoe(_ moves: [[Int]]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun tictactoe(moves: Array<IntArray>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String tictactoe(List<List<int>> moves) {
    
  }
}
```

### Go

```golang
func tictactoe(moves [][]int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} moves
# @return {String}
def tictactoe(moves)
    
end
```

### Scala

```scala
object Solution {
    def tictactoe(moves: Array[Array[Int]]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn tictactoe(moves: Vec<Vec<i32>>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (tictactoe moves)
  (-> (listof (listof exact-integer?)) string?)
  )
```

### Erlang

```erlang
-spec tictactoe(Moves :: [[integer()]]) -> unicode:unicode_binary().
tictactoe(Moves) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec tictactoe(moves :: [[integer]]) :: String.t
  def tictactoe(moves) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func tictactoe(moves: Array<Array<Int64>>): String {

    }
}
```

