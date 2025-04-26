# 3222. 求出硬币游戏的赢家

## 题目描述

<p>给你两个 <strong>正</strong>&nbsp;整数&nbsp;<code>x</code>&nbsp;和&nbsp;<code>y</code>&nbsp;，分别表示价值为 75 和 10 的硬币的数目。</p>

<p>Alice 和 Bob 正在玩一个游戏。每一轮中，Alice&nbsp;先进行操作，Bob 后操作。每次操作中，玩家需要拿走价值 <b>总和</b>&nbsp;为 115 的硬币。如果一名玩家无法执行此操作，那么这名玩家 <strong>输掉</strong>&nbsp;游戏。</p>

<p>两名玩家都采取 <strong>最优</strong>&nbsp;策略，请你返回游戏的赢家。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>x = 2, y = 7</span></p>

<p><span class="example-io"><b>输出：</b>"Alice"</span></p>

<p><strong>解释：</strong></p>

<p>游戏一次操作后结束：</p>

<ul>
	<li>Alice 拿走 1 枚价值为 75 的硬币和 4 枚价值为 10 的硬币。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>x = 4, y = 11</span></p>

<p><span class="example-io"><b>输出：</b>"Bob"</span></p>

<p><strong>解释：</strong></p>

<p>游戏 2 次操作后结束：</p>

<ul>
	<li>Alice 拿走&nbsp;1 枚价值为 75 的硬币和 4 枚价值为 10 的硬币。</li>
	<li>Bob 拿走&nbsp;1 枚价值为 75 的硬币和 4 枚价值为 10 的硬币。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x, y &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 博弈
- 模拟

## 提示

1. The only way to make 115 is to use one coin of value 75 and four coins of value 10. Each turn uses up these many coins.
2. Hence the number of turns is <code>min(x, y / 4)</code>.
3. Determine the winner from its parity.

## 示例

```
2
7
4
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string winningPlayer(int x, int y) {
        
    }
};
```

### Java

```java
class Solution {
    public String winningPlayer(int x, int y) {
        
    }
}
```

### Python

```python
class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        
```

### C

```c
char* winningPlayer(int x, int y) {
    
}
```

### C#

```csharp
public class Solution {
    public string WinningPlayer(int x, int y) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @return {string}
 */
var winningPlayer = function(x, y) {
    
};
```

### TypeScript

```typescript
function winningPlayer(x: number, y: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @return String
     */
    function winningPlayer($x, $y) {
        
    }
}
```

### Swift

```swift
class Solution {
    func winningPlayer(_ x: Int, _ y: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun winningPlayer(x: Int, y: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String winningPlayer(int x, int y) {
    
  }
}
```

### Go

```golang
func winningPlayer(x int, y int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @param {Integer} y
# @return {String}
def winning_player(x, y)
    
end
```

### Scala

```scala
object Solution {
    def winningPlayer(x: Int, y: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn winning_player(x: i32, y: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (winning-player x y)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec winning_player(X :: integer(), Y :: integer()) -> unicode:unicode_binary().
winning_player(X, Y) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec winning_player(x :: integer, y :: integer) :: String.t
  def winning_player(x, y) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func winningPlayer(x: Int64, y: Int64): String {

    }
}
```

