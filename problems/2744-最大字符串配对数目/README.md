# 2744. 最大字符串配对数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>words</code>&nbsp;，数组中包含 <strong>互不相同</strong>&nbsp;的字符串。</p>

<p>如果字符串&nbsp;<code>words[i]</code>&nbsp;与字符串 <code>words[j]</code>&nbsp;满足以下条件，我们称它们可以匹配：</p>

<ul>
	<li>字符串&nbsp;<code>words[i]</code>&nbsp;等于&nbsp;<code>words[j]</code>&nbsp;的反转字符串。</li>
	<li><code>0 &lt;= i &lt; j &lt; words.length</code></li>
</ul>

<p>请你返回数组 <code>words</code>&nbsp;中的&nbsp;<strong>最大</strong>&nbsp;匹配数目。</p>

<p>注意，每个字符串最多匹配一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>words = ["cd","ac","dc","ca","zz"]
<b>输出：</b>2
<strong>解释：</strong>在此示例中，我们可以通过以下方式匹配 2 对字符串：
- 我们将第 0 个字符串与第 2 个字符串匹配，因为 word[0] 的反转字符串是 "dc" 并且等于 words[2]。
- 我们将第 1 个字符串与第 3 个字符串匹配，因为 word[1] 的反转字符串是 "ca" 并且等于 words[3]。
可以证明最多匹配数目是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>words = ["ab","ba","cc"]
<b>输出：</b>1
<b>解释：</b>在此示例中，我们可以通过以下方式匹配 1 对字符串：
- 我们将第 0 个字符串与第 1 个字符串匹配，因为 words[1] 的反转字符串 "ab" 与 words[0] 相等。
可以证明最多匹配数目是 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>words = ["aa","ab"]
<b>输出：</b>0
<strong>解释：</strong>这个例子中，无法匹配任何字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>words[i].length == 2</code></li>
	<li><code>words</code>&nbsp;包含的字符串互不相同。</li>
	<li><code>words[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串
- 模拟

## 提示

1. Notice that array words consist of distinct strings.
2. Iterate over all indices (i, j) and check if they can be paired.

## 示例

```
["cd","ac","dc","ca","zz"]
["ab","ba","cc"]
["aa","ab"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
```

### C

```c
int maximumNumberOfStringPairs(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumNumberOfStringPairs(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var maximumNumberOfStringPairs = function(words) {
    
};
```

### TypeScript

```typescript
function maximumNumberOfStringPairs(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function maximumNumberOfStringPairs($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumNumberOfStringPairs(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumNumberOfStringPairs(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumNumberOfStringPairs(List<String> words) {
    
  }
}
```

### Go

```golang
func maximumNumberOfStringPairs(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def maximum_number_of_string_pairs(words)
    
end
```

### Scala

```scala
object Solution {
    def maximumNumberOfStringPairs(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-number-of-string-pairs words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_number_of_string_pairs(Words :: [unicode:unicode_binary()]) -> integer().
maximum_number_of_string_pairs(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_number_of_string_pairs(words :: [String.t]) :: integer
  def maximum_number_of_string_pairs(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumNumberOfStringPairs(words: Array<String>): Int64 {

    }
}
```

