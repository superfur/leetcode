# 926. 将字符串翻转到单调递增

## 题目描述

<p>如果一个二进制字符串，是以一些 <code>0</code>（可能没有 <code>0</code>）后面跟着一些 <code>1</code>（也可能没有 <code>1</code>）的形式组成的，那么该字符串是 <strong>单调递增 </strong>的。</p>

<p>给你一个二进制字符串 <code>s</code>，你可以将任何 <code>0</code> 翻转为 <code>1</code> 或者将 <code>1</code> 翻转为 <code>0</code> 。</p>

<p>返回使 <code>s</code> 单调递增的最小翻转次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "00110"
<strong>输出：</strong>1
<strong>解释：</strong>翻转最后一位得到 00111.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "010110"
<strong>输出：</strong>2
<strong>解释：</strong>翻转得到 011111，或者是 000111。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "00011000"
<strong>输出：</strong>2
<strong>解释：</strong>翻转得到 00000000。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 示例

```
"00110"
"010110"
"00011000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFlipsMonoIncr(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
```

### C

```c
int minFlipsMonoIncr(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFlipsMonoIncr(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function(s) {
    
};
```

### TypeScript

```typescript
function minFlipsMonoIncr(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minFlipsMonoIncr($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFlipsMonoIncr(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFlipsMonoIncr(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFlipsMonoIncr(String s) {
    
  }
}
```

### Go

```golang
func minFlipsMonoIncr(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_flips_mono_incr(s)
    
end
```

### Scala

```scala
object Solution {
    def minFlipsMonoIncr(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-flips-mono-incr s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_flips_mono_incr(S :: unicode:unicode_binary()) -> integer().
min_flips_mono_incr(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_flips_mono_incr(s :: String.t) :: integer
  def min_flips_mono_incr(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFlipsMonoIncr(s: String): Int64 {

    }
}
```

