# 472. 连接词

## 题目描述

<p>给你一个 <strong>不含重复 </strong>单词的字符串数组 <code>words</code> ，请你找出并返回 <code>words</code> 中的所有 <strong>连接词</strong> 。</p>

<p><strong>连接词</strong> 定义为：一个完全由给定数组中的至少两个较短单词（不一定是不同的两个单词）组成的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
<strong>输出：</strong>["catsdogcats","dogcatsdog","ratcatdogcat"]
<strong>解释：</strong>"catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["cat","dog","catdog"]
<strong>输出：</strong>["catdog"]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code>&nbsp;仅由小写英文字母组成。&nbsp;</li>
	<li><code>words</code>&nbsp;中的所有字符串都是 <strong>唯一</strong> 的。</li>
	<li><code>1 &lt;= sum(words[i].length) &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 字典树
- 数组
- 字符串
- 动态规划

## 示例

```
["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
["cat","dog","catdog"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findAllConcatenatedWordsInADict(char** words, int wordsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> FindAllConcatenatedWordsInADict(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function(words) {
    
};
```

### TypeScript

```typescript
function findAllConcatenatedWordsInADict(words: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String[]
     */
    function findAllConcatenatedWordsInADict($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findAllConcatenatedWordsInADict(_ words: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findAllConcatenatedWordsInADict(words: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findAllConcatenatedWordsInADict(List<String> words) {
    
  }
}
```

### Go

```golang
func findAllConcatenatedWordsInADict(words []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String[]}
def find_all_concatenated_words_in_a_dict(words)
    
end
```

### Scala

```scala
object Solution {
    def findAllConcatenatedWordsInADict(words: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_all_concatenated_words_in_a_dict(words: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-all-concatenated-words-in-a-dict words)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec find_all_concatenated_words_in_a_dict(Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_all_concatenated_words_in_a_dict(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_all_concatenated_words_in_a_dict(words :: [String.t]) :: [String.t]
  def find_all_concatenated_words_in_a_dict(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findAllConcatenatedWordsInADict(words: Array<String>): ArrayList<String> {

    }
}
```

