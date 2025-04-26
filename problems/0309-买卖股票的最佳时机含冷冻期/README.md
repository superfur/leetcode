# 309. 买卖股票的最佳时机含冷冻期

## 题目描述

<p>给定一个整数数组<meta charset="UTF-8" /><code>prices</code>，其中第&nbsp;<em>&nbsp;</em><code>prices[i]</code>&nbsp;表示第&nbsp;<code><em>i</em></code>&nbsp;天的股票价格 。​</p>

<p>设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:</p>

<ul>
	<li>卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。</li>
</ul>

<p><strong>注意：</strong>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> prices = [1,2,3,0,2]
<strong>输出: </strong>3 
<strong>解释:</strong> 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> prices = [1]
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 5000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
[1,2,3,0,2]
[1]
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

