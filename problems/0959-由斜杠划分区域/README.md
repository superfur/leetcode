# 959. 由斜杠划分区域

## 题目描述

<p>在由 <code>1 x 1</code> 方格组成的 <code>n&nbsp;x n</code>&nbsp;网格&nbsp;<code>grid</code> 中，每个 <code>1 x 1</code>&nbsp;方块由 <code>'/'</code>、<code>'\'</code> 或空格构成。这些字符会将方块划分为一些共边的区域。</p>

<p>给定网格&nbsp;<code>grid</code>&nbsp;表示为一个字符串数组，返回 <em>区域的数量</em> 。</p>

<p>请注意，反斜杠字符是转义的，因此&nbsp;<code>'\'</code> 用 <code>'\\'</code>&nbsp;表示。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/12/15/1.png" style="height: 200px; width: 200px;" /></p>

<pre>
<strong>输入：</strong>grid = [" /","/ "]
<strong>输出：</strong>2</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/12/15/2.png" style="height: 198px; width: 200px;" /></p>

<pre>
<strong>输入：</strong>grid = [" /","  "]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/12/15/4.png" style="height: 200px; width: 200px;" /></p>

<pre>
<strong>输入：</strong>grid = ["/\\","\\/"]
<strong>输出：</strong>5
<strong>解释：</strong>回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 30</code></li>
	<li><code>grid[i][j]</code> 是&nbsp;<code>'/'</code>、<code>'\'</code>、或&nbsp;<code>' '</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 哈希表
- 矩阵

## 示例

```
[" /","/ "]
[" /","  "]
["/\\","\\/"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int regionsBySlashes(String[] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
```

### C

```c
int regionsBySlashes(char** grid, int gridSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int RegionsBySlashes(string[] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} grid
 * @return {number}
 */
var regionsBySlashes = function(grid) {
    
};
```

### TypeScript

```typescript
function regionsBySlashes(grid: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $grid
     * @return Integer
     */
    function regionsBySlashes($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func regionsBySlashes(_ grid: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun regionsBySlashes(grid: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int regionsBySlashes(List<String> grid) {
    
  }
}
```

### Go

```golang
func regionsBySlashes(grid []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} grid
# @return {Integer}
def regions_by_slashes(grid)
    
end
```

### Scala

```scala
object Solution {
    def regionsBySlashes(grid: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn regions_by_slashes(grid: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (regions-by-slashes grid)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec regions_by_slashes(Grid :: [unicode:unicode_binary()]) -> integer().
regions_by_slashes(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec regions_by_slashes(grid :: [String.t]) :: integer
  def regions_by_slashes(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func regionsBySlashes(grid: Array<String>): Int64 {

    }
}
```

