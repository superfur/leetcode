# 1668. 最大重复子字符串

## 题目描述

<p>给你一个字符串 <code>sequence</code> ，如果字符串 <code>word</code> 连续重复 <code>k</code> 次形成的字符串是 <code>sequence</code> 的一个子字符串，那么单词 <code>word</code> 的 <strong>重复值为 <code>k</code></strong><strong> </strong>。单词 <code>word</code> 的 <strong>最</strong><strong>大重复值</strong> 是单词 <code>word</code> 在 <code>sequence</code> 中最大的重复值。如果 <code>word</code> 不是 <code>sequence</code> 的子串，那么重复值 <code>k</code> 为 <code>0</code> 。</p>

<p>给你一个字符串 <code>sequence</code> 和 <code>word</code> ，请你返回 <strong>最大重复值 <code>k</code> </strong>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>sequence = "ababc", word = "ab"
<b>输出：</b>2
<strong>解释：</strong>"abab" 是 "<strong>abab</strong>c" 的子字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>sequence = "ababc", word = "ba"
<b>输出：</b>1
<strong>解释：</strong>"ba" 是 "a<strong>ba</strong>bc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>sequence = "ababc", word = "ac"
<b>输出：</b>0
<strong>解释：</strong>"ac" 不是 "ababc" 的子字符串。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= sequence.length <= 100</code></li>
	<li><code>1 <= word.length <= 100</code></li>
	<li><code>sequence</code> 和 <code>word</code> 都只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 动态规划
- 字符串匹配

## 提示

1. The constraints are low enough for a brute force approach.
2. Try every k value from 0 upwards until word is no longer k-repeating.

## 示例

```
"ababc"
"ab"
"ababc"
"ba"
"ababc"
"ac"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxRepeating(string sequence, string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxRepeating(String sequence, String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
```

### C

```c
int maxRepeating(char* sequence, char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxRepeating(string sequence, string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} sequence
 * @param {string} word
 * @return {number}
 */
var maxRepeating = function(sequence, word) {
    
};
```

### TypeScript

```typescript
function maxRepeating(sequence: string, word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $sequence
     * @param String $word
     * @return Integer
     */
    function maxRepeating($sequence, $word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxRepeating(_ sequence: String, _ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxRepeating(sequence: String, word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxRepeating(String sequence, String word) {
    
  }
}
```

### Go

```golang
func maxRepeating(sequence string, word string) int {
    
}
```

### Ruby

```ruby
# @param {String} sequence
# @param {String} word
# @return {Integer}
def max_repeating(sequence, word)
    
end
```

### Scala

```scala
object Solution {
    def maxRepeating(sequence: String, word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-repeating sequence word)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_repeating(Sequence :: unicode:unicode_binary(), Word :: unicode:unicode_binary()) -> integer().
max_repeating(Sequence, Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_repeating(sequence :: String.t, word :: String.t) :: integer
  def max_repeating(sequence, word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxRepeating(sequence: String, word: String): Int64 {

    }
}
```

