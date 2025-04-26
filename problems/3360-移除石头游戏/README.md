# 3360. 移除石头游戏

## 题目描述

<p>Alice 和 Bob 在玩一个游戏，他们俩轮流从一堆石头中移除石头，Alice 先进行操作。</p>

<ul>
	<li>Alice 在第一次操作中移除 <strong>恰好</strong>&nbsp;10 个石头。</li>
	<li>接下来的每次操作中，每位玩家移除的石头数 <strong>恰好</strong>&nbsp;为另一位玩家上一次操作的石头数减 1 。</li>
</ul>

<p>第一位没法进行操作的玩家输掉这个游戏。</p>

<p>给你一个正整数&nbsp;<code>n</code>&nbsp;表示一开始石头的数目，如果 Alice 赢下这个游戏，请你返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 12</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>Alice 第一次操作中移除 10 个石头，剩下 2 个石头给 Bob 。</li>
	<li>Bob 无法移除 9 个石头，所以 Alice 赢下游戏。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 1</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><b>解释：</b></p>

<ul>
	<li>Alice 无法移除 10 个石头，所以 Alice 输掉游戏。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. The constraints are small enough that a brute-force solution is feasible.

## 示例

```
12
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canAliceWin(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canAliceWin(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canAliceWin(self, n: int) -> bool:
        
```

### C

```c
bool canAliceWin(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanAliceWin(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var canAliceWin = function(n) {
    
};
```

### TypeScript

```typescript
function canAliceWin(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function canAliceWin($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canAliceWin(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canAliceWin(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canAliceWin(int n) {
    
  }
}
```

### Go

```golang
func canAliceWin(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def can_alice_win(n)
    
end
```

### Scala

```scala
object Solution {
    def canAliceWin(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_alice_win(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-alice-win n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_alice_win(N :: integer()) -> boolean().
can_alice_win(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_alice_win(n :: integer) :: boolean
  def can_alice_win(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canAliceWin(n: Int64): Bool {

    }
}
```

