# LCP 13. 寻宝

## 题目描述

<p>我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。</p>

<p>迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 &#39;S&#39; 表示），和唯一的宝藏地点（用 &#39;T&#39; 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 &#39;M&#39; 表示），<strong>只有所有机关均被触发，才可以拿到宝藏。</strong></p>

<p>要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 &#39;O&#39; 表示），每个石堆都有<strong>无限</strong>个足够触发机关的重石。但是由于石头太重，我们一次只能搬<strong>一个</strong>石头到指定地点。</p>

<p>迷宫中同样有一些墙壁（用 &#39;#&#39; 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 &#39;.&#39; 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。</p>

<p>我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入： [&quot;S#O&quot;, &quot;M..&quot;, &quot;M.T&quot;]</p>

<p>输出：16</p>

<p>解释：最优路线为： S-&gt;O, cost = 4, 去搬石头 O-&gt;第二行的M, cost = 3, M机关触发 第二行的M-&gt;O, cost = 3, 我们需要继续回去 O 搬石头。 O-&gt;第三行的M, cost = 4, 此时所有机关均触发 第三行的M-&gt;T, cost = 2，去T点拿宝藏。 总步数为16。 <img alt="图片.gif" src="https://pic.leetcode-cn.com/6bfff669ad65d494cdc237bcedfec10a2b1ac2f2593c2bf97e9aecb41dc8a08b-%E5%9B%BE%E7%89%87.gif" /></p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入： [&quot;S#O&quot;, &quot;M.#&quot;, &quot;M.T&quot;]</p>

<p>输出：-1</p>

<p>解释：我们无法搬到石头触发机关</p>
</blockquote>

<p><strong>示例 3：</strong></p>

<blockquote>
<p>输入： [&quot;S#O&quot;, &quot;M.T&quot;, &quot;M..&quot;]</p>

<p>输出：17</p>

<p>解释：注意终点也是可以通行的。</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= maze.length&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;= maze[i].length&nbsp;&lt;= 100</code></li>
	<li><code>maze[i].length == maze[j].length</code></li>
	<li>S 和 T 有且只有一个</li>
	<li>0 &lt;= M的数量 &lt;= 16</li>
	<li>0 &lt;= O的数量 &lt;= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 广度优先搜索
- 数组
- 动态规划
- 状态压缩
- 矩阵

## 示例

```
["S#O", "M..", "M.T"]
["S#O", "M.#", "M.T"]
["S#O", "M.T", "M.."]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimalSteps(vector<string>& maze) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimalSteps(String[] maze) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimalSteps(self, maze):
        """
        :type maze: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        
```

### C

```c
int minimalSteps(char** maze, int mazeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimalSteps(string[] maze) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} maze
 * @return {number}
 */
var minimalSteps = function(maze) {
    
};
```

### TypeScript

```typescript
function minimalSteps(maze: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $maze
     * @return Integer
     */
    function minimalSteps($maze) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimalSteps(_ maze: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimalSteps(maze: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimalSteps(List<String> maze) {
    
  }
}
```

### Go

```golang
func minimalSteps(maze []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} maze
# @return {Integer}
def minimal_steps(maze)
    
end
```

### Scala

```scala
object Solution {
    def minimalSteps(maze: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimal_steps(maze: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimal-steps maze)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimal_steps(Maze :: [unicode:unicode_binary()]) -> integer().
minimal_steps(Maze) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimal_steps(maze :: [String.t]) :: integer
  def minimal_steps(maze) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimalSteps(maze: Array<String>): Int64 {

    }
}
```

