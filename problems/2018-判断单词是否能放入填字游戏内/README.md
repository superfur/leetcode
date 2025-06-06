# 2018. 判断单词是否能放入填字游戏内

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的矩阵&nbsp;<code>board</code>&nbsp;，它代表一个填字游戏&nbsp;<strong>当前</strong>&nbsp;的状态。填字游戏格子中包含小写英文字母（已填入的单词），表示&nbsp;<strong>空</strong>&nbsp;格的&nbsp;<code>' '</code>&nbsp;和表示&nbsp;<strong>障碍</strong>&nbsp;格子的&nbsp;<code>'#'</code>&nbsp;。</p>

<p>如果满足以下条件，那么我们可以 <strong>水平</strong>&nbsp;（从左到右 <strong>或者</strong>&nbsp;从右到左）或 <strong>竖直</strong>&nbsp;（从上到下 <strong>或者</strong>&nbsp;从下到上）填入一个单词：</p>

<ul>
	<li>该单词不占据任何&nbsp;<code>'#'</code>&nbsp;对应的格子。</li>
	<li>每个字母对应的格子要么是&nbsp;<code>' '</code>&nbsp;（空格）要么与 <code>board</code>&nbsp;中已有字母 <strong>匹配</strong>&nbsp;。</li>
	<li>如果单词是 <strong>水平</strong>&nbsp;放置的，那么该单词左边和右边 <strong>相邻</strong>&nbsp;格子不能为&nbsp;<code>' '</code>&nbsp;或小写英文字母。</li>
	<li>如果单词是&nbsp;<strong>竖直</strong>&nbsp;放置的，那么该单词上边和下边&nbsp;<strong>相邻</strong><strong>&nbsp;</strong>格子不能为&nbsp;<code>' '</code>&nbsp;或小写英文字母。</li>
</ul>

<p>给你一个字符串&nbsp;<code>word</code>&nbsp;，如果&nbsp;<code>word</code>&nbsp;可以被放入&nbsp;<code>board</code>&nbsp;中，请你返回&nbsp;<code>true</code>&nbsp;，否则请返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/18/crossword-1.png" style="width: 170px; height: 150px;" /></p>

<pre>
<b>输入：</b>board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
<b>输出：</b>true
<b>解释：</b>单词 "abc" 可以如上图放置（从上往下）。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/18/c2.png" style="width: 170px; height: 151px;" /></p>

<pre>
<b>输入：</b>board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
<b>输出：</b>false
<b>解释：</b>无法放置单词，因为放置该单词后上方或者下方相邻格会有空格。</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/18/crossword-2.png" style="width: 171px; height: 146px;" /></p>

<pre>
<b>输入：</b>board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
<b>输出：</b>true
<b>解释：</b>单词 "ca" 可以如上图放置（从右到左）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m * n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>board[i][j]</code>&nbsp;可能为&nbsp;<code>' '</code>&nbsp;，<code>'#'</code>&nbsp;或者一个小写英文字母。</li>
	<li><code>1 &lt;= word.length &lt;= max(m, n)</code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 枚举
- 矩阵

## 提示

1. Check all possible placements for the word.
2. There is a limited number of places where a word can start.

## 示例

```
[["#"," ","#"],[" "," ","#"],["#","c"," "]]
"abc"
[[" ","#","a"],[" ","#", "c"],[" ","#","a"]]
"ac"
[["#"," ","#"],[" "," ","#"],["#"," ","c"]]
"ca"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool placeWordInCrossword(vector<vector<char>>& board, string word) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean placeWordInCrossword(char[][] board, String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
```

### C

```c
bool placeWordInCrossword(char** board, int boardSize, int* boardColSize, char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public bool PlaceWordInCrossword(char[][] board, string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var placeWordInCrossword = function(board, word) {
    
};
```

### TypeScript

```typescript
function placeWordInCrossword(board: string[][], word: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $board
     * @param String $word
     * @return Boolean
     */
    function placeWordInCrossword($board, $word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func placeWordInCrossword(_ board: [[Character]], _ word: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun placeWordInCrossword(board: Array<CharArray>, word: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool placeWordInCrossword(List<List<String>> board, String word) {
    
  }
}
```

### Go

```golang
func placeWordInCrossword(board [][]byte, word string) bool {
    
}
```

### Ruby

```ruby
# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
def place_word_in_crossword(board, word)
    
end
```

### Scala

```scala
object Solution {
    def placeWordInCrossword(board: Array[Array[Char]], word: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn place_word_in_crossword(board: Vec<Vec<char>>, word: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (place-word-in-crossword board word)
  (-> (listof (listof char?)) string? boolean?)
  )
```

### Erlang

```erlang
-spec place_word_in_crossword(Board :: [[char()]], Word :: unicode:unicode_binary()) -> boolean().
place_word_in_crossword(Board, Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec place_word_in_crossword(board :: [[char]], word :: String.t) :: boolean
  def place_word_in_crossword(board, word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func placeWordInCrossword(board: Array<Array<Rune>>, word: String): Bool {

    }
}
```

