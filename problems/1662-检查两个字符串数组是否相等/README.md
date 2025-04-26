# 1662. 检查两个字符串数组是否相等

## 题目描述

<p>给你两个字符串数组 <code>word1</code> 和 <code>word2</code> 。如果两个数组表示的字符串相同，返回<em> </em><code>true</code><em> </em>；否则，返回 <code>false</code><em> 。</em></p>

<p><strong>数组表示的字符串</strong> 是由数组中的所有元素 <strong>按顺序</strong> 连接形成的字符串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word1 = ["ab", "c"], word2 = ["a", "bc"]
<strong>输出：</strong>true
<strong>解释：</strong>
word1 表示的字符串为 "ab" + "c" -> "abc"
word2 表示的字符串为 "a" + "bc" -> "abc"
两个字符串相同，返回 true</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word1 = ["a", "cb"], word2 = ["ab", "c"]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
<strong>输出：</strong>true
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= word1.length, word2.length <= 10<sup>3</sup></code></li>
	<li><code>1 <= word1[i].length, word2[i].length <= 10<sup>3</sup></code></li>
	<li><code>1 <= sum(word1[i].length), sum(word2[i].length) <= 10<sup>3</sup></code></li>
	<li><code>word1[i]</code> 和 <code>word2[i]</code> 由小写字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Concatenate all strings in the first array into a single string in the given order, the same for the second array.
2. Both arrays represent the same string if and only if the generated strings are the same.

## 示例

```
["ab", "c"]
["a", "bc"]
["a", "cb"]
["ab", "c"]
["abc", "d", "defg"]
["abcddefg"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
```

### C

```c
bool arrayStringsAreEqual(char** word1, int word1Size, char** word2, int word2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ArrayStringsAreEqual(string[] word1, string[] word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $word1
     * @param String[] $word2
     * @return Boolean
     */
    function arrayStringsAreEqual($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func arrayStringsAreEqual(_ word1: [String], _ word2: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun arrayStringsAreEqual(word1: Array<String>, word2: Array<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool arrayStringsAreEqual(List<String> word1, List<String> word2) {
    
  }
}
```

### Go

```golang
func arrayStringsAreEqual(word1 []string, word2 []string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} word1
# @param {String[]} word2
# @return {Boolean}
def array_strings_are_equal(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def arrayStringsAreEqual(word1: Array[String], word2: Array[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (array-strings-are-equal word1 word2)
  (-> (listof string?) (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec array_strings_are_equal(Word1 :: [unicode:unicode_binary()], Word2 :: [unicode:unicode_binary()]) -> boolean().
array_strings_are_equal(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec array_strings_are_equal(word1 :: [String.t], word2 :: [String.t]) :: boolean
  def array_strings_are_equal(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func arrayStringsAreEqual(word1: Array<String>, word2: Array<String>): Bool {

    }
}
```

