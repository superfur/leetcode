# 1316. 不同的循环子字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>text</code> ，请你返回满足下述条件的&nbsp;<strong>不同</strong> 非空子字符串的数目：</p>

<ul>
	<li>可以写成某个字符串与其自身相连接的形式（即，可以写为 <code>a&nbsp;+ a</code>，其中 <code>a</code> 是某个字符串）。</li>
</ul>

<p>例如，<code>abcabc</code>&nbsp;就是&nbsp;<code>abc</code>&nbsp;和它自身连接形成的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>text = &quot;abcabcabc&quot;
<strong>输出：</strong>3
<strong>解释：</strong>3 个子字符串分别为 &quot;abcabc&quot;，&quot;bcabca&quot; 和 &quot;cabcab&quot; 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>text = &quot;leetcodeleetcode&quot;
<strong>输出：</strong>2
<strong>解释：</strong>2 个子字符串为 &quot;ee&quot; 和 &quot;leetcodeleetcode&quot; 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 2000</code></li>
	<li><code>text</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 字典树
- 字符串
- 哈希函数
- 滚动哈希

## 提示

1. Given a substring of the text, how to check if it can be written as the concatenation of a string with itself ?
2. We can do that in linear time, a faster way is to use hashing.
3. Try all substrings and use hashing to check them.

## 示例

```
"abcabcabc"
"leetcodeleetcode"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distinctEchoSubstrings(string text) {
        
    }
};
```

### Java

```java
class Solution {
    public int distinctEchoSubstrings(String text) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        
```

### C

```c
int distinctEchoSubstrings(char* text) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistinctEchoSubstrings(string text) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var distinctEchoSubstrings = function(text) {
    
};
```

### TypeScript

```typescript
function distinctEchoSubstrings(text: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function distinctEchoSubstrings($text) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distinctEchoSubstrings(_ text: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distinctEchoSubstrings(text: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distinctEchoSubstrings(String text) {
    
  }
}
```

### Go

```golang
func distinctEchoSubstrings(text string) int {
    
}
```

### Ruby

```ruby
# @param {String} text
# @return {Integer}
def distinct_echo_substrings(text)
    
end
```

### Scala

```scala
object Solution {
    def distinctEchoSubstrings(text: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distinct_echo_substrings(text: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distinct-echo-substrings text)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec distinct_echo_substrings(Text :: unicode:unicode_binary()) -> integer().
distinct_echo_substrings(Text) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distinct_echo_substrings(text :: String.t) :: integer
  def distinct_echo_substrings(text) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distinctEchoSubstrings(text: String): Int64 {

    }
}
```

