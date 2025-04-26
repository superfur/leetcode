# 2108. 找出数组中的第一个回文字符串

## 题目描述

<p>给你一个字符串数组 <code>words</code> ，找出并返回数组中的 <strong>第一个回文字符串</strong> 。如果不存在满足要求的字符串，返回一个 <strong>空字符串</strong><em> </em><code>""</code> 。</p>

<p><strong>回文字符串</strong> 的定义为：如果一个字符串正着读和反着读一样，那么该字符串就是一个 <strong>回文字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = ["abc","car","ada","racecar","cool"]
<strong>输出：</strong>"ada"
<strong>解释：</strong>第一个回文字符串是 "ada" 。
注意，"racecar" 也是回文字符串，但它不是第一个。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = ["notapalindrome","racecar"]
<strong>输出：</strong>"racecar"
<strong>解释：</strong>第一个也是唯一一个回文字符串是 "racecar" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>words = ["def","ghi"]
<strong>输出：</strong>""
<strong>解释：</strong>不存在回文字符串，所以返回一个空字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针
- 字符串

## 提示

1. Iterate through the elements in order. As soon as the current element is a palindrome, return it.
2. To check if an element is a palindrome, can you reverse the string?

## 示例

```
["abc","car","ada","racecar","cool"]
["notapalindrome","racecar"]
["def","ghi"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public String firstPalindrome(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
```

### C

```c
char* firstPalindrome(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string FirstPalindrome(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    
};
```

### TypeScript

```typescript
function firstPalindrome(words: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function firstPalindrome($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func firstPalindrome(_ words: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun firstPalindrome(words: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String firstPalindrome(List<String> words) {
    
  }
}
```

### Go

```golang
func firstPalindrome(words []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String}
def first_palindrome(words)
    
end
```

### Scala

```scala
object Solution {
    def firstPalindrome(words: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (first-palindrome words)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec first_palindrome(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
first_palindrome(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec first_palindrome(words :: [String.t]) :: String.t
  def first_palindrome(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func firstPalindrome(words: Array<String>): String {

    }
}
```

