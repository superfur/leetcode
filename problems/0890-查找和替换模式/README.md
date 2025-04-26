# 890. 查找和替换模式

## 题目描述

<p>你有一个单词列表&nbsp;<code>words</code>&nbsp;和一个模式&nbsp;&nbsp;<code>pattern</code>，你想知道 <code>words</code> 中的哪些单词与模式匹配。</p>

<p>如果存在字母的排列 <code>p</code>&nbsp;，使得将模式中的每个字母 <code>x</code> 替换为 <code>p(x)</code> 之后，我们就得到了所需的单词，那么单词与模式是匹配的。</p>

<p><em>（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）</em></p>

<p>返回 <code>words</code> 中与给定模式匹配的单词列表。</p>

<p>你可以按任何顺序返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>words = [&quot;abc&quot;,&quot;deq&quot;,&quot;mee&quot;,&quot;aqq&quot;,&quot;dkd&quot;,&quot;ccc&quot;], pattern = &quot;abb&quot;
<strong>输出：</strong>[&quot;mee&quot;,&quot;aqq&quot;]
<strong>解释：
</strong>&quot;mee&quot; 与模式匹配，因为存在排列 {a -&gt; m, b -&gt; e, ...}。
&quot;ccc&quot; 与模式不匹配，因为 {a -&gt; c, b -&gt; c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>1 &lt;= pattern.length = words[i].length&nbsp;&lt;= 20</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["abc","deq","mee","aqq","dkd","ccc"]
"abb"
["a","b","c"]
"a"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findAndReplacePattern(char** words, int wordsSize, char* pattern, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> FindAndReplacePattern(string[] words, string pattern) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} pattern
 * @return {string[]}
 */
var findAndReplacePattern = function(words, pattern) {
    
};
```

### TypeScript

```typescript
function findAndReplacePattern(words: string[], pattern: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $pattern
     * @return String[]
     */
    function findAndReplacePattern($words, $pattern) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findAndReplacePattern(_ words: [String], _ pattern: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findAndReplacePattern(words: Array<String>, pattern: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findAndReplacePattern(List<String> words, String pattern) {
    
  }
}
```

### Go

```golang
func findAndReplacePattern(words []string, pattern string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} pattern
# @return {String[]}
def find_and_replace_pattern(words, pattern)
    
end
```

### Scala

```scala
object Solution {
    def findAndReplacePattern(words: Array[String], pattern: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-and-replace-pattern words pattern)
  (-> (listof string?) string? (listof string?))
  )
```

### Erlang

```erlang
-spec find_and_replace_pattern(Words :: [unicode:unicode_binary()], Pattern :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
find_and_replace_pattern(Words, Pattern) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_and_replace_pattern(words :: [String.t], pattern :: String.t) :: [String.t]
  def find_and_replace_pattern(words, pattern) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findAndReplacePattern(words: Array<String>, pattern: String): ArrayList<String> {

    }
}
```

