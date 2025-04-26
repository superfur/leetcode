# 3042. 统计前后缀下标对 I

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> 。</p>

<p>定义一个 <strong>布尔 </strong>函数 <code>isPrefixAndSuffix</code> ，它接受两个字符串参数 <code>str1</code> 和 <code>str2</code> ：</p>

<ul>
	<li>当 <code>str1</code> 同时是 <code>str2</code> 的前缀（<span data-keyword="string-prefix">prefix</span>）和后缀（<span data-keyword="string-suffix">suffix</span>）时，<code>isPrefixAndSuffix(str1, str2)</code> 返回 <code>true</code>，否则返回 <code>false</code>。</li>
</ul>

<p>例如，<code>isPrefixAndSuffix("aba", "ababa")</code> 返回 <code>true</code>，因为 <code>"aba"</code> 既是 <code>"ababa"</code> 的前缀，也是 <code>"ababa"</code> 的后缀，但是 <code>isPrefixAndSuffix("abc", "abcd")</code> 返回<code> false</code>。</p>

<p>以整数形式，返回满足 <code>i &lt; j</code> 且 <code>isPrefixAndSuffix(words[i], words[j])</code> 为 <code>true</code> 的下标对 <code>(i, j)</code> 的<strong> 数量 </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["a","aba","ababa","aa"]
<strong>输出：</strong>4
<strong>解释：</strong>在本示例中，计数的下标对包括：
i = 0 且 j = 1 ，因为 isPrefixAndSuffix("a", "aba") 为 true 。
i = 0 且 j = 2 ，因为 isPrefixAndSuffix("a", "ababa") 为 true 。
i = 0 且 j = 3 ，因为 isPrefixAndSuffix("a", "aa") 为 true 。
i = 1 且 j = 2 ，因为 isPrefixAndSuffix("aba", "ababa") 为 true 。
因此，答案是 4 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["pa","papa","ma","mama"]
<strong>输出：</strong>2
<strong>解释：</strong>在本示例中，计数的下标对包括：
i = 0 且 j = 1 ，因为 isPrefixAndSuffix("pa", "papa") 为 true 。
i = 2 且 j = 3 ，因为 isPrefixAndSuffix("ma", "mama") 为 true 。
因此，答案是 2 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["abab","ab"]
<strong>输出：</strong>0
<strong>解释：</strong>在本示例中，唯一有效的下标对是 i = 0 且 j = 1 ，但是 isPrefixAndSuffix("abab", "ab") 为 false 。
因此，答案是 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 字典树
- 数组
- 字符串
- 字符串匹配
- 哈希函数
- 滚动哈希

## 提示

1. Iterate through all index pairs <code>(i, j)</code>, such that <code>i < j</code>, and check <code>isPrefixAndSuffix(words[i], words[j])</code>.
2. The answer is the total number of pairs where <code>isPrefixAndSuffix(words[i], words[j]) == true</code>.

## 示例

```
["a","aba","ababa","aa"]
["pa","papa","ma","mama"]
["abab","ab"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
```

### C

```c
int countPrefixSuffixPairs(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPrefixSuffixPairs(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) {
    
};
```

### TypeScript

```typescript
function countPrefixSuffixPairs(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function countPrefixSuffixPairs($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPrefixSuffixPairs(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPrefixSuffixPairs(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPrefixSuffixPairs(List<String> words) {
    
  }
}
```

### Go

```golang
func countPrefixSuffixPairs(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def count_prefix_suffix_pairs(words)
    
end
```

### Scala

```scala
object Solution {
    def countPrefixSuffixPairs(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-prefix-suffix-pairs words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_prefix_suffix_pairs(Words :: [unicode:unicode_binary()]) -> integer().
count_prefix_suffix_pairs(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_prefix_suffix_pairs(words :: [String.t]) :: integer
  def count_prefix_suffix_pairs(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPrefixSuffixPairs(words: Array<String>): Int64 {

    }
}
```

