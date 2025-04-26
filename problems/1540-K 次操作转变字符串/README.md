# 1540. K 次操作转变字符串

## 题目描述

<p>给你两个字符串&nbsp;<code>s</code>&nbsp;和&nbsp;<code>t</code>&nbsp;，你的目标是在 <code>k</code>&nbsp;次操作以内把字符串&nbsp;<code>s</code>&nbsp;转变成&nbsp;<code>t</code>&nbsp;。</p>

<p>在第 <code>i</code>&nbsp;次操作时（<code>1 &lt;= i &lt;= k</code>），你可以选择进行如下操作：</p>

<ul>
	<li>选择字符串 <code>s</code>&nbsp;中满足 <code>1 &lt;= j &lt;= s.length</code>&nbsp;且之前未被选过的任意下标 <code>j</code>&nbsp;（下标从 1 开始），并将此位置的字符切换 <code>i</code>&nbsp;次。</li>
	<li>不进行任何操作。</li>
</ul>

<p>切换 1 个字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 <code>'z'</code>&nbsp;切换后会变成 <code>'a'</code>）。第 <code>i</code>&nbsp;次操作意味着该字符应切换&nbsp;<code>i</code>&nbsp;次</p>

<p>请记住任意一个下标 <code>j</code>&nbsp;最多只能被操作&nbsp;1 次。</p>

<p>如果在不超过 <code>k</code>&nbsp;次操作内可以把字符串 <code>s</code>&nbsp;转变成 <code>t</code>&nbsp;，那么请你返回&nbsp;<code>true</code>&nbsp;，否则请你返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "input", t = "ouput", k = 9
<strong>输出：</strong>true
<strong>解释：</strong>第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abc", t = "bcd", k = 10
<strong>输出：</strong>false
<strong>解释：</strong>我们需要将每个字符切换 1 次才能得到 t 。我们可以在第 1 次操作时将 'a' 切换成 'b' ，但另外 2 个字母在剩余操作中无法再转变为 t 中对应字母。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "aab", t = "bbb", k = 27
<strong>输出：</strong>true
<strong>解释：</strong>第 1 次操作时，我们将第一个 'a' 切换 1 次得到 'b' 。在第 27 次操作时，我们将第二个字母 'a' 切换 27 次得到 'b' 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= k &lt;= 10^9</code></li>
	<li><code>s</code>&nbsp;和&nbsp;<code>t</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串

## 提示

1. Observe that shifting a letter x times has the same effect of shifting the letter x + 26 times.
2. You need to check whether k is large enough to cover all shifts with the same remainder after modulo 26.

## 示例

```
"input"
"ouput"
9
"abc"
"bcd"
10
"aab"
"bbb"
27
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canConvertString(string s, string t, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canConvertString(String s, String t, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
```

### C

```c
bool canConvertString(char* s, char* t, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanConvertString(string s, string t, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number} k
 * @return {boolean}
 */
var canConvertString = function(s, t, k) {
    
};
```

### TypeScript

```typescript
function canConvertString(s: string, t: string, k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer $k
     * @return Boolean
     */
    function canConvertString($s, $t, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canConvertString(_ s: String, _ t: String, _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canConvertString(s: String, t: String, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canConvertString(String s, String t, int k) {
    
  }
}
```

### Go

```golang
func canConvertString(s string, t string, k int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Boolean}
def can_convert_string(s, t, k)
    
end
```

### Scala

```scala
object Solution {
    def canConvertString(s: String, t: String, k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_convert_string(s: String, t: String, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-convert-string s t k)
  (-> string? string? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_convert_string(S :: unicode:unicode_binary(), T :: unicode:unicode_binary(), K :: integer()) -> boolean().
can_convert_string(S, T, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_convert_string(s :: String.t, t :: String.t, k :: integer) :: boolean
  def can_convert_string(s, t, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canConvertString(s: String, t: String, k: Int64): Bool {

    }
}
```

