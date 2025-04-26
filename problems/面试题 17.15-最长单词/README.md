# 面试题 17.15. 最长单词

## 题目描述

<p>给定一组单词<code>words</code>，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong> [&quot;cat&quot;,&quot;banana&quot;,&quot;dog&quot;,&quot;nana&quot;,&quot;walk&quot;,&quot;walker&quot;,&quot;dogwalker&quot;]
<strong>输出：</strong> &quot;dogwalker&quot;
<strong>解释：</strong> &quot;dogwalker&quot;可由&quot;dog&quot;和&quot;walker&quot;组成。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= len(words) &lt;= 200</code></li>
	<li><code>1 &lt;= len(words[i]) &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串

## 提示

1. 试着简化这个问题：如果你只需要知道由列表中其他两个单词组成的最长单词会如何？
2. 如果只想知道由列表中其他两个单词组成的最长单词，那么可以遍历全部单词，从最长到最短，检查每个单词是否可以由其他两个单词组成。为了检查，我们可以将字符串从所有可能的位置分开。
3. 将前面的想法扩展到多个单词的情况。我们能不能把每个单词都拆分为所有可能的形式?
4. 当你得到非常低效的递归算法时，试着查找重复发生的子问题。

## 示例

```
[""]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestWord(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestWord(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
```

### C

```c
char* longestWord(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestWord(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function(words) {
    
};
```

### TypeScript

```typescript
function longestWord(words: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function longestWord($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestWord(_ words: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestWord(words: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestWord(List<String> words) {
    
  }
}
```

### Go

```golang
func longestWord(words []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String}
def longest_word(words)
    
end
```

### Scala

```scala
object Solution {
    def longestWord(words: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_word(words: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-word words)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec longest_word(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
longest_word(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_word(words :: [String.t]) :: String.t
  def longest_word(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestWord(words: Array<String>): String {

    }
}
```

