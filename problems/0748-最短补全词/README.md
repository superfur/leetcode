# 748. 最短补全词

## 题目描述

<p>给你一个字符串 <code>licensePlate</code> 和一个字符串数组 <code>words</code> ，请你找出&nbsp;<code>words</code> 中的 <strong>最短补全词</strong> 。</p>

<p><strong>补全词 </strong>是一个包含 <code>licensePlate</code> 中所有字母的单词。<strong>忽略</strong>&nbsp;<code>licensePlate</code> 中的 <strong>数字和空格 </strong>。<strong>不区分大小写</strong>。如果某个字母在 <code>licensePlate</code> 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。</p>

<p>例如：<code>licensePlate</code><code> = "aBc 12c"</code>，那么它的补全词应当包含字母 <code>'a'</code>、<code>'b'</code> （忽略大写）和两个 <code>'c'</code> 。可能的 <strong>补全词</strong> 有 <code>"abccdef"</code>、<code>"caaacab"</code> 以及 <code>"cbca"</code> 。</p>

<p>请返回 <code>words</code> 中的 <strong>最短补全词</strong> 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 <code>words</code> 中 <strong>第一个</strong> 出现的那个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
<strong>输出：</strong>"steps"
<strong>解释：</strong>最短补全词应该包括 "s"、"p"、"s"（忽略大小写） 以及 "t"。
"step" 包含 "t"、"p"，但只包含一个 "s"，所以它不符合条件。
"steps" 包含 "t"、"p" 和两个 "s"。
"stripe" 缺一个 "s"。
"stepple" 缺一个 "s"。
因此，"steps" 是唯一一个包含所有字母的单词，也是本例的答案。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
<strong>输出：</strong>"pest"
<strong>解释：</strong>licensePlate 只包含字母 "s" 。所有的单词都包含字母 "s" ，其中 "pest"、"stew"、和 "show" 三者最短。答案是 "pest" ，因为它是三个单词中在 words 里最靠前的那个。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= licensePlate.length &lt;= 7</code></li>
	<li><code>licensePlate</code> 由数字、大小写字母或空格 <code>' '</code> 组成</li>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 15</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Count only the letters (possibly converted to lowercase) of each word.  If a word is shorter and the count of each letter is at least the count of that letter in the licensePlate, it is the best answer we've seen yet.

## 示例

```
"1s3 PSt"
["step","steps","stripe","stepple"]
"1s3 456"
["looks","pest","stew","show"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
```

### C

```c
char* shortestCompletingWord(char* licensePlate, char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string ShortestCompletingWord(string licensePlate, string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
var shortestCompletingWord = function(licensePlate, words) {
    
};
```

### TypeScript

```typescript
function shortestCompletingWord(licensePlate: string, words: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $licensePlate
     * @param String[] $words
     * @return String
     */
    function shortestCompletingWord($licensePlate, $words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestCompletingWord(_ licensePlate: String, _ words: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestCompletingWord(licensePlate: String, words: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String shortestCompletingWord(String licensePlate, List<String> words) {
    
  }
}
```

### Go

```golang
func shortestCompletingWord(licensePlate string, words []string) string {
    
}
```

### Ruby

```ruby
# @param {String} license_plate
# @param {String[]} words
# @return {String}
def shortest_completing_word(license_plate, words)
    
end
```

### Scala

```scala
object Solution {
    def shortestCompletingWord(licensePlate: String, words: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_completing_word(license_plate: String, words: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-completing-word licensePlate words)
  (-> string? (listof string?) string?)
  )
```

### Erlang

```erlang
-spec shortest_completing_word(LicensePlate :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
shortest_completing_word(LicensePlate, Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_completing_word(license_plate :: String.t, words :: [String.t]) :: String.t
  def shortest_completing_word(license_plate, words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestCompletingWord(licensePlate: String, words: Array<String>): String {

    }
}
```

