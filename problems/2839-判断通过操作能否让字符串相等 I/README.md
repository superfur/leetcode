# 2839. 判断通过操作能否让字符串相等 I

## 题目描述

<p>给你两个字符串&nbsp;<code>s1</code> 和&nbsp;<code>s2</code>&nbsp;，两个字符串的长度都为&nbsp;<code>4</code>&nbsp;，且只包含 <strong>小写</strong> 英文字母。</p>

<p>你可以对两个字符串中的 <strong>任意一个</strong>&nbsp;执行以下操作 <strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>选择两个下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;且满足&nbsp;<code>j - i = 2</code>&nbsp;，然后 <strong>交换</strong> 这个字符串中两个下标对应的字符。</li>
</ul>

<p>如果你可以让字符串<em>&nbsp;</em><code>s1</code><em> </em>和<em>&nbsp;</em><code>s2</code>&nbsp;相等，那么返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s1 = "abcd", s2 = "cdab"
<b>输出：</b>true
<strong>解释：</strong> 我们可以对 s1 执行以下操作：
- 选择下标 i = 0 ，j = 2 ，得到字符串 s1 = "cbad" 。
- 选择下标 i = 1 ，j = 3 ，得到字符串 s1 = "cdab" = s2 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s1 = "abcd", s2 = "dacb"
<b>输出：</b>false
<b>解释：</b>无法让两个字符串相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s1.length == s2.length == 4</code></li>
	<li><code>s1</code> 和&nbsp;<code>s2</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. <div class="_1l1MA">Since the strings are very small you can try a brute-force approach.</div>
2. <div class="_1l1MA">There are only <code>2</code> different swaps that are possible in a string.</div>

## 示例

```
"abcd"
"cdab"
"abcd"
"dacb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canBeEqual(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canBeEqual(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
```

### C

```c
bool canBeEqual(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanBeEqual(string s1, string s2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var canBeEqual = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function canBeEqual(s1: string, s2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function canBeEqual($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canBeEqual(_ s1: String, _ s2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canBeEqual(s1: String, s2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canBeEqual(String s1, String s2) {
    
  }
}
```

### Go

```golang
func canBeEqual(s1 string, s2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def can_be_equal(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def canBeEqual(s1: String, s2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_be_equal(s1: String, s2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-be-equal s1 s2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec can_be_equal(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
can_be_equal(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_be_equal(s1 :: String.t, s2 :: String.t) :: boolean
  def can_be_equal(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canBeEqual(s1: String, s2: String): Bool {

    }
}
```

