# 1805. 字符串中不同整数的数目

## 题目描述

<p>给你一个字符串 <code>word</code> ，该字符串由数字和小写英文字母组成。</p>

<p>请你用空格替换每个不是数字的字符。例如，<code>"a123bc34d8ef34"</code> 将会变成 <code>" 123  34 8  34"</code> 。注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）：<code>"123"</code>、<code>"34"</code>、<code>"8"</code> 和 <code>"34"</code> 。</p>

<p>返回对 <code>word</code> 完成替换后形成的 <strong>不同</strong> 整数的数目。</p>

<p>只有当两个整数的 <strong>不含前导零</strong> 的十进制表示不同， 才认为这两个整数也不同。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "a<strong>123</strong>bc<strong>34</strong>d<strong>8</strong>ef<strong>34</strong>"
<strong>输出：</strong>3
<strong>解释：</strong>不同的整数有 "123"、"34" 和 "8" 。注意，"34" 只计数一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "leet<strong>1234</strong>code<strong>234</strong>"
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word = "a<strong>1</strong>b<strong>01</strong>c<strong>001</strong>"
<strong>输出：</strong>1
<strong>解释：</strong>"1"、"01" 和 "001" 视为同一个整数的十进制表示，因为在比较十进制值时会忽略前导零的存在。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= word.length <= 1000</code></li>
	<li><code>word</code> 由数字和小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. Try to split the string so that each integer is in a different string.
2. Try to remove each integer's leading zeroes and compare the strings to find how many of them are unique.

## 示例

```
"a123bc34d8ef34"
"leet1234code234"
"a1b01c001"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numDifferentIntegers(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int numDifferentIntegers(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
```

### C

```c
int numDifferentIntegers(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumDifferentIntegers(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var numDifferentIntegers = function(word) {
    
};
```

### TypeScript

```typescript
function numDifferentIntegers(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function numDifferentIntegers($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numDifferentIntegers(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numDifferentIntegers(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numDifferentIntegers(String word) {
    
  }
}
```

### Go

```golang
func numDifferentIntegers(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def num_different_integers(word)
    
end
```

### Scala

```scala
object Solution {
    def numDifferentIntegers(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_different_integers(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-different-integers word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_different_integers(Word :: unicode:unicode_binary()) -> integer().
num_different_integers(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_different_integers(word :: String.t) :: integer
  def num_different_integers(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numDifferentIntegers(word: String): Int64 {

    }
}
```

