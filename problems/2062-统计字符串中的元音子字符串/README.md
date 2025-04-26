# 2062. 统计字符串中的元音子字符串

## 题目描述

<p><strong>子字符串</strong> 是字符串中的一个连续（非空）的字符序列。</p>

<p><strong>元音子字符串</strong> 是 <strong>仅</strong> 由元音（<code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code> 和 <code>'u'</code>）组成的一个子字符串，且必须包含 <strong>全部五种</strong> 元音。</p>

<p>给你一个字符串 <code>word</code> ，统计并返回 <code>word</code> 中 <strong>元音子字符串的数目</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "aeiouu"
<strong>输出：</strong>2
<strong>解释：</strong>下面列出 word 中的元音子字符串（斜体加粗部分）：
- "<em><strong>aeiou</strong></em>u"
- "<strong><em>aeiouu</em></strong>"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "unicornarihan"
<strong>输出：</strong>0
<strong>解释：</strong>word 中不含 5 种元音，所以也不会存在元音子字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word = "cuaieuouac"
<strong>输出：</strong>7
<strong>解释：</strong>下面列出 word 中的元音子字符串（斜体加粗部分）：
- "c<em><strong>uaieuo</strong></em>uac"
- "c<em><strong>uaieuou</strong></em>ac"
- "c<em><strong>uaieuoua</strong></em>c"
- "cu<em><strong>aieuo</strong></em>uac"
- "cu<em><strong>aieuou</strong></em>ac"
- "cu<em><strong>aieuoua</strong></em>c"
- "cua<em><strong>ieuoua</strong></em>c"</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>word = "bbaeixoubb"
<strong>输出：</strong>0
<strong>解释：</strong>所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. While generating substrings starting at any index, do you need to continue generating larger substrings if you encounter a consonant?
2. Can you store the count of characters to avoid generating substrings altogether?

## 示例

```
"aeiouu"
"unicornarihan"
"cuaieuouac"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countVowelSubstrings(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int countVowelSubstrings(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
```

### C

```c
int countVowelSubstrings(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountVowelSubstrings(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var countVowelSubstrings = function(word) {
    
};
```

### TypeScript

```typescript
function countVowelSubstrings(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function countVowelSubstrings($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countVowelSubstrings(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countVowelSubstrings(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countVowelSubstrings(String word) {
    
  }
}
```

### Go

```golang
func countVowelSubstrings(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def count_vowel_substrings(word)
    
end
```

### Scala

```scala
object Solution {
    def countVowelSubstrings(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_vowel_substrings(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-vowel-substrings word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_vowel_substrings(Word :: unicode:unicode_binary()) -> integer().
count_vowel_substrings(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_vowel_substrings(word :: String.t) :: integer
  def count_vowel_substrings(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countVowelSubstrings(word: String): Int64 {

    }
}
```

