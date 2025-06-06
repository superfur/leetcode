# 966. 元音拼写检查器

## 题目描述

<p>在给定单词列表&nbsp;<code>wordlist</code>&nbsp;的情况下，我们希望实现一个拼写检查器，将查询单词转换为正确的单词。</p>

<p>对于给定的查询单词&nbsp;<code>query</code>，拼写检查器将会处理两类拼写错误：</p>

<ul>
	<li>大小写：如果查询匹配单词列表中的某个单词（<strong>不区分大小写</strong>），则返回的正确单词与单词列表中的大小写相同。

	<ul>
		<li>例如：<code>wordlist = ["yellow"]</code>, <code>query = "YellOw"</code>: <code>correct = "yellow"</code></li>
		<li>例如：<code>wordlist = ["Yellow"]</code>, <code>query = "yellow"</code>: <code>correct = "Yellow"</code></li>
		<li>例如：<code>wordlist = ["yellow"]</code>, <code>query = "yellow"</code>: <code>correct = "yellow"</code></li>
	</ul>
	</li>
	<li>元音错误：如果在将查询单词中的元音 <code>('a', 'e', 'i', 'o', 'u')</code>&nbsp;&nbsp;分别替换为任何元音后，能与单词列表中的单词匹配（<strong>不区分大小写</strong>），则返回的正确单词与单词列表中的匹配项大小写相同。
	<ul>
		<li>例如：<code>wordlist = ["YellOw"]</code>, <code>query = "yollow"</code>: <code>correct = "YellOw"</code></li>
		<li>例如：<code>wordlist = ["YellOw"]</code>, <code>query = "yeellow"</code>: <code>correct = ""</code> （无匹配项）</li>
		<li>例如：<code>wordlist = ["YellOw"]</code>, <code>query = "yllw"</code>: <code>correct = ""</code> （无匹配项）</li>
	</ul>
	</li>
</ul>

<p>此外，拼写检查器还按照以下优先级规则操作：</p>

<ul>
	<li>当查询完全匹配单词列表中的某个单词（<strong>区分大小写</strong>）时，应返回相同的单词。</li>
	<li>当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。</li>
	<li>当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。</li>
	<li>如果该查询在单词列表中没有匹配项，则应返回空字符串。</li>
</ul>

<p>给出一些查询 <code>queries</code>，返回一个单词列表 <code>answer</code>，其中 <code>answer[i]</code> 是由查询 <code>query = queries[i]</code> 得到的正确单词。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
<strong>输出：</strong>["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>wordlist = ["yellow"], queries = ["YellOw"]
<b>输出：</b>["yellow"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= wordlist.length, queries.length &lt;= 5000</code></li>
	<li><code>1 &lt;= wordlist[i].length, queries[i].length &lt;= 7</code></li>
	<li><code>wordlist[i]</code>&nbsp;和&nbsp;<code>queries[i]</code>&nbsp;只包含英文字母</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["KiTe","kite","hare","Hare"]
["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
["yellow"]
["YellOw"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** spellchecker(char** wordlist, int wordlistSize, char** queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] Spellchecker(string[] wordlist, string[] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} wordlist
 * @param {string[]} queries
 * @return {string[]}
 */
var spellchecker = function(wordlist, queries) {
    
};
```

### TypeScript

```typescript
function spellchecker(wordlist: string[], queries: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $wordlist
     * @param String[] $queries
     * @return String[]
     */
    function spellchecker($wordlist, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func spellchecker(_ wordlist: [String], _ queries: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun spellchecker(wordlist: Array<String>, queries: Array<String>): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> spellchecker(List<String> wordlist, List<String> queries) {
    
  }
}
```

### Go

```golang
func spellchecker(wordlist []string, queries []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} wordlist
# @param {String[]} queries
# @return {String[]}
def spellchecker(wordlist, queries)
    
end
```

### Scala

```scala
object Solution {
    def spellchecker(wordlist: Array[String], queries: Array[String]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn spellchecker(wordlist: Vec<String>, queries: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (spellchecker wordlist queries)
  (-> (listof string?) (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec spellchecker(Wordlist :: [unicode:unicode_binary()], Queries :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
spellchecker(Wordlist, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec spellchecker(wordlist :: [String.t], queries :: [String.t]) :: [String.t]
  def spellchecker(wordlist, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func spellchecker(wordlist: Array<String>, queries: Array<String>): Array<String> {

    }
}
```

