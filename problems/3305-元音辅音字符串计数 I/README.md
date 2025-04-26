# 3305. 元音辅音字符串计数 I

## 题目描述

<p>给你一个字符串 <code>word</code> 和一个 <strong>非负 </strong>整数 <code>k</code>。</p>

<p>返回 <code>word</code> 的 <span data-keyword="substring-nonempty">子字符串</span> 中，每个元音字母（<code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code>、<code>'u'</code>）<strong>至少</strong> 出现一次，并且 <strong>恰好 </strong>包含 <code>k</code> 个辅音字母的子字符串的总数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "aeioqq", k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>不存在包含所有元音字母的子字符串。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "aeiou", k = 0</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>唯一一个包含所有元音字母且不含辅音字母的子字符串是 <code>word[0..4]</code>，即 <code>"aeiou"</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">word = "ieaouqqieaouqq", k = 1</span></p>

<p><strong>输出：</strong>3</p>

<p><strong>解释：</strong></p>

<p>包含所有元音字母并且恰好含有一个辅音字母的子字符串有：</p>

<ul>
	<li><code>word[0..5]</code>，即 <code>"ieaouq"</code>。</li>
	<li><code>word[6..11]</code>，即 <code>"qieaou"</code>。</li>
	<li><code>word[7..12]</code>，即 <code>"ieaouq"</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>5 &lt;= word.length &lt;= 250</code></li>
	<li><code>word</code> 仅由小写英文字母组成。</li>
	<li><code>0 &lt;= k &lt;= word.length - 5</code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. Use a HashMap and check all the substrings.

## 示例

```
"aeioqq"
1
"aeiou"
0
"ieaouqqieaouqq"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countOfSubstrings(string word, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countOfSubstrings(String word, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
```

### C

```c
int countOfSubstrings(char* word, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountOfSubstrings(string word, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var countOfSubstrings = function(word, k) {
    
};
```

### TypeScript

```typescript
function countOfSubstrings(word: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function countOfSubstrings($word, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countOfSubstrings(_ word: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countOfSubstrings(word: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countOfSubstrings(String word, int k) {
    
  }
}
```

### Go

```golang
func countOfSubstrings(word string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {Integer} k
# @return {Integer}
def count_of_substrings(word, k)
    
end
```

### Scala

```scala
object Solution {
    def countOfSubstrings(word: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_of_substrings(word: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-of-substrings word k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_of_substrings(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
count_of_substrings(Word, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_of_substrings(word :: String.t, k :: integer) :: integer
  def count_of_substrings(word, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countOfSubstrings(word: String, k: Int64): Int64 {

    }
}
```

