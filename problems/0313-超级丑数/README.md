# 313. 超级丑数

## 题目描述

<p><strong>超级丑数</strong> 是一个正整数，并满足其所有质因数都出现在质数数组 <code>primes</code> 中。</p>

<p>给你一个整数 <code>n</code> 和一个整数数组 <code>primes</code> ，返回第 <code>n</code> 个 <strong>超级丑数</strong> 。</p>

<p>题目数据保证第 <code>n</code> 个 <strong>超级丑数</strong> 在 <strong>32-bit</strong> 带符号整数范围内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 12, <code>primes</code> = <code>[2,7,13,19]</code>
<strong>输出：</strong>32 
<strong>解释：</strong>给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, primes = [2,3,5]
<strong>输出：</strong>1
<strong>解释：</strong>1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
</pre>
&nbsp;

<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= primes.length &lt;= 100</code></li>
	<li><code>2 &lt;= primes[i] &lt;= 1000</code></li>
	<li>题目数据<strong> 保证</strong> <code>primes[i]</code> 是一个质数</li>
	<li><code>primes</code> 中的所有值都 <strong>互不相同</strong> ，且按 <strong>递增顺序</strong> 排列</li>
</ul>
</div>
</div>
</div>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划

## 示例

```
12
[2,7,13,19]
1
[2,3,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        
    }
};
```

### Java

```java
class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
```

### C

```c
int nthSuperUglyNumber(int n, int* primes, int primesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NthSuperUglyNumber(int n, int[] primes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
    
};
```

### TypeScript

```typescript
function nthSuperUglyNumber(n: number, primes: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $primes
     * @return Integer
     */
    function nthSuperUglyNumber($n, $primes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nthSuperUglyNumber(_ n: Int, _ primes: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nthSuperUglyNumber(n: Int, primes: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int nthSuperUglyNumber(int n, List<int> primes) {
    
  }
}
```

### Go

```golang
func nthSuperUglyNumber(n int, primes []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} primes
# @return {Integer}
def nth_super_ugly_number(n, primes)
    
end
```

### Scala

```scala
object Solution {
    def nthSuperUglyNumber(n: Int, primes: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nth_super_ugly_number(n: i32, primes: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (nth-super-ugly-number n primes)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec nth_super_ugly_number(N :: integer(), Primes :: [integer()]) -> integer().
nth_super_ugly_number(N, Primes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nth_super_ugly_number(n :: integer, primes :: [integer]) :: integer
  def nth_super_ugly_number(n, primes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nthSuperUglyNumber(n: Int64, primes: Array<Int64>): Int64 {

    }
}
```

