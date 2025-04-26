# 212. 单词搜索 II

## 题目描述

<p>给定一个&nbsp;<code>m x n</code> 二维字符网格&nbsp;<code>board</code><strong>&nbsp;</strong>和一个单词（字符串）列表 <code>words</code>，&nbsp;<em>返回所有二维网格上的单词</em>&nbsp;。</p>

<p>单词必须按照字母顺序，通过 <strong>相邻的单元格</strong> 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" />
<pre>
<strong>输入：</strong>board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
<strong>输出：</strong>["eat","oath"]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search2.jpg" />
<pre>
<strong>输入：</strong>board = [["a","b"],["c","d"]], words = ["abcb"]
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 12</code></li>
	<li><code>board[i][j]</code> 是一个小写英文字母</li>
	<li><code>1 &lt;= words.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
	<li><code>words</code> 中的所有字符串互不相同</li>
</ul>


## 难度

Hard

## 标签

- 字典树
- 数组
- 字符串
- 回溯
- 矩阵

## 提示

1. You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
2. If the current candidate does not exist in all words&#39; prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: <a href="https://leetcode.com/problems/implement-trie-prefix-tree/">Implement Trie (Prefix Tree)</a> first.

## 示例

```
[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
["oath","pea","eat","rain"]
[["a","b"],["c","d"]]
["abcb"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findWords(char** board, int boardSize, int* boardColSize, char** words, int wordsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> FindWords(char[][] board, string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    
};
```

### TypeScript

```typescript
function findWords(board: string[][], words: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $board
     * @param String[] $words
     * @return String[]
     */
    function findWords($board, $words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findWords(_ board: [[Character]], _ words: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findWords(board: Array<CharArray>, words: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findWords(List<List<String>> board, List<String> words) {
    
  }
}
```

### Go

```golang
func findWords(board [][]byte, words []string) []string {
    
}
```

### Ruby

```ruby
# @param {Character[][]} board
# @param {String[]} words
# @return {String[]}
def find_words(board, words)
    
end
```

### Scala

```scala
object Solution {
    def findWords(board: Array[Array[Char]], words: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-words board words)
  (-> (listof (listof char?)) (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec find_words(Board :: [[char()]], Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_words(Board, Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_words(board :: [[char]], words :: [String.t]) :: [String.t]
  def find_words(board, words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findWords(board: Array<Array<Rune>>, words: Array<String>): ArrayList<String> {

    }
}
```

