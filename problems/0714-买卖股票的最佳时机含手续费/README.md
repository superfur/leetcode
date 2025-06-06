# 714. 买卖股票的最佳时机含手续费

## 题目描述

<p>给定一个整数数组&nbsp;<code>prices</code>，其中 <code>prices[i]</code>表示第&nbsp;<code>i</code>&nbsp;天的股票价格 ；整数&nbsp;<code>fee</code> 代表了交易股票的手续费用。</p>

<p>你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。</p>

<p>返回获得利润的最大值。</p>

<p><strong>注意：</strong>这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>prices = [1, 3, 2, 8, 4, 9], fee = 2
<strong>输出：</strong>8
<strong>解释：</strong>能够达到的最大利润:  
在此处买入&nbsp;prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润:&nbsp;((8 - 1) - 2) + ((9 - 4) - 2) = 8</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [1,3,7,5,10,3], fee = 3
<strong>输出：</strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt; 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= fee &lt; 5 * 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 提示

1. Consider the first K stock prices.  At the end, the only legal states are that you don't own a share of stock, or that you do.  Calculate the most profit you could have under each of these two cases.

## 示例

```
[1,3,2,8,4,9]
2
[1,3,7,5,10,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProfit(int[] prices, int fee) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
```

### C

```c
int maxProfit(int* prices, int pricesSize, int fee) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProfit(int[] prices, int fee) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function(prices, fee) {
    
};
```

### TypeScript

```typescript
function maxProfit(prices: number[], fee: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @param Integer $fee
     * @return Integer
     */
    function maxProfit($prices, $fee) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProfit(_ prices: [Int], _ fee: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProfit(prices: IntArray, fee: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProfit(List<int> prices, int fee) {
    
  }
}
```

### Go

```golang
func maxProfit(prices []int, fee int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prices
# @param {Integer} fee
# @return {Integer}
def max_profit(prices, fee)
    
end
```

### Scala

```scala
object Solution {
    def maxProfit(prices: Array[Int], fee: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-profit prices fee)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_profit(Prices :: [integer()], Fee :: integer()) -> integer().
max_profit(Prices, Fee) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_profit(prices :: [integer], fee :: integer) :: integer
  def max_profit(prices, fee) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProfit(prices: Array<Int64>, fee: Int64): Int64 {

    }
}
```

