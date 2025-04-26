# 1048. 最长字符串链

## 题目描述

<p>给出一个单词数组&nbsp;<code>words</code>&nbsp;，其中每个单词都由小写英文字母组成。</p>

<p>如果我们可以&nbsp;<strong>不改变其他字符的顺序&nbsp;</strong>，在 <code>word<sub>A</sub></code>&nbsp;的任何地方添加 <strong>恰好一个</strong> 字母使其变成&nbsp;<code>word<sub>B</sub></code>&nbsp;，那么我们认为&nbsp;<code>word<sub>A</sub></code>&nbsp;是&nbsp;<code>word<sub>B</sub></code>&nbsp;的 <strong>前身</strong> 。</p>

<ul>
	<li>例如，<code>"abc"</code>&nbsp;是&nbsp;<code>"abac"</code>&nbsp;的 <strong>前身</strong>&nbsp;，而&nbsp;<code>"cba"</code>&nbsp;不是&nbsp;<code>"bcad"</code>&nbsp;的 <strong>前身</strong></li>
</ul>

<p><strong>词链</strong>是单词&nbsp;<code>[word_1, word_2, ..., word_k]</code>&nbsp;组成的序列，<code>k &gt;= 1</code>，其中&nbsp;<code>word<sub>1</sub></code>&nbsp;是&nbsp;<code>word<sub>2</sub></code>&nbsp;的前身，<code>word<sub>2</sub></code>&nbsp;是&nbsp;<code>word<sub>3</sub></code>&nbsp;的前身，依此类推。一个单词通常是 <code>k == 1</code> 的 <strong>单词链</strong>&nbsp;。</p>

<p>从给定单词列表 <code>words</code> 中选择单词组成词链，返回 词链的&nbsp;<strong>最长可能长度</strong> 。<br />
&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["a","b","ba","bca","bda","bdca"]
<strong>输出：</strong>4
<strong>解释：</strong>最长单词链之一为 ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
<b>输出：</b>5
<b>解释：</b>所有的单词都可以放入单词链 ["xb", "xb<u>c</u>", "<u>c</u>xbc", "<u>p</u>cxbc", "pcxbc<u>f</u>"].
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<b>输入：</b>words = ["abcd","dbqca"]
<strong>输出：</strong>1
<b>解释：</b>字链["abcd"]是最长的字链之一。
["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变了。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code>&nbsp;仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 字符串
- 动态规划
- 排序

## 提示

1. Instead of adding a character, try deleting a character to form a chain in reverse.
2. For each word in order of length, for each word2 which is word with one character removed, length[word2] = max(length[word2], length[word] + 1).

## 示例

```
["a","b","ba","bca","bda","bdca"]
["xbc","pcxbcf","xb","cxbc","pcxbc"]
["abcd","dbqca"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestStrChain(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
```

### C

```c
int longestStrChain(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestStrChain(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var longestStrChain = function(words) {
    
};
```

### TypeScript

```typescript
function longestStrChain(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function longestStrChain($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestStrChain(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestStrChain(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestStrChain(List<String> words) {
    
  }
}
```

### Go

```golang
func longestStrChain(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def longest_str_chain(words)
    
end
```

### Scala

```scala
object Solution {
    def longestStrChain(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_str_chain(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-str-chain words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_str_chain(Words :: [unicode:unicode_binary()]) -> integer().
longest_str_chain(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_str_chain(words :: [String.t]) :: integer
  def longest_str_chain(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestStrChain(words: Array<String>): Int64 {

    }
}
```

