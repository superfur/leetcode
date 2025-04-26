# 2220. 转换数字的最少位翻转次数

## 题目描述

<p>一次 <strong>位翻转</strong>&nbsp;定义为将数字&nbsp;<code>x</code>&nbsp;二进制中的一个位进行 <strong>翻转</strong>&nbsp;操作，即将&nbsp;<code>0</code>&nbsp;变成&nbsp;<code>1</code>&nbsp;，或者将&nbsp;<code>1</code>&nbsp;变成&nbsp;<code>0</code>&nbsp;。</p>

<ul>
	<li>比方说，<code>x = 7</code>&nbsp;，二进制表示为&nbsp;<code>111</code>&nbsp;，我们可以选择任意一个位（包含没有显示的前导 0 ）并进行翻转。比方说我们可以翻转最右边一位得到&nbsp;<code>110</code>&nbsp;，或者翻转右边起第二位得到&nbsp;<code>101</code>&nbsp;，或者翻转右边起第五位（这一位是前导 0 ）得到&nbsp;<code>10111</code>&nbsp;等等。</li>
</ul>

<p>给你两个整数&nbsp;<code>start</code> 和&nbsp;<code>goal</code>&nbsp;，请你返回将&nbsp;<code>start</code>&nbsp;转变成&nbsp;<code>goal</code>&nbsp;的&nbsp;<strong>最少位翻转</strong>&nbsp;次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>start = 10, goal = 7
<b>输出：</b>3
<b>解释：</b>10 和 7 的二进制表示分别为 1010 和 0111 。我们可以通过 3 步将 10 转变成 7 ：
- 翻转右边起第一位得到：101<strong><em>0</em></strong> -&gt; 101<strong><em>1 。</em></strong>
- 翻转右边起第三位：1<strong><em>0</em></strong>11 -&gt; 1<strong><em>1</em></strong>11 。
- 翻转右边起第四位：<strong><em>1</em></strong>111 -&gt; <strong><em>0</em></strong>111 。
我们无法在 3 步内将 10 转变成 7 。所以我们返回 3 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>start = 3, goal = 4
<b>输出：</b>3
<b>解释：</b>3 和 4 的二进制表示分别为 011 和 100 。我们可以通过 3 步将 3 转变成 4 ：
- 翻转右边起第一位：01<strong><em>1</em></strong> -&gt; 01<em><strong>0 </strong></em>。
- 翻转右边起第二位：0<strong><em>1</em></strong>0 -&gt; 0<strong><em>0</em></strong>0 。
- 翻转右边起第三位：<strong><em>0</em></strong>00 -&gt; <strong><em>1</em></strong>00 。
我们无法在 3 步内将 3 变成 4 。所以我们返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= start, goal &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与&nbsp;<a href="https://leetcode.cn/problems/hamming-distance/">461. 汉明距离</a>&nbsp;相同。</p>


## 难度

Easy

## 标签

- 位运算

## 提示

1. If the value of a bit in start and goal differ, then we need to flip that bit.
2. Consider using the XOR operation to determine which bits need a bit flip.

## 示例

```
10
7
3
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minBitFlips(int start, int goal) {
        
    }
};
```

### Java

```java
class Solution {
    public int minBitFlips(int start, int goal) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
```

### C

```c
int minBitFlips(int start, int goal) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinBitFlips(int start, int goal) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minBitFlips = function(start, goal) {
    
};
```

### TypeScript

```typescript
function minBitFlips(start: number, goal: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $start
     * @param Integer $goal
     * @return Integer
     */
    function minBitFlips($start, $goal) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minBitFlips(_ start: Int, _ goal: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minBitFlips(start: Int, goal: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minBitFlips(int start, int goal) {
    
  }
}
```

### Go

```golang
func minBitFlips(start int, goal int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} start
# @param {Integer} goal
# @return {Integer}
def min_bit_flips(start, goal)
    
end
```

### Scala

```scala
object Solution {
    def minBitFlips(start: Int, goal: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-bit-flips start goal)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_bit_flips(Start :: integer(), Goal :: integer()) -> integer().
min_bit_flips(Start, Goal) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_bit_flips(start :: integer, goal :: integer) :: integer
  def min_bit_flips(start, goal) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minBitFlips(start: Int64, goal: Int64): Int64 {

    }
}
```

