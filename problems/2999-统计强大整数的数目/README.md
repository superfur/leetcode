# 2999. 统计强大整数的数目

## 题目描述

<p>给你三个整数&nbsp;<code>start</code>&nbsp;，<code>finish</code>&nbsp;和&nbsp;<code>limit</code>&nbsp;。同时给你一个下标从&nbsp;<strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;，表示一个 <strong>正</strong>&nbsp;整数。</p>

<p>如果一个 <strong>正</strong>&nbsp;整数&nbsp;<code>x</code> 末尾部分是&nbsp;<code>s</code>&nbsp;（换句话说，<code>s</code>&nbsp;是 <code>x</code>&nbsp;的 <strong>后缀</strong>），且 <code>x</code>&nbsp;中的每个数位至多是 <code>limit</code>&nbsp;，那么我们称 <code>x</code>&nbsp;是 <strong>强大的</strong>&nbsp;。</p>

<p>请你返回区间&nbsp;<code>[start..finish]</code>&nbsp;内强大整数的&nbsp;<strong>总数目</strong>&nbsp;。</p>

<p>如果一个字符串 <code>x</code>&nbsp;是 <code>y</code>&nbsp;中某个下标开始（<strong>包括</strong>&nbsp;<code>0</code>&nbsp;），到下标为&nbsp;<code>y.length - 1</code>&nbsp;结束的子字符串，那么我们称&nbsp;<code>x</code>&nbsp;是&nbsp;<code>y</code>&nbsp;的一个后缀。比方说，<code>25</code>&nbsp;是&nbsp;<code>5125</code>&nbsp;的一个后缀，但不是&nbsp;<code>512</code>&nbsp;的后缀。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>start = 1, finish = 6000, limit = 4, s = "124"
<b>输出：</b>5
<b>解释：</b>区间 [1..6000] 内的强大数字为 124 ，1124 ，2124 ，3124 和 4124 。这些整数的各个数位都 &lt;= 4 且 "124" 是它们的后缀。注意 5124 不是强大整数，因为第一个数位 5 大于 4 。
这个区间内总共只有这 5 个强大整数。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>start = 15, finish = 215, limit = 6, s = "10"
<b>输出：</b>2
<b>解释：</b>区间 [15..215] 内的强大整数为 110 和 210 。这些整数的各个数位都 &lt;= 6 且 "10" 是它们的后缀。
这个区间总共只有这 2 个强大整数。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>start = 1000, finish = 2000, limit = 4, s = "3000"
<b>输出：</b>0
<b>解释：</b>区间 [1000..2000] 内的整数都小于 3000 ，所以 "3000" 不可能是这个区间内任何整数的后缀。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= start &lt;= finish &lt;= 10<sup>15</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 9</code></li>
	<li><code>1 &lt;= s.length &lt;= floor(log<sub>10</sub>(finish)) + 1</code></li>
	<li><code>s</code>&nbsp;数位中每个数字都小于等于&nbsp;<code>limit</code>&nbsp;。</li>
	<li><code>s</code>&nbsp;不包含任何前导 0 。</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 动态规划

## 提示

1. We can use digit DP to count powerful integers in the range <code>[1, x]</code>.
2. Let <code>dp[i][j]</code> be the number of integers that have <code>i</code> digits (with allowed leading 0s) and <code>j</code> refers to the comparison between the current number and the prefix of <code>x</code>, <code>j == 0</code> if the i-digit number formed currently is identical to the leftmost <code>i</code> digits of <code>x</code>, else if <code>j ==1</code> it means the i-digit number is smaller than the leftmost <code>i</code> digits of <code>x</code>.
3. The answer is <code>count[finish] - count[start - 1]</code>, where <code>count[i]</code> refers to the number of powerful integers in the range <code>[1..i]</code>.

## 示例

```
1
6000
4
"124"
15
215
6
"10"
1000
2000
4
"3000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long numberOfPowerfulInt(long long start, long long finish, int limit, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long numberOfPowerfulInt(long start, long finish, int limit, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
```

### C

```c
long long numberOfPowerfulInt(long long start, long long finish, int limit, char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long NumberOfPowerfulInt(long start, long finish, int limit, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} start
 * @param {number} finish
 * @param {number} limit
 * @param {string} s
 * @return {number}
 */
var numberOfPowerfulInt = function(start, finish, limit, s) {
    
};
```

### TypeScript

```typescript
function numberOfPowerfulInt(start: number, finish: number, limit: number, s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $start
     * @param Integer $finish
     * @param Integer $limit
     * @param String $s
     * @return Integer
     */
    function numberOfPowerfulInt($start, $finish, $limit, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPowerfulInt(_ start: Int, _ finish: Int, _ limit: Int, _ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPowerfulInt(start: Long, finish: Long, limit: Int, s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPowerfulInt(int start, int finish, int limit, String s) {
    
  }
}
```

### Go

```golang
func numberOfPowerfulInt(start int64, finish int64, limit int, s string) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} start
# @param {Integer} finish
# @param {Integer} limit
# @param {String} s
# @return {Integer}
def number_of_powerful_int(start, finish, limit, s)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPowerfulInt(start: Long, finish: Long, limit: Int, s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_powerful_int(start: i64, finish: i64, limit: i32, s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-powerful-int start finish limit s)
  (-> exact-integer? exact-integer? exact-integer? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_powerful_int(Start :: integer(), Finish :: integer(), Limit :: integer(), S :: unicode:unicode_binary()) -> integer().
number_of_powerful_int(Start, Finish, Limit, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_powerful_int(start :: integer, finish :: integer, limit :: integer, s :: String.t) :: integer
  def number_of_powerful_int(start, finish, limit, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPowerfulInt(start: Int64, finish: Int64, limit: Int64, s: String): Int64 {

    }
}
```

