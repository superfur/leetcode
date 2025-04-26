# 2586. 统计范围内的元音字符串数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> 和两个整数：<code>left</code> 和 <code>right</code> 。</p>

<p>如果字符串以元音字母开头并以元音字母结尾，那么该字符串就是一个 <strong>元音字符串</strong> ，其中元音字母是 <code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code>、<code>'u'</code> 。</p>

<p>返回<em> </em><code>words[i]</code> 是元音字符串的数目，其中<em> </em><code>i</code> 在闭区间 <code>[left, right]</code> 内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["are","amy","u"], left = 0, right = 2
<strong>输出：</strong>2
<strong>解释：</strong>
- "are" 是一个元音字符串，因为它以 'a' 开头并以 'e' 结尾。
- "amy" 不是元音字符串，因为它没有以元音字母结尾。
- "u" 是一个元音字符串，因为它以 'u' 开头并以 'u' 结尾。
在上述范围中的元音字符串数目为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
<strong>输出：</strong>3
<strong>解释：</strong>
- "aeo" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
- "mu" 不是元音字符串，因为它没有以元音字母开头。
- "ooo" 是一个元音字符串，因为它以 'o' 开头并以 'o' 结尾。
- "artro" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
在上述范围中的元音字符串数目为 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
	<li><code>0 &lt;= left &lt;= right &lt; words.length</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串
- 计数

## 提示

1. consider iterating over all strings from left to right and use an if condition to check if the first character and last character are vowels.

## 示例

```
["are","amy","u"]
0
2
["hey","aeo","mu","ooo","artro"]
1
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int vowelStrings(vector<string>& words, int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
```

### C

```c
int vowelStrings(char** words, int wordsSize, int left, int right) {
    
}
```

### C#

```csharp
public class Solution {
    public int VowelStrings(string[] words, int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var vowelStrings = function(words, left, right) {
    
};
```

### TypeScript

```typescript
function vowelStrings(words: string[], left: number, right: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function vowelStrings($words, $left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func vowelStrings(_ words: [String], _ left: Int, _ right: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun vowelStrings(words: Array<String>, left: Int, right: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int vowelStrings(List<String> words, int left, int right) {
    
  }
}
```

### Go

```golang
func vowelStrings(words []string, left int, right int) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def vowel_strings(words, left, right)
    
end
```

### Scala

```scala
object Solution {
    def vowelStrings(words: Array[String], left: Int, right: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn vowel_strings(words: Vec<String>, left: i32, right: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (vowel-strings words left right)
  (-> (listof string?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec vowel_strings(Words :: [unicode:unicode_binary()], Left :: integer(), Right :: integer()) -> integer().
vowel_strings(Words, Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec vowel_strings(words :: [String.t], left :: integer, right :: integer) :: integer
  def vowel_strings(words, left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func vowelStrings(words: Array<String>, left: Int64, right: Int64): Int64 {

    }
}
```

