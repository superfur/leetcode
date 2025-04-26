# 1684. 统计一致字符串的数目

## 题目描述

<p>给你一个由不同字符组成的字符串 <code>allowed</code> 和一个字符串数组 <code>words</code> 。如果一个字符串的每一个字符都在 <code>allowed</code> 中，就称这个字符串是 <strong>一致字符串 </strong>。</p>

<p>请你返回 <code>words</code> 数组中 <strong>一致字符串</strong> 的数目。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
<b>输出：</b>2
<b>解释：</b>字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
<b>输出：</b>7
<b>解释：</b>所有字符串都是一致的。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
<b>输出：</b>4
<b>解释：</b>字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= words.length <= 10<sup>4</sup></code></li>
	<li><code>1 <= allowed.length <=<sup> </sup>26</code></li>
	<li><code>1 <= words[i].length <= 10</code></li>
	<li><code>allowed</code> 中的字符 <strong>互不相同</strong> 。</li>
	<li><code>words[i]</code> 和 <code>allowed</code> 只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. A string is incorrect if it contains a character that is not allowed
2. Constraints are small enough for brute force

## 示例

```
"ab"
["ad","bd","aaab","baa","badab"]
"abc"
["a","b","c","ab","ac","bc","abc"]
"cad"
["cc","acd","b","ba","bac","bad","ac","d"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
```

### C

```c
int countConsistentStrings(char* allowed, char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountConsistentStrings(string allowed, string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    
};
```

### TypeScript

```typescript
function countConsistentStrings(allowed: string, words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $allowed
     * @param String[] $words
     * @return Integer
     */
    function countConsistentStrings($allowed, $words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countConsistentStrings(_ allowed: String, _ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countConsistentStrings(allowed: String, words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countConsistentStrings(String allowed, List<String> words) {
    
  }
}
```

### Go

```golang
func countConsistentStrings(allowed string, words []string) int {
    
}
```

### Ruby

```ruby
# @param {String} allowed
# @param {String[]} words
# @return {Integer}
def count_consistent_strings(allowed, words)
    
end
```

### Scala

```scala
object Solution {
    def countConsistentStrings(allowed: String, words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-consistent-strings allowed words)
  (-> string? (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_consistent_strings(Allowed :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> integer().
count_consistent_strings(Allowed, Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_consistent_strings(allowed :: String.t, words :: [String.t]) :: integer
  def count_consistent_strings(allowed, words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countConsistentStrings(allowed: String, words: Array<String>): Int64 {

    }
}
```

