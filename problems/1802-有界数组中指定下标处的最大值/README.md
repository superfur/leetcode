# 1802. 有界数组中指定下标处的最大值

## 题目描述

<p>给你三个正整数 <code>n</code>、<code>index</code> 和 <code>maxSum</code> 。你需要构造一个同时满足下述所有条件的数组 <code>nums</code>（下标 <strong>从 0 开始</strong> 计数）：</p>

<ul>
	<li><code>nums.length == n</code></li>
	<li><code>nums[i]</code> 是 <strong>正整数</strong> ，其中 <code>0 &lt;= i &lt; n</code></li>
	<li><code>abs(nums[i] - nums[i+1]) &lt;= 1</code> ，其中 <code>0 &lt;= i &lt; n-1</code></li>
	<li><code>nums</code> 中所有元素之和不超过 <code>maxSum</code></li>
	<li><code>nums[index]</code> 的值被 <strong>最大化</strong></li>
</ul>

<p>返回你所构造的数组中的 <code>nums[index]</code> 。</p>

<p>注意：<code>abs(x)</code> 等于 <code>x</code> 的前提是 <code>x &gt;= 0</code> ；否则，<code>abs(x)</code> 等于 <code>-x</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 4, index = 2,  maxSum = 6
<strong>输出：</strong>2
<strong>解释：</strong>数组 [1,1,<strong>2</strong>,1] 和 [1,2,<strong>2</strong>,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 6, index = 1,  maxSum = 10
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= maxSum &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= index &lt; n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 二分查找

## 提示

1. What if the problem was instead determining if you could generate a valid array with nums[index] == target?
2. To generate the array, set nums[index] to target, nums[index-i] to target-i, and nums[index+i] to target-i. Then, this will give the minimum possible sum, so check if the sum is less than or equal to maxSum.
3. n is too large to actually generate the array, so you can use the formula 1 + 2 + ... + n = n * (n+1) / 2 to quickly find the sum of nums[0...index] and nums[index...n-1].
4. Binary search for the target. If it is possible, then move the lower bound up. Otherwise, move the upper bound down.

## 示例

```
4
2
6
6
1
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxValue(int n, int index, int maxSum) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
```

### C

```c
int maxValue(int n, int index, int maxSum) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxValue(int n, int index, int maxSum) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} index
 * @param {number} maxSum
 * @return {number}
 */
var maxValue = function(n, index, maxSum) {
    
};
```

### TypeScript

```typescript
function maxValue(n: number, index: number, maxSum: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $index
     * @param Integer $maxSum
     * @return Integer
     */
    function maxValue($n, $index, $maxSum) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxValue(_ n: Int, _ index: Int, _ maxSum: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxValue(n: Int, index: Int, maxSum: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxValue(int n, int index, int maxSum) {
    
  }
}
```

### Go

```golang
func maxValue(n int, index int, maxSum int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} index
# @param {Integer} max_sum
# @return {Integer}
def max_value(n, index, max_sum)
    
end
```

### Scala

```scala
object Solution {
    def maxValue(n: Int, index: Int, maxSum: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_value(n: i32, index: i32, max_sum: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-value n index maxSum)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_value(N :: integer(), Index :: integer(), MaxSum :: integer()) -> integer().
max_value(N, Index, MaxSum) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_value(n :: integer, index :: integer, max_sum :: integer) :: integer
  def max_value(n, index, max_sum) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxValue(n: Int64, index: Int64, maxSum: Int64): Int64 {

    }
}
```

