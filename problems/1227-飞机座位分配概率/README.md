# 1227. 飞机座位分配概率

## 题目描述

<p>有 <code>n</code> 位乘客即将登机，飞机正好有 <code>n</code> 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。</p>

<p>剩下的乘客将会：</p>

<ul>
	<li>
	<p>如果他们自己的座位还空着，就坐到自己的座位上，</p>
	</li>
	<li>当他们自己的座位被占用时，随机选择其他座位</li>
</ul>

<p>第 <code>n</code>&nbsp;位乘客坐在自己的座位上的概率是多少？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1.00000
<strong>解释：</strong>第一个人只会坐在自己的位置上。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> n = 2
<strong>输出:</strong> 0.50000
<strong>解释：</strong>在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>


## 难度

Medium

## 标签

- 脑筋急转弯
- 数学
- 动态规划
- 概率与统计

## 提示

1. Let f(n) denote the probability of the n-th person getting correct seat in n-person case, then:

f(1) = 1 (base case, trivial)
f(2) = 1/2 (also trivial)
2. Try to calculate f(3), f(4), and f(5) using the base cases. What is the value of them?
f(i) for i >= 2 will also be 1/2.
3. Try to proof why f(i) = 1/2 for i >= 2.

## 示例

```
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public double nthPersonGetsNthSeat(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        
```

### C

```c
double nthPersonGetsNthSeat(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public double NthPersonGetsNthSeat(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var nthPersonGetsNthSeat = function(n) {
    
};
```

### TypeScript

```typescript
function nthPersonGetsNthSeat(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Float
     */
    function nthPersonGetsNthSeat($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nthPersonGetsNthSeat(_ n: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nthPersonGetsNthSeat(n: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double nthPersonGetsNthSeat(int n) {
    
  }
}
```

### Go

```golang
func nthPersonGetsNthSeat(n int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Float}
def nth_person_gets_nth_seat(n)
    
end
```

### Scala

```scala
object Solution {
    def nthPersonGetsNthSeat(n: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nth_person_gets_nth_seat(n: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (nth-person-gets-nth-seat n)
  (-> exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec nth_person_gets_nth_seat(N :: integer()) -> float().
nth_person_gets_nth_seat(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nth_person_gets_nth_seat(n :: integer) :: float
  def nth_person_gets_nth_seat(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nthPersonGetsNthSeat(n: Int64): Float64 {

    }
}
```

