# 2452. 距离字典两次编辑以内的单词

## 题目描述

<p>给你两个字符串数组&nbsp;<code>queries</code> 和&nbsp;<code>dictionary</code>&nbsp;。数组中所有单词都只包含小写英文字母，且长度都相同。</p>

<p>一次 <strong>编辑</strong>&nbsp;中，你可以从 <code>queries</code>&nbsp;中选择一个单词，将任意一个字母修改成任何其他字母。从&nbsp;<code>queries</code>&nbsp;中找到所有满足以下条件的字符串：<strong>不超过</strong>&nbsp;两次编辑内，字符串与&nbsp;<code>dictionary</code>&nbsp;中某个字符串相同。</p>

<p>请你返回<em>&nbsp;</em><code>queries</code>&nbsp;中的单词列表，这些单词距离&nbsp;<code>dictionary</code>&nbsp;中的单词&nbsp;<strong>编辑次数</strong>&nbsp;不超过&nbsp;<strong>两次</strong>&nbsp;。单词返回的顺序需要与&nbsp;<code>queries</code>&nbsp;中原本顺序相同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
<b>输出：</b>["word","note","wood"]
<strong>解释：</strong>
- 将 "word" 中的 'r' 换成 'o' ，得到 dictionary 中的单词 "wood" 。
- 将 "note" 中的 'n' 换成 'j' 且将 't' 换成 'k' ，得到 "joke" 。
- "ants" 需要超过 2 次编辑才能得到 dictionary 中的单词。
- "wood" 不需要修改（0 次编辑），就得到 dictionary 中相同的单词。
所以我们返回 ["word","note","wood"] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>queries = ["yes"], dictionary = ["not"]
<b>输出：</b>[]
<strong>解释：</strong>
"yes" 需要超过 2 次编辑才能得到 "not" 。
所以我们返回空数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= queries.length, dictionary.length &lt;= 100</code></li>
	<li><code>n == queries[i].length == dictionary[j].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li>所有&nbsp;<code>queries[i]</code> 和&nbsp;<code>dictionary[j]</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 字符串

## 提示

1. Try brute-forcing the problem.
2. For each word in queries, try comparing to each word in dictionary.
3. If there is a maximum of two edit differences, the word should be present in answer.

## 示例

```
["word","note","ants","wood"]
["wood","joke","moat"]
["yes"]
["not"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        
    }
}
```

### Python

```python
class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** twoEditWords(char** queries, int queriesSize, char** dictionary, int dictionarySize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> TwoEditWords(string[] queries, string[] dictionary) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
var twoEditWords = function(queries, dictionary) {
    
};
```

### TypeScript

```typescript
function twoEditWords(queries: string[], dictionary: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $queries
     * @param String[] $dictionary
     * @return String[]
     */
    function twoEditWords($queries, $dictionary) {
        
    }
}
```

### Swift

```swift
class Solution {
    func twoEditWords(_ queries: [String], _ dictionary: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun twoEditWords(queries: Array<String>, dictionary: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> twoEditWords(List<String> queries, List<String> dictionary) {
    
  }
}
```

### Go

```golang
func twoEditWords(queries []string, dictionary []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} queries
# @param {String[]} dictionary
# @return {String[]}
def two_edit_words(queries, dictionary)
    
end
```

### Scala

```scala
object Solution {
    def twoEditWords(queries: Array[String], dictionary: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (two-edit-words queries dictionary)
  (-> (listof string?) (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec two_edit_words(Queries :: [unicode:unicode_binary()], Dictionary :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
two_edit_words(Queries, Dictionary) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec two_edit_words(queries :: [String.t], dictionary :: [String.t]) :: [String.t]
  def two_edit_words(queries, dictionary) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func twoEditWords(queries: Array<String>, dictionary: Array<String>): ArrayList<String> {

    }
}
```

