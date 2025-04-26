# 1750. 删除字符串两端相同字符后的最短长度

## 题目描述

<p>给你一个只包含字符 <code>'a'</code>，<code>'b'</code> 和 <code>'c'</code> 的字符串 <code>s</code> ，你可以执行下面这个操作（5 个步骤）任意次：</p>

<ol>
	<li>选择字符串 <code>s</code> 一个 <strong>非空</strong> 的前缀，这个前缀的所有字符都相同。</li>
	<li>选择字符串 <code>s</code> 一个 <strong>非空</strong> 的后缀，这个后缀的所有字符都相同。</li>
	<li>前缀和后缀在字符串中任意位置都不能有交集。</li>
	<li>前缀和后缀包含的所有字符都要相同。</li>
	<li>同时删除前缀和后缀。</li>
</ol>

<p>请你返回对字符串 <code>s</code> 执行上面操作任意次以后（可能 0 次），能得到的 <strong>最短长度</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "ca"
<b>输出：</b>2
<strong>解释：</strong>你没法删除任何一个字符，所以字符串长度仍然保持不变。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "cabaabac"
<b>输出：</b>0
<b>解释：</b>最优操作序列为：
- 选择前缀 "c" 和后缀 "c" 并删除它们，得到 s = "abaaba" 。
- 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "baab" 。
- 选择前缀 "b" 和后缀 "b" 并删除它们，得到 s = "aa" 。
- 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "" 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = "aabccabba"
<b>输出：</b>3
<b>解释：</b>最优操作序列为：
- 选择前缀 "aa" 和后缀 "a" 并删除它们，得到 s = "bccabb" 。
- 选择前缀 "b" 和后缀 "bb" 并删除它们，得到 s = "cca" 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 只包含字符 <code>'a'</code>，<code>'b'</code> 和 <code>'c'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 提示

1. If both ends have distinct characters, no more operations can be made. Otherwise, the only operation is to remove all of the same characters from both ends. We will do this as many times as we can.
2. Note that if the length is equal 1 the answer is 1

## 示例

```
"ca"
"cabaabac"
"aabccabba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumLength(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumLength(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumLength(self, s: str) -> int:
        
```

### C

```c
int minimumLength(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumLength(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    
};
```

### TypeScript

```typescript
function minimumLength(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumLength($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumLength(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumLength(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumLength(String s) {
    
  }
}
```

### Go

```golang
func minimumLength(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_length(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumLength(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-length s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_length(S :: unicode:unicode_binary()) -> integer().
minimum_length(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_length(s :: String.t) :: integer
  def minimum_length(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumLength(s: String): Int64 {

    }
}
```

