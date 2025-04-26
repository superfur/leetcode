# 647. 回文子串

## 题目描述

<p>给你一个字符串 <code>s</code> ，请你统计并返回这个字符串中 <strong>回文子串</strong> 的数目。</p>

<p><strong>回文字符串</strong> 是正着读和倒过来读一样的字符串。</p>

<p><strong>子字符串</strong> 是字符串中的由连续字符组成的一个序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abc"
<strong>输出：</strong>3
<strong>解释：</strong>三个回文子串: "a", "b", "c"
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "aaa"
<strong>输出：</strong>6
<strong>解释：</strong>6个回文子串: "a", "a", "a", "aa", "aa", "aaa"</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串
- 动态规划

## 提示

1. How can we reuse a previously computed palindrome to compute a larger palindrome?
2. If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
3. Complexity based hint:</br>
If we use brute force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation?

## 示例

```
"abc"
"aaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSubstrings(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        
```

### C

```c
int countSubstrings(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSubstrings(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    
};
```

### TypeScript

```typescript
function countSubstrings(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countSubstrings($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubstrings(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubstrings(String s) {
    
  }
}
```

### Go

```golang
func countSubstrings(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_substrings(s)
    
end
```

### Scala

```scala
object Solution {
    def countSubstrings(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_substrings(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-substrings s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_substrings(S :: unicode:unicode_binary()) -> integer().
count_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t) :: integer
  def count_substrings(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubstrings(s: String): Int64 {

    }
}
```

