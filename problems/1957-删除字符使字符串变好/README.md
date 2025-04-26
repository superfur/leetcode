# 1957. 删除字符使字符串变好

## 题目描述

<p>一个字符串如果没有 <strong>三个连续</strong>&nbsp;相同字符，那么它就是一个 <strong>好字符串</strong>&nbsp;。</p>

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，请你从 <code>s</code>&nbsp;删除&nbsp;<strong>最少</strong>&nbsp;的字符，使它变成一个 <strong>好字符串</strong> 。</p>

<p>请你返回删除后的字符串。题目数据保证答案总是 <strong>唯一的 </strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "le<strong>e</strong>etcode"
<b>输出：</b>"leetcode"
<strong>解释：</strong>
从第一组 'e' 里面删除一个 'e' ，得到 "leetcode" 。
没有连续三个相同字符，所以返回 "leetcode" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "<strong>a</strong>aab<strong>aa</strong>aa"
<b>输出：</b>"aabaa"
<strong>解释：</strong>
从第一组 'a' 里面删除一个 'a' ，得到 "aabaaaa" 。
从第二组 'a' 里面删除两个 'a' ，得到 "aabaa" 。
没有连续三个相同字符，所以返回 "aabaa" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = "aab"
<b>输出：</b>"aab"
<b>解释：</b>没有连续三个相同字符，所以返回 "aab" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. What's the optimal way to delete characters if three or more consecutive characters are equal?
2. If three or more consecutive characters are equal, keep two of them and delete the rest.

## 示例

```
"leeetcode"
"aaabaaaa"
"aab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string makeFancyString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String makeFancyString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def makeFancyString(self, s: str) -> str:
        
```

### C

```c
char* makeFancyString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string MakeFancyString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
    
};
```

### TypeScript

```typescript
function makeFancyString(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function makeFancyString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeFancyString(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeFancyString(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String makeFancyString(String s) {
    
  }
}
```

### Go

```golang
func makeFancyString(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def make_fancy_string(s)
    
end
```

### Scala

```scala
object Solution {
    def makeFancyString(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (make-fancy-string s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec make_fancy_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_fancy_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_fancy_string(s :: String.t) :: String.t
  def make_fancy_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeFancyString(s: String): String {

    }
}
```

