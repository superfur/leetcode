# 127. 单词接龙

## 题目描述

<p>字典&nbsp;<code>wordList</code> 中从单词 <code>beginWord</code><em>&nbsp;</em>到&nbsp;<code>endWord</code> 的 <strong>转换序列 </strong>是一个按下述规格形成的序列<meta charset="UTF-8" />&nbsp;<code>beginWord -&gt; s<sub>1</sub>&nbsp;-&gt; s<sub>2</sub>&nbsp;-&gt; ... -&gt; s<sub>k</sub></code>：</p>

<ul>
	<li>每一对相邻的单词只差一个字母。</li>
	<li><meta charset="UTF-8" />&nbsp;对于&nbsp;<code>1 &lt;= i &lt;= k</code>&nbsp;时，每个<meta charset="UTF-8" />&nbsp;<code>s<sub>i</sub></code>&nbsp;都在<meta charset="UTF-8" />&nbsp;<code>wordList</code>&nbsp;中。注意， <code>beginWord</code><em>&nbsp;</em>不需要在<meta charset="UTF-8" />&nbsp;<code>wordList</code>&nbsp;中。<meta charset="UTF-8" /></li>
	<li><code>s<sub>k</sub>&nbsp;== endWord</code></li>
</ul>

<p>给你两个单词<em> </em><code>beginWord</code><em>&nbsp;</em>和 <code>endWord</code> 和一个字典 <code>wordList</code> ，返回 <em>从&nbsp;<code>beginWord</code> 到&nbsp;<code>endWord</code> 的 <strong>最短转换序列</strong> 中的 <strong>单词数目</strong></em> 。如果不存在这样的转换序列，返回 <code>0</code> 。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>输出：</strong>5
<strong>解释：</strong>一个最短转换序列是 "hit" -&gt; "hot" -&gt; "dot" -&gt; "dog" -&gt; "cog", 返回它的长度 5。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>输出：</strong>0
<strong>解释：</strong>endWord "cog" 不在字典中，所以无法进行转换。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= beginWord.length &lt;= 10</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 5000</code></li>
	<li><code>wordList[i].length == beginWord.length</code></li>
	<li><code>beginWord</code>、<code>endWord</code> 和 <code>wordList[i]</code> 由小写英文字母组成</li>
	<li><code>beginWord != endWord</code></li>
	<li><code>wordList</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 哈希表
- 字符串

## 示例

```
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
"hit"
"cog"
["hot","dot","dog","lot","log"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
    }
};
```

### Java

```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
    }
}
```

### Python

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
```

### C

```c
int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LadderLength(string beginWord, string endWord, IList<string> wordList) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    
};
```

### TypeScript

```typescript
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $beginWord
     * @param String $endWord
     * @param String[] $wordList
     * @return Integer
     */
    function ladderLength($beginWord, $endWord, $wordList) {
        
    }
}
```

### Swift

```swift
class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int ladderLength(String beginWord, String endWord, List<String> wordList) {
    
  }
}
```

### Go

```golang
func ladderLength(beginWord string, endWord string, wordList []string) int {
    
}
```

### Ruby

```ruby
# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {Integer}
def ladder_length(begin_word, end_word, word_list)
    
end
```

### Scala

```scala
object Solution {
    def ladderLength(beginWord: String, endWord: String, wordList: List[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ladder-length beginWord endWord wordList)
  (-> string? string? (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec ladder_length(BeginWord :: unicode:unicode_binary(), EndWord :: unicode:unicode_binary(), WordList :: [unicode:unicode_binary()]) -> integer().
ladder_length(BeginWord, EndWord, WordList) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ladder_length(begin_word :: String.t, end_word :: String.t, word_list :: [String.t]) :: integer
  def ladder_length(begin_word, end_word, word_list) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func ladderLength(beginWord: String, endWord: String, wordList: ArrayList<String>): Int64 {

    }
}
```

