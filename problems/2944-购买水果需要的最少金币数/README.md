# 2944. 购买水果需要的最少金币数

## 题目描述

<p>给你一个 <strong>下标从 0&nbsp;开始的</strong> 整数数组&nbsp;<code>prices</code>&nbsp;，其中&nbsp;<code>prices[i]</code>&nbsp;表示你购买第 <code>i + 1</code>&nbsp;个水果需要花费的金币数目。</p>

<p>水果超市有如下促销活动：</p>

<ul>
	<li>如果你花费 <code>prices[i]</code>&nbsp;购买了下标为&nbsp;<code>i + 1</code>&nbsp;的水果，那么你可以免费获得下标范围在&nbsp;<code>[i + 1, i + i]</code>&nbsp;的水果。</li>
</ul>

<p><strong>注意</strong>&nbsp;，即使你&nbsp;<strong>可以</strong>&nbsp;免费获得水果&nbsp;<code>j</code>&nbsp;，你仍然可以花费&nbsp;<code>prices[j - 1]</code>&nbsp;个金币去购买它以获得它的奖励。</p>

<p>请你返回获得所有水果所需要的 <strong>最少</strong>&nbsp;金币数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">prices = [3,1,2]</span></p>

<p><strong>输出：</strong><span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>用&nbsp;<code>prices[0] = 3</code>&nbsp;个金币购买第 1 个水果，你可以免费获得第 2 个水果。</li>
	<li>用&nbsp;<code>prices[1] = 1</code>&nbsp;个金币购买第 2 个水果，你可以免费获得第 3 个水果。</li>
	<li>免费获得第 3 个水果。</li>
</ul>

<p>请注意，即使您可以免费获得第 2 个水果作为购买第 1 个水果的奖励，但您购买它是为了获得其奖励，这是更优化的。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">prices = [1,10,1,1]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>用&nbsp;<code>prices[0] = 1</code> 个金币购买第 1 个水果，你可以免费获得第 2 个水果。</li>
	<li>免费获得第 2 个水果。</li>
	<li>用&nbsp;<code>prices[2] = 1</code> 个金币购买第 3 个水果，你可以免费获得第 4 个水果。</li>
	<li>免费获得第 4 个水果。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">prices = [26,18,6,12,49,7,45,45]</span></p>

<p><strong>输出：</strong><span class="example-io">39</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>用&nbsp;<code>prices[0] = 26</code> 个金币购买第 1 个水果，你可以免费获得第 2 个水果。</li>
	<li>免费获得第 2 个水果。</li>
	<li>用&nbsp;<code>prices[2] = 6</code> 个金币购买第 3 个水果，你可以免费获得第 4，5，6（接下来的三个）水果。</li>
	<li>免费获得第 4 个水果。</li>
	<li>免费获得第 5&nbsp;个水果。</li>
	<li>用&nbsp;<code>prices[5] = 7</code>&nbsp;个金币购买第 6 个水果，你可以免费获得第 7 和 第 8 个水果。</li>
	<li>免费获得第 7&nbsp;个水果。</li>
	<li>免费获得第 8&nbsp;个水果。</li>
</ul>

<p>请注意，即使您可以免费获得第 6 个水果作为购买第 3 个水果的奖励，但您购买它是为了获得其奖励，这是更优化的。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 1000</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 队列
- 数组
- 动态规划
- 单调队列
- 堆（优先队列）

## 提示

1. The intended solution uses Dynamic Programming.
2. Let <code>dp[i]</code> denote the minimum number of coins, such that we bought <code>i<sup>th</sup></code> fruit and acquired all the fruits in the range <code>[i...n]</code>.
3. <code>dp[i] = min(dp[i], dp[j] + prices[i]) </code>, where <code>j</code> is in the range <code>[i + 1, i + 1 + i]</code>.

## 示例

```
[3,1,2]
[1,10,1,1]
[26,18,6,12,49,7,45,45]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumCoins(vector<int>& prices) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumCoins(int[] prices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
```

### C

```c
int minimumCoins(int* prices, int pricesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumCoins(int[] prices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var minimumCoins = function(prices) {
    
};
```

### TypeScript

```typescript
function minimumCoins(prices: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function minimumCoins($prices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCoins(_ prices: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCoins(prices: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCoins(List<int> prices) {
    
  }
}
```

### Go

```golang
func minimumCoins(prices []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prices
# @return {Integer}
def minimum_coins(prices)
    
end
```

### Scala

```scala
object Solution {
    def minimumCoins(prices: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_coins(prices: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-coins prices)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_coins(Prices :: [integer()]) -> integer().
minimum_coins(Prices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_coins(prices :: [integer]) :: integer
  def minimum_coins(prices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCoins(prices: Array<Int64>): Int64 {

    }
}
```

