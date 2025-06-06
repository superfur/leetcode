# 1728. 猫和老鼠 II

## 题目描述

<p>一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。</p>

<p>它们所处的环境设定是一个 <code>rows x cols</code> 的方格 <code>grid</code> ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。</p>

<ul>
	<li>玩家由字符 <code>'C'</code> （代表猫）和 <code>'M'</code> （代表老鼠）表示。</li>
	<li>地板由字符 <code>'.'</code> 表示，玩家可以通过这个格子。</li>
	<li>墙用字符 <code>'#'</code> 表示，玩家不能通过这个格子。</li>
	<li>食物用字符 <code>'F'</code> 表示，玩家可以通过这个格子。</li>
	<li>字符 <code>'C'</code> ， <code>'M'</code> 和 <code>'F'</code> 在 <code>grid</code> 中都只会出现一次。</li>
</ul>

<p>猫和老鼠按照如下规则移动：</p>

<ul>
	<li>老鼠 <strong>先移动</strong> ，然后两名玩家轮流移动。</li>
	<li>每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出 <code>grid</code> 。</li>
	<li><code>catJump</code> 和 <code>mouseJump</code> 是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。</li>
	<li>它们可以停留在原地。</li>
	<li>老鼠可以跳跃过猫的位置。</li>
</ul>

<p>游戏有 4 种方式会结束：</p>

<ul>
	<li>如果猫跟老鼠处在相同的位置，那么猫获胜。</li>
	<li>如果猫先到达食物，那么猫获胜。</li>
	<li>如果老鼠先到达食物，那么老鼠获胜。</li>
	<li>如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。</li>
</ul>

<p>给你 <code>rows x cols</code> 的矩阵 <code>grid</code> 和两个整数 <code>catJump</code> 和 <code>mouseJump</code> ，双方都采取最优策略，如果老鼠获胜，那么请你返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/sample_111_1955.png" style="width: 580px; height: 239px;" /></strong></p>

<pre>
<b>输入：</b>grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
<b>输出：</b>true
<b>解释：</b>猫无法抓到老鼠，也没法比老鼠先到达食物。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/sample_2_1955.png" style="width: 580px; height: 175px;" /></p>

<pre>
<b>输入：</b>grid = ["M.C...F"], catJump = 1, mouseJump = 4
<b>输出：</b>true
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>grid = ["M.C...F"], catJump = 1, mouseJump = 3
<b>输出：</b>false
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
<b>输出：</b>false
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<b>输入：</b>grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
<b>输出：</b>true
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rows == grid.length</code></li>
	<li><code>cols = grid[i].length</code></li>
	<li><code>1 <= rows, cols <= 8</code></li>
	<li><code>grid[i][j]</code> 只包含字符 <code>'C'</code> ，<code>'M'</code> ，<code>'F'</code> ，<code>'.'</code> 和 <code>'#'</code> 。</li>
	<li><code>grid</code> 中只包含一个 <code>'C'</code> ，<code>'M'</code> 和 <code>'F'</code> 。</li>
	<li><code>1 <= catJump, mouseJump <= 8</code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 拓扑排序
- 记忆化搜索
- 数组
- 数学
- 动态规划
- 博弈
- 矩阵

## 提示

1. Try working backward: consider all trivial states you know to be winning or losing, and work backward to determine which other states can be labeled as winning or losing.

## 示例

```
["####F","#C...","M...."]
1
2
["M.C...F"]
1
4
["M.C...F"]
1
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canMouseWin(vector<string>& grid, int catJump, int mouseJump) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canMouseWin(String[] grid, int catJump, int mouseJump) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        
```

### C

```c
bool canMouseWin(char** grid, int gridSize, int catJump, int mouseJump) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanMouseWin(string[] grid, int catJump, int mouseJump) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} grid
 * @param {number} catJump
 * @param {number} mouseJump
 * @return {boolean}
 */
var canMouseWin = function(grid, catJump, mouseJump) {
    
};
```

### TypeScript

```typescript
function canMouseWin(grid: string[], catJump: number, mouseJump: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $grid
     * @param Integer $catJump
     * @param Integer $mouseJump
     * @return Boolean
     */
    function canMouseWin($grid, $catJump, $mouseJump) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canMouseWin(_ grid: [String], _ catJump: Int, _ mouseJump: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canMouseWin(grid: Array<String>, catJump: Int, mouseJump: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canMouseWin(List<String> grid, int catJump, int mouseJump) {
    
  }
}
```

### Go

```golang
func canMouseWin(grid []string, catJump int, mouseJump int) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} grid
# @param {Integer} cat_jump
# @param {Integer} mouse_jump
# @return {Boolean}
def can_mouse_win(grid, cat_jump, mouse_jump)
    
end
```

### Scala

```scala
object Solution {
    def canMouseWin(grid: Array[String], catJump: Int, mouseJump: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_mouse_win(grid: Vec<String>, cat_jump: i32, mouse_jump: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-mouse-win grid catJump mouseJump)
  (-> (listof string?) exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_mouse_win(Grid :: [unicode:unicode_binary()], CatJump :: integer(), MouseJump :: integer()) -> boolean().
can_mouse_win(Grid, CatJump, MouseJump) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_mouse_win(grid :: [String.t], cat_jump :: integer, mouse_jump :: integer) :: boolean
  def can_mouse_win(grid, cat_jump, mouse_jump) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canMouseWin(grid: Array<String>, catJump: Int64, mouseJump: Int64): Bool {

    }
}
```

