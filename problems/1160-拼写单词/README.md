# 1160. 拼写单词

## 题目描述

<p>给你一份『词汇表』（字符串数组）&nbsp;<code>words</code>&nbsp;和一张『字母表』（字符串）&nbsp;<code>chars</code>。</p>

<p>假如你可以用&nbsp;<code>chars</code>&nbsp;中的『字母』（字符）拼写出 <code>words</code>&nbsp;中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。</p>

<p>注意：每次拼写（指拼写词汇表中的一个单词）时，<code>chars</code> 中的每个字母都只能用一次。</p>

<p>返回词汇表&nbsp;<code>words</code>&nbsp;中你掌握的所有单词的 <strong>长度之和</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["cat","bt","hat","tree"], chars = "atach"
<strong>输出：</strong>6
<strong>解释： </strong>
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["hello","world","leetcode"], chars = "welldonehoneyr"
<strong>输出：</strong>10
<strong>解释：</strong>
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length, chars.length&nbsp;&lt;= 100</code></li>
	<li>所有字符串中都仅包含小写英文字母</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. Solve the problem for each string in <code>words</code> independently.
2. Now try to think in frequency of letters.
3. Count how many times each character occurs in string <code>chars</code>.
4. To form a string using characters from <code>chars</code>, the frequency of each character in <code>chars</code> must be greater than or equal the frequency of that character in the string to be formed.

## 示例

```
["cat","bt","hat","tree"]
"atach"
["hello","world","leetcode"]
"welldonehoneyr"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        
    }
};
```

### Java

```java
class Solution {
    public int countCharacters(String[] words, String chars) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
```

### C

```c
int countCharacters(char** words, int wordsSize, char* chars) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountCharacters(string[] words, string chars) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    
};
```

### TypeScript

```typescript
function countCharacters(words: string[], chars: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $chars
     * @return Integer
     */
    function countCharacters($words, $chars) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countCharacters(_ words: [String], _ chars: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countCharacters(words: Array<String>, chars: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countCharacters(List<String> words, String chars) {
    
  }
}
```

### Go

```golang
func countCharacters(words []string, chars string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} chars
# @return {Integer}
def count_characters(words, chars)
    
end
```

### Scala

```scala
object Solution {
    def countCharacters(words: Array[String], chars: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-characters words chars)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_characters(Words :: [unicode:unicode_binary()], Chars :: unicode:unicode_binary()) -> integer().
count_characters(Words, Chars) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_characters(words :: [String.t], chars :: String.t) :: integer
  def count_characters(words, chars) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countCharacters(words: Array<String>, chars: String): Int64 {

    }
}
```

