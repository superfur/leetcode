# 28. 找出字符串中第一个匹配项的下标

## 题目描述

<p>给你两个字符串&nbsp;<code>haystack</code> 和 <code>needle</code> ，请你在 <code>haystack</code> 字符串中找出 <code>needle</code> 字符串的第一个匹配项的下标（下标从 0 开始）。如果&nbsp;<code>needle</code> 不是 <code>haystack</code> 的一部分，则返回&nbsp; <code>-1</code><strong> </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>haystack = "sadbutsad", needle = "sad"
<strong>输出：</strong>0
<strong>解释：</strong>"sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>haystack = "leetcode", needle = "leeto"
<strong>输出：</strong>-1
<strong>解释：</strong>"leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> 和 <code>needle</code> 仅由小写英文字符组成</li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串
- 字符串匹配

## 示例

```
"sadbutsad"
"sad"
"leetcode"
"leeto"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        
    }
};
```

### Java

```java
class Solution {
    public int strStr(String haystack, String needle) {
        
    }
}
```

### Python

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
```

### C

```c
int strStr(char* haystack, char* needle) {
    
}
```

### C#

```csharp
public class Solution {
    public int StrStr(string haystack, string needle) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    
};
```

### TypeScript

```typescript
function strStr(haystack: string, needle: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $haystack
     * @param String $needle
     * @return Integer
     */
    function strStr($haystack, $needle) {
        
    }
}
```

### Swift

```swift
class Solution {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun strStr(haystack: String, needle: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int strStr(String haystack, String needle) {
    
  }
}
```

### Go

```golang
func strStr(haystack string, needle string) int {
    
}
```

### Ruby

```ruby
# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
    
end
```

### Scala

```scala
object Solution {
    def strStr(haystack: String, needle: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (str-str haystack needle)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec str_str(Haystack :: unicode:unicode_binary(), Needle :: unicode:unicode_binary()) -> integer().
str_str(Haystack, Needle) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec str_str(haystack :: String.t, needle :: String.t) :: integer
  def str_str(haystack, needle) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func strStr(haystack: String, needle: String): Int64 {

    }
}
```

