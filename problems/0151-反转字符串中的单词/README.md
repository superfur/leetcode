# 151. 反转字符串中的单词

## 题目描述

<p>给你一个字符串 <code>s</code> ，请你反转字符串中 <strong>单词</strong> 的顺序。</p>

<p><strong>单词</strong> 是由非空格字符组成的字符串。<code>s</code> 中使用至少一个空格将字符串中的 <strong>单词</strong> 分隔开。</p>

<p>返回 <strong>单词</strong> 顺序颠倒且 <strong>单词</strong> 之间用单个空格连接的结果字符串。</p>

<p><strong>注意：</strong>输入字符串 <code>s</code>中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "the sky is blue"
<strong>输出：</strong>"blue is sky the"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = " &nbsp;hello world &nbsp;"
<strong>输出：</strong>"world hello"
<strong>解释：</strong>反转后的字符串中不能存在前导空格和尾随空格。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "a good &nbsp; example"
<strong>输出：</strong>"example good a"
<strong>解释：</strong>如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 包含英文大小写字母、数字和空格 <code>' '</code></li>
	<li><code>s</code> 中 <strong>至少存在一个</strong> 单词</li>
</ul>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用&nbsp;<code>O(1)</code> 额外空间复杂度的 <strong>原地</strong> 解法。</p>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 示例

```
"the sky is blue"
"  hello world  "
"a good   example"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reverseWords(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String reverseWords(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        
```

### C

```c
char* reverseWords(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReverseWords(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    
};
```

### TypeScript

```typescript
function reverseWords(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseWords($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reverseWords(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reverseWords(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reverseWords(String s) {
    
  }
}
```

### Go

```golang
func reverseWords(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def reverse_words(s)
    
end
```

### Scala

```scala
object Solution {
    def reverseWords(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_words(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-words s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec reverse_words(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_words(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_words(s :: String.t) :: String.t
  def reverse_words(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reverseWords(s: String): String {

    }
}
```

