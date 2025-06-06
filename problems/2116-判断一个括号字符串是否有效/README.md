# 2116. 判断一个括号字符串是否有效

## 题目描述

<p>一个括号字符串是只由&nbsp;<code>'('</code> 和&nbsp;<code>')'</code>&nbsp;组成的&nbsp;<strong>非空</strong>&nbsp;字符串。如果一个字符串满足下面 <b>任意</b>&nbsp;一个条件，那么它就是有效的：</p>

<ul>
	<li>字符串为&nbsp;<code>()</code>.</li>
	<li>它可以表示为 <code>AB</code><span style="">（</span><code>A</code>&nbsp;与&nbsp;<code>B</code>&nbsp;连接），其中<code>A</code> 和&nbsp;<code>B</code>&nbsp;都是有效括号字符串。</li>
	<li>它可以表示为&nbsp;<code>(A)</code>&nbsp;，其中&nbsp;<code>A</code>&nbsp;是一个有效括号字符串。</li>
</ul>

<p>给你一个括号字符串&nbsp;<code>s</code>&nbsp;和一个字符串&nbsp;<code>locked</code>&nbsp;，两者长度都为&nbsp;<code>n</code>&nbsp;。<code>locked</code>&nbsp;是一个二进制字符串，只包含&nbsp;<code>'0'</code>&nbsp;和&nbsp;<code>'1'</code>&nbsp;。对于&nbsp;<code>locked</code>&nbsp;中&nbsp;<strong>每一个</strong>&nbsp;下标&nbsp;<code>i</code> ：</p>

<ul>
	<li>如果&nbsp;<code>locked[i]</code>&nbsp;是&nbsp;<code>'1'</code>&nbsp;，你 <strong>不能</strong>&nbsp;改变&nbsp;<code>s[i]</code>&nbsp;。</li>
	<li>如果&nbsp;<code>locked[i]</code>&nbsp;是&nbsp;<code>'0'</code>&nbsp;，你&nbsp;<strong>可以</strong>&nbsp;将&nbsp;<code>s[i]</code>&nbsp;变为&nbsp;<code>'('</code>&nbsp;或者&nbsp;<code>')'</code>&nbsp;。</li>
</ul>

<p>如果你可以将 <code>s</code>&nbsp;变为有效括号字符串，请你返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/11/06/eg1.png" style="width: 311px; height: 101px;" /></p>

<pre>
<b>输入：</b>s = "))()))", locked = "010100"
<b>输出：</b>true
<b>解释：</b>locked[1] == '1' 和 locked[3] == '1' ，所以我们无法改变 s[1] 或者 s[3] 。
我们可以将 s[0] 和 s[4] 变为 '(' ，不改变 s[2] 和 s[5] ，使 s 变为有效字符串。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "()()", locked = "0000"
<b>输出：</b>true
<b>解释：</b>我们不需要做任何改变，因为 s 已经是有效字符串了。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = ")", locked = "0"
<b>输出：</b>false
<b>解释：</b>locked 允许改变 s[0] 。
但无论将 s[0] 变为 '(' 或者 ')' 都无法使 s 变为有效字符串。
</pre>

<p><strong class="example">示例 4：</strong></p>

<pre>
<b>输入：</b>s = "(((())(((())", locked = "111111010111"
<b>输出：</b>true
<b>解释：</b>locked 允许我们改变 s[6] 和 s[8]。
我们将 s[6] 和 s[8] 改为 ')' 使 s 变为有效字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == s.length == locked.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code>&nbsp;要么是&nbsp;<code>'('</code>&nbsp;要么是&nbsp;<code>')'</code>&nbsp;。</li>
	<li><code>locked[i]</code> 要么是&nbsp;<code>'0'</code>&nbsp;要么是&nbsp;<code>'1'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串

## 提示

1. Can an odd length string ever be valid?
2. From left to right, if a locked ')' is encountered, it must be balanced with either a locked '(' or an unlocked index on its left. If neither exist, what conclusion can be drawn? If both exist, which one is more preferable to use?
3. After the above, we may have locked indices of '(' and additional unlocked indices. How can you balance out the locked '(' now? What if you cannot balance any locked '('?

## 示例

```
"))()))"
"010100"
"()()"
"0000"
")"
"0"
"(((())(((())"
"111111010111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canBeValid(string s, string locked) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canBeValid(String s, String locked) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
```

### C

```c
bool canBeValid(char* s, char* locked) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanBeValid(string s, string locked) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
var canBeValid = function(s, locked) {
    
};
```

### TypeScript

```typescript
function canBeValid(s: string, locked: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $locked
     * @return Boolean
     */
    function canBeValid($s, $locked) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canBeValid(_ s: String, _ locked: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canBeValid(s: String, locked: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canBeValid(String s, String locked) {
    
  }
}
```

### Go

```golang
func canBeValid(s string, locked string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} locked
# @return {Boolean}
def can_be_valid(s, locked)
    
end
```

### Scala

```scala
object Solution {
    def canBeValid(s: String, locked: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_be_valid(s: String, locked: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-be-valid s locked)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec can_be_valid(S :: unicode:unicode_binary(), Locked :: unicode:unicode_binary()) -> boolean().
can_be_valid(S, Locked) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_be_valid(s :: String.t, locked :: String.t) :: boolean
  def can_be_valid(s, locked) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canBeValid(s: String, locked: String): Bool {

    }
}
```

