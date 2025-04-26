# 140. 单词拆分 II

## 题目描述

<p>给定一个字符串 <code>s</code> 和一个字符串字典<meta charset="UTF-8" />&nbsp;<code>wordDict</code>&nbsp;，在字符串<meta charset="UTF-8" />&nbsp;<code>s</code>&nbsp;中增加空格来构建一个句子，使得句子中所有的单词都在词典中。<strong>以任意顺序</strong> 返回所有这些可能的句子。</p>

<p><strong>注意：</strong>词典中的同一个单词可能在分段中被重复使用多次。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入:</strong>s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
<strong>输出:</strong>["cats and dog","cat sand dog"]
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入:</strong>s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
<strong>输出:</strong>["pine apple pen apple","pineapple pen apple","pine applepen apple"]
<strong>解释:</strong> 注意你可以重复使用字典中的单词。
</pre>

<p><strong class="example">示例&nbsp;3：</strong></p>

<pre>
<strong>输入:</strong>s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>输出:</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 10</code></li>
	<li><code>s</code>&nbsp;和&nbsp;<code>wordDict[i]</code>&nbsp;仅有小写英文字母组成</li>
	<li><code>wordDict</code>&nbsp;中所有字符串都 <strong>不同</strong></li>
</ul>


## 难度

Hard

## 标签

- 字典树
- 记忆化搜索
- 数组
- 哈希表
- 字符串
- 动态规划
- 回溯

## 示例

```
"catsanddog"
["cat","cats","and","sand","dog"]
"pineapplepenapple"
["apple","pen","applepen","pine","pineapple"]
"catsandog"
["cats","dog","sand","and","cat"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** wordBreak(char* s, char** wordDict, int wordDictSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> WordBreak(string s, IList<string> wordDict) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 */
var wordBreak = function(s, wordDict) {
    
};
```

### TypeScript

```typescript
function wordBreak(s: string, wordDict: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $wordDict
     * @return String[]
     */
    function wordBreak($s, $wordDict) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wordBreak(s: String, wordDict: List<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> wordBreak(String s, List<String> wordDict) {
    
  }
}
```

### Go

```golang
func wordBreak(s string, wordDict []string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
    
end
```

### Scala

```scala
object Solution {
    def wordBreak(s: String, wordDict: List[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (word-break s wordDict)
  (-> string? (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec word_break(S :: unicode:unicode_binary(), WordDict :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
word_break(S, WordDict) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec word_break(s :: String.t, word_dict :: [String.t]) :: [String.t]
  def word_break(s, word_dict) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wordBreak(s: String, wordDict: ArrayList<String>): ArrayList<String> {

    }
}
```

