# 2788. 按分隔符拆分字符串

## 题目描述

<p>给你一个字符串数组 <code>words</code> 和一个字符 <code>separator</code> ，请你按 <code>separator</code> 拆分 <code>words</code> 中的每个字符串。</p>

<p>返回一个由拆分后的新字符串组成的字符串数组，<strong>不包括空字符串</strong> 。</p>

<p><strong>注意</strong></p>

<ul>
	<li><code>separator</code> 用于决定拆分发生的位置，但它不包含在结果字符串中。</li>
	<li>拆分可能形成两个以上的字符串。</li>
	<li>结果字符串必须保持初始相同的先后顺序。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["one.two.three","four.five","six"], separator = "."
<strong>输出：</strong>["one","two","three","four","five","six"]
<strong>解释：</strong>在本示例中，我们进行下述拆分：

"one.two.three" 拆分为 "one", "two", "three"
"four.five" 拆分为 "four", "five"
"six" 拆分为 "six" 

因此，结果数组为 ["one","two","three","four","five","six"] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["$easy$","$problem$"], separator = "$"
<strong>输出：</strong>["easy","problem"]
<strong>解释：</strong>在本示例中，我们进行下述拆分：

"$easy$" 拆分为 "easy"（不包括空字符串）
"$problem$" 拆分为 "problem"（不包括空字符串）

因此，结果数组为 ["easy","problem"] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["|||"], separator = "|"
<strong>输出：</strong>[]
<strong>解释：</strong>在本示例中，"|||" 的拆分结果将只包含一些空字符串，所以我们返回一个空数组 [] 。 </pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>words[i]</code> 中的字符要么是小写英文字母，要么就是字符串 <code>".,|$#@"</code> 中的字符（不包括引号）</li>
	<li><code>separator</code> 是字符串 <code>".,|$#@"</code> 中的某个字符（不包括引号）</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Iterate over each string in the given array using a loop and perform string splitting based on the provided separator character.
2. Be sure not to return empty strings.

## 示例

```
["one.two.three","four.five","six"]
"."
["$easy$","$problem$"]
"$"
["|||"]
"|"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        
    }
}
```

### Python

```python
class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** splitWordsBySeparator(char** words, int wordsSize, char separator, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> SplitWordsBySeparator(IList<string> words, char separator) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {character} separator
 * @return {string[]}
 */
var splitWordsBySeparator = function(words, separator) {
    
};
```

### TypeScript

```typescript
function splitWordsBySeparator(words: string[], separator: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $separator
     * @return String[]
     */
    function splitWordsBySeparator($words, $separator) {
        
    }
}
```

### Swift

```swift
class Solution {
    func splitWordsBySeparator(_ words: [String], _ separator: Character) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun splitWordsBySeparator(words: List<String>, separator: Char): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> splitWordsBySeparator(List<String> words, String separator) {
    
  }
}
```

### Go

```golang
func splitWordsBySeparator(words []string, separator byte) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {Character} separator
# @return {String[]}
def split_words_by_separator(words, separator)
    
end
```

### Scala

```scala
object Solution {
    def splitWordsBySeparator(words: List[String], separator: Char): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn split_words_by_separator(words: Vec<String>, separator: char) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (split-words-by-separator words separator)
  (-> (listof string?) char? (listof string?))
  )
```

### Erlang

```erlang
-spec split_words_by_separator(Words :: [unicode:unicode_binary()], Separator :: char()) -> [unicode:unicode_binary()].
split_words_by_separator(Words, Separator) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec split_words_by_separator(words :: [String.t], separator :: char) :: [String.t]
  def split_words_by_separator(words, separator) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func splitWordsBySeparator(words: ArrayList<String>, separator: Rune): ArrayList<String> {

    }
}
```

