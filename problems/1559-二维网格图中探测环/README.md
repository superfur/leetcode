# 1559. 二维网格图中探测环

## 题目描述

<p>给你一个二维字符网格数组&nbsp;<code>grid</code>&nbsp;，大小为&nbsp;<code>m x n</code>&nbsp;，你需要检查&nbsp;<code>grid</code>&nbsp;中是否存在 <strong>相同值</strong> 形成的环。</p>

<p>一个环是一条开始和结束于同一个格子的长度 <strong>大于等于 4</strong>&nbsp;的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 <strong>相同的值&nbsp;</strong>。</p>

<p>同时，你也不能回到上一次移动时所在的格子。比方说，环&nbsp;&nbsp;<code>(1, 1) -&gt; (1, 2) -&gt; (1, 1)</code>&nbsp;是不合法的，因为从 <code>(1, 2)</code>&nbsp;移动到 <code>(1, 1)</code> 回到了上一次移动时的格子。</p>

<p>如果 <code>grid</code>&nbsp;中有相同值形成的环，请你返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e1.png" style="height: 152px; width: 231px;"></strong></p>

<pre><strong>输入：</strong>grid = [[&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;]]
<strong>输出：</strong>true
<strong>解释：</strong>如下图所示，有 2 个用不同颜色标出来的环：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e11.png" style="height: 163px; width: 225px;">
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e2.png" style="height: 154px; width: 236px;"></strong></p>

<pre><strong>输入：</strong>grid = [[&quot;c&quot;,&quot;c&quot;,&quot;c&quot;,&quot;a&quot;],[&quot;c&quot;,&quot;d&quot;,&quot;c&quot;,&quot;c&quot;],[&quot;c&quot;,&quot;c&quot;,&quot;e&quot;,&quot;c&quot;],[&quot;f&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]]
<strong>输出：</strong>true
<strong>解释：</strong>如下图所示，只有高亮所示的一个合法环：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e22.png" style="height: 157px; width: 229px;">
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e3.png" style="height: 120px; width: 183px;"></strong></p>

<pre><strong>输入：</strong>grid = [[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;z&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;b&quot;,&quot;a&quot;]]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 500</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>grid</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 提示

1. Keep track of the parent (previous position) to avoid considering an invalid path.
2. Use DFS or BFS and keep track of visited cells to see if there is a cycle.

## 示例

```
[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
[["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
[["a","b","b"],["b","z","b"],["b","b","a"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool containsCycle(vector<vector<char>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean containsCycle(char[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
```

### C

```c
bool containsCycle(char** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ContainsCycle(char[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var containsCycle = function(grid) {
    
};
```

### TypeScript

```typescript
function containsCycle(grid: string[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function containsCycle($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func containsCycle(_ grid: [[Character]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun containsCycle(grid: Array<CharArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool containsCycle(List<List<String>> grid) {
    
  }
}
```

### Go

```golang
func containsCycle(grid [][]byte) bool {
    
}
```

### Ruby

```ruby
# @param {Character[][]} grid
# @return {Boolean}
def contains_cycle(grid)
    
end
```

### Scala

```scala
object Solution {
    def containsCycle(grid: Array[Array[Char]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn contains_cycle(grid: Vec<Vec<char>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (contains-cycle grid)
  (-> (listof (listof char?)) boolean?)
  )
```

### Erlang

```erlang
-spec contains_cycle(Grid :: [[char()]]) -> boolean().
contains_cycle(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec contains_cycle(grid :: [[char]]) :: boolean
  def contains_cycle(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func containsCycle(grid: Array<Array<Rune>>): Bool {

    }
}
```

