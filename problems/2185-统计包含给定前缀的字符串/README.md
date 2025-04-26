# 2185. 统计包含给定前缀的字符串

## 题目描述

<p>给你一个字符串数组 <code>words</code> 和一个字符串 <code>pref</code> 。</p>

<p>返回 <code>words</code><em> </em>中以 <code>pref</code> 作为 <strong>前缀</strong> 的字符串的数目。</p>

<p>字符串 <code>s</code> 的 <strong>前缀</strong> 就是&nbsp; <code>s</code> 的任一前导连续字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = ["pay","<em><strong>at</strong></em>tention","practice","<em><strong>at</strong></em>tend"], <code>pref </code>= "at"
<strong>输出：</strong>2
<strong>解释：</strong>以 "at" 作为前缀的字符串有两个，分别是："<em><strong>at</strong></em>tention" 和 "<em><strong>at</strong></em>tend" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = ["leetcode","win","loops","success"], <code>pref </code>= "code"
<strong>输出：</strong>0
<strong>解释：</strong>不存在以 "code" 作为前缀的字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length, pref.length &lt;= 100</code></li>
	<li><code>words[i]</code> 和 <code>pref</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串
- 字符串匹配

## 提示

1. Go through each word in words and increment the answer if pref is a prefix of the word.

## 示例

```
["pay","attention","practice","attend"]
"at"
["leetcode","win","loops","success"]
"code"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        
    }
};
```

### Java

```java
class Solution {
    public int prefixCount(String[] words, String pref) {
        
    }
}
```

### Python

```python
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
```

### C

```c
int prefixCount(char** words, int wordsSize, char* pref) {
    
}
```

### C#

```csharp
public class Solution {
    public int PrefixCount(string[] words, string pref) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
    
};
```

### TypeScript

```typescript
function prefixCount(words: string[], pref: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $pref
     * @return Integer
     */
    function prefixCount($words, $pref) {
        
    }
}
```

### Swift

```swift
class Solution {
    func prefixCount(_ words: [String], _ pref: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun prefixCount(words: Array<String>, pref: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int prefixCount(List<String> words, String pref) {
    
  }
}
```

### Go

```golang
func prefixCount(words []string, pref string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} pref
# @return {Integer}
def prefix_count(words, pref)
    
end
```

### Scala

```scala
object Solution {
    def prefixCount(words: Array[String], pref: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn prefix_count(words: Vec<String>, pref: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (prefix-count words pref)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec prefix_count(Words :: [unicode:unicode_binary()], Pref :: unicode:unicode_binary()) -> integer().
prefix_count(Words, Pref) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec prefix_count(words :: [String.t], pref :: String.t) :: integer
  def prefix_count(words, pref) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func prefixCount(words: Array<String>, pref: String): Int64 {

    }
}
```

