# 1808. 好因子的最大数目

## 题目描述

<p>给你一个正整数 <code>primeFactors</code> 。你需要构造一个正整数 <code>n</code> ，它满足以下条件：</p>

<ul>
	<li><code>n</code> 质因数（质因数需要考虑重复的情况）的数目 <strong>不超过 </strong><code>primeFactors</code> 个。</li>
	<li><code>n</code> 好因子的数目最大化。如果 <code>n</code> 的一个因子可以被 <code>n</code> 的每一个质因数整除，我们称这个因子是 <strong>好因子</strong> 。比方说，如果 <code>n = 12</code> ，那么它的质因数为 <code>[2,2,3]</code> ，那么 <code>6</code> 和 <code>12</code> 是好因子，但 <code>3</code> 和 <code>4</code> 不是。</li>
</ul>

<p>请你返回 <code>n</code> 的好因子的数目。由于答案可能会很大，请返回答案对 <code>10<sup>9</sup> + 7</code> <b>取余</b> 的结果。</p>

<p>请注意，一个质数的定义是大于 <code>1</code> ，且不能被分解为两个小于该数的自然数相乘。一个数 <code>n</code> 的质因子是将 <code>n</code> 分解为若干个质因子，且它们的乘积为 <code>n</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>primeFactors = 5
<strong>输出：</strong>6
<b>解释：</b>200 是一个可行的 n 。
它有 5 个质因子：[2,2,2,5,5] ，且有 6 个好因子：[10,20,40,50,100,200] 。
不存在别的 n 有至多 5 个质因子，且同时有更多的好因子。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>primeFactors = 8
<b>输出：</b>18
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= primeFactors <= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 递归
- 数学
- 数论

## 提示

1. The number of nice divisors is equal to the product of the count of each prime factor. Then the problem is reduced to: given n, find a sequence of numbers whose sum equals n and whose product is maximized.
2. This sequence can have no numbers that are larger than 4. Proof: if it contains a number x that is larger than 4, then you can replace x with floor(x/2) and ceil(x/2), and floor(x/2) * ceil(x/2) > x. You can also replace 4s with two 2s. Hence, there will always be optimal solutions with only 2s and 3s.
3. If there are three 2s, you can replace them with two 3s to get a better product. Hence, you'll never have more than two 2s.
4. Keep adding 3s as long as n ≥ 5.

## 示例

```
5
8
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxNiceDivisors(int primeFactors) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxNiceDivisors(int primeFactors) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        
```

### C

```c


int maxNiceDivisors(int primeFactors){

}
```

### C#

```csharp
public class Solution {
    public int MaxNiceDivisors(int primeFactors) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} primeFactors
 * @return {number}
 */
var maxNiceDivisors = function(primeFactors) {
    
};
```

### TypeScript

```typescript
function maxNiceDivisors(primeFactors: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $primeFactors
     * @return Integer
     */
    function maxNiceDivisors($primeFactors) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNiceDivisors(_ primeFactors: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNiceDivisors(primeFactors: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxNiceDivisors(int primeFactors) {
    
  }
}
```

### Go

```golang
func maxNiceDivisors(primeFactors int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} prime_factors
# @return {Integer}
def max_nice_divisors(prime_factors)
    
end
```

### Scala

```scala
object Solution {
    def maxNiceDivisors(primeFactors: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_nice_divisors(prime_factors: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-nice-divisors primeFactors)
  (-> exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec max_nice_divisors(PrimeFactors :: integer()) -> integer().
max_nice_divisors(PrimeFactors) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_nice_divisors(prime_factors :: integer) :: integer
  def max_nice_divisors(prime_factors) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNiceDivisors(primeFactors: Int64): Int64 {

    }
}
```

