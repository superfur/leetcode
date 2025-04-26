# 696. 计数二进制子串

## 题目描述

<p>给定一个字符串&nbsp;<code>s</code>，统计并返回具有相同数量 <code>0</code> 和 <code>1</code> 的非空（连续）子字符串的数量，并且这些子字符串中的所有 <code>0</code> 和所有 <code>1</code> 都是成组连续的。</p>

<p>重复出现（不同位置）的子串也要统计它们出现的次数。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "00110011"
<strong>输出：</strong>6
<strong>解释：</strong>6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "10101"
<strong>输出：</strong>4
<strong>解释：</strong>有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 提示

1. How many valid binary substrings exist in "000111", and how many in "11100"?  What about "00011100"?

## 示例

```
"00110011"
"10101"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countBinarySubstrings(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countBinarySubstrings(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
```

### C

```c
int countBinarySubstrings(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountBinarySubstrings(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countBinarySubstrings = function(s) {
    
};
```

### TypeScript

```typescript
function countBinarySubstrings(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countBinarySubstrings($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countBinarySubstrings(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countBinarySubstrings(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countBinarySubstrings(String s) {
    
  }
}
```

### Go

```golang
func countBinarySubstrings(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_binary_substrings(s)
    
end
```

### Scala

```scala
object Solution {
    def countBinarySubstrings(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-binary-substrings s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_binary_substrings(S :: unicode:unicode_binary()) -> integer().
count_binary_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_binary_substrings(s :: String.t) :: integer
  def count_binary_substrings(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countBinarySubstrings(s: String): Int64 {

    }
}
```

