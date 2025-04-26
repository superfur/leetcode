# 1768. 交替合并字符串

## 题目描述

<p>给你两个字符串 <code>word1</code> 和 <code>word2</code> 。请你从 <code>word1</code> 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。</p>

<p>返回 <strong>合并后的字符串</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word1 = "abc", word2 = "pqr"
<strong>输出：</strong>"apbqcr"
<strong>解释：</strong>字符串合并情况如下所示：
word1：  a   b   c
word2：    p   q   r
合并后：  a p b q c r
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word1 = "ab", word2 = "pqrs"
<strong>输出：</strong>"apbqrs"
<strong>解释：</strong>注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
word1：  a   b 
word2：    p   q   r   s
合并后：  a p b q   r   s
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word1 = "abcd", word2 = "pq"
<strong>输出：</strong>"apbqcd"
<strong>解释：</strong>注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。
word1：  a   b   c   d
word2：    p   q 
合并后：  a p b q c   d
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= word1.length, word2.length <= 100</code></li>
	<li><code>word1</code> 和 <code>word2</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 提示

1. Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.

## 示例

```
"abc"
"pqr"
"ab"
"pqrs"
"abcd"
"pq"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public String mergeAlternately(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
```

### C

```c
char* mergeAlternately(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public string MergeAlternately(string word1, string word2) {
        
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
var mergeAlternately = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function mergeAlternately(word1: string, word2: string): string {
    
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
    function mergeAlternately($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mergeAlternately(_ word1: String, _ word2: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String mergeAlternately(String word1, String word2) {
    
  }
}
```

### Go

```golang
func mergeAlternately(word1 string, word2 string) string {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {String}
def merge_alternately(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def mergeAlternately(word1: String, word2: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (merge-alternately word1 word2)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec merge_alternately(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
merge_alternately(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec merge_alternately(word1 :: String.t, word2 :: String.t) :: String.t
  def merge_alternately(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mergeAlternately(word1: String, word2: String): String {

    }
}
```

