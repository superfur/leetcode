# 2840. 判断通过操作能否让字符串相等 II

## 题目描述

<p>给你两个字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;，两个字符串长度都为&nbsp;<code>n</code>&nbsp;，且只包含&nbsp;<strong>小写&nbsp;</strong>英文字母。</p>

<p>你可以对两个字符串中的 <strong>任意一个</strong>&nbsp;执行以下操作 <strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>选择两个下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;，满足 <code>i &lt; j</code>&nbsp;且 <code>j - i</code>&nbsp;是 <strong>偶数</strong>，然后 <strong>交换</strong> 这个字符串中两个下标对应的字符。</li>
</ul>

<p>&nbsp;</p>

<p>如果你可以让字符串<em>&nbsp;</em><code>s1</code><em> </em>和<em>&nbsp;</em><code>s2</code>&nbsp;相等，那么返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s1 = "abcdba", s2 = "cabdab"
<b>输出：</b>true
<b>解释：</b>我们可以对 s1 执行以下操作：
- 选择下标 i = 0 ，j = 2 ，得到字符串 s1 = "cbadba" 。
- 选择下标 i = 2 ，j = 4 ，得到字符串 s1 = "cbbdaa" 。
- 选择下标 i = 1 ，j = 5 ，得到字符串 s1 = "cabdab" = s2 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s1 = "abe", s2 = "bea"
<b>输出：</b>false
<b>解释：</b>无法让两个字符串相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == s1.length == s2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s1</code> 和&nbsp;<code>s2</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 排序

## 提示

1. <div class="_1l1MA">Characters in two positions can be swapped if and only if the two positions have the same parity.</div>
2. <div class="_1l1MA">To be able to make the two strings equal, the characters at even and odd positions in the strings should be the same.</div>

## 示例

```
"abcdba"
"cabdab"
"abe"
"bea"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkStrings(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkStrings(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
```

### C

```c
bool checkStrings(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckStrings(string s1, string s2) {
        
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
var checkStrings = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function checkStrings(s1: string, s2: string): boolean {
    
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
    function checkStrings($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkStrings(_ s1: String, _ s2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkStrings(s1: String, s2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkStrings(String s1, String s2) {
    
  }
}
```

### Go

```golang
func checkStrings(s1 string, s2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_strings(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def checkStrings(s1: String, s2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_strings(s1: String, s2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-strings s1 s2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec check_strings(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
check_strings(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_strings(s1 :: String.t, s2 :: String.t) :: boolean
  def check_strings(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkStrings(s1: String, s2: String): Bool {

    }
}
```

