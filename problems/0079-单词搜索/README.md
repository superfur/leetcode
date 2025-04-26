# 79. 单词搜索

## 题目描述

<p>给定一个 <code>m x n</code> 二维字符网格 <code>board</code> 和一个字符串单词 <code>word</code> 。如果 <code>word</code> 存在于网格中，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 <= m, n <= 6</code></li>
	<li><code>1 <= word.length <= 15</code></li>
	<li><code>board</code> 和 <code>word</code> 仅由大小写英文字母组成</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以使用搜索剪枝的技术来优化解决方案，使其在 <code>board</code> 更大的情况下可以更快解决问题？</p>


## 难度

Medium

## 标签

- 深度优先搜索
- 数组
- 字符串
- 回溯
- 矩阵

## 示例

```
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"SEE"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCB"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean exist(char[][] board, String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
```

### C

```c
bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public bool Exist(char[][] board, string word) {
        
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
var exist = function(board, word) {
    
};
```

### TypeScript

```typescript
function exist(board: string[][], word: string): boolean {
    
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
    function exist($board, $word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func exist(_ board: [[Character]], _ word: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool exist(List<List<String>> board, String word) {
    
  }
}
```

### Go

```golang
func exist(board [][]byte, word string) bool {
    
}
```

### Ruby

```ruby
# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
def exist(board, word)
    
end
```

### Scala

```scala
object Solution {
    def exist(board: Array[Array[Char]], word: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (exist board word)
  (-> (listof (listof char?)) string? boolean?)
  )
```

### Erlang

```erlang
-spec exist(Board :: [[char()]], Word :: unicode:unicode_binary()) -> boolean().
exist(Board, Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec exist(board :: [[char]], word :: String.t) :: boolean
  def exist(board, word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func exist(board: Array<Array<Rune>>, word: String): Bool {

    }
}
```

