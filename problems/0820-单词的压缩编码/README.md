# 820. 单词的压缩编码

## 题目描述

<p>单词数组 <code>words</code> 的 <strong>有效编码</strong> 由任意助记字符串 <code>s</code> 和下标数组 <code>indices</code> 组成，且满足：</p>

<ul>
	<li><code>words.length == indices.length</code></li>
	<li>助记字符串 <code>s</code> 以 <code>'#'</code> 字符结尾</li>
	<li>对于每个下标 <code>indices[i]</code> ，<code>s</code> 的一个从 <code>indices[i]</code> 开始、到下一个 <code>'#'</code> 字符结束（但不包括 <code>'#'</code>）的 <strong>子字符串</strong> 恰好与 <code>words[i]</code> 相等</li>
</ul>

<p>给你一个单词数组 <code>words</code> ，返回成功对 <code>words</code> 进行编码的最小助记字符串 <code>s</code> 的长度 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["time", "me", "bell"]
<strong>输出：</strong>10
<strong>解释：</strong>一组有效编码为 s = <code>"time#bell#" 和 indices = [0, 2, 5</code>] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "<strong>time</strong>#bell#"
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "ti<strong>me</strong>#bell#"
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#<strong>bell</strong>#"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["t"]
<strong>输出：</strong>2
<strong>解释：</strong>一组有效编码为 s = "t#" 和 indices = [0] 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= words.length <= 2000</code></li>
	<li><code>1 <= words[i].length <= 7</code></li>
	<li><code>words[i]</code> 仅由小写字母组成</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串

## 示例

```
["time","me","bell"]
["t"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumLengthEncoding(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
```

### C

```c
int minimumLengthEncoding(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumLengthEncoding(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding = function(words) {
    
};
```

### TypeScript

```typescript
function minimumLengthEncoding(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function minimumLengthEncoding($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumLengthEncoding(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumLengthEncoding(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumLengthEncoding(List<String> words) {
    
  }
}
```

### Go

```golang
func minimumLengthEncoding(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def minimum_length_encoding(words)
    
end
```

### Scala

```scala
object Solution {
    def minimumLengthEncoding(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-length-encoding words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_length_encoding(Words :: [unicode:unicode_binary()]) -> integer().
minimum_length_encoding(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_length_encoding(words :: [String.t]) :: integer
  def minimum_length_encoding(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumLengthEncoding(words: Array<String>): Int64 {

    }
}
```

