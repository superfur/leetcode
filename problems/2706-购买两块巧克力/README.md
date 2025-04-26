# 2706. 购买两块巧克力

## 题目描述

<p>给你一个整数数组&nbsp;<code>prices</code>&nbsp;，它表示一个商店里若干巧克力的价格。同时给你一个整数&nbsp;<code>money</code>&nbsp;，表示你一开始拥有的钱数。</p>

<p>你必须购买 <strong>恰好&nbsp;</strong>两块巧克力，而且剩余的钱数必须是 <strong>非负数</strong>&nbsp;。同时你想最小化购买两块巧克力的总花费。</p>

<p>请你返回在购买两块巧克力后，最多能剩下多少钱。如果购买任意两块巧克力都超过了你拥有的钱，请你返回 <code>money</code>&nbsp;。注意剩余钱数必须是非负数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>prices = [1,2,2], money = 3
<b>输出：</b>0
<b>解释：</b>分别购买价格为 1 和 2 的巧克力。你剩下 3 - 3 = 0 块钱。所以我们返回 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>prices = [3,2,3], money = 3
<b>输出：</b>3
<b>解释：</b>购买任意 2 块巧克力都会超过你拥有的钱数，所以我们返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= prices.length &lt;= 50</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 100</code></li>
	<li><code>1 &lt;= money &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Sort the array and check if the money is more than or equal to the sum of the two cheapest elements.

## 示例

```
[1,2,2]
3
[3,2,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        
    }
};
```

### Java

```java
class Solution {
    public int buyChoco(int[] prices, int money) {
        
    }
}
```

### Python

```python
class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
```

### C

```c
int buyChoco(int* prices, int pricesSize, int money) {
    
}
```

### C#

```csharp
public class Solution {
    public int BuyChoco(int[] prices, int money) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function(prices, money) {
    
};
```

### TypeScript

```typescript
function buyChoco(prices: number[], money: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @param Integer $money
     * @return Integer
     */
    function buyChoco($prices, $money) {
        
    }
}
```

### Swift

```swift
class Solution {
    func buyChoco(_ prices: [Int], _ money: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun buyChoco(prices: IntArray, money: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int buyChoco(List<int> prices, int money) {
    
  }
}
```

### Go

```golang
func buyChoco(prices []int, money int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prices
# @param {Integer} money
# @return {Integer}
def buy_choco(prices, money)
    
end
```

### Scala

```scala
object Solution {
    def buyChoco(prices: Array[Int], money: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (buy-choco prices money)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec buy_choco(Prices :: [integer()], Money :: integer()) -> integer().
buy_choco(Prices, Money) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec buy_choco(prices :: [integer], money :: integer) :: integer
  def buy_choco(prices, money) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func buyChoco(prices: Array<Int64>, money: Int64): Int64 {

    }
}
```

