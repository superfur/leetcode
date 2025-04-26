# 1833. 雪糕的最大数量

## 题目描述

<p>夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。</p>

<p>商店中新到 <code>n</code> 支雪糕，用长度为 <code>n</code> 的数组 <code>costs</code> 表示雪糕的定价，其中 <code>costs[i]</code> 表示第 <code>i</code> 支雪糕的现金价格。Tony 一共有 <code>coins</code> 现金可以用于消费，他想要买尽可能多的雪糕。</p>

<p><strong>注意：</strong>Tony 可以按任意顺序购买雪糕。</p>

<p>给你价格数组 <code>costs</code> 和现金量 <code>coins</code> ，请你计算并返回 Tony 用 <code>coins</code> 现金能够买到的雪糕的 <strong>最大数量</strong> 。</p>

<p>你必须使用计数排序解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>costs = [1,3,2,4,1], coins = 7
<strong>输出：</strong>4
<strong>解释：</strong>Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>costs = [10,6,8,7,7,8], coins = 5
<strong>输出：</strong>0
<strong>解释：</strong>Tony 没有足够的钱买任何一支雪糕。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>costs = [1,6,3,1,2,5], coins = 20
<strong>输出：</strong>6
<strong>解释：</strong>Tony 可以买下所有的雪糕，总价为 1 + 6 + 3 + 1 + 2 + 5 = 18 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>costs.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= costs[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= coins &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 计数排序
- 排序

## 提示

1. It is always optimal to buy the least expensive ice cream bar first.
2. Sort the prices so that the cheapest ice cream bar comes first.

## 示例

```
[1,3,2,4,1]
7
[10,6,8,7,7,8]
5
[1,6,3,1,2,5]
20
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxIceCream(int[] costs, int coins) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
```

### C

```c
int maxIceCream(int* costs, int costsSize, int coins) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxIceCream(int[] costs, int coins) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function(costs, coins) {
    
};
```

### TypeScript

```typescript
function maxIceCream(costs: number[], coins: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $costs
     * @param Integer $coins
     * @return Integer
     */
    function maxIceCream($costs, $coins) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxIceCream(_ costs: [Int], _ coins: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxIceCream(costs: IntArray, coins: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxIceCream(List<int> costs, int coins) {
    
  }
}
```

### Go

```golang
func maxIceCream(costs []int, coins int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} costs
# @param {Integer} coins
# @return {Integer}
def max_ice_cream(costs, coins)
    
end
```

### Scala

```scala
object Solution {
    def maxIceCream(costs: Array[Int], coins: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_ice_cream(costs: Vec<i32>, coins: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-ice-cream costs coins)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_ice_cream(Costs :: [integer()], Coins :: integer()) -> integer().
max_ice_cream(Costs, Coins) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_ice_cream(costs :: [integer], coins :: integer) :: integer
  def max_ice_cream(costs, coins) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxIceCream(costs: Array<Int64>, coins: Int64): Int64 {

    }
}
```

