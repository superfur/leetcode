# 3295. 举报垃圾信息

## 题目描述

<p>给你一个字符串数组 <code>message</code> 和一个字符串数组 <code>bannedWords</code>。</p>

<p>如果数组中 <strong>至少</strong> 存在两个单词与 <code>bannedWords</code> 中的任一单词 <strong>完全相同</strong>，则该数组被视为 <strong>垃圾信息</strong>。</p>

<p>如果数组 <code>message</code> 是垃圾信息，则返回 <code>true</code>；否则返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">message = ["hello","world","leetcode"], bannedWords = ["world","hello"]</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>数组 <code>message</code> 中的 <code>"hello"</code> 和 <code>"world"</code> 都出现在数组 <code>bannedWords</code> 中。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]</span></p>

<p><strong>输出：</strong> <span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>数组 <code>message</code> 中只有一个单词（<code>"programming"</code>）出现在数组 <code>bannedWords</code> 中。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= message.length, bannedWords.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= message[i].length, bannedWords[i].length &lt;= 15</code></li>
	<li><code>message[i]</code> 和 <code>bannedWords[i]</code> 都只由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Use hash set.

## 示例

```
["hello","world","leetcode"]
["world","hello"]
["hello","programming","fun"]
["world","programming","leetcode"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool reportSpam(vector<string>& message, vector<string>& bannedWords) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean reportSpam(String[] message, String[] bannedWords) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reportSpam(self, message, bannedWords):
        """
        :type message: List[str]
        :type bannedWords: List[str]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        
```

### C

```c
bool reportSpam(char** message, int messageSize, char** bannedWords, int bannedWordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ReportSpam(string[] message, string[] bannedWords) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} message
 * @param {string[]} bannedWords
 * @return {boolean}
 */
var reportSpam = function(message, bannedWords) {
    
};
```

### TypeScript

```typescript
function reportSpam(message: string[], bannedWords: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $message
     * @param String[] $bannedWords
     * @return Boolean
     */
    function reportSpam($message, $bannedWords) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reportSpam(_ message: [String], _ bannedWords: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reportSpam(message: Array<String>, bannedWords: Array<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool reportSpam(List<String> message, List<String> bannedWords) {
    
  }
}
```

### Go

```golang
func reportSpam(message []string, bannedWords []string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} message
# @param {String[]} banned_words
# @return {Boolean}
def report_spam(message, banned_words)
    
end
```

### Scala

```scala
object Solution {
    def reportSpam(message: Array[String], bannedWords: Array[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn report_spam(message: Vec<String>, banned_words: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (report-spam message bannedWords)
  (-> (listof string?) (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec report_spam(Message :: [unicode:unicode_binary()], BannedWords :: [unicode:unicode_binary()]) -> boolean().
report_spam(Message, BannedWords) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec report_spam(message :: [String.t], banned_words :: [String.t]) :: boolean
  def report_spam(message, banned_words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reportSpam(message: Array<String>, bannedWords: Array<String>): Bool {

    }
}
```

