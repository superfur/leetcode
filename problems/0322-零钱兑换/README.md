# 322. 零钱兑换

## 题目描述

<p>给你一个整数数组 <code>coins</code> ，表示不同面额的硬币；以及一个整数 <code>amount</code> ，表示总金额。</p>

<p>计算并返回可以凑成总金额所需的 <strong>最少的硬币个数</strong> 。如果没有任何一种硬币组合能组成总金额，返回&nbsp;<code>-1</code> 。</p>

<p>你可以认为每种硬币的数量是无限的。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>coins = <code>[1, 2, 5]</code>, amount = <code>11</code>
<strong>输出：</strong><code>3</code> 
<strong>解释：</strong>11 = 5 + 5 + 1</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>coins = <code>[2]</code>, amount = <code>3</code>
<strong>输出：</strong>-1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>coins = [1], amount = 0
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 12</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 动态规划

## 示例

```
[1,2,5]
11
[2]
3
[1]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
    }
};
```

### Java

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        
    }
}
```

### Python

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
```

### C

```c
int coinChange(int* coins, int coinsSize, int amount) {
    
}
```

### C#

```csharp
public class Solution {
    public int CoinChange(int[] coins, int amount) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    
};
```

### TypeScript

```typescript
function coinChange(coins: number[], amount: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @param Integer $amount
     * @return Integer
     */
    function coinChange($coins, $amount) {
        
    }
}
```

### Swift

```swift
class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int coinChange(List<int> coins, int amount) {
    
  }
}
```

### Go

```golang
func coinChange(coins []int, amount int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def coin_change(coins, amount)
    
end
```

### Scala

```scala
object Solution {
    def coinChange(coins: Array[Int], amount: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (coin-change coins amount)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec coin_change(Coins :: [integer()], Amount :: integer()) -> integer().
coin_change(Coins, Amount) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec coin_change(coins :: [integer], amount :: integer) :: integer
  def coin_change(coins, amount) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func coinChange(coins: Array<Int64>, amount: Int64): Int64 {

    }
}
```

