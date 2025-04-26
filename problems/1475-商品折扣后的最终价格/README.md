# 1475. 商品折扣后的最终价格

## 题目描述

<p>给你一个数组&nbsp;<code>prices</code>&nbsp;，其中&nbsp;<code>prices[i]</code>&nbsp;是商店里第&nbsp;<code>i</code>&nbsp;件商品的价格。</p>

<p>商店里正在进行促销活动，如果你要买第&nbsp;<code>i</code>&nbsp;件商品，那么你可以得到与 <code>prices[j]</code> 相等的折扣，其中&nbsp;<code>j</code>&nbsp;是满足&nbsp;<code>j &gt; i</code>&nbsp;且&nbsp;<code>prices[j] &lt;= prices[i]</code>&nbsp;的&nbsp;<strong>最小下标</strong>&nbsp;，如果没有满足条件的&nbsp;<code>j</code>&nbsp;，你将没有任何折扣。</p>

<p>请你返回一个数组，数组中第&nbsp;<code>i</code>&nbsp;个元素是折扣后你购买商品 <code>i</code>&nbsp;最终需要支付的价格。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>prices = [8,4,6,2,3]
<strong>输出：</strong>[4,2,4,2,3]
<strong>解释：</strong>
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>prices = [1,2,3,4,5]
<strong>输出：</strong>[1,2,3,4,5]
<strong>解释：</strong>在这个例子中，所有商品都没有折扣。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>prices = [10,1,1,6]
<strong>输出：</strong>[9,0,1,6]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 500</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10^3</code></li>
</ul>


## 难度

Easy

## 标签

- 栈
- 数组
- 单调栈

## 提示

1. Use brute force: For the ith item in the shop with a loop find the first position j satisfying the conditions and apply the discount, otherwise, the discount is 0.

## 示例

```
[8,4,6,2,3]
[1,2,3,4,5]
[10,1,1,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] finalPrices(int[] prices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* finalPrices(int* prices, int pricesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FinalPrices(int[] prices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    
};
```

### TypeScript

```typescript
function finalPrices(prices: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer[]
     */
    function finalPrices($prices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func finalPrices(_ prices: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun finalPrices(prices: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> finalPrices(List<int> prices) {
    
  }
}
```

### Go

```golang
func finalPrices(prices []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prices
# @return {Integer[]}
def final_prices(prices)
    
end
```

### Scala

```scala
object Solution {
    def finalPrices(prices: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn final_prices(prices: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (final-prices prices)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec final_prices(Prices :: [integer()]) -> [integer()].
final_prices(Prices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec final_prices(prices :: [integer]) :: [integer]
  def final_prices(prices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func finalPrices(prices: Array<Int64>): Array<Int64> {

    }
}
```

