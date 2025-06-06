# 3163. 压缩字符串 III

## 题目描述

<p>给你一个字符串 <code>word</code>，请你使用以下算法进行压缩：</p>

<ul>
	<li>从空字符串 <code>comp</code> 开始。当 <code>word</code> <strong>不为空</strong> 时，执行以下操作：

	<ul>
		<li>移除 <code>word</code> 的最长单字符前缀，该前缀由单一字符 <code>c</code> 重复多次组成，且该前缀长度 <strong>最多 </strong>为 9 。</li>
		<li>将前缀的长度和字符 <code>c</code> 追加到 <code>comp</code> 。</li>
	</ul>
	</li>
</ul>

<p>返回字符串 <code>comp</code> 。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "abcde"</span></p>

<p><strong>输出：</strong><span class="example-io">"1a1b1c1d1e"</span></p>

<p><strong>解释：</strong></p>

<p>初始时，<code>comp = ""</code> 。进行 5 次操作，每次操作分别选择 <code>"a"</code>、<code>"b"</code>、<code>"c"</code>、<code>"d"</code> 和 <code>"e"</code> 作为前缀。</p>

<p>对每个前缀，将 <code>"1"</code> 和对应的字符追加到 <code>comp</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "aaaaaaaaaaaaaabb"</span></p>

<p><strong>输出：</strong><span class="example-io">"9a5a2b"</span></p>

<p><strong>解释：</strong></p>

<p>初始时，<code>comp = ""</code>。进行 3 次操作，每次操作分别选择 <code>"aaaaaaaaa"</code>、<code>"aaaaa"</code> 和 <code>"bb"</code> 作为前缀。</p>

<ul>
	<li>对于前缀 <code>"aaaaaaaaa"</code>，将 <code>"9"</code> 和 <code>"a"</code> 追加到 <code>comp</code>。</li>
	<li>对于前缀 <code>"aaaaa"</code>，将 <code>"5"</code> 和 <code>"a"</code> 追加到 <code>comp</code>。</li>
	<li>对于前缀 <code>"bb"</code>，将 <code>"2"</code> 和 <code>"b"</code> 追加到 <code>comp</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>word</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 提示

1. Each time, just cut the same character in prefix up to at max 9 times. It’s always better to cut a bigger prefix.

## 示例

```
"abcde"
"aaaaaaaaaaaaaabb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string compressedString(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public String compressedString(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def compressedString(self, word: str) -> str:
        
```

### C

```c
char* compressedString(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public string CompressedString(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {string}
 */
var compressedString = function(word) {
    
};
```

### TypeScript

```typescript
function compressedString(word: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return String
     */
    function compressedString($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func compressedString(_ word: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun compressedString(word: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String compressedString(String word) {
    
  }
}
```

### Go

```golang
func compressedString(word string) string {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {String}
def compressed_string(word)
    
end
```

### Scala

```scala
object Solution {
    def compressedString(word: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn compressed_string(word: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (compressed-string word)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec compressed_string(Word :: unicode:unicode_binary()) -> unicode:unicode_binary().
compressed_string(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec compressed_string(word :: String.t) :: String.t
  def compressed_string(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func compressedString(word: String): String {

    }
}
```

