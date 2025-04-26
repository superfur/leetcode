# 139. 单词拆分

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符串列表 <code>wordDict</code> 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 <code>s</code>&nbsp;则返回 <code>true</code>。</p>

<p><strong>注意：</strong>不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> s = "leetcode", wordDict = ["leet", "code"]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> s = "applepenapple", wordDict = ["apple", "pen"]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
&nbsp;    注意，你可以重复使用字典中的单词。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
<strong>输出:</strong> false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 20</code></li>
	<li><code>s</code> 和 <code>wordDict[i]</code> 仅由小写英文字母组成</li>
	<li><code>wordDict</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 记忆化搜索
- 数组
- 哈希表
- 字符串
- 动态规划

## 示例

```
"leetcode"
["leet","code"]
"applepenapple"
["apple","pen"]
"catsandog"
["cats","dog","sand","and","cat"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
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
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
```

### C

```c
bool wordBreak(char* s, char** wordDict, int wordDictSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    
};
```

### TypeScript

```typescript
function wordBreak(s: string, wordDict: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $wordDict
     * @return Boolean
     */
    function wordBreak($s, $wordDict) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool wordBreak(String s, List<String> wordDict) {
    
  }
}
```

### Go

```golang
func wordBreak(s string, wordDict []string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    
end
```

### Scala

```scala
object Solution {
    def wordBreak(s: String, wordDict: List[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (word-break s wordDict)
  (-> string? (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec word_break(S :: unicode:unicode_binary(), WordDict :: [unicode:unicode_binary()]) -> boolean().
word_break(S, WordDict) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec word_break(s :: String.t, word_dict :: [String.t]) :: boolean
  def word_break(s, word_dict) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wordBreak(s: String, wordDict: ArrayList<String>): Bool {

    }
}
```

