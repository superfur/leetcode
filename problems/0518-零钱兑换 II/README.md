# 518. 零钱兑换 II

## 题目描述

<p>给你一个整数数组 <code>coins</code> 表示不同面额的硬币，另给一个整数 <code>amount</code> 表示总金额。</p>

<p>请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 <code>0</code> 。</p>

<p>假设每一种面额的硬币有无限个。 </p>

<p>题目数据保证结果符合 32 位带符号整数。</p>

<p> </p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>amount = 5, coins = [1, 2, 5]
<strong>输出：</strong>4
<strong>解释：</strong>有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>amount = 3, coins = [2]
<strong>输出：</strong>0
<strong>解释：</strong>只用面额 2 的硬币不能凑成总金额 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>amount = 10, coins = [10] 
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= coins.length <= 300</code></li>
	<li><code>1 <= coins[i] <= 5000</code></li>
	<li><code>coins</code> 中的所有值 <strong>互不相同</strong></li>
	<li><code>0 <= amount <= 5000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
5
[1,2,5]
3
[2]
10
[10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        
    }
};
```

### Java

```java
class Solution {
    public int change(int amount, int[] coins) {
        
    }
}
```

### Python

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
```

### C

```c
int change(int amount, int* coins, int coinsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int Change(int amount, int[] coins) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
var change = function(amount, coins) {
    
};
```

### TypeScript

```typescript
function change(amount: number, coins: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $amount
     * @param Integer[] $coins
     * @return Integer
     */
    function change($amount, $coins) {
        
    }
}
```

### Swift

```swift
class Solution {
    func change(_ amount: Int, _ coins: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun change(amount: Int, coins: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int change(int amount, List<int> coins) {
    
  }
}
```

### Go

```golang
func change(amount int, coins []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} amount
# @param {Integer[]} coins
# @return {Integer}
def change(amount, coins)
    
end
```

### Scala

```scala
object Solution {
    def change(amount: Int, coins: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (change amount coins)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec change(Amount :: integer(), Coins :: [integer()]) -> integer().
change(Amount, Coins) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec change(amount :: integer, coins :: [integer]) :: integer
  def change(amount, coins) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func change(amount: Int64, coins: Array<Int64>): Int64 {

    }
}
```

