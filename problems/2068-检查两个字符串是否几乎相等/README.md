# 2068. 检查两个字符串是否几乎相等

## 题目描述

<p>如果两个字符串 <code>word1</code>&nbsp;和 <code>word2</code>&nbsp;中从 <code>'a'</code>&nbsp;到 <code>'z'</code>&nbsp;每一个字母出现频率之差都 <strong>不超过</strong>&nbsp;<code>3</code>&nbsp;，那么我们称这两个字符串&nbsp;<code>word1</code> 和&nbsp;<code>word2</code> <strong>几乎相等</strong>&nbsp;。</p>

<p>给你两个长度都为&nbsp;<code>n</code>&nbsp;的字符串&nbsp;<code>word1</code> 和&nbsp;<code>word2</code>&nbsp;，如果&nbsp;<code>word1</code>&nbsp;和&nbsp;<code>word2</code>&nbsp;<strong>几乎相等</strong>&nbsp;，请你返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>一个字母 <code>x</code>&nbsp;的出现 <strong>频率</strong>&nbsp;指的是它在字符串中出现的次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>word1 = "aaaa", word2 = "bccb"
<b>输出：</b>false
<b>解释：</b>字符串 "aaaa" 中有 4 个 'a' ，但是 "bccb" 中有 0 个 'a' 。
两者之差为 4 ，大于上限 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>word1 = "abcdeef", word2 = "abaaacc"
<b>输出：</b>true
<b>解释：</b>word1 和 word2 中每个字母出现频率之差至多为 3 ：
- 'a' 在 word1 中出现了 1 次，在 word2 中出现了 4 次，差为 3 。
- 'b' 在 word1 中出现了 1 次，在 word2 中出现了 1 次，差为 0 。
- 'c' 在 word1 中出现了 1 次，在 word2 中出现了 2 次，差为 1 。
- 'd' 在 word1 中出现了 1 次，在 word2 中出现了 0 次，差为 1 。
- 'e' 在 word1 中出现了 2 次，在 word2 中出现了 0 次，差为 2 。
- 'f' 在 word1 中出现了 1 次，在 word2 中出现了 0 次，差为 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>word1 = "cccddabba", word2 = "babababab"
<b>输出：</b>true
<b>解释：</b>word1 和 word2 中每个字母出现频率之差至多为 3 ：
- 'a' 在 word1 中出现了 2 次，在 word2 中出现了 4 次，差为 2 。
- 'b' 在 word1 中出现了 2 次，在 word2 中出现了 5 次，差为 3 。
- 'c' 在 word1 中出现了 3 次，在 word2 中出现了 0 次，差为 3 。
- 'd' 在 word1 中出现了 2 次，在 word2 中出现了 0 次，差为 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == word1.length == word2.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>word1</code> 和&nbsp;<code>word2</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. What data structure can we use to count the frequency of each character?
2. Are there edge cases where a character is present in one string but not the other?

## 示例

```
"aaaa"
"bccb"
"abcdeef"
"abaaacc"
"cccddabba"
"babababab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkAlmostEquivalent(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkAlmostEquivalent(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
```

### C

```c
bool checkAlmostEquivalent(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckAlmostEquivalent(string word1, string word2) {
        
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
var checkAlmostEquivalent = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function checkAlmostEquivalent(word1: string, word2: string): boolean {
    
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
    function checkAlmostEquivalent($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkAlmostEquivalent(_ word1: String, _ word2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkAlmostEquivalent(word1: String, word2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkAlmostEquivalent(String word1, String word2) {
    
  }
}
```

### Go

```golang
func checkAlmostEquivalent(word1 string, word2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {Boolean}
def check_almost_equivalent(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def checkAlmostEquivalent(word1: String, word2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_almost_equivalent(word1: String, word2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-almost-equivalent word1 word2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec check_almost_equivalent(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> boolean().
check_almost_equivalent(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_almost_equivalent(word1 :: String.t, word2 :: String.t) :: boolean
  def check_almost_equivalent(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkAlmostEquivalent(word1: String, word2: String): Bool {

    }
}
```

