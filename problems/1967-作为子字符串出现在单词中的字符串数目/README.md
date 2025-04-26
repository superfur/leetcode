# 1967. 作为子字符串出现在单词中的字符串数目

## 题目描述

<p>给你一个字符串数组 <code>patterns</code> 和一个字符串 <code>word</code> ，统计 <code>patterns</code> 中有多少个字符串是 <code>word</code> 的子字符串。返回字符串数目。</p>

<p><strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>patterns = ["a","abc","bc","d"], word = "abc"
<strong>输出：</strong>3
<strong>解释：</strong>
- "a" 是 "<em><strong>a</strong></em>bc" 的子字符串。
- "abc" 是 "<em><strong>abc</strong></em>" 的子字符串。
- "bc" 是 "a<em><strong>bc</strong></em>" 的子字符串。
- "d" 不是 "abc" 的子字符串。
patterns 中有 3 个字符串作为子字符串出现在 word 中。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>patterns = ["a","b","c"], word = "aaaaabbbbb"
<strong>输出：</strong>2
<strong>解释：</strong>
- "a" 是 "a<em><strong>a</strong></em>aaabbbbb" 的子字符串。
- "b" 是 "aaaaabbbb<em><strong>b</strong></em>" 的子字符串。
- "c" 不是 "aaaaabbbbb" 的字符串。
patterns 中有 2 个字符串作为子字符串出现在 word 中。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>patterns = ["a","a","a"], word = "ab"
<strong>输出：</strong>3
<strong>解释：</strong>patterns 中的每个字符串都作为子字符串出现在 word "<em><strong>a</strong></em>b" 中。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= patterns.length &lt;= 100</code></li>
	<li><code>1 &lt;= patterns[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>patterns[i]</code> 和 <code>word</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Deal with each of the patterns individually.
2. Use the built-in function in the language you are using to find if the pattern exists as a substring in <code>word</code>.

## 示例

```
["a","abc","bc","d"]
"abc"
["a","b","c"]
"aaaaabbbbb"
["a","a","a"]
"ab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfStrings(String[] patterns, String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
```

### C

```c
int numOfStrings(char** patterns, int patternsSize, char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfStrings(string[] patterns, string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    
};
```

### TypeScript

```typescript
function numOfStrings(patterns: string[], word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $patterns
     * @param String $word
     * @return Integer
     */
    function numOfStrings($patterns, $word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfStrings(_ patterns: [String], _ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfStrings(patterns: Array<String>, word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfStrings(List<String> patterns, String word) {
    
  }
}
```

### Go

```golang
func numOfStrings(patterns []string, word string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} patterns
# @param {String} word
# @return {Integer}
def num_of_strings(patterns, word)
    
end
```

### Scala

```scala
object Solution {
    def numOfStrings(patterns: Array[String], word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-strings patterns word)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_strings(Patterns :: [unicode:unicode_binary()], Word :: unicode:unicode_binary()) -> integer().
num_of_strings(Patterns, Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_strings(patterns :: [String.t], word :: String.t) :: integer
  def num_of_strings(patterns, word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfStrings(patterns: Array<String>, word: String): Int64 {

    }
}
```

