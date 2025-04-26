# 524. 通过删除字母匹配到字典里最长单词

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符串数组 <code>dictionary</code> ，找出并返回&nbsp;<code>dictionary</code> 中最长的字符串，该字符串可以通过删除 <code>s</code> 中的某些字符得到。</p>

<p>如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
<strong>输出：</strong>"apple"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abpcplea", dictionary = ["a","b","c"]
<strong>输出：</strong>"a"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 1000</code></li>
	<li><code>s</code> 和 <code>dictionary[i]</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 字符串
- 排序

## 示例

```
"abpcplea"
["ale","apple","monkey","plea"]
"abpcplea"
["a","b","c"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        
    }
};
```

### Java

```java
class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
```

### C

```c
char* findLongestWord(char* s, char** dictionary, int dictionarySize) {
    
}
```

### C#

```csharp
public class Solution {
    public string FindLongestWord(string s, IList<string> dictionary) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {string}
 */
var findLongestWord = function(s, dictionary) {
    
};
```

### TypeScript

```typescript
function findLongestWord(s: string, dictionary: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $dictionary
     * @return String
     */
    function findLongestWord($s, $dictionary) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLongestWord(_ s: String, _ dictionary: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLongestWord(s: String, dictionary: List<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String findLongestWord(String s, List<String> dictionary) {
    
  }
}
```

### Go

```golang
func findLongestWord(s string, dictionary []string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String[]} dictionary
# @return {String}
def find_longest_word(s, dictionary)
    
end
```

### Scala

```scala
object Solution {
    def findLongestWord(s: String, dictionary: List[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_longest_word(s: String, dictionary: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (find-longest-word s dictionary)
  (-> string? (listof string?) string?)
  )
```

### Erlang

```erlang
-spec find_longest_word(S :: unicode:unicode_binary(), Dictionary :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
find_longest_word(S, Dictionary) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_longest_word(s :: String.t, dictionary :: [String.t]) :: String.t
  def find_longest_word(s, dictionary) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLongestWord(s: String, dictionary: ArrayList<String>): String {

    }
}
```

