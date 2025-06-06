# 3517. 最小回文排列 I

## 题目描述

<p>给你一个&nbsp;<strong>回文&nbsp;</strong>字符串 <code>s</code>。</p>

<p>返回 <code>s</code> 的按字典序排列的&nbsp;<strong>最小&nbsp;</strong>回文排列。</p>

<p>如果一个字符串从前往后和从后往前读都相同，那么这个字符串是一个&nbsp;<strong>回文 </strong>字符串。</p>

<p><strong>排列&nbsp;</strong>是字符串中所有字符的重排。</p>
如果字符串 <code>a</code> 按字典序小于字符串 <code>b</code>，则表示在第一个不同的位置，<code>a</code> 中的字符比 <code>b</code> 中的对应字符在字母表中更靠前。<br />
如果在前 <code>min(a.length, b.length)</code> 个字符中没有区别，则较短的字符串按字典序更小。

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "z"</span></p>

<p><strong>输出：</strong> <span class="example-io">"z"</span></p>

<p><strong>解释：</strong></p>

<p>仅由一个字符组成的字符串已经是按字典序最小的回文。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "babab"</span></p>

<p><strong>输出：</strong> <span class="example-io">"abbba"</span></p>

<p><strong>解释：</strong></p>

<p>通过重排 <code>"babab"</code> → <code>"abbba"</code>，可以得到按字典序最小的回文。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "daccad"</span></p>

<p><strong>输出：</strong> <span class="example-io">"acddca"</span></p>

<p><strong>解释：</strong></p>

<p>通过重排 <code>"daccad"</code> → <code>"acddca"</code>，可以得到按字典序最小的回文。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成。</li>
	<li>保证 <code>s</code> 是回文字符串。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 计数排序
- 排序

## 提示

1. Consider a palindrome as composed of two mirror-image halves.
2. Construct one half (using <code>s</code>), and then the other half is its reverse to obtain the lexicographically smallest permutation.

## 示例

```
"z"
"babab"
"daccad"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string smallestPalindrome(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String smallestPalindrome(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
```

### C

```c
char* smallestPalindrome(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string SmallestPalindrome(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var smallestPalindrome = function(s) {
    
};
```

### TypeScript

```typescript
function smallestPalindrome(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function smallestPalindrome($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestPalindrome(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestPalindrome(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String smallestPalindrome(String s) {
    
  }
}
```

### Go

```golang
func smallestPalindrome(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def smallest_palindrome(s)
    
end
```

### Scala

```scala
object Solution {
    def smallestPalindrome(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_palindrome(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-palindrome s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec smallest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_palindrome(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_palindrome(s :: String.t) :: String.t
  def smallest_palindrome(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestPalindrome(s: String): String {

    }
}
```

