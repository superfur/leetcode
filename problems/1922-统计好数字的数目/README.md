# 1922. 统计好数字的数目

## 题目描述

<p>我们称一个数字字符串是 <strong>好数字</strong> 当它满足（下标从 <strong>0</strong> 开始）<strong>偶数</strong> 下标处的数字为 <strong>偶数</strong> 且 <strong>奇数</strong> 下标处的数字为 <strong>质数</strong> （<code>2</code>，<code>3</code>，<code>5</code> 或 <code>7</code>）。</p>

<ul>
	<li>比方说，<code>"2582"</code> 是好数字，因为偶数下标处的数字（<code>2</code> 和 <code>8</code>）是偶数且奇数下标处的数字（<code>5</code> 和 <code>2</code>）为质数。但 <code>"3245"</code> <strong>不是</strong> 好数字，因为 <code>3</code> 在偶数下标处但不是偶数。</li>
</ul>

<p>给你一个整数 <code>n</code> ，请你返回长度为 <code>n</code> 且为好数字的数字字符串 <strong>总数</strong> 。由于答案可能会很大，请你将它对<strong> </strong><code>10<sup>9</sup> + 7</code> <strong>取余后返回</strong> 。</p>

<p>一个 <strong>数字字符串</strong> 是每一位都由 <code>0</code> 到 <code>9</code> 组成的字符串，且可能包含前导 0 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 1
<b>输出：</b>5
<b>解释：</b>长度为 1 的好数字包括 "0"，"2"，"4"，"6"，"8" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 4
<b>输出：</b>400
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>n = 50
<b>输出：</b>564908303
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 10<sup>15</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 递归
- 数学

## 提示

1. Is there a formula we can use to find the count of all the good numbers?
2. Exponentiation can be done very fast if we looked at the binary bits of n.

## 示例

```
1
4
50
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countGoodNumbers(long long n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countGoodNumbers(long n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
```

### C

```c
int countGoodNumbers(long long n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountGoodNumbers(long n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countGoodNumbers = function(n) {
    
};
```

### TypeScript

```typescript
function countGoodNumbers(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countGoodNumbers($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGoodNumbers(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGoodNumbers(n: Long): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGoodNumbers(int n) {
    
  }
}
```

### Go

```golang
func countGoodNumbers(n int64) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_good_numbers(n)
    
end
```

### Scala

```scala
object Solution {
    def countGoodNumbers(n: Long): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good_numbers(n: i64) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good-numbers n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good_numbers(N :: integer()) -> integer().
count_good_numbers(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good_numbers(n :: integer) :: integer
  def count_good_numbers(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGoodNumbers(n: Int64): Int64 {

    }
}
```

