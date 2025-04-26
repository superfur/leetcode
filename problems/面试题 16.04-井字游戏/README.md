# 面试题 16.04. 井字游戏

## 题目描述

<p>设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符&quot; &quot;，&quot;X&quot;和&quot;O&quot;组成，其中字符&quot; &quot;代表一个空位。</p>

<p>以下是井字游戏的规则：</p>

<ul>
	<li>玩家轮流将字符放入空位（&quot; &quot;）中。</li>
	<li>第一个玩家总是放字符&quot;O&quot;，且第二个玩家总是放字符&quot;X&quot;。</li>
	<li>&quot;X&quot;和&quot;O&quot;只允许放置在空位中，不允许对已放有字符的位置进行填充。</li>
	<li>当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。</li>
	<li>当所有位置非空时，也算为游戏结束。</li>
	<li>如果游戏结束，玩家不允许再放置字符。</li>
</ul>

<p>如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（&quot;X&quot;或&quot;O&quot;）；如果游戏以平局结束，则返回 &quot;Draw&quot;；如果仍会有行动（游戏未结束），则返回 &quot;Pending&quot;。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> board = [&quot;O X&quot;,&quot; XO&quot;,&quot;X O&quot;]
<strong>输出：</strong> &quot;X&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> board = [&quot;OOX&quot;,&quot;XXO&quot;,&quot;OXO&quot;]
<strong>输出：</strong> &quot;Draw&quot;
<strong>解释：</strong> 没有玩家获胜且不存在空位
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong> board = [&quot;OOX&quot;,&quot;XXO&quot;,&quot;OX &quot;]
<strong>输出：</strong> &quot;Pending&quot;
<strong>解释：</strong> 没有玩家获胜且仍存在空位
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= board.length == board[i].length &lt;= 100</code></li>
	<li>输入一定遵循井字棋规则</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 计数
- 矩阵

## 提示

1. 如果多次调用hasWon，你的解决方案可能会发生什么变化？
2. 如果你正在为N×N的大小进行计算，你的解决方案可能会发生什么变化？

## 示例

```
["OX ","OX ","O  "]
["O"]
["OOXXOXXX","XXXOXOXO","OXOXXXOO","XOXOXXXX","OXOOXOOO","XOOOOOOO","OXXXOOOX","XOXOOXXX"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string tictactoe(vector<string>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public String tictactoe(String[] board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def tictactoe(self, board):
        """
        :type board: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        
```

### C

```c
char* tictactoe(char** board, int boardSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string Tictactoe(string[] board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} board
 * @return {string}
 */
var tictactoe = function(board) {
    
};
```

### TypeScript

```typescript
function tictactoe(board: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $board
     * @return String
     */
    function tictactoe($board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func tictactoe(_ board: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun tictactoe(board: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String tictactoe(List<String> board) {
    
  }
}
```

### Go

```golang
func tictactoe(board []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} board
# @return {String}
def tictactoe(board)
    
end
```

### Scala

```scala
object Solution {
    def tictactoe(board: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn tictactoe(board: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (tictactoe board)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec tictactoe(Board :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
tictactoe(Board) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec tictactoe(board :: [String.t]) :: String.t
  def tictactoe(board) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func tictactoe(board: Array<String>): String {

    }
}
```

