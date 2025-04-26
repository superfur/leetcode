# 50. Pow(x, n)

## 题目描述

<p>实现&nbsp;<a href="https://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(<em>x</em>, <em>n</em>)</a>&nbsp;，即计算 <code>x</code> 的整数&nbsp;<code>n</code> 次幂函数（即，<code>x<sup>n</sup></code><sup><span style="font-size:10.8333px"> </span></sup>）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 2.00000, n = 10
<strong>输出：</strong>1024.00000
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = 2.10000, n = 3
<strong>输出：</strong>9.26100
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 2.00000, n = -2
<strong>输出：</strong>0.25000
<strong>解释：</strong>2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-100.0 &lt; x &lt; 100.0</code></li>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup>-1</code></li>
	<li><code>n</code>&nbsp;是一个整数</li>
	<li>要么 <code>x</code> 不为零，要么 <code>n &gt; 0</code> 。</li>
	<li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 递归
- 数学

## 示例

```
2.00000
10
2.10000
3
2.00000
-2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public double myPow(double x, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
```

### C

```c
double myPow(double x, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public double MyPow(double x, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    
};
```

### TypeScript

```typescript
function myPow(x: number, n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Float $x
     * @param Integer $n
     * @return Float
     */
    function myPow($x, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func myPow(_ x: Double, _ n: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun myPow(x: Double, n: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double myPow(double x, int n) {
    
  }
}
```

### Go

```golang
func myPow(x float64, n int) float64 {
    
}
```

### Ruby

```ruby
# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
    
end
```

### Scala

```scala
object Solution {
    def myPow(x: Double, n: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (my-pow x n)
  (-> flonum? exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec my_pow(X :: float(), N :: integer()) -> float().
my_pow(X, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec my_pow(x :: float, n :: integer) :: float
  def my_pow(x, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func myPow(x: Float64, n: Int64): Float64 {

    }
}
```

