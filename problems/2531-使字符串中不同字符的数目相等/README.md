# 2531. 使字符串中不同字符的数目相等

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的字符串 <code>word1</code> 和 <code>word2</code> 。</p>

<p>一次 <strong>移动</strong> 由以下两个步骤组成：</p>

<ul>
	<li>选中两个下标&nbsp;<code>i</code> 和 <code>j</code> ，分别满足 <code>0 &lt;= i &lt; word1.length</code> 和 <code>0 &lt;= j &lt; word2.length</code> ，</li>
	<li>交换 <code>word1[i]</code> 和 <code>word2[j]</code> 。</li>
</ul>

<p>如果可以通过 <strong>恰好一次</strong> 移动，使 <code>word1</code> 和 <code>word2</code> 中不同字符的数目相等，则返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>word1 = "ac", word2 = "b"
<strong>输出：</strong>false
<strong>解释：</strong>交换任何一组下标都会导致第一个字符串中有 2 个不同的字符，而在第二个字符串中只有 1 个不同字符。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>word1 = "abcc", word2 = "aab"
<strong>输出：</strong>true
<strong>解释：</strong>交换第一个字符串的下标 2 和第二个字符串的下标 0 。之后得到 word1 = "abac" 和 word2 = "cab" ，各有 3 个不同字符。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>word1 = "abcde", word2 = "fghij"
<strong>输出：</strong>true
<strong>解释：</strong>无论交换哪一组下标，两个字符串中都会有 5 个不同字符。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word1</code> 和 <code>word2</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Create a frequency array of the letters of each string.
2. There are 26*26 possible pairs of letters to swap. Can we try them all?
3. Iterate over all possible pairs of letters and check if swapping them will yield two strings that have the same number of distinct characters. Use the frequency array for the check.

## 示例

```
"ac"
"b"
"abcc"
"aab"
"abcde"
"fghij"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isItPossible(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isItPossible(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isItPossible(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
```

### C

```c
bool isItPossible(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsItPossible(string word1, string word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var isItPossible = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function isItPossible(word1: string, word2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function isItPossible($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isItPossible(_ word1: String, _ word2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isItPossible(word1: String, word2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isItPossible(String word1, String word2) {
    
  }
}
```

### Go

```golang
func isItPossible(word1 string, word2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {Boolean}
def is_it_possible(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def isItPossible(word1: String, word2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_it_possible(word1: String, word2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-it-possible word1 word2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_it_possible(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> boolean().
is_it_possible(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_it_possible(word1 :: String.t, word2 :: String.t) :: boolean
  def is_it_possible(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isItPossible(word1: String, word2: String): Bool {

    }
}
```

