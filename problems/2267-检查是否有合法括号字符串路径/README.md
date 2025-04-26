# 2267. 检查是否有合法括号字符串路径

## 题目描述

<p>一个括号字符串是一个 <strong>非空</strong>&nbsp;且只包含&nbsp;<code>'('</code>&nbsp;和&nbsp;<code>')'</code>&nbsp;的字符串。如果下面&nbsp;<strong>任意</strong>&nbsp;条件为&nbsp;<strong>真</strong>&nbsp;，那么这个括号字符串就是&nbsp;<strong>合法的</strong>&nbsp;。</p>

<ul>
	<li>字符串是&nbsp;<code>()</code>&nbsp;。</li>
	<li>字符串可以表示为&nbsp;<code>AB</code>（<code>A</code>&nbsp;连接&nbsp;<code>B</code>），<code>A</code> 和&nbsp;<code>B</code>&nbsp;都是合法括号序列。</li>
	<li>字符串可以表示为&nbsp;<code>(A)</code>&nbsp;，其中&nbsp;<code>A</code>&nbsp;是合法括号序列。</li>
</ul>

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的括号网格图矩阵&nbsp;<code>grid</code>&nbsp;。网格图中一个&nbsp;<strong>合法括号路径</strong>&nbsp;是满足以下所有条件的一条路径：</p>

<ul>
	<li>路径开始于左上角格子&nbsp;<code>(0, 0)</code>&nbsp;。</li>
	<li>路径结束于右下角格子&nbsp;<code>(m - 1, n - 1)</code>&nbsp;。</li>
	<li>路径每次只会向 <strong>下</strong>&nbsp;或者向 <strong>右</strong>&nbsp;移动。</li>
	<li>路径经过的格子组成的括号字符串是<strong>&nbsp;合法</strong>&nbsp;的。</li>
</ul>

<p>如果网格图中存在一条 <strong>合法括号路径</strong>&nbsp;，请返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/example1drawio.png" style="width: 521px; height: 300px;" /></p>

<pre>
<b>输入：</b>grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
<b>输出：</b>true
<b>解释：</b>上图展示了两条路径，它们都是合法括号字符串路径。
第一条路径得到的合法字符串是 "()(())" 。
第二条路径得到的合法字符串是 "((()))" 。
注意可能有其他的合法括号字符串路径。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/example2drawio.png" style="width: 165px; height: 165px;" /></p>

<pre>
<b>输入：</b>grid = [[")",")"],["(","("]]
<b>输出：</b>false
<b>解释：</b>两条可行路径分别得到 "))(" 和 ")((" 。由于它们都不是合法括号字符串，我们返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>grid[i][j]</code>&nbsp;要么是&nbsp;<code>'('</code>&nbsp;，要么是&nbsp;<code>')'</code> 。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. What observations can you make about the number of open brackets and close brackets for any prefix of a valid bracket sequence?
2. The number of open brackets must always be greater than or equal to the number of close brackets.
3. Could you use dynamic programming?

## 示例

```
[["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
[[")",")"],["(","("]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean hasValidPath(char[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        
```

### C

```c
bool hasValidPath(char** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HasValidPath(char[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var hasValidPath = function(grid) {
    
};
```

### TypeScript

```typescript
function hasValidPath(grid: string[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function hasValidPath($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hasValidPath(_ grid: [[Character]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hasValidPath(grid: Array<CharArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool hasValidPath(List<List<String>> grid) {
    
  }
}
```

### Go

```golang
func hasValidPath(grid [][]byte) bool {
    
}
```

### Ruby

```ruby
# @param {Character[][]} grid
# @return {Boolean}
def has_valid_path(grid)
    
end
```

### Scala

```scala
object Solution {
    def hasValidPath(grid: Array[Array[Char]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (has-valid-path grid)
  (-> (listof (listof char?)) boolean?)
  )
```

### Erlang

```erlang
-spec has_valid_path(Grid :: [[char()]]) -> boolean().
has_valid_path(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec has_valid_path(grid :: [[char]]) :: boolean
  def has_valid_path(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hasValidPath(grid: Array<Array<Rune>>): Bool {

    }
}
```

