# 1876. 长度为三且各字符不同的子字符串

## 题目描述

<p>如果一个字符串不含有任何重复字符，我们称这个字符串为 <strong>好</strong> 字符串。</p>

<p>给你一个字符串 <code>s</code> ，请你返回 <code>s</code> 中长度为 <strong>3</strong> 的 <strong>好子字符串</strong> 的数量。</p>

<p>注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。</p>

<p><strong>子字符串</strong> 是一个字符串中连续的字符序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "xyzzaz"
<b>输出：</b>1
<b>解释：</b>总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
唯一的长度为 3 的好子字符串是 "xyz" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "aababcabc"
<b>输出：</b>4
<b>解释：</b>总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 100</code></li>
	<li><code>s</code>​​​​​​ 只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数
- 滑动窗口

## 提示

1. Try using a set to find out the number of distinct characters in a substring.

## 示例

```
"xyzzaz"
"aababcabc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countGoodSubstrings(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countGoodSubstrings(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
```

### C

```c
int countGoodSubstrings(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountGoodSubstrings(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function(s) {
    
};
```

### TypeScript

```typescript
function countGoodSubstrings(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countGoodSubstrings($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGoodSubstrings(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGoodSubstrings(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGoodSubstrings(String s) {
    
  }
}
```

### Go

```golang
func countGoodSubstrings(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_good_substrings(s)
    
end
```

### Scala

```scala
object Solution {
    def countGoodSubstrings(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good_substrings(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good-substrings s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good_substrings(S :: unicode:unicode_binary()) -> integer().
count_good_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good_substrings(s :: String.t) :: integer
  def count_good_substrings(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGoodSubstrings(s: String): Int64 {

    }
}
```

