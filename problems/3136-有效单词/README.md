# 3136. 有效单词

## 题目描述

<p><strong>有效单词</strong> 需要满足以下几个条件：</p>

<ul>
	<li><strong>至少 </strong>包含 3 个字符。</li>
	<li>由数字 0-9 和英文大小写字母组成。（不必包含所有这类字符。）</li>
	<li><strong>至少</strong> 包含一个 <strong>元音字母 </strong>。</li>
	<li><strong>至少</strong> 包含一个 <strong>辅音字母 </strong>。</li>
</ul>

<p>给你一个字符串 <code>word</code> 。如果 <code>word</code> 是一个有效单词，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code>、<code>'u'</code> 及其大写形式都属于<strong> 元音字母 </strong>。</li>
	<li>英文中的 <strong>辅音字母 </strong>是指那些除元音字母之外的字母。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "234Adas"</span></p>

<p><strong>输出：</strong><span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>这个单词满足所有条件。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "b3"</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>这个单词的长度少于 3 且没有包含元音字母。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "a3$e"</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>这个单词包含了 <code>'$'</code> 字符且没有包含辅音字母。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 20</code></li>
	<li><code>word</code> 由英文大写和小写字母、数字、<code>'@'</code>、<code>'#'</code> 和 <code>'$'</code> 组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Use if-else to check all the conditions.

## 示例

```
"234Adas"
"b3"
"a3$e"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isValid(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isValid(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isValid(self, word: str) -> bool:
        
```

### C

```c
bool isValid(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsValid(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function(word) {
    
};
```

### TypeScript

```typescript
function isValid(word: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Boolean
     */
    function isValid($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isValid(_ word: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isValid(word: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isValid(String word) {
    
  }
}
```

### Go

```golang
func isValid(word string) bool {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Boolean}
def is_valid(word)
    
end
```

### Scala

```scala
object Solution {
    def isValid(word: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_valid(word: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-valid word)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_valid(Word :: unicode:unicode_binary()) -> boolean().
is_valid(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_valid(word :: String.t) :: boolean
  def is_valid(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isValid(word: String): Bool {

    }
}
```

