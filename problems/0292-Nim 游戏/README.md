# 292. Nim 游戏

## 题目描述

<p>你和你的朋友，两个人一起玩&nbsp;<a href="https://baike.baidu.com/item/Nim游戏/6737105" target="_blank">Nim 游戏</a>：</p>

<ul>
	<li>桌子上有一堆石头。</li>
	<li>你们轮流进行自己的回合，&nbsp;<strong>你作为先手&nbsp;</strong>。</li>
	<li>每一回合，轮到的人拿掉&nbsp;1 - 3 块石头。</li>
	<li>拿掉最后一块石头的人就是获胜者。</li>
</ul>

<p>假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 <code>n</code> 的情况下赢得游戏。如果可以赢，返回 <code>true</code>；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>n = 4</code>
<strong>输出：</strong>false 
<strong>解释：</strong>以下是可能的结果:
1. 移除1颗石头。你的朋友移走了3块石头，包括最后一块。你的朋友赢了。
2. 移除2个石子。你的朋友移走2块石头，包括最后一块。你的朋友赢了。
3.你移走3颗石子。你的朋友移走了最后一块石头。你的朋友赢了。
在所有结果中，你的朋友是赢家。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Easy

## 标签

- 脑筋急转弯
- 数学
- 博弈

## 提示

1. If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?

## 示例

```
4
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canWinNim(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canWinNim(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canWinNim(self, n: int) -> bool:
        
```

### C

```c
bool canWinNim(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanWinNim(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var canWinNim = function(n) {
    
};
```

### TypeScript

```typescript
function canWinNim(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function canWinNim($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canWinNim(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canWinNim(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canWinNim(int n) {
    
  }
}
```

### Go

```golang
func canWinNim(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def can_win_nim(n)
    
end
```

### Scala

```scala
object Solution {
    def canWinNim(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_win_nim(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-win-nim n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_win_nim(N :: integer()) -> boolean().
can_win_nim(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_win_nim(n :: integer) :: boolean
  def can_win_nim(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canWinNim(n: Int64): Bool {

    }
}
```

