# 884. 两句话中的不常见单词

## 题目描述

<p><strong>句子</strong> 是一串由空格分隔的单词。每个 <strong>单词</strong><em> </em>仅由小写字母组成。</p>

<p>如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 <strong>没有出现</strong> ，那么这个单词就是 <strong>不常见的</strong><em> </em>。</p>

<p>给你两个 <strong>句子</strong> <code>s1</code> 和 <code>s2</code> ，返回所有 <strong>不常用单词</strong> 的列表。返回列表中单词可以按 <strong>任意顺序</strong> 组织。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "this apple is sweet", s2 = "this apple is sour"
<strong>输出：</strong>["sweet","sour"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "apple apple", s2 = "banana"
<strong>输出：</strong>["banana"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 200</code></li>
	<li><code>s1</code> 和 <code>s2</code> 由小写英文字母和空格组成</li>
	<li><code>s1</code> 和 <code>s2</code> 都不含前导或尾随空格</li>
	<li><code>s1</code> 和 <code>s2</code> 中的所有单词间均由单个空格分隔</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 示例

```
"this apple is sweet"
"this apple is sour"
"apple apple"
"banana"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** uncommonFromSentences(char* s1, char* s2, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] UncommonFromSentences(string s1, string s2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function uncommonFromSentences(s1: string, s2: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return String[]
     */
    function uncommonFromSentences($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func uncommonFromSentences(_ s1: String, _ s2: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uncommonFromSentences(s1: String, s2: String): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> uncommonFromSentences(String s1, String s2) {
    
  }
}
```

### Go

```golang
func uncommonFromSentences(s1 string, s2 string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {String[]}
def uncommon_from_sentences(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def uncommonFromSentences(s1: String, s2: String): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (uncommon-from-sentences s1 s2)
  (-> string? string? (listof string?))
  )
```

### Erlang

```erlang
-spec uncommon_from_sentences(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
uncommon_from_sentences(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec uncommon_from_sentences(s1 :: String.t, s2 :: String.t) :: [String.t]
  def uncommon_from_sentences(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func uncommonFromSentences(s1: String, s2: String): Array<String> {

    }
}
```

