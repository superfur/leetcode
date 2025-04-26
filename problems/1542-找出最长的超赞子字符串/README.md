# 1542. 找出最长的超赞子字符串

## 题目描述

<p>给你一个字符串 <code>s</code> 。请返回 <code>s</code> 中最长的 <strong>超赞子字符串</strong> 的长度。</p>

<p>「超赞子字符串」需满足满足下述两个条件：</p>

<ul>
	<li>该字符串是 <code>s</code> 的一个非空子字符串</li>
	<li>进行任意次数的字符交换后，该字符串可以变成一个回文字符串</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;3242415&quot;
<strong>输出：</strong>5
<strong>解释：</strong>&quot;24241&quot; 是最长的超赞子字符串，交换其中的字符后，可以得到回文 &quot;24142&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;12345678&quot;
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;213123&quot;
<strong>输出：</strong>6
<strong>解释：</strong>&quot;213123&quot; 是最长的超赞子字符串，交换其中的字符后，可以得到回文 &quot;231132&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;00&quot;
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s</code> 仅由数字组成</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 哈希表
- 字符串

## 提示

1. Given the character counts, under what conditions can a palindrome be formed ?
2. From left to right, use bitwise xor-operation to compute for any prefix the number of times modulo 2 of each digit.  (mask ^= (1<<(s[i]-'0')).
3. Expected complexity is O(n*A) where A is the alphabet (10).

## 示例

```
"3242415"
"12345678"
"213123"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestAwesome(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestAwesome(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestAwesome(self, s: str) -> int:
        
```

### C

```c
int longestAwesome(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestAwesome(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestAwesome = function(s) {
    
};
```

### TypeScript

```typescript
function longestAwesome(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestAwesome($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestAwesome(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestAwesome(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestAwesome(String s) {
    
  }
}
```

### Go

```golang
func longestAwesome(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def longest_awesome(s)
    
end
```

### Scala

```scala
object Solution {
    def longestAwesome(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_awesome(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-awesome s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_awesome(S :: unicode:unicode_binary()) -> integer().
longest_awesome(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_awesome(s :: String.t) :: integer
  def longest_awesome(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestAwesome(s: String): Int64 {

    }
}
```

