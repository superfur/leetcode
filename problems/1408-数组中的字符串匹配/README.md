# 1408. 数组中的字符串匹配

## 题目描述

<p>给你一个字符串数组 <code>words</code> ，数组中的每个字符串都可以看作是一个单词。请你按 <strong>任意</strong> 顺序返回 <code>words</code> 中是其他单词的 <span data-keyword="substring-nonempty">子字符串</span> 的所有单词。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["mass","as","hero","superhero"]
<strong>输出：</strong>["as","hero"]
<strong>解释：</strong>"as" 是 "mass" 的子字符串，"hero" 是 "superhero" 的子字符串。
["hero","as"] 也是有效的答案。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["leetcode","et","code"]
<strong>输出：</strong>["et","code"]
<strong>解释：</strong>"et" 和 "code" 都是 "leetcode" 的子字符串。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["blue","green","bu"]
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code> 仅包含小写英文字母。</li>
	<li>题目数据 <strong>保证</strong> <code>words</code>&nbsp;的每个字符串都是独一无二的。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串
- 字符串匹配

## 提示

1. Bruteforce to find if one string is substring of another or use KMP algorithm.

## 示例

```
["mass","as","hero","superhero"]
["leetcode","et","code"]
["blue","green","bu"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> stringMatching(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** stringMatching(char** words, int wordsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> StringMatching(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function(words) {
    
};
```

### TypeScript

```typescript
function stringMatching(words: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String[]
     */
    function stringMatching($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stringMatching(_ words: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stringMatching(words: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> stringMatching(List<String> words) {
    
  }
}
```

### Go

```golang
func stringMatching(words []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String[]}
def string_matching(words)
    
end
```

### Scala

```scala
object Solution {
    def stringMatching(words: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (string-matching words)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec string_matching(Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
string_matching(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec string_matching(words :: [String.t]) :: [String.t]
  def string_matching(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stringMatching(words: Array<String>): ArrayList<String> {

    }
}
```

