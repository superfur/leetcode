# 1025. 除数博弈

## 题目描述

<p>爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。</p>

<p>最初，黑板上有一个数字&nbsp;<code>n</code>&nbsp;。在每个玩家的回合，玩家需要执行以下操作：</p>

<ul>
	<li>选出任一&nbsp;<code>x</code>，满足&nbsp;<code>0 &lt; x &lt; n</code>&nbsp;且&nbsp;<code>n % x == 0</code>&nbsp;。</li>
	<li>用 <code>n - x</code>&nbsp;替换黑板上的数字&nbsp;<code>n</code> 。</li>
</ul>

<p>如果玩家无法执行这些操作，就会输掉游戏。</p>

<p><em>只有在爱丽丝在游戏中取得胜利时才返回&nbsp;<code>true</code>&nbsp;。假设两个玩家都以最佳状态参与游戏。</em></p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>true
<strong>解释：</strong>爱丽丝选择 1，鲍勃无法进行操作。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>false
<strong>解释：</strong>爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 脑筋急转弯
- 数学
- 动态规划
- 博弈

## 提示

1. If the current number is even, we can always subtract a 1 to make it odd.  If the current number is odd, we must subtract an odd number to make it even.

## 示例

```
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool divisorGame(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean divisorGame(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def divisorGame(self, n: int) -> bool:
        
```

### C

```c
bool divisorGame(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool DivisorGame(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var divisorGame = function(n) {
    
};
```

### TypeScript

```typescript
function divisorGame(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function divisorGame($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divisorGame(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divisorGame(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool divisorGame(int n) {
    
  }
}
```

### Go

```golang
func divisorGame(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def divisor_game(n)
    
end
```

### Scala

```scala
object Solution {
    def divisorGame(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divisor_game(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (divisor-game n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec divisor_game(N :: integer()) -> boolean().
divisor_game(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divisor_game(n :: integer) :: boolean
  def divisor_game(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divisorGame(n: Int64): Bool {

    }
}
```

