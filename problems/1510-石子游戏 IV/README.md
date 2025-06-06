# 1510. 石子游戏 IV

## 题目描述

<p>Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。</p>

<p>一开始，有 <code>n</code>&nbsp;个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 <strong>任意</strong>&nbsp;非零 <strong>平方数</strong>&nbsp;个石子。</p>

<p>如果石子堆里没有石子了，则无法操作的玩家输掉游戏。</p>

<p>给你正整数&nbsp;<code>n</code>&nbsp;，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回&nbsp;<code>True</code>&nbsp;，否则返回&nbsp;<code>False</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>true
<strong>解释：</strong>Alice 拿走 1 个石子并赢得胜利，因为 Bob 无法进行任何操作。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>false
<strong>解释：</strong>Alice 只能拿走 1 个石子，然后 Bob 拿走最后一个石子并赢得胜利（2 -&gt; 1 -&gt; 0）。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>true
<strong>解释：</strong>n 已经是一个平方数，Alice 可以一次全拿掉 4 个石子并赢得胜利（4 -&gt; 0）。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>n = 7
<strong>输出：</strong>false
<strong>解释：</strong>当 Bob 采取最优策略时，Alice 无法赢得比赛。
如果 Alice 一开始拿走 4 个石子， Bob 会拿走 1 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -&gt; 3 -&gt; 2 -&gt; 1 -&gt; 0）。
如果 Alice 一开始拿走 1 个石子， Bob 会拿走 4 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -&gt; 6 -&gt; 2 -&gt; 1 -&gt; 0）。</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>n = 17
<strong>输出：</strong>false
<strong>解释：</strong>如果 Bob 采取最优策略，Alice 无法赢得胜利。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划
- 博弈

## 提示

1. Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.

## 示例

```
1
2
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool winnerSquareGame(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean winnerSquareGame(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
```

### C

```c
bool winnerSquareGame(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool WinnerSquareGame(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var winnerSquareGame = function(n) {
    
};
```

### TypeScript

```typescript
function winnerSquareGame(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function winnerSquareGame($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func winnerSquareGame(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun winnerSquareGame(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool winnerSquareGame(int n) {
    
  }
}
```

### Go

```golang
func winnerSquareGame(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def winner_square_game(n)
    
end
```

### Scala

```scala
object Solution {
    def winnerSquareGame(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn winner_square_game(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (winner-square-game n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec winner_square_game(N :: integer()) -> boolean().
winner_square_game(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec winner_square_game(n :: integer) :: boolean
  def winner_square_game(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func winnerSquareGame(n: Int64): Bool {

    }
}
```

