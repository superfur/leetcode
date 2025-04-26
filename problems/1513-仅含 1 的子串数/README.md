# 1513. 仅含 1 的子串数

## 题目描述

<p>给你一个二进制字符串 <code>s</code>（仅由 &#39;0&#39; 和 &#39;1&#39; 组成的字符串）。</p>

<p>返回所有字符都为 1 的子字符串的数目。</p>

<p>由于答案可能很大，请你将它对 10^9 + 7 取模后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;0110111&quot;
<strong>输出</strong>：9
<strong>解释：</strong>共有 9 个子字符串仅由 &#39;1&#39; 组成
&quot;1&quot; -&gt; 5 次
&quot;11&quot; -&gt; 3 次
&quot;111&quot; -&gt; 1 次</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;101&quot;
<strong>输出：</strong>2
<strong>解释：</strong>子字符串 &quot;1&quot; 在 s 中共出现 2 次
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;111111&quot;
<strong>输出：</strong>21
<strong>解释：</strong>每个子字符串都仅由 &#39;1&#39; 组成
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;000&quot;
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s[i] == &#39;0&#39;</code> 或 <code>s[i] == &#39;1&#39;</code></li>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串

## 提示

1. Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.

## 示例

```
"0110111"
"101"
"111111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSub(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSub(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSub(self, s: str) -> int:
        
```

### C

```c
int numSub(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSub(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    
};
```

### TypeScript

```typescript
function numSub(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numSub($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSub(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSub(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSub(String s) {
    
  }
}
```

### Go

```golang
func numSub(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def num_sub(s)
    
end
```

### Scala

```scala
object Solution {
    def numSub(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-sub s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_sub(S :: unicode:unicode_binary()) -> integer().
num_sub(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_sub(s :: String.t) :: integer
  def num_sub(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSub(s: String): Int64 {

    }
}
```

