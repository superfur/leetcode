# 1416. 恢复数组

## 题目描述

<p>某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 <code>[1, k]</code>&nbsp;之间，且数组中的数字都没有前导 0 。</p>

<p>给你字符串&nbsp;<code>s</code>&nbsp;和整数&nbsp;<code>k</code>&nbsp;。可能会有多种不同的数组恢复结果。</p>

<p>按照上述程序，请你返回所有可能输出字符串&nbsp;<code>s</code>&nbsp;的数组方案数。</p>

<p>由于数组方案数可能会很大，请你返回它对&nbsp;<code>10^9 + 7</code>&nbsp;<strong>取余</strong>&nbsp;后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;1000&quot;, k = 10000
<strong>输出：</strong>1
<strong>解释：</strong>唯一一种可能的数组方案是 [1000]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;1000&quot;, k = 10
<strong>输出：</strong>0
<strong>解释：</strong>不存在任何数组方案满足所有整数都 &gt;= 1 且 &lt;= 10 同时输出结果为 s 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;1317&quot;, k = 2000
<strong>输出：</strong>8
<strong>解释：</strong>可行的数组方案为 [1317]，[131,7]，[13,17]，[1,317]，[13,1,7]，[1,31,7]，[1,3,17]，[1,3,1,7]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;2020&quot;, k = 30
<strong>输出：</strong>1
<strong>解释：</strong>唯一可能的数组方案是 [20,20] 。 [2020] 不是可行的数组方案，原因是 2020 &gt; 30 。 [2,020] 也不是可行的数组方案，因为 020 含有前导 0 。
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>s = &quot;1234567890&quot;, k = 90
<strong>输出：</strong>34
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code>.</li>
	<li><code>s</code>&nbsp;只包含数字且不包含前导 0 。</li>
	<li><code>1 &lt;= k &lt;= 10^9</code>.</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Use dynamic programming. Build an array dp where dp[i] is the number of ways you can divide the string starting from index i to the end.
2. Keep in mind that the answer is modulo 10^9 + 7 and take the mod for each operation.

## 示例

```
"1000"
10000
"1000"
10
"1317"
2000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfArrays(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfArrays(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
```

### C

```c
int numberOfArrays(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfArrays(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var numberOfArrays = function(s, k) {
    
};
```

### TypeScript

```typescript
function numberOfArrays(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function numberOfArrays($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfArrays(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfArrays(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfArrays(String s, int k) {
    
  }
}
```

### Go

```golang
func numberOfArrays(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def number_of_arrays(s, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfArrays(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-arrays s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_arrays(S :: unicode:unicode_binary(), K :: integer()) -> integer().
number_of_arrays(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_arrays(s :: String.t, k :: integer) :: integer
  def number_of_arrays(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfArrays(s: String, k: Int64): Int64 {

    }
}
```

