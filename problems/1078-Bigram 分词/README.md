# 1078. Bigram 分词

## 题目描述

<p>给出第一个词&nbsp;<code>first</code> 和第二个词&nbsp;<code>second</code>，考虑在某些文本&nbsp;<code>text</code>&nbsp;中可能以 <code>"first second third"</code> 形式出现的情况，其中&nbsp;<code>second</code>&nbsp;紧随&nbsp;<code>first</code>&nbsp;出现，<code>third</code>&nbsp;紧随&nbsp;<code>second</code>&nbsp;出现。</p>

<p>对于每种这样的情况，将第三个词 "<code>third</code>" 添加到答案中，并返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>text = "alice is a good girl she is a good student", first = "a", second = "good"
<strong>输出：</strong>["girl","student"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>text = "we will we will rock you", first = "we", second = "will"
<strong>输出：</strong>["we","rock"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 1000</code></li>
	<li><code>text</code>&nbsp;由小写英文字母和空格组成</li>
	<li><code>text</code> 中的所有单词之间都由 <strong>单个空格字符</strong> 分隔</li>
	<li><code>1 &lt;= first.length, second.length &lt;= 10</code></li>
	<li><code>first</code> 和&nbsp;<code>second</code>&nbsp;由小写英文字母组成</li>
	<li><code>text</code>&nbsp;不包含任何前缀或尾随空格。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Split the string into words, then look at adjacent triples of words.

## 示例

```
"alice is a good girl she is a good student"
"a"
"good"
"we will we will rock you"
"we"
"will"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findOcurrences(char* text, char* first, char* second, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] FindOcurrences(string text, string first, string second) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @param {string} first
 * @param {string} second
 * @return {string[]}
 */
var findOcurrences = function(text, first, second) {
    
};
```

### TypeScript

```typescript
function findOcurrences(text: string, first: string, second: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @param String $first
     * @param String $second
     * @return String[]
     */
    function findOcurrences($text, $first, $second) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findOcurrences(_ text: String, _ first: String, _ second: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findOcurrences(text: String, first: String, second: String): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findOcurrences(String text, String first, String second) {
    
  }
}
```

### Go

```golang
func findOcurrences(text string, first string, second string) []string {
    
}
```

### Ruby

```ruby
# @param {String} text
# @param {String} first
# @param {String} second
# @return {String[]}
def find_ocurrences(text, first, second)
    
end
```

### Scala

```scala
object Solution {
    def findOcurrences(text: String, first: String, second: String): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_ocurrences(text: String, first: String, second: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-ocurrences text first second)
  (-> string? string? string? (listof string?))
  )
```

### Erlang

```erlang
-spec find_ocurrences(Text :: unicode:unicode_binary(), First :: unicode:unicode_binary(), Second :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
find_ocurrences(Text, First, Second) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_ocurrences(text :: String.t, first :: String.t, second :: String.t) :: [String.t]
  def find_ocurrences(text, first, second) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findOcurrences(text: String, first: String, second: String): Array<String> {

    }
}
```

