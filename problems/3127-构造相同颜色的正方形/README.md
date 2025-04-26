# 3127. 构造相同颜色的正方形

## 题目描述

<p>给你一个二维 <code>3 x 3</code>&nbsp;的矩阵&nbsp;<code>grid</code>&nbsp;，每个格子都是一个字符，要么是&nbsp;<code>'B'</code>&nbsp;，要么是&nbsp;<code>'W'</code>&nbsp;。字符&nbsp;<code>'W'</code>&nbsp;表示白色，字符&nbsp;<code>'B'</code>&nbsp;表示黑色。</p>

<p>你的任务是改变 <strong>至多一个</strong>&nbsp;格子的颜色，使得矩阵中存在一个 <code>2 x 2</code>&nbsp;颜色完全相同的正方形。<!-- notionvc: adf957e1-fa0f-40e5-9a2e-933b95e276a7 --></p>

<p>如果可以得到一个相同颜色的 <code>2 x 2</code>&nbsp;正方形，那么返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>
<style type="text/css">.grid-container {
  display: grid;
  grid-template-columns: 30px 30px 30px;
  padding: 10px;
}
.grid-item {
  background-color: black;
  border: 1px solid gray;
  height: 30px;
  font-size: 30px;
  text-align: center;
}
.grid-item-white {
  background-color: white;
}
</style>
<style class="darkreader darkreader--sync" media="screen" type="text/css">
</style>
<p><strong class="example">示例 1：</strong></p>

<div class="grid-container">
<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>
</div>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [["B","W","B"],["B","W","W"],["B","W","B"]]</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><strong>解释：</strong></p>

<p>修改&nbsp;<code>grid[0][2]</code> 的颜色，可以满足要求。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="grid-container">
<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>
</div>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [["B","W","B"],["W","B","W"],["B","W","B"]]</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><strong>解释：</strong></p>

<p>只改变一个格子颜色无法满足要求。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="grid-container">
<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>

<div class="grid-item grid-item-white">&nbsp;</div>
</div>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [["B","W","B"],["B","W","W"],["B","W","W"]]</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><strong>解释：</strong></p>

<p><code>grid</code>&nbsp;已经包含一个&nbsp;<code>2 x 2</code>&nbsp;颜色相同的正方形了。<!-- notionvc: 9a8b2d3d-1e73-457a-abe0-c16af51ad5c2 --></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>grid.length == 3</code></li>
	<li><code>grid[i].length == 3</code></li>
	<li><code>grid[i][j]</code>&nbsp;要么是&nbsp;<code>'W'</code>&nbsp;，要么是&nbsp;<code>'B'</code> 。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举
- 矩阵

## 提示

1. It is impossible to create <code>2 x 2</code> square with the same color by changing the color of at most one cell when the number of <code>‘W'</code> or <code>'B’</code> in all squares is 2.

## 示例

```
[["B","W","B"],["B","W","W"],["B","W","B"]]
[["B","W","B"],["W","B","W"],["B","W","B"]]
[["B","W","B"],["B","W","W"],["B","W","W"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canMakeSquare(vector<vector<char>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canMakeSquare(char[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        
```

### C

```c
bool canMakeSquare(char** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanMakeSquare(char[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var canMakeSquare = function(grid) {
    
};
```

### TypeScript

```typescript
function canMakeSquare(grid: string[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function canMakeSquare($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canMakeSquare(_ grid: [[Character]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canMakeSquare(grid: Array<CharArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canMakeSquare(List<List<String>> grid) {
    
  }
}
```

### Go

```golang
func canMakeSquare(grid [][]byte) bool {
    
}
```

### Ruby

```ruby
# @param {Character[][]} grid
# @return {Boolean}
def can_make_square(grid)
    
end
```

### Scala

```scala
object Solution {
    def canMakeSquare(grid: Array[Array[Char]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_make_square(grid: Vec<Vec<char>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-make-square grid)
  (-> (listof (listof char?)) boolean?)
  )
```

### Erlang

```erlang
-spec can_make_square(Grid :: [[char()]]) -> boolean().
can_make_square(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_make_square(grid :: [[char]]) :: boolean
  def can_make_square(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canMakeSquare(grid: Array<Array<Rune>>): Bool {

    }
}
```

