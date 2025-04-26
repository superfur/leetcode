# 819. 最常见的单词

## 题目描述

<p>给你一个字符串 <code>paragraph</code> 和一个表示禁用词的字符串数组 <code>banned</code> ，返回出现频率最高的非禁用词。题目数据 <strong>保证 </strong>至少存在一个非禁用词，且答案<strong> 唯一 </strong>。</p>

<p><code>paragraph</code> 中的单词 <strong>不区分大小写</strong> ，答案应以 <strong>小写 </strong>形式返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
<strong>输出：</strong>"ball"
<strong>解释：</strong>
"hit" 出现了 3 次，但它是禁用词。
"ball" 出现了两次（没有其他单词出现这么多次），因此它是段落中出现频率最高的非禁用词。
请注意，段落中的单词不区分大小写，
标点符号会被忽略（即使它们紧挨着单词，如 "ball,"），
并且尽管 "hit" 出现的次数更多，但它不能作为答案，因为它是禁用词。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>paragraph = "a.", banned = []
<strong>输出：</strong>"a"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= paragraph.length &lt;= 1000</code></li>
	<li><code>paragraph</code> 由英文字母、空格 <code>' '</code>、和以下符号组成：<code>"!?',;."</code></li>
	<li><code>0 &lt;= banned.length &lt;= 100</code></li>
	<li><code>1 &lt;= banned[i].length &lt;= 10</code></li>
	<li><code>banned[i]</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 示例

```
"Bob hit a ball, the hit BALL flew far after it was hit."
["hit"]
"a."
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        
    }
};
```

### Java

```java
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
```

### C

```c
char* mostCommonWord(char* paragraph, char** banned, int bannedSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string MostCommonWord(string paragraph, string[] banned) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function(paragraph, banned) {
    
};
```

### TypeScript

```typescript
function mostCommonWord(paragraph: string, banned: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $paragraph
     * @param String[] $banned
     * @return String
     */
    function mostCommonWord($paragraph, $banned) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostCommonWord(_ paragraph: String, _ banned: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String mostCommonWord(String paragraph, List<String> banned) {
    
  }
}
```

### Go

```golang
func mostCommonWord(paragraph string, banned []string) string {
    
}
```

### Ruby

```ruby
# @param {String} paragraph
# @param {String[]} banned
# @return {String}
def most_common_word(paragraph, banned)
    
end
```

### Scala

```scala
object Solution {
    def mostCommonWord(paragraph: String, banned: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_common_word(paragraph: String, banned: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (most-common-word paragraph banned)
  (-> string? (listof string?) string?)
  )
```

### Erlang

```erlang
-spec most_common_word(Paragraph :: unicode:unicode_binary(), Banned :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
most_common_word(Paragraph, Banned) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_common_word(paragraph :: String.t, banned :: [String.t]) :: String.t
  def most_common_word(paragraph, banned) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostCommonWord(paragraph: String, banned: Array<String>): String {

    }
}
```

