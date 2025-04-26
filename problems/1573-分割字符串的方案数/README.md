# 1573. 分割字符串的方案数

## 题目描述

<p>给你一个二进制串&nbsp;<code>s</code>&nbsp; （一个只包含 0 和 1 的字符串），我们可以将 <code>s</code>&nbsp;分割成 3 个 <strong>非空</strong>&nbsp;字符串 s1, s2, s3 （s1 + s2 + s3 = s）。</p>

<p>请你返回分割&nbsp;<code>s</code>&nbsp;的方案数，满足 s1，s2 和 s3 中字符 &#39;1&#39; 的数目相同。</p>

<p>由于答案可能很大，请将它对 10^9 + 7 取余后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;10101&quot;
<strong>输出：</strong>4
<strong>解释：</strong>总共有 4 种方法将 s 分割成含有 &#39;1&#39; 数目相同的三个子字符串。
&quot;1|010|1&quot;
&quot;1|01|01&quot;
&quot;10|10|1&quot;
&quot;10|1|01&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;1001&quot;
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;0000&quot;
<strong>输出：</strong>3
<strong>解释：</strong>总共有 3 种分割 s 的方法。
&quot;0|0|00&quot;
&quot;0|00|0&quot;
&quot;00|0|0&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;100100010100110&quot;
<strong>输出：</strong>12
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s[i] == &#39;0&#39;</code>&nbsp;或者&nbsp;<code>s[i] == &#39;1&#39;</code></li>
	<li><code>3 &lt;= s.length &lt;= 10^5</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串

## 提示

1. There is no way if the sum (number of '1's) is not divisible by the number of splits. So sum%3 should be 0.
2. Preffix s1 , and suffix s3 should have sum/3 characters '1'.
3. Follow up: Can you generalize the problem with numbers between [-10^9, 10^9] such the sum between subarrays s1, s2, s3 are the same?

## 示例

```
"10101"
"1001"
"0000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numWays(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int numWays(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numWays(self, s: str) -> int:
        
```

### C

```c
int numWays(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumWays(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numWays = function(s) {
    
};
```

### TypeScript

```typescript
function numWays(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numWays($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numWays(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numWays(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numWays(String s) {
    
  }
}
```

### Go

```golang
func numWays(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def num_ways(s)
    
end
```

### Scala

```scala
object Solution {
    def numWays(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_ways(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-ways s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_ways(S :: unicode:unicode_binary()) -> integer().
num_ways(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_ways(s :: String.t) :: integer
  def num_ways(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numWays(s: String): Int64 {

    }
}
```

