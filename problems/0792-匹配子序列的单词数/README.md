# 792. 匹配子序列的单词数

## 题目描述

<p>给定字符串 <code>s</code>&nbsp;和字符串数组&nbsp;<code>words</code>, 返回&nbsp;&nbsp;<em><code>words[i]</code>&nbsp;中是<code>s</code>的子序列的单词个数</em>&nbsp;。</p>

<p>字符串的 <strong>子序列</strong> 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。</p>

<ul>
	<li>例如， <code>“ace”</code> 是 <code>“abcde”</code> 的子序列。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> s = "abcde", words = ["a","bb","acd","ace"]
<strong>输出:</strong> 3
<strong>解释:</strong> 有三个是&nbsp;s 的子序列的单词: "a", "acd", "ace"。
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>输入: </strong>s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
<strong>输出:</strong> 2
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words.length &lt;= 5000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>words[i]</code>和 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size: 12.6px; background-color: rgb(249, 242, 244);">s</span></font>&nbsp;都只由小写字母组成。</li>
</ul>
<span style="display:block"><span style="height:0px"><span style="position:absolute">​​​​</span></span></span>

## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串
- 二分查找
- 动态规划
- 排序

## 示例

```
"abcde"
["a","bb","acd","ace"]
"dsahjpjauf"
["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
```

### C

```c
int numMatchingSubseq(char* s, char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumMatchingSubseq(string s, string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var numMatchingSubseq = function(s, words) {
    
};
```

### TypeScript

```typescript
function numMatchingSubseq(s: string, words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $words
     * @return Integer
     */
    function numMatchingSubseq($s, $words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numMatchingSubseq(_ s: String, _ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numMatchingSubseq(s: String, words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numMatchingSubseq(String s, List<String> words) {
    
  }
}
```

### Go

```golang
func numMatchingSubseq(s string, words []string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String[]} words
# @return {Integer}
def num_matching_subseq(s, words)
    
end
```

### Scala

```scala
object Solution {
    def numMatchingSubseq(s: String, words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_matching_subseq(s: String, words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-matching-subseq s words)
  (-> string? (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_matching_subseq(S :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> integer().
num_matching_subseq(S, Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_matching_subseq(s :: String.t, words :: [String.t]) :: integer
  def num_matching_subseq(s, words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numMatchingSubseq(s: String, words: Array<String>): Int64 {

    }
}
```

