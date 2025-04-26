# 1754. 构造字典序最大的合并字符串

## 题目描述

<p>给你两个字符串 <code>word1</code> 和 <code>word2</code> 。你需要按下述方式构造一个新字符串 <code>merge</code> ：如果 <code>word1</code> 或 <code>word2</code> 非空，选择 <strong>下面选项之一</strong> 继续操作：</p>

<ul>
	<li>如果 <code>word1</code> 非空，将 <code>word1</code> 中的第一个字符附加到 <code>merge</code> 的末尾，并将其从 <code>word1</code> 中移除。

	<ul>
		<li>例如，<code>word1 = "abc" </code>且 <code>merge = "dv"</code> ，在执行此选项操作之后，<code>word1 = "bc"</code> ，同时 <code>merge = "dva"</code> 。</li>
	</ul>
	</li>
	<li>如果 <code>word2</code> 非空，将 <code>word2</code> 中的第一个字符附加到 <code>merge</code> 的末尾，并将其从 <code>word2</code> 中移除。
	<ul>
		<li>例如，<code>word2 = "abc" </code>且 <code>merge = ""</code> ，在执行此选项操作之后，<code>word2 = "bc"</code> ，同时 <code>merge = "a"</code> 。</li>
	</ul>
	</li>
</ul>

<p>返回你可以构造的字典序 <strong>最大</strong> 的合并字符串<em> </em><code>merge</code><em> 。</em></p>

<p>长度相同的两个字符串 <code>a</code> 和 <code>b</code> 比较字典序大小，如果在 <code>a</code> 和 <code>b</code> 出现不同的第一个位置，<code>a</code> 中字符在字母表中的出现顺序位于 <code>b</code> 中相应字符之后，就认为字符串 <code>a</code> 按字典序比字符串 <code>b</code> 更大。例如，<code>"abcd"</code> 按字典序比 <code>"abcc"</code> 更大，因为两个字符串出现不同的第一个位置是第四个字符，而 <code>d</code> 在字母表中的出现顺序位于 <code>c</code> 之后。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word1 = "cabaa", word2 = "bcaaa"
<strong>输出：</strong>"cbcabaaaaa"
<strong>解释：</strong>构造字典序最大的合并字符串，可行的一种方法如下所示：
- 从 word1 中取第一个字符：merge = "c"，word1 = "abaa"，word2 = "bcaaa"
- 从 word2 中取第一个字符：merge = "cb"，word1 = "abaa"，word2 = "caaa"
- 从 word2 中取第一个字符：merge = "cbc"，word1 = "abaa"，word2 = "aaa"
- 从 word1 中取第一个字符：merge = "cbca"，word1 = "baa"，word2 = "aaa"
- 从 word1 中取第一个字符：merge = "cbcab"，word1 = "aa"，word2 = "aaa"
- 将 word1 和 word2 中剩下的 5 个 a 附加到 merge 的末尾。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word1 = "abcabc", word2 = "abdcaba"
<strong>输出：</strong>"abdcabcabcaba"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= word1.length, word2.length <= 3000</code></li>
	<li><code>word1</code> 和 <code>word2</code> 仅由小写英文组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 双指针
- 字符串

## 提示

1. Build the result character by character. At each step, you choose a character from one of the two strings.
2. If the next character of the first string is larger than that of the second string, or vice versa, it's optimal to use the larger one.
3. If both are equal, think of a criteria that lets you decide which string to consume the next character from.
4. You should choose the next character from the larger string.

## 示例

```
"cabaa"
"bcaaa"
"abcabc"
"abdcaba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestMerge(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestMerge(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
```

### C

```c
char* largestMerge(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestMerge(string word1, string word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var largestMerge = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function largestMerge(word1: string, word2: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function largestMerge($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestMerge(_ word1: String, _ word2: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestMerge(word1: String, word2: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestMerge(String word1, String word2) {
    
  }
}
```

### Go

```golang
func largestMerge(word1 string, word2 string) string {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {String}
def largest_merge(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def largestMerge(word1: String, word2: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_merge(word1: String, word2: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-merge word1 word2)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec largest_merge(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_merge(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_merge(word1 :: String.t, word2 :: String.t) :: String.t
  def largest_merge(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestMerge(word1: String, word2: String): String {

    }
}
```

