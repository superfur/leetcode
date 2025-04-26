# 122. 买卖股票的最佳时机 II

## 题目描述

<p>给你一个整数数组 <code>prices</code> ，其中&nbsp;<code>prices[i]</code> 表示某支股票第 <code>i</code> 天的价格。</p>

<p>在每一天，你可以决定是否购买和/或出售股票。你在任何时候&nbsp;<strong>最多</strong>&nbsp;只能持有 <strong>一股</strong> 股票。你也可以先购买，然后在 <strong>同一天</strong> 出售。</p>

<p>返回 <em>你能获得的 <strong>最大</strong> 利润</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,1,5,3,6,4]
<strong>输出：</strong>7
<strong>解释：</strong>在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
最大总利润为 4 + 3 = 7 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [1,2,3,4,5]
<strong>输出：</strong>4
<strong>解释：</strong>在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
最大总利润为 4 。</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,6,4,3,1]
<strong>输出：</strong>0
<strong>解释：</strong>在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 示例

```
[7,1,5,3,6,4]
[1,2,3,4,5]
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

