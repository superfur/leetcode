# 3090. 每个字符最多出现两次的最长子字符串

## 题目描述

<p>给你一个字符串 <code>s</code> ，请找出满足每个字符最多出现两次的最长子字符串，并返回该<span data-keyword="substring">子字符串</span>的<strong> 最大 </strong>长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "bcbbbcba"</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>以下子字符串长度为 4，并且每个字符最多出现两次：<code>"bcbb<u>bcba</u>"</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aaaa"</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>以下子字符串长度为 2，并且每个字符最多出现两次：<code>"<u>aa</u>aa"</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul><!-- 字符串 s 的长度在 2 到 100 之间 -->
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<!-- 字符串 s 仅包含小写英文字母 -->
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. We can try all substrings by brute-force since the constraints are very small.

## 示例

```
"bcbbbcba"
"aaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumLengthSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumLengthSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
```

### C

```c
int maximumLengthSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumLengthSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function maximumLengthSubstring(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maximumLengthSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumLengthSubstring(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumLengthSubstring(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumLengthSubstring(String s) {
    
  }
}
```

### Go

```golang
func maximumLengthSubstring(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def maximum_length_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def maximumLengthSubstring(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_length_substring(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-length-substring s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_length_substring(S :: unicode:unicode_binary()) -> integer().
maximum_length_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_length_substring(s :: String.t) :: integer
  def maximum_length_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumLengthSubstring(s: String): Int64 {

    }
}
```

