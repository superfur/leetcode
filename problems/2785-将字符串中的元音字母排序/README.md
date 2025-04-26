# 2785. 将字符串中的元音字母排序

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;，将&nbsp;<code>s</code>&nbsp;中的元素重新 <b>排列</b>&nbsp;得到新的字符串&nbsp;<code>t</code>&nbsp;，它满足：</p>

<ul>
	<li>所有辅音字母都在原来的位置上。更正式的，如果满足&nbsp;<code>0 &lt;= i &lt; s.length</code>&nbsp;的下标 <code>i</code>&nbsp;处的&nbsp;<code>s[i]</code>&nbsp;是个辅音字母，那么&nbsp;<code>t[i] = s[i]</code>&nbsp;。</li>
	<li>元音字母都必须以他们的 <strong>ASCII</strong>&nbsp;值按 <strong>非递减</strong>&nbsp;顺序排列。更正式的，对于满足&nbsp;<code>0 &lt;= i &lt; j &lt; s.length</code>&nbsp;的下标 <code>i</code>&nbsp;和 <code>j</code>&nbsp; ，如果&nbsp;<code>s[i]</code> 和&nbsp;<code>s[j]</code>&nbsp;都是元音字母，那么&nbsp;<code>t[i]</code>&nbsp;的 ASCII 值不能大于&nbsp;<code>t[j]</code>&nbsp;的 ASCII 值。</li>
</ul>

<p>请你返回结果字母串。</p>

<p>元音字母为&nbsp;<code>'a'</code>&nbsp;，<code>'e'</code>&nbsp;，<code>'i'</code>&nbsp;，<code>'o'</code>&nbsp;和&nbsp;<code>'u'</code>&nbsp;，它们可能是小写字母也可能是大写字母，辅音字母是除了这 5 个字母以外的所有字母。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "lEetcOde"
<b>输出：</b>"lEOtcede"
<b>解释：</b>'E' ，'O' 和 'e' 是 s 中的元音字母，'l' ，'t' ，'c' 和 'd' 是所有的辅音。将元音字母按照 ASCII 值排序，辅音字母留在原地。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "lYmpH"
<b>输出：</b>"lYmpH"
<b>解释：</b>s 中没有元音字母（s 中都为辅音字母），所以我们返回 "lYmpH" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含英语字母表中的 <strong>大写&nbsp;</strong>和 <strong>小写&nbsp;</strong>字母。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 排序

## 提示

1. Add all the vowels in an array and sort the array.
2. Replace characters in string s if it's a vowel from the new array.

## 示例

```
"lEetcOde"
"lYmpH"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string sortVowels(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String sortVowels(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def sortVowels(self, s: str) -> str:
        
```

### C

```c
char* sortVowels(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string SortVowels(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function(s) {
    
};
```

### TypeScript

```typescript
function sortVowels(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function sortVowels($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortVowels(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortVowels(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String sortVowels(String s) {
    
  }
}
```

### Go

```golang
func sortVowels(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def sort_vowels(s)
    
end
```

### Scala

```scala
object Solution {
    def sortVowels(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_vowels(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (sort-vowels s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec sort_vowels(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
sort_vowels(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_vowels(s :: String.t) :: String.t
  def sort_vowels(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortVowels(s: String): String {

    }
}
```

