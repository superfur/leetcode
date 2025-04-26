# 1156. 单字符重复子串的最大长度

## 题目描述

<p>如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。</p>

<p>给你一个字符串&nbsp;<code>text</code>，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>text = &quot;ababa&quot;
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>text = &quot;aaabaaa&quot;
<strong>输出：</strong>6
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>text = &quot;aaabbaaa&quot;
<strong>输出：</strong>4
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>text = &quot;aaaaa&quot;
<strong>输出：</strong>5
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>text = &quot;abcdef&quot;
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 20000</code></li>
	<li><code>text</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. There are two cases:  a block of characters, or two blocks of characters between one different character. 
 By keeping a run-length encoded version of the string, we can easily check these cases.

## 示例

```
"ababa"
"aaabaaa"
"aaaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxRepOpt1(string text) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxRepOpt1(String text) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
```

### C

```c
int maxRepOpt1(char* text) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxRepOpt1(string text) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var maxRepOpt1 = function(text) {
    
};
```

### TypeScript

```typescript
function maxRepOpt1(text: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function maxRepOpt1($text) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxRepOpt1(_ text: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxRepOpt1(text: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxRepOpt1(String text) {
    
  }
}
```

### Go

```golang
func maxRepOpt1(text string) int {
    
}
```

### Ruby

```ruby
# @param {String} text
# @return {Integer}
def max_rep_opt1(text)
    
end
```

### Scala

```scala
object Solution {
    def maxRepOpt1(text: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_rep_opt1(text: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-rep-opt1 text)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_rep_opt1(Text :: unicode:unicode_binary()) -> integer().
max_rep_opt1(Text) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_rep_opt1(text :: String.t) :: integer
  def max_rep_opt1(text) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxRepOpt1(text: String): Int64 {

    }
}
```

