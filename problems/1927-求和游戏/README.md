# 1927. 求和游戏

## 题目描述

<p>Alice 和 Bob 玩一个游戏，两人轮流行动，<strong>Alice 先手</strong> 。</p>

<p>给你一个 <strong>偶数长度</strong> 的字符串 <code>num</code> ，每一个字符为数字字符或者 <code>'?'</code> 。每一次操作中，如果 <code>num</code> 中至少有一个 <code>'?'</code> ，那么玩家可以执行以下操作：</p>

<ol>
	<li>选择一个下标 <code>i</code> 满足 <code>num[i] == '?'</code> 。</li>
	<li>将 <code>num[i]</code> 用 <code>'0'</code> 到 <code>'9'</code> 之间的一个数字字符替代。</li>
</ol>

<p>当 <code>num</code> 中没有<span style=""> </span><code>'?'</code> 时，游戏结束。</p>

<p>Bob 获胜的条件是 <code>num</code> 中前一半数字的和 <strong>等于</strong> 后一半数字的和。Alice 获胜的条件是前一半的和与后一半的和 <strong>不相等</strong> 。</p>

<ul>
	<li>比方说，游戏结束时 <code>num = "243801"</code> ，那么 Bob 获胜，因为 <code>2+4+3 = 8+0+1</code> 。如果游戏结束时 <code>num = "243803"</code> ，那么 Alice 获胜，因为 <code>2+4+3 != 8+0+3</code> 。</li>
</ul>

<p>在 Alice 和 Bob 都采取 <strong>最优</strong> 策略的前提下，如果 Alice 获胜，请返回 <code>true</code> ，如果 Bob 获胜，请返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = "5023"
<b>输出：</b>false
<b>解释：</b>num 中没有 '?' ，没法进行任何操作。
前一半的和等于后一半的和：5 + 0 = 2 + 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = "25??"
<b>输出：</b>true
<strong>解释：</strong>Alice 可以将两个 '?' 中的一个替换为 '9' ，Bob 无论如何都无法使前一半的和等于后一半的和。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>num = "?3295???"
<b>输出：</b>false
<b>解释：</b>Bob 总是能赢。一种可能的结果是：
- Alice 将第一个 '?' 用 '9' 替换。num = "93295???" 。
- Bob 将后面一半中的一个 '?' 替换为 '9' 。num = "932959??" 。
- Alice 将后面一半中的一个 '?' 替换为 '2' 。num = "9329592?" 。
- Bob 将后面一半中最后一个 '?' 替换为 '7' 。num = "93295927" 。
Bob 获胜，因为 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= num.length <= 10<sup>5</sup></code></li>
	<li><code>num.length</code> 是 <strong>偶数</strong> 。</li>
	<li><code>num</code> 只包含数字字符和 <code>'?'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学
- 字符串
- 博弈

## 提示

1. Bob can always make the total sum of both sides equal in mod 9.
2. Why does the difference between the number of question marks on the left and right side matter?

## 示例

```
"5023"
"25??"
"?3295???"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool sumGame(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean sumGame(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def sumGame(self, num: str) -> bool:
        
```

### C

```c
bool sumGame(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public bool SumGame(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {boolean}
 */
var sumGame = function(num) {
    
};
```

### TypeScript

```typescript
function sumGame(num: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function sumGame($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumGame(_ num: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumGame(num: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool sumGame(String num) {
    
  }
}
```

### Go

```golang
func sumGame(num string) bool {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {Boolean}
def sum_game(num)
    
end
```

### Scala

```scala
object Solution {
    def sumGame(num: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_game(num: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (sum-game num)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec sum_game(Num :: unicode:unicode_binary()) -> boolean().
sum_game(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_game(num :: String.t) :: boolean
  def sum_game(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumGame(num: String): Bool {

    }
}
```

