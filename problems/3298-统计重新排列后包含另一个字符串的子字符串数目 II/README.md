# 3298. 统计重新排列后包含另一个字符串的子字符串数目 II

## 题目描述

<p>给你两个字符串&nbsp;<code>word1</code> 和&nbsp;<code>word2</code>&nbsp;。</p>

<p>如果一个字符串 <code>x</code>&nbsp;重新排列后，<code>word2</code>&nbsp;是重排字符串的&nbsp;<span data-keyword="string-prefix">前缀</span>&nbsp;，那么我们称字符串&nbsp;<code>x</code>&nbsp;是&nbsp;<strong>合法的</strong>&nbsp;。</p>

<p>请你返回 <code>word1</code>&nbsp;中 <strong>合法</strong>&nbsp;<span data-keyword="substring-nonempty">子字符串</span>&nbsp;的数目。</p>

<p><strong>注意</strong>&nbsp;，这个问题中的内存限制比其他题目要&nbsp;<strong>小</strong>&nbsp;，所以你&nbsp;<strong>必须</strong>&nbsp;实现一个线性复杂度的解法。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word1 = "bcca", word2 = "abc"</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>唯一合法的子字符串是&nbsp;<code>"bcca"</code>&nbsp;，可以重新排列得到&nbsp;<code>"abcc"</code>&nbsp;，<code>"abc"</code>&nbsp;是它的前缀。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word1 = "abcabc", word2 = "abc"</span></p>

<p><span class="example-io"><b>输出：</b>10</span></p>

<p><strong>解释：</strong></p>

<p>除了长度为 1 和 2 的所有子字符串都是合法的。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>word1 = "abcabc", word2 = "aaabc"</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>
</div>

<p>&nbsp;</p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>1 &lt;= word1.length &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= word2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>word1</code> 和&nbsp;<code>word2</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. Use sliding window along with two-pointer here.
2. Use constant space to store the frequency of characters.

## 示例

```
"bcca"
"abc"
"abcabc"
"abc"
"abcabc"
"aaabc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public long validSubstringCount(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        
```

### C

```c
long long validSubstringCount(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public long ValidSubstringCount(string word1, string word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var validSubstringCount = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function validSubstringCount(word1: string, word2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function validSubstringCount($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validSubstringCount(_ word1: String, _ word2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validSubstringCount(word1: String, word2: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int validSubstringCount(String word1, String word2) {
    
  }
}
```

### Go

```golang
func validSubstringCount(word1 string, word2 string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {Integer}
def valid_substring_count(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def validSubstringCount(word1: String, word2: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_substring_count(word1: String, word2: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (valid-substring-count word1 word2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec valid_substring_count(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
valid_substring_count(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_substring_count(word1 :: String.t, word2 :: String.t) :: integer
  def valid_substring_count(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validSubstringCount(word1: String, word2: String): Int64 {

    }
}
```

