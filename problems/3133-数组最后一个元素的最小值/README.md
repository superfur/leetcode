# 3133. 数组最后一个元素的最小值

## 题目描述

<p>给你两个整数 <code>n</code> 和 <code>x</code> 。你需要构造一个长度为 <code>n</code> 的 <strong>正整数 </strong>数组 <code>nums</code> ，对于所有 <code>0 &lt;= i &lt; n - 1</code> ，满足 <code>nums[i + 1]</code><strong> 大于 </strong><code>nums[i]</code> ，并且数组 <code>nums</code> 中所有元素的按位 <code>AND</code> 运算结果为 <code>x</code> 。</p>

<p>返回 <code>nums[n - 1]</code> 可能的<strong> 最小 </strong>值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 3, x = 4</span></p>

<p><strong>输出：</strong><span class="example-io">6</span></p>

<p><strong>解释：</strong></p>

<p>数组 <code>nums</code> 可以是 <code>[4,5,6]</code> ，最后一个元素为 <code>6</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 2, x = 7</span></p>

<p><strong>输出：</strong><span class="example-io">15</span></p>

<p><strong>解释：</strong></p>

<p>数组 <code>nums</code> 可以是 <code>[7,15]</code> ，最后一个元素为 <code>15</code> 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, x &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算

## 提示

1. Each element of the array should be obtained by “merging” <code>x</code> and <code>v</code> where <code>v = 0, 1, 2, …(n - 1)</code>.
2. To merge <code>x</code> with another number <code>v</code>, keep the set bits of <code>x</code> untouched, for all the other bits, fill the set bits of <code>v</code> from right to left in order one by one.
3. So the final answer is the “merge” of <code>x</code> and <code>n - 1</code>.

## 示例

```
3
4
2
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minEnd(int n, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public long minEnd(int n, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
```

### C

```c
long long minEnd(int n, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinEnd(int n, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var minEnd = function(n, x) {
    
};
```

### TypeScript

```typescript
function minEnd(n: number, x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $x
     * @return Integer
     */
    function minEnd($n, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minEnd(_ n: Int, _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minEnd(n: Int, x: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minEnd(int n, int x) {
    
  }
}
```

### Go

```golang
func minEnd(n int, x int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} x
# @return {Integer}
def min_end(n, x)
    
end
```

### Scala

```scala
object Solution {
    def minEnd(n: Int, x: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_end(n: i32, x: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-end n x)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_end(N :: integer(), X :: integer()) -> integer().
min_end(N, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_end(n :: integer, x :: integer) :: integer
  def min_end(n, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minEnd(n: Int64, x: Int64): Int64 {

    }
}
```

