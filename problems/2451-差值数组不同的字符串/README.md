# 2451. 差值数组不同的字符串

## 题目描述

<p>给你一个字符串数组 <code>words</code>&nbsp;，每一个字符串长度都相同，令所有字符串的长度都为 <code>n</code>&nbsp;。</p>

<p>每个字符串&nbsp;<code>words[i]</code>&nbsp;可以被转化为一个长度为&nbsp;<code>n - 1</code>&nbsp;的&nbsp;<strong>差值整数数组</strong>&nbsp;<code>difference[i]</code>&nbsp;，其中对于&nbsp;<code>0 &lt;= j &lt;= n - 2</code>&nbsp;有&nbsp;<code>difference[i][j] = words[i][j+1] - words[i][j]</code>&nbsp;。注意两个字母的差值定义为它们在字母表中&nbsp;<strong>位置</strong>&nbsp;之差，也就是说&nbsp;<code>'a'</code>&nbsp;的位置是&nbsp;<code>0</code>&nbsp;，<code>'b'</code>&nbsp;的位置是&nbsp;<code>1</code>&nbsp;，<code>'z'</code>&nbsp;的位置是&nbsp;<code>25</code>&nbsp;。</p>

<ul>
	<li>比方说，字符串&nbsp;<code>"acb"</code>&nbsp;的差值整数数组是&nbsp;<code>[2 - 0, 1 - 2] = [2, -1]</code>&nbsp;。</li>
</ul>

<p><code>words</code>&nbsp;中所有字符串 <strong>除了一个字符串以外</strong>&nbsp;，其他字符串的差值整数数组都相同。你需要找到那个不同的字符串。</p>

<p>请你返回<em>&nbsp;</em><code>words</code>中&nbsp;<strong>差值整数数组</strong>&nbsp;不同的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>words = ["adc","wzy","abc"]
<b>输出：</b>"abc"
<b>解释：</b>
- "adc" 的差值整数数组是 [3 - 0, 2 - 3] = [3, -1] 。
- "wzy" 的差值整数数组是 [25 - 22, 24 - 25]= [3, -1] 。
- "abc" 的差值整数数组是 [1 - 0, 2 - 1] = [1, 1] 。
不同的数组是 [1, 1]，所以返回对应的字符串，"abc"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>words = ["aaa","bob","ccc","ddd"]
<b>输出：</b>"bob"
<b>解释：</b>除了 "bob" 的差值整数数组是 [13, -13] 以外，其他字符串的差值整数数组都是 [0, 0] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= words.length &lt;= 100</code></li>
	<li><code>n == words[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 20</code></li>
	<li><code>words[i]</code>&nbsp;只含有小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Find the difference integer array for each string.
2. Compare them to find the odd one out.

## 示例

```
["adc","wzy","abc"]
["aaa","bob","ccc","ddd"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string oddString(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public String oddString(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def oddString(self, words: List[str]) -> str:
        
```

### C

```c
char* oddString(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string OddString(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var oddString = function(words) {
    
};
```

### TypeScript

```typescript
function oddString(words: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function oddString($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func oddString(_ words: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun oddString(words: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String oddString(List<String> words) {
    
  }
}
```

### Go

```golang
func oddString(words []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String}
def odd_string(words)
    
end
```

### Scala

```scala
object Solution {
    def oddString(words: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn odd_string(words: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (odd-string words)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec odd_string(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
odd_string(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec odd_string(words :: [String.t]) :: String.t
  def odd_string(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func oddString(words: Array<String>): String {

    }
}
```

