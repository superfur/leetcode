# LCR 188. 买卖芯片的最佳时机

## 题目描述

<p>数组 <code>prices</code> 记录了某芯片近期的交易价格，其中 <code>prices[i]</code> 表示的 <code>i</code> 天该芯片的价格。你只能选择 <strong>某一天</strong> 买入芯片，并选择在 <strong>未来的某一个不同的日子</strong> 卖出该芯片。请设计一个算法计算并返回你从这笔交易中能获取的最大利润。</p>

<p>如果你不能获取任何利润，返回 0。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>prices = [3, 6, 2, 9, 8, 5]
<strong>输出：</strong>7
<strong>解释：</strong>在第 3 天（芯片价格 = 2）买入，在第 4 天（芯片价格 = 9）卖出，最大利润 = 9 - 2 = 7。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [8, 12, 15, 7, 3, 10]
<strong>输出：</strong>7
<strong>解释：</strong>在第 5 天（芯片价格 = 3）买入，在第 6 天（芯片价格 = 10）卖出，最大利润 = 10 - 3 = 7。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>0 &lt;= prices.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10^4</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 121 题相同：<a href="https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/">https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/</a></p>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
[3,6,2,9,8,5]
[8,12,15,7,3,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int bestTiming(vector<int>& prices) {
        
    }
};
```

### Java

```java
class Solution {
    public int bestTiming(int[] prices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bestTiming(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        
```

### C

```c
int bestTiming(int* prices, int pricesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int BestTiming(int[] prices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var bestTiming = function(prices) {
    
};
```

### TypeScript

```typescript
function bestTiming(prices: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function bestTiming($prices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bestTiming(_ prices: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bestTiming(prices: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int bestTiming(List<int> prices) {
    
  }
}
```

### Go

```golang
func bestTiming(prices []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prices
# @return {Integer}
def best_timing(prices)
    
end
```

### Scala

```scala
object Solution {
    def bestTiming(prices: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn best_timing(prices: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (best-timing prices)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec best_timing(Prices :: [integer()]) -> integer().
best_timing(Prices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec best_timing(prices :: [integer]) :: integer
  def best_timing(prices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bestTiming(prices: Array<Int64>): Int64 {

    }
}
```

