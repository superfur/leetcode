# 2466. 统计构造好字符串的方案数

## 题目描述

<p>给你整数&nbsp;<code>zero</code>&nbsp;，<code>one</code>&nbsp;，<code>low</code>&nbsp;和&nbsp;<code>high</code>&nbsp;，我们从空字符串开始构造一个字符串，每一步执行下面操作中的一种：</p>

<ul>
	<li>将&nbsp;<code>'0'</code>&nbsp;在字符串末尾添加&nbsp;<code>zero</code>&nbsp; 次。</li>
	<li>将&nbsp;<code>'1'</code>&nbsp;在字符串末尾添加&nbsp;<code>one</code>&nbsp;次。</li>
</ul>

<p>以上操作可以执行任意次。</p>

<p>如果通过以上过程得到一个 <strong>长度</strong>&nbsp;在&nbsp;<code>low</code> 和&nbsp;<code>high</code>&nbsp;之间（包含上下边界）的字符串，那么这个字符串我们称为&nbsp;<strong>好</strong>&nbsp;字符串。</p>

<p>请你返回满足以上要求的 <strong>不同</strong>&nbsp;好字符串数目。由于答案可能很大，请将结果对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>low = 3, high = 3, zero = 1, one = 1
<b>输出：</b>8
<b>解释：</b>
一个可能的好字符串是 "011" 。
可以这样构造得到："" -&gt; "0" -&gt; "01" -&gt; "011" 。
从 "000" 到 "111" 之间所有的二进制字符串都是好字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>low = 2, high = 3, zero = 1, one = 2
<b>输出：</b>5
<b>解释：</b>好字符串为 "00" ，"11" ，"000" ，"110" 和 "011" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= low&nbsp;&lt;= high&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= zero, one &lt;= low</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 提示

1. Calculate the number of good strings with length less or equal to some constant x.
2. Apply dynamic programming using the group size of consecutive zeros and ones.

## 示例

```
3
3
1
1
2
3
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        
    }
};
```

### Java

```java
class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
```

### C

```c
int countGoodStrings(int low, int high, int zero, int one) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountGoodStrings(int low, int high, int zero, int one) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @param {number} zero
 * @param {number} one
 * @return {number}
 */
var countGoodStrings = function(low, high, zero, one) {
    
};
```

### TypeScript

```typescript
function countGoodStrings(low: number, high: number, zero: number, one: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @param Integer $zero
     * @param Integer $one
     * @return Integer
     */
    function countGoodStrings($low, $high, $zero, $one) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGoodStrings(_ low: Int, _ high: Int, _ zero: Int, _ one: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGoodStrings(int low, int high, int zero, int one) {
    
  }
}
```

### Go

```golang
func countGoodStrings(low int, high int, zero int, one int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} low
# @param {Integer} high
# @param {Integer} zero
# @param {Integer} one
# @return {Integer}
def count_good_strings(low, high, zero, one)
    
end
```

### Scala

```scala
object Solution {
    def countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good-strings low high zero one)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good_strings(Low :: integer(), High :: integer(), Zero :: integer(), One :: integer()) -> integer().
count_good_strings(Low, High, Zero, One) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good_strings(low :: integer, high :: integer, zero :: integer, one :: integer) :: integer
  def count_good_strings(low, high, zero, one) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGoodStrings(low: Int64, high: Int64, zero: Int64, one: Int64): Int64 {

    }
}
```

