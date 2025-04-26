# 264. 丑数 II

## 题目描述

<p>给你一个整数 <code>n</code> ，请你找出并返回第 <code>n</code> 个 <strong>丑数</strong> 。</p>

<p><strong>丑数 </strong>就是质因子只包含&nbsp;<code>2</code>、<code>3</code> 和&nbsp;<code>5</code>&nbsp;的正整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10
<strong>输出：</strong>12
<strong>解释：</strong>[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
<strong>解释：</strong>1 通常被视为丑数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1690</code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 动态规划
- 堆（优先队列）

## 提示

1. The naive approach is to call <code>isUgly</code> for every number until you reach the n<sup>th</sup> one. Most numbers are <i>not</i> ugly. Try to focus your effort on generating only the ugly ones.
2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
3. The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L<sub>1</sub>, L<sub>2</sub>, and L<sub>3</sub>.
4. Assume you have U<sub>k</sub>, the k<sup>th</sup> ugly number. Then U<sub>k+1</sub> must be Min(L<sub>1</sub> * 2, L<sub>2</sub> * 3, L<sub>3</sub> * 5).

## 示例

```
10
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int nthUglyNumber(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
```

### C

```c
int nthUglyNumber(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int NthUglyNumber(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    
};
```

### TypeScript

```typescript
function nthUglyNumber(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function nthUglyNumber($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nthUglyNumber(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nthUglyNumber(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int nthUglyNumber(int n) {
    
  }
}
```

### Go

```golang
func nthUglyNumber(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def nth_ugly_number(n)
    
end
```

### Scala

```scala
object Solution {
    def nthUglyNumber(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nth_ugly_number(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (nth-ugly-number n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec nth_ugly_number(N :: integer()) -> integer().
nth_ugly_number(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nth_ugly_number(n :: integer) :: integer
  def nth_ugly_number(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nthUglyNumber(n: Int64): Int64 {

    }
}
```

