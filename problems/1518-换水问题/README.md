# 1518. 换水问题

## 题目描述

<p>超市正在促销，你可以用 <code>numExchange</code> 个空水瓶从超市兑换一瓶水。最开始，你一共购入了 <code>numBottles</code> 瓶水。</p>

<p>如果喝掉了水瓶中的水，那么水瓶就会变成空的。</p>

<p>给你两个整数 <code>numBottles</code> 和 <code>numExchange</code> ，返回你 <strong>最多</strong> 可以喝到多少瓶水。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/sample_1_1875.png" style="height: 240px; width: 480px;" /></strong></p>

<pre>
<strong>输入：</strong>numBottles = 9, numExchange = 3
<strong>输出：</strong>13
<strong>解释：</strong>你可以用 <code>3</code> 个空瓶兑换 1 瓶水。
所以最多能喝到 9 + 3 + 1 = 13 瓶水。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/sample_2_1875.png" style="height: 240px; width: 790px;" /></p>

<pre>
<strong>输入：</strong>numBottles = 15, numExchange = 4
<strong>输出：</strong>19
<strong>解释：</strong>你可以用 <code>4</code> 个空瓶兑换 1 瓶水。
所以最多能喝到 15 + 3 + 1 = 19 瓶水。
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= numBottles &lt;= 100</code></li>
	<li><code>2 &lt;= numExchange &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. Simulate the process until there are not enough empty bottles for even one full bottle of water.

## 示例

```
9
3
15
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        
    }
};
```

### Java

```java
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
```

### C

```c
int numWaterBottles(int numBottles, int numExchange) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumWaterBottles(int numBottles, int numExchange) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    
};
```

### TypeScript

```typescript
function numWaterBottles(numBottles: number, numExchange: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $numBottles
     * @param Integer $numExchange
     * @return Integer
     */
    function numWaterBottles($numBottles, $numExchange) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numWaterBottles(_ numBottles: Int, _ numExchange: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numWaterBottles(numBottles: Int, numExchange: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numWaterBottles(int numBottles, int numExchange) {
    
  }
}
```

### Go

```golang
func numWaterBottles(numBottles int, numExchange int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num_bottles
# @param {Integer} num_exchange
# @return {Integer}
def num_water_bottles(num_bottles, num_exchange)
    
end
```

### Scala

```scala
object Solution {
    def numWaterBottles(numBottles: Int, numExchange: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-water-bottles numBottles numExchange)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_water_bottles(NumBottles :: integer(), NumExchange :: integer()) -> integer().
num_water_bottles(NumBottles, NumExchange) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_water_bottles(num_bottles :: integer, num_exchange :: integer) :: integer
  def num_water_bottles(num_bottles, num_exchange) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numWaterBottles(numBottles: Int64, numExchange: Int64): Int64 {

    }
}
```

