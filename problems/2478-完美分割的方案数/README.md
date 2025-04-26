# 2478. 完美分割的方案数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，每个字符是数字&nbsp;<code>'1'</code>&nbsp;到&nbsp;<code>'9'</code>&nbsp;，再给你两个整数&nbsp;<code>k</code> 和&nbsp;<code>minLength</code>&nbsp;。</p>

<p>如果对 <code>s</code>&nbsp;的分割满足以下条件，那么我们认为它是一个 <strong>完美</strong>&nbsp;分割：</p>

<ul>
	<li><code>s</code>&nbsp;被分成 <code>k</code>&nbsp;段互不相交的子字符串。</li>
	<li>每个子字符串长度都 <strong>至少</strong>&nbsp;为&nbsp;<code>minLength</code>&nbsp;。</li>
	<li>每个子字符串的第一个字符都是一个 <b>质数</b> 数字，最后一个字符都是一个 <strong>非质数</strong>&nbsp;数字。质数数字为&nbsp;<code>'2'</code>&nbsp;，<code>'3'</code>&nbsp;，<code>'5'</code>&nbsp;和&nbsp;<code>'7'</code>&nbsp;，剩下的都是非质数数字。</li>
</ul>

<p>请你返回 <code>s</code>&nbsp;的 <strong>完美</strong>&nbsp;分割数目。由于答案可能很大，请返回答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后的结果。</p>

<p>一个 <strong>子字符串</strong>&nbsp;是字符串中一段连续字符串序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "23542185131", k = 3, minLength = 2
<b>输出：</b>3
<b>解释：</b>存在 3 种完美分割方案：
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "23542185131", k = 3, minLength = 3
<b>输出：</b>1
<b>解释：</b>存在一种完美分割方案："2354 | 218 | 5131" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = "3312958", k = 3, minLength = 1
<b>输出：</b>1
<b>解释：</b>存在一种完美分割方案："331 | 29 | 58" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k, minLength &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code>&nbsp;每个字符都为数字&nbsp;<code>'1'</code>&nbsp;到&nbsp;<code>'9'</code> 之一。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Try using a greedy approach where you take as many digits as possible from the left of the string for each partition.
2. You can also use a dynamic programming approach, let an array dp where dp[i] is the solution of the problem for the prefix of the string ending at index i, the answer of the problem will be dp[n-1]. What are the transitions of this dp?

## 示例

```
"23542185131"
3
2
"23542185131"
3
3
"3312958"
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int beautifulPartitions(string s, int k, int minLength) {
        
    }
};
```

### Java

```java
class Solution {
    public int beautifulPartitions(String s, int k, int minLength) {
        
    }
}
```

### Python

```python
class Solution(object):
    def beautifulPartitions(self, s, k, minLength):
        """
        :type s: str
        :type k: int
        :type minLength: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        
```

### C

```c
int beautifulPartitions(char* s, int k, int minLength) {
    
}
```

### C#

```csharp
public class Solution {
    public int BeautifulPartitions(string s, int k, int minLength) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {number} minLength
 * @return {number}
 */
var beautifulPartitions = function(s, k, minLength) {
    
};
```

### TypeScript

```typescript
function beautifulPartitions(s: string, k: number, minLength: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @param Integer $minLength
     * @return Integer
     */
    function beautifulPartitions($s, $k, $minLength) {
        
    }
}
```

### Swift

```swift
class Solution {
    func beautifulPartitions(_ s: String, _ k: Int, _ minLength: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautifulPartitions(s: String, k: Int, minLength: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int beautifulPartitions(String s, int k, int minLength) {
    
  }
}
```

### Go

```golang
func beautifulPartitions(s string, k int, minLength int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @param {Integer} min_length
# @return {Integer}
def beautiful_partitions(s, k, min_length)
    
end
```

### Scala

```scala
object Solution {
    def beautifulPartitions(s: String, k: Int, minLength: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn beautiful_partitions(s: String, k: i32, min_length: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (beautiful-partitions s k minLength)
  (-> string? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec beautiful_partitions(S :: unicode:unicode_binary(), K :: integer(), MinLength :: integer()) -> integer().
beautiful_partitions(S, K, MinLength) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beautiful_partitions(s :: String.t, k :: integer, min_length :: integer) :: integer
  def beautiful_partitions(s, k, min_length) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func beautifulPartitions(s: String, k: Int64, minLength: Int64): Int64 {

    }
}
```

