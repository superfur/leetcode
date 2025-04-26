# 188. 买卖股票的最佳时机 IV

## 题目描述

<p>给你一个整数数组&nbsp;<code>prices</code> 和一个整数 <code>k</code> ，其中 <code>prices[i]</code> 是某支给定的股票在第 <code>i</code><em> </em>天的价格。</p>

<p>设计一个算法来计算你所能获取的最大利润。你最多可以完成 <code>k</code> 笔交易。也就是说，你最多可以买 <code>k</code> 次，卖 <code>k</code> 次。</p>

<p><strong>注意：</strong>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>k = 2, prices = [2,4,1]
<strong>输出：</strong>2
<strong>解释：</strong>在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 2, prices = [3,2,6,5,0,3]
<strong>输出：</strong>7
<strong>解释：</strong>在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>1 &lt;= prices.length &lt;= 1000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
2
[2,4,1]
2
[3,2,6,5,0,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProfit(int k, int[] prices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
```

### C

```c
int maxProfit(int k, int* prices, int pricesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProfit(int k, int[] prices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
    
};
```

### TypeScript

```typescript
function maxProfit(k: number, prices: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($k, $prices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProfit(_ k: Int, _ prices: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProfit(k: Int, prices: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProfit(int k, List<int> prices) {
    
  }
}
```

### Go

```golang
func maxProfit(k int, prices []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer[]} prices
# @return {Integer}
def max_profit(k, prices)
    
end
```

### Scala

```scala
object Solution {
    def maxProfit(k: Int, prices: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-profit k prices)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_profit(K :: integer(), Prices :: [integer()]) -> integer().
max_profit(K, Prices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_profit(k :: integer, prices :: [integer]) :: integer
  def max_profit(k, prices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProfit(k: Int64, prices: Array<Int64>): Int64 {

    }
}
```

