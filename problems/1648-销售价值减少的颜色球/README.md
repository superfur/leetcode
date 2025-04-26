# 1648. 销售价值减少的颜色球

## 题目描述

<p>你有一些球的库存 <code>inventory</code> ，里面包含着不同颜色的球。一个顾客想要 <strong>任意颜色</strong> 总数为 <code>orders</code> 的球。</p>

<p>这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的 <strong>同色球</strong> 的数目。比方说还剩下 <code>6</code> 个黄球，那么顾客买第一个黄球的时候该黄球的价值为 <code>6</code> 。这笔交易以后，只剩下 <code>5</code> 个黄球了，所以下一个黄球的价值为 <code>5</code> （也就是球的价值随着顾客购买同色球是递减的）</p>

<p>给你整数数组 <code>inventory</code> ，其中 <code>inventory[i]</code> 表示第 <code>i</code> 种颜色球一开始的数目。同时给你整数 <code>orders</code> ，表示顾客总共想买的球数目。你可以按照 <strong>任意顺序</strong> 卖球。</p>

<p>请你返回卖了 <code>orders</code> 个球以后 <strong>最大</strong> 总价值之和。由于答案可能会很大，请你返回答案对 <code>10<sup>9</sup> + 7</code> <strong>取余数</strong> 的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/08/jj.gif" style="width: 480px; height: 270px;" />
<pre>
<b>输入：</b>inventory = [2,5], orders = 4
<b>输出：</b>14
<b>解释：</b>卖 1 个第一种颜色的球（价值为 2 )，卖 3 个第二种颜色的球（价值为 5 + 4 + 3）。
最大总和为 2 + 5 + 4 + 3 = 14 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>inventory = [3,5], orders = 6
<b>输出：</b>19
<strong>解释：</strong>卖 2 个第一种颜色的球（价值为 3 + 2），卖 4 个第二种颜色的球（价值为 5 + 4 + 3 + 2）。
最大总和为 3 + 2 + 5 + 4 + 3 + 2 = 19 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>inventory = [2,8,4,10,6], orders = 20
<b>输出：</b>110
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>inventory = [1000000000], orders = 1000000000
<b>输出：</b>21
<strong>解释：</strong>卖 1000000000 次第一种颜色的球，总价值为 500000000500000000 。 500000000500000000 对 10<sup>9 </sup>+ 7 取余为 21 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= inventory.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= inventory[i] <= 10<sup>9</sup></code></li>
	<li><code>1 <= orders <= min(sum(inventory[i]), 10<sup>9</sup>)</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 二分查找
- 排序
- 堆（优先队列）

## 提示

1. Greedily sell the most expensive ball.
2. There is some value k where all balls of value > k are sold, and some, (maybe 0) of balls of value k are sold.
3. Use binary search to find this value k, and use maths to find the total sum.

## 示例

```
[2,5]
4
[3,5]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& inventory, int orders) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProfit(int[] inventory, int orders) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
```

### C

```c
int maxProfit(int* inventory, int inventorySize, int orders) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProfit(int[] inventory, int orders) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} inventory
 * @param {number} orders
 * @return {number}
 */
var maxProfit = function(inventory, orders) {
    
};
```

### TypeScript

```typescript
function maxProfit(inventory: number[], orders: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $inventory
     * @param Integer $orders
     * @return Integer
     */
    function maxProfit($inventory, $orders) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProfit(_ inventory: [Int], _ orders: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProfit(inventory: IntArray, orders: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProfit(List<int> inventory, int orders) {
    
  }
}
```

### Go

```golang
func maxProfit(inventory []int, orders int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} inventory
# @param {Integer} orders
# @return {Integer}
def max_profit(inventory, orders)
    
end
```

### Scala

```scala
object Solution {
    def maxProfit(inventory: Array[Int], orders: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_profit(inventory: Vec<i32>, orders: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-profit inventory orders)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_profit(Inventory :: [integer()], Orders :: integer()) -> integer().
max_profit(Inventory, Orders) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_profit(inventory :: [integer], orders :: integer) :: integer
  def max_profit(inventory, orders) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProfit(inventory: Array<Int64>, orders: Int64): Int64 {

    }
}
```

