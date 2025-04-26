# 2063. 所有子字符串中的元音

## 题目描述

<p>给你一个字符串 <code>word</code> ，返回 <code>word</code> 的所有子字符串中 <strong>元音的总数</strong> ，元音是指 <code>'a'</code>、<code>'e'</code><em>、</em><code>'i'</code><em>、</em><code>'o'</code><em> </em>和 <code>'u'</code><em> 。</em></p>

<p><strong>子字符串</strong> 是字符串中一个连续（非空）的字符序列。</p>

<p><strong>注意：</strong>由于对 <code>word</code> 长度的限制比较宽松，答案可能超过有符号 32 位整数的范围。计算时需当心。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "aba"
<strong>输出：</strong>6
<strong>解释：</strong>
所有子字符串是："a"、"ab"、"aba"、"b"、"ba" 和 "a" 。
- "b" 中有 0 个元音
- "a"、"ab"、"ba" 和 "a" 每个都有 1 个元音
- "aba" 中有 2 个元音
因此，元音总数 = 0 + 1 + 1 + 1 + 1 + 2 = 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "abc"
<strong>输出：</strong>3
<strong>解释：</strong>
所有子字符串是："a"、"ab"、"abc"、"b"、"bc" 和 "c" 。
- "a"、"ab" 和 "abc" 每个都有 1 个元音
- "b"、"bc" 和 "c" 每个都有 0 个元音
因此，元音总数 = 1 + 1 + 1 + 0 + 0 + 0 = 3 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word = "ltcd"
<strong>输出：</strong>0
<strong>解释：</strong>"ltcd" 的子字符串均不含元音。</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>word = "noosabasboosa"
<strong>输出：</strong>237
<strong>解释：</strong>所有子字符串中共有 237 个元音。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串
- 动态规划
- 组合数学

## 提示

1. Since generating substrings is not an option, can we count the number of substrings a vowel appears in?
2. How much does each vowel contribute to the total sum?

## 示例

```
"aba"
"abc"
"ltcd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countVowels(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public long countVowels(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countVowels(self, word: str) -> int:
        
```

### C

```c
long long countVowels(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountVowels(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var countVowels = function(word) {
    
};
```

### TypeScript

```typescript
function countVowels(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function countVowels($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countVowels(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countVowels(word: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countVowels(String word) {
    
  }
}
```

### Go

```golang
func countVowels(word string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def count_vowels(word)
    
end
```

### Scala

```scala
object Solution {
    def countVowels(word: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_vowels(word: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-vowels word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_vowels(Word :: unicode:unicode_binary()) -> integer().
count_vowels(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_vowels(word :: String.t) :: integer
  def count_vowels(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countVowels(word: String): Int64 {

    }
}
```

