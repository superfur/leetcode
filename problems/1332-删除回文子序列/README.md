# 1332. 删除回文子序列

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>，它仅由字母&nbsp;<code>'a'</code> 和 <code>'b'</code>&nbsp;组成。每一次删除操作都可以从 <code>s</code> 中删除一个回文 <strong>子序列</strong>。</p>

<p>返回删除给定字符串中所有字符（字符串为空）的最小删除次数。</p>

<p>「子序列」定义：如果一个字符串可以通过删除原字符串某些字符而不改变原字符顺序得到，那么这个字符串就是原字符串的一个子序列。</p>

<p>「回文」定义：如果一个字符串向后和向前读是一致的，那么这个字符串就是一个回文。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ababa"
<strong>输出：</strong>1
<strong>解释：</strong>字符串本身就是回文序列，只需要删除一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abb"
<strong>输出：</strong>2
<strong>解释：</strong>"<strong>a</strong>bb" -&gt; "<strong>bb</strong>" -&gt; "". 
先删除回文子序列 "a"，然后再删除 "bb"。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "baabb"
<strong>输出：</strong>2
<strong>解释：</strong>"<strong>baa</strong>b<strong>b</strong>" -&gt; "b" -&gt; "". 
先删除回文子序列 "baab"，然后再删除 "b"。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 仅包含字母&nbsp;<code>'a'</code>&nbsp; 和 <code>'b'</code></li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 提示

1. Use the fact that string contains only 2 characters.
2. Are subsequences composed of only one type of letter always palindrome strings ?

## 示例

```
"ababa"
"abb"
"baabb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int removePalindromeSub(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int removePalindromeSub(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
```

### C

```c
int removePalindromeSub(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int RemovePalindromeSub(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    
};
```

### TypeScript

```typescript
function removePalindromeSub(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function removePalindromeSub($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removePalindromeSub(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removePalindromeSub(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int removePalindromeSub(String s) {
    
  }
}
```

### Go

```golang
func removePalindromeSub(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def remove_palindrome_sub(s)
    
end
```

### Scala

```scala
object Solution {
    def removePalindromeSub(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_palindrome_sub(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (remove-palindrome-sub s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec remove_palindrome_sub(S :: unicode:unicode_binary()) -> integer().
remove_palindrome_sub(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_palindrome_sub(s :: String.t) :: integer
  def remove_palindrome_sub(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removePalindromeSub(s: String): Int64 {

    }
}
```

