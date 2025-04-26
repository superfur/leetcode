# 1624. 两个相同字符之间的最长子字符串

## 题目描述

<p>给你一个字符串 <code>s</code>，请你返回 <strong>两个相同字符之间的最长子字符串的长度</strong> <em>，</em>计算长度时不含这两个字符。如果不存在这样的子字符串，返回 <code>-1</code> 。</p>

<p><strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "aa"
<strong>输出：</strong>0
<strong>解释：</strong>最优的子字符串是两个 'a' 之间的空子字符串。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "abca"
<strong>输出：</strong>2
<strong>解释：</strong>最优的子字符串是 "bc" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = "cbzxy"
<strong>输出：</strong>-1
<strong>解释：</strong>s 中不存在出现出现两次的字符，所以返回 -1 。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = "cabbac"
<strong>输出：</strong>4
<strong>解释：</strong>最优的子字符串是 "abba" ，其他的非最优解包括 "bb" 和 "" 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>s</code> 只含小写英文字母</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. Try saving the first and last position of each character
2. Try finding every pair of indexes with equal characters

## 示例

```
"aa"
"abca"
"cbzxy"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
```

### C

```c
int maxLengthBetweenEqualCharacters(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxLengthBetweenEqualCharacters(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxLengthBetweenEqualCharacters = function(s) {
    
};
```

### TypeScript

```typescript
function maxLengthBetweenEqualCharacters(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxLengthBetweenEqualCharacters($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxLengthBetweenEqualCharacters(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxLengthBetweenEqualCharacters(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxLengthBetweenEqualCharacters(String s) {
    
  }
}
```

### Go

```golang
func maxLengthBetweenEqualCharacters(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_length_between_equal_characters(s)
    
end
```

### Scala

```scala
object Solution {
    def maxLengthBetweenEqualCharacters(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-length-between-equal-characters s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_length_between_equal_characters(S :: unicode:unicode_binary()) -> integer().
max_length_between_equal_characters(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_length_between_equal_characters(s :: String.t) :: integer
  def max_length_between_equal_characters(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxLengthBetweenEqualCharacters(s: String): Int64 {

    }
}
```

