# 1871. 跳跃游戏 VII

## 题目描述

<p>给你一个下标从 <strong>0 </strong>开始的二进制字符串 <code>s</code> 和两个整数 <code>minJump</code> 和 <code>maxJump</code> 。一开始，你在下标 <code>0</code> 处，且该位置的值一定为 <code>'0'</code> 。当同时满足如下条件时，你可以从下标 <code>i</code> 移动到下标 <code>j</code> 处：</p>

<ul>
	<li><code>i + minJump <= j <= min(i + maxJump, s.length - 1)</code> 且</li>
	<li><code>s[j] == '0'</code>.</li>
</ul>

<p>如果你可以到达 <code>s</code> 的下标<i> </i><code>s.length - 1</code> 处，请你返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "<strong>0</strong>11<strong>0</strong>1<strong>0</strong>", minJump = 2, maxJump = 3
<b>输出：</b>true
<strong>解释：</strong>
第一步，从下标 0 移动到下标 3 。
第二步，从下标 3 移动到下标 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "01101110", minJump = 2, maxJump = 3
<b>输出：</b>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 要么是 <code>'0'</code> ，要么是 <code>'1'</code></li>
	<li><code>s[0] == '0'</code></li>
	<li><code>1 <= minJump <= maxJump < s.length</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划
- 前缀和
- 滑动窗口

## 提示

1. Consider for each reachable index i the interval [i + a, i + b].
2. Use partial sums to mark the intervals as reachable.

## 示例

```
"011010"
2
3
"01101110"
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
```

### C

```c
bool canReach(char* s, int minJump, int maxJump) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanReach(string s, int minJump, int maxJump) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} minJump
 * @param {number} maxJump
 * @return {boolean}
 */
var canReach = function(s, minJump, maxJump) {
    
};
```

### TypeScript

```typescript
function canReach(s: string, minJump: number, maxJump: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $minJump
     * @param Integer $maxJump
     * @return Boolean
     */
    function canReach($s, $minJump, $maxJump) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canReach(_ s: String, _ minJump: Int, _ maxJump: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canReach(s: String, minJump: Int, maxJump: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canReach(String s, int minJump, int maxJump) {
    
  }
}
```

### Go

```golang
func canReach(s string, minJump int, maxJump int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} min_jump
# @param {Integer} max_jump
# @return {Boolean}
def can_reach(s, min_jump, max_jump)
    
end
```

### Scala

```scala
object Solution {
    def canReach(s: String, minJump: Int, maxJump: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-reach s minJump maxJump)
  (-> string? exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_reach(S :: unicode:unicode_binary(), MinJump :: integer(), MaxJump :: integer()) -> boolean().
can_reach(S, MinJump, MaxJump) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_reach(s :: String.t, min_jump :: integer, max_jump :: integer) :: boolean
  def can_reach(s, min_jump, max_jump) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canReach(s: String, minJump: Int64, maxJump: Int64): Bool {

    }
}
```

