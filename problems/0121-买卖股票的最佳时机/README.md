# 121. 买卖股票的最佳时机

## 题目描述

<p>给定一个数组 <code>prices</code> ，它的第 <code>i</code> 个元素 <code>prices[i]</code> 表示一支给定股票第 <code>i</code> 天的价格。</p>

<p>你只能选择 <strong>某一天</strong> 买入这只股票，并选择在 <strong>未来的某一个不同的日子</strong> 卖出该股票。设计一个算法来计算你所能获取的最大利润。</p>

<p>返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 <code>0</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[7,1,5,3,6,4]
<strong>输出：</strong>5
<strong>解释：</strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,6,4,3,1]
<strong>输出：</strong>0
<strong>解释：</strong>在这种情况下, 没有交易完成, 所以最大利润为 0。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= prices.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= prices[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 动态规划

## 示例

```
[7,1,5,3,6,4]
[7,6,4,3,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
```

### C

```c
int maxProfit(int* prices, int pricesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProfit(int[] prices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
};
```

### TypeScript

```typescript
function maxProfit(prices: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProfit(prices: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProfit(List<int> prices) {
    
  }
}
```

### Go

```golang
func maxProfit(prices []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    
end
```

### Scala

```scala
object Solution {
    def maxProfit(prices: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-profit prices)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_profit(Prices :: [integer()]) -> integer().
max_profit(Prices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit(prices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProfit(prices: Array<Int64>): Int64 {

    }
}
```

