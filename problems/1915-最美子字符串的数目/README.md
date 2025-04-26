# 1915. 最美子字符串的数目

## 题目描述

<p>如果某个字符串中 <strong>至多一个</strong> 字母出现 <strong>奇数</strong> 次，则称其为 <strong>最美</strong> 字符串。</p>

<ul>
	<li>例如，<code>"ccjjc"</code> 和 <code>"abab"</code> 都是最美字符串，但 <code>"ab"</code> 不是。</li>
</ul>

<p>给你一个字符串 <code>word</code> ，该字符串由前十个小写英文字母组成（<code>'a'</code> 到 <code>'j'</code>）。请你返回 <code>word</code> 中 <strong>最美非空子字符串</strong> 的数目<em>。</em>如果同样的子字符串在<em> </em><code>word</code> 中出现多次，那么应当对 <strong>每次出现</strong> 分别计数<em>。</em></p>

<p><strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "aba"
<strong>输出：</strong>4
<strong>解释：</strong>4 个最美子字符串如下所示：
- "<strong>a</strong>ba" -> "a"
- "a<strong>b</strong>a" -> "b"
- "ab<strong>a</strong>" -> "a"
- "<strong>aba</strong>" -> "aba"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "aabb"
<strong>输出：</strong>9
<strong>解释：</strong>9 个最美子字符串如下所示：
- "<strong>a</strong>abb" -> "a"
- "<strong>aa</strong>bb" -> "aa"
- "<strong>aab</strong>b" -> "aab"
- "<strong>aabb</strong>" -> "aabb"
- "a<strong>a</strong>bb" -> "a"
- "a<strong>abb</strong>" -> "abb"
- "aa<strong>b</strong>b" -> "b"
- "aa<strong>bb</strong>" -> "bb"
- "aab<strong>b</strong>" -> "b"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word = "he"
<strong>输出：</strong>2
<strong>解释：</strong>2 个最美子字符串如下所示：
- "<b>h</b>e" -> "h"
- "h<strong>e</strong>" -> "e"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= word.length <= 10<sup>5</sup></code></li>
	<li><code>word</code> 由从 <code>'a'</code> 到 <code>'j'</code> 的小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 哈希表
- 字符串
- 前缀和

## 提示

1. For each prefix of the string, check which characters are of even frequency and which are not and represent it by a bitmask.
2. Find the other prefixes whose masks differs from the current prefix mask by at most one bit.

## 示例

```
"aba"
"aabb"
"he"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long wonderfulSubstrings(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public long wonderfulSubstrings(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
```

### C

```c
long long wonderfulSubstrings(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public long WonderfulSubstrings(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var wonderfulSubstrings = function(word) {
    
};
```

### TypeScript

```typescript
function wonderfulSubstrings(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function wonderfulSubstrings($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wonderfulSubstrings(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wonderfulSubstrings(word: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int wonderfulSubstrings(String word) {
    
  }
}
```

### Go

```golang
func wonderfulSubstrings(word string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def wonderful_substrings(word)
    
end
```

### Scala

```scala
object Solution {
    def wonderfulSubstrings(word: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn wonderful_substrings(word: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (wonderful-substrings word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec wonderful_substrings(Word :: unicode:unicode_binary()) -> integer().
wonderful_substrings(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec wonderful_substrings(word :: String.t) :: integer
  def wonderful_substrings(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wonderfulSubstrings(word: String): Int64 {

    }
}
```

