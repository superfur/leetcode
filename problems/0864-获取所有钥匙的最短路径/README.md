# 864. 获取所有钥匙的最短路径

## 题目描述

<p>给定一个二维网格&nbsp;<code>grid</code>&nbsp;，其中：</p>

<ul>
	<li><font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'.'</span></span></font></font> 代表一个空房间</li>
	<li><font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'#'</span></span></font></font> 代表一堵墙</li>
	<li><font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'@'</span></span></font></font>&nbsp;是起点</li>
	<li>小写字母代表钥匙</li>
	<li>大写字母代表锁</li>
</ul>

<p>我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。</p>

<p>假设 k&nbsp;为 钥匙/锁 的个数，且满足&nbsp;<code>1 &lt;= k&nbsp;&lt;= 6</code>，字母表中的前 <code>k</code>&nbsp;个字母在网格中都有自己对应的一个小写和一个大写字母。换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。</p>

<p>返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/07/23/lc-keys2.jpg" /></p>

<pre>
<strong>输入：</strong>grid = ["@.a..","###.#","b.A.B"]
<strong>输出：</strong>8
<strong>解释：</strong>目标是获得所有钥匙，而不是打开所有锁。
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/07/23/lc-key2.jpg" /></p>

<pre>
<strong>输入：</strong>grid = ["@..aA","..B#.","....b"]
<strong>输出：</strong>6
</pre>

<p><strong>示例 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-keys3.jpg" />
<pre>
<strong>输入:</strong> grid = ["@Aa"]
<strong>输出:</strong> -1</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 30</code></li>
	<li><code>grid[i][j]</code>&nbsp;只含有&nbsp;<code>'.'</code>,&nbsp;<code>'#'</code>,&nbsp;<code>'@'</code>,&nbsp;<code>'a'-</code><code>'f</code><code>'</code>&nbsp;以及&nbsp;<code>'A'-'F'</code></li>
	<li>钥匙的数目范围是&nbsp;<code>[1, 6]</code>&nbsp;</li>
	<li>每个钥匙都对应一个 <strong>不同</strong> 的字母</li>
	<li>每个钥匙正好打开一个对应的锁</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 广度优先搜索
- 数组
- 矩阵

## 示例

```
["@.a..","###.#","b.A.B"]
["@..aA","..B#.","....b"]
["@Aa"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shortestPathAllKeys(vector<string>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int shortestPathAllKeys(String[] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
```

### C

```c
int shortestPathAllKeys(char** grid, int gridSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShortestPathAllKeys(string[] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} grid
 * @return {number}
 */
var shortestPathAllKeys = function(grid) {
    
};
```

### TypeScript

```typescript
function shortestPathAllKeys(grid: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $grid
     * @return Integer
     */
    function shortestPathAllKeys($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestPathAllKeys(_ grid: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestPathAllKeys(grid: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shortestPathAllKeys(List<String> grid) {
    
  }
}
```

### Go

```golang
func shortestPathAllKeys(grid []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} grid
# @return {Integer}
def shortest_path_all_keys(grid)
    
end
```

### Scala

```scala
object Solution {
    def shortestPathAllKeys(grid: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-path-all-keys grid)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec shortest_path_all_keys(Grid :: [unicode:unicode_binary()]) -> integer().
shortest_path_all_keys(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_path_all_keys(grid :: [String.t]) :: integer
  def shortest_path_all_keys(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestPathAllKeys(grid: Array<String>): Int64 {

    }
}
```

