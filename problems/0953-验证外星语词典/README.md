# 953. 验证外星语词典

## 题目描述

<p>某种外星语也使用英文小写字母，但可能顺序 <code>order</code> 不同。字母表的顺序（<code>order</code>）是一些小写字母的排列。</p>

<p>给定一组用外星语书写的单词 <code>words</code>，以及其字母表的顺序 <code>order</code>，只有当给定的单词在这种外星语中按字典序排列时，返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
<strong>输出：</strong>true
<strong>解释：</strong>在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
<strong>输出：</strong>false
<strong>解释：</strong>在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
<strong>输出：</strong>false
<strong>解释：</strong>当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（<a href="https://baike.baidu.com/item/%E5%AD%97%E5%85%B8%E5%BA%8F" target="_blank">更多信息</a>）。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= words.length <= 100</code></li>
	<li><code>1 <= words[i].length <= 20</code></li>
	<li><code>order.length == 26</code></li>
	<li>在 <code>words[i]</code> 和 <code>order</code> 中的所有字符都是英文小写字母。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["hello","leetcode"]
"hlabcdefgijkmnopqrstuvwxyz"
["word","world","row"]
"worldabcefghijkmnpqstuvxyz"
["apple","app"]
"abcdefghijklmnopqrstuvwxyz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
```

### C

```c
bool isAlienSorted(char** words, int wordsSize, char* order) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsAlienSorted(string[] words, string order) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    
};
```

### TypeScript

```typescript
function isAlienSorted(words: string[], order: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $order
     * @return Boolean
     */
    function isAlienSorted($words, $order) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isAlienSorted(_ words: [String], _ order: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isAlienSorted(words: Array<String>, order: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isAlienSorted(List<String> words, String order) {
    
  }
}
```

### Go

```golang
func isAlienSorted(words []string, order string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} order
# @return {Boolean}
def is_alien_sorted(words, order)
    
end
```

### Scala

```scala
object Solution {
    def isAlienSorted(words: Array[String], order: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-alien-sorted words order)
  (-> (listof string?) string? boolean?)
  )
```

### Erlang

```erlang
-spec is_alien_sorted(Words :: [unicode:unicode_binary()], Order :: unicode:unicode_binary()) -> boolean().
is_alien_sorted(Words, Order) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_alien_sorted(words :: [String.t], order :: String.t) :: boolean
  def is_alien_sorted(words, order) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isAlienSorted(words: Array<String>, order: String): Bool {

    }
}
```

