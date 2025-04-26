# LCR 129. 字母迷宫

## 题目描述

<p>字母迷宫游戏初始界面记作 <code>m x n</code> 二维字符串数组 <code>grid</code>，请判断玩家是否能在 <code>grid</code> 中找到目标单词 <code>target</code>。<br />
注意：寻找单词时 <strong>必须</strong> 按照字母顺序，通过水平或垂直方向相邻的单元格内的字母构成，同时，同一个单元格内的字母&nbsp;<strong>不允许被重复使用&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" /></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCCED"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "SEE"
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCB"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n = grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 6</code></li>
	<li><code>1 &lt;= target.length &lt;= 15</code></li>
	<li><code>grid</code> 和 <code>target</code> 仅由大小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 79 题相同：<a href="https://leetcode-cn.com/problems/word-search/">https://leetcode-cn.com/problems/word-search/</a></p>

<p>&nbsp;</p>

<p>&nbsp;</p>


## 难度

Medium

## 标签

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
    bool wordPuzzle(vector<vector<char>>& grid, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean wordPuzzle(char[][] grid, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wordPuzzle(self, grid, target):
        """
        :type grid: List[List[str]]
        :type target: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
        
```

### C

```c
bool wordPuzzle(char** grid, int gridSize, int* gridColSize, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool WordPuzzle(char[][] grid, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} grid
 * @param {string} target
 * @return {boolean}
 */
var wordPuzzle = function(grid, target) {
    
};
```

### TypeScript

```typescript
function wordPuzzle(grid: string[][], target: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $grid
     * @param String $target
     * @return Boolean
     */
    function wordPuzzle($grid, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wordPuzzle(_ grid: [[Character]], _ target: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wordPuzzle(grid: Array<CharArray>, target: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool wordPuzzle(List<List<String>> grid, String target) {
    
  }
}
```

### Go

```golang
func wordPuzzle(grid [][]byte, target string) bool {
    
}
```

### Ruby

```ruby
# @param {Character[][]} grid
# @param {String} target
# @return {Boolean}
def word_puzzle(grid, target)
    
end
```

### Scala

```scala
object Solution {
    def wordPuzzle(grid: Array[Array[Char]], target: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn word_puzzle(grid: Vec<Vec<char>>, target: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (word-puzzle grid target)
  (-> (listof (listof char?)) string? boolean?)
  )
```

### Erlang

```erlang
-spec word_puzzle(Grid :: [[char()]], Target :: unicode:unicode_binary()) -> boolean().
word_puzzle(Grid, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec word_puzzle(grid :: [[char]], target :: String.t) :: boolean
  def word_puzzle(grid, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wordPuzzle(grid: Array<Array<Rune>>, target: String): Bool {

    }
}
```

