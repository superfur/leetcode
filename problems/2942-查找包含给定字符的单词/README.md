# 2942. 查找包含给定字符的单词

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串数组&nbsp;<code>words</code>&nbsp;和一个字符&nbsp;<code>x</code>&nbsp;。</p>

<p>请你返回一个 <strong>下标数组</strong>&nbsp;，表示下标在数组中对应的单词包含字符 <code>x</code>&nbsp;。</p>

<p><b>注意</b>&nbsp;，返回的数组可以是&nbsp;<strong>任意</strong>&nbsp;顺序。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>words = ["leet","code"], x = "e"
<b>输出：</b>[0,1]
<b>解释：</b>"e" 在两个单词中都出现了："l<em><strong>ee</strong></em>t" 和 "cod<em><strong>e</strong></em>" 。所以我们返回下标 0 和 1 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>words = ["abc","bcd","aaaa","cbc"], x = "a"
<b>输出：</b>[0,2]
<b>解释：</b>"a" 在 "<em><strong>a</strong></em>bc" 和 "<em><strong>aaaa</strong></em>" 中出现了，所以我们返回下标 0 和 2 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>words = ["abc","bcd","aaaa","cbc"], x = "z"
<b>输出：</b>[]
<b>解释：</b>"z" 没有在任何单词中出现。所以我们返回空数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>x</code>&nbsp;是一个小写英文字母。</li>
	<li><code>words[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Use two nested loops.

## 示例

```
["leet","code"]
"e"
["abc","bcd","aaaa","cbc"]
"a"
["abc","bcd","aaaa","cbc"]
"z"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindWordsContaining(string[] words, char x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function(words, x) {
    
};
```

### TypeScript

```typescript
function findWordsContaining(words: string[], x: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $x
     * @return Integer[]
     */
    function findWordsContaining($words, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findWordsContaining(_ words: [String], _ x: Character) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findWordsContaining(words: Array<String>, x: Char): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findWordsContaining(List<String> words, String x) {
    
  }
}
```

### Go

```golang
func findWordsContaining(words []string, x byte) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {Character} x
# @return {Integer[]}
def find_words_containing(words, x)
    
end
```

### Scala

```scala
object Solution {
    def findWordsContaining(words: Array[String], x: Char): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-words-containing words x)
  (-> (listof string?) char? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_words_containing(Words :: [unicode:unicode_binary()], X :: char()) -> [integer()].
find_words_containing(Words, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_words_containing(words :: [String.t], x :: char) :: [integer]
  def find_words_containing(words, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findWordsContaining(words: Array<String>, x: Rune): ArrayList<Int64> {

    }
}
```

