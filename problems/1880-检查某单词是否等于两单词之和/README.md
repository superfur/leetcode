# 1880. 检查某单词是否等于两单词之和

## 题目描述

<p>字母的 <strong>字母值</strong> 取决于字母在字母表中的位置，<strong>从 0 开始</strong> 计数。即，<code>'a' -&gt; 0</code>、<code>'b' -&gt; 1</code>、<code>'c' -&gt; 2</code>，以此类推。</p>

<p>对某个由小写字母组成的字符串 <code>s</code> 而言，其 <strong>数值</strong> 就等于将 <code>s</code> 中每个字母的 <strong>字母值</strong> 按顺序 <strong>连接</strong> 并 <strong>转换</strong> 成对应整数。</p>

<ul>
	<li>例如，<code>s = "acb"</code> ，依次连接每个字母的字母值可以得到 <code>"021"</code> ，转换为整数得到 <code>21</code> 。</li>
</ul>

<p>给你三个字符串 <code>firstWord</code>、<code>secondWord</code> 和 <code>targetWord</code> ，每个字符串都由从 <code>'a'</code> 到 <code>'j'</code> （<strong>含 </strong><code>'a'</code> 和 <code>'j'</code><strong> </strong>）的小写英文字母组成。</p>

<p>如果 <code>firstWord</code><em> </em>和<em> </em><code>secondWord</code> 的 <strong>数值之和</strong> 等于<em> </em><code>targetWord</code><em> </em>的数值，返回 <code>true</code> ；否则，返回<em> </em><code>false</code><em> </em>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>firstWord = "acb", secondWord = "cba", targetWord = "cdb"
<strong>输出：</strong>true
<strong>解释：</strong>
firstWord 的数值为 "acb" -&gt; "021" -&gt; 21
secondWord 的数值为 "cba" -&gt; "210" -&gt; 210
targetWord 的数值为 "cdb" -&gt; "231" -&gt; 231
由于 21 + 210 == 231 ，返回 true
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>firstWord = "aaa", secondWord = "a", targetWord = "aab"
<strong>输出：</strong>false
<strong>解释：</strong>
firstWord 的数值为 "aaa" -&gt; "000" -&gt; 0
secondWord 的数值为 "a" -&gt; "0" -&gt; 0
targetWord 的数值为 "aab" -&gt; "001" -&gt; 1
由于 0 + 0 != 1 ，返回 false</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
<strong>输出：</strong>true
<strong>解释：</strong>
firstWord 的数值为 "aaa" -&gt; "000" -&gt; 0
secondWord 的数值为 "a" -&gt; "0" -&gt; 0
targetWord 的数值为 "aaaa" -&gt; "0000" -&gt; 0
由于 0 + 0 == 0 ，返回 true
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= firstWord.length, </code><code>secondWord.length, </code><code>targetWord.length &lt;= 8</code></li>
	<li><code>firstWord</code>、<code>secondWord</code> 和 <code>targetWord</code> 仅由从 <code>'a'</code> 到 <code>'j'</code> （<strong>含 </strong><code>'a'</code> 和 <code>'j'</code><strong> </strong>）的小写英文字母组成<strong>。</strong></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Convert each character of each word to its numerical value.
2. Check if the numerical values satisfies the condition.

## 示例

```
"acb"
"cba"
"cdb"
"aaa"
"a"
"aab"
"aaa"
"a"
"aaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
```

### C

```c
bool isSumEqual(char* firstWord, char* secondWord, char* targetWord) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsSumEqual(string firstWord, string secondWord, string targetWord) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} firstWord
 * @param {string} secondWord
 * @param {string} targetWord
 * @return {boolean}
 */
var isSumEqual = function(firstWord, secondWord, targetWord) {
    
};
```

### TypeScript

```typescript
function isSumEqual(firstWord: string, secondWord: string, targetWord: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $firstWord
     * @param String $secondWord
     * @param String $targetWord
     * @return Boolean
     */
    function isSumEqual($firstWord, $secondWord, $targetWord) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isSumEqual(_ firstWord: String, _ secondWord: String, _ targetWord: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isSumEqual(String firstWord, String secondWord, String targetWord) {
    
  }
}
```

### Go

```golang
func isSumEqual(firstWord string, secondWord string, targetWord string) bool {
    
}
```

### Ruby

```ruby
# @param {String} first_word
# @param {String} second_word
# @param {String} target_word
# @return {Boolean}
def is_sum_equal(first_word, second_word, target_word)
    
end
```

### Scala

```scala
object Solution {
    def isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_sum_equal(first_word: String, second_word: String, target_word: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-sum-equal firstWord secondWord targetWord)
  (-> string? string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_sum_equal(FirstWord :: unicode:unicode_binary(), SecondWord :: unicode:unicode_binary(), TargetWord :: unicode:unicode_binary()) -> boolean().
is_sum_equal(FirstWord, SecondWord, TargetWord) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_sum_equal(first_word :: String.t, second_word :: String.t, target_word :: String.t) :: boolean
  def is_sum_equal(first_word, second_word, target_word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isSumEqual(firstWord: String, secondWord: String, targetWord: String): Bool {

    }
}
```

