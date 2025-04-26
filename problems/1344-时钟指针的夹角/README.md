# 1344. 时钟指针的夹角

## 题目描述

<p>给你两个数&nbsp;<code>hour</code>&nbsp;和&nbsp;<code>minutes</code>&nbsp;。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_1_1673.png" style="height: 225px; width: 230px;"></p>

<pre><strong>输入：</strong>hour = 12, minutes = 30
<strong>输出：</strong>165
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_2_1673.png" style="height: 225px; width: 230px;"></p>

<pre><strong>输入：</strong>hour = 3, minutes = 30
<strong>输出；</strong>75
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_3_1673.png" style="height: 231px; width: 230px;"></strong></p>

<pre><strong>输入：</strong>hour = 3, minutes = 15
<strong>输出：</strong>7.5
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>hour = 4, minutes = 50
<strong>输出：</strong>155
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>hour = 12, minutes = 0
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= hour &lt;= 12</code></li>
	<li><code>0 &lt;= minutes &lt;= 59</code></li>
	<li>与标准答案误差在&nbsp;<code>10^-5</code>&nbsp;以内的结果都被视为正确结果。</li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. The tricky part is determining how the minute hand affects the position of the hour hand.
2. Calculate the angles separately then find the difference.

## 示例

```
12
30
3
30
3
15
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double angleClock(int hour, int minutes) {
        
    }
};
```

### Java

```java
class Solution {
    public double angleClock(int hour, int minutes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
```

### C

```c
double angleClock(int hour, int minutes) {
    
}
```

### C#

```csharp
public class Solution {
    public double AngleClock(int hour, int minutes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} hour
 * @param {number} minutes
 * @return {number}
 */
var angleClock = function(hour, minutes) {
    
};
```

### TypeScript

```typescript
function angleClock(hour: number, minutes: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $hour
     * @param Integer $minutes
     * @return Float
     */
    function angleClock($hour, $minutes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func angleClock(_ hour: Int, _ minutes: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun angleClock(hour: Int, minutes: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double angleClock(int hour, int minutes) {
    
  }
}
```

### Go

```golang
func angleClock(hour int, minutes int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} hour
# @param {Integer} minutes
# @return {Float}
def angle_clock(hour, minutes)
    
end
```

### Scala

```scala
object Solution {
    def angleClock(hour: Int, minutes: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn angle_clock(hour: i32, minutes: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (angle-clock hour minutes)
  (-> exact-integer? exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec angle_clock(Hour :: integer(), Minutes :: integer()) -> float().
angle_clock(Hour, Minutes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec angle_clock(hour :: integer, minutes :: integer) :: float
  def angle_clock(hour, minutes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func angleClock(hour: Int64, minutes: Int64): Float64 {

    }
}
```

