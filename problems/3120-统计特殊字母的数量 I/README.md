# 3120. 统计特殊字母的数量 I

## 题目描述

<p>给你一个字符串 <code>word</code>。如果 <code>word</code> 中同时存在某个字母的小写形式和大写形式，则称这个字母为 <strong>特殊字母</strong> 。</p>

<p>返回 <code>word</code> 中<strong> </strong><strong>特殊字母 </strong>的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "aaAbcBC"</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p><code>word</code> 中的特殊字母是 <code>'a'</code>、<code>'b'</code> 和 <code>'c'</code>。</p>
</div>

<p><strong class="example">示例 2:</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "abc"</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p><code>word</code> 中不存在大小写形式同时出现的字母。</p>
</div>

<p><strong class="example">示例 3:</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "abBCab"</span></p>

<p><strong>输出：</strong>1</p>

<p><strong>解释：</strong></p>

<p><code>word</code> 中唯一的特殊字母是 <code>'b'</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 50</code></li>
	<li><code>word</code> 仅由小写和大写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. The constraints are small. For all 52 characters, check if they are present in <code>word</code>.

## 示例

```
"aaAbcBC"
"abc"
"abBCab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSpecialChars(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSpecialChars(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
```

### C

```c
int numberOfSpecialChars(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSpecialChars(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    
};
```

### TypeScript

```typescript
function numberOfSpecialChars(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function numberOfSpecialChars($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSpecialChars(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSpecialChars(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSpecialChars(String word) {
    
  }
}
```

### Go

```golang
func numberOfSpecialChars(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def number_of_special_chars(word)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSpecialChars(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-special-chars word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_special_chars(Word :: unicode:unicode_binary()) -> integer().
number_of_special_chars(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_special_chars(word :: String.t) :: integer
  def number_of_special_chars(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSpecialChars(word: String): Int64 {

    }
}
```

