# 2144. 打折购买糖果的最小开销

## 题目描述

<p>一家商店正在打折销售糖果。每购买 <strong>两个</strong>&nbsp;糖果，商店会 <strong>免费</strong>&nbsp;送一个糖果。</p>

<p>免费送的糖果唯一的限制是：它的价格需要小于等于购买的两个糖果价格的 <strong>较小值</strong>&nbsp;。</p>

<ul>
	<li>比方说，总共有 <code>4</code>&nbsp;个糖果，价格分别为&nbsp;<code>1</code>&nbsp;，<code>2</code>&nbsp;，<code>3</code>&nbsp;和&nbsp;<code>4</code>&nbsp;，一位顾客买了价格为&nbsp;<code>2</code> 和&nbsp;<code>3</code>&nbsp;的糖果，那么他可以免费获得价格为 <code>1</code>&nbsp;的糖果，但不能获得价格为&nbsp;<code>4</code>&nbsp;的糖果。</li>
</ul>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>cost</code>&nbsp;，其中&nbsp;<code>cost[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个糖果的价格，请你返回获得 <strong>所有</strong>&nbsp;糖果的 <strong>最小</strong>&nbsp;总开销。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>cost = [1,2,3]
<b>输出：</b>5
<b>解释：</b>我们购买价格为 2 和 3 的糖果，然后免费获得价格为 1 的糖果。
总开销为 2 + 3 = 5 。这是开销最小的 <strong>唯一</strong>&nbsp;方案。
注意，我们不能购买价格为 1 和 3 的糖果，并免费获得价格为 2 的糖果。
这是因为免费糖果的价格必须小于等于购买的 2 个糖果价格的较小值。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>cost = [6,5,7,9,2,2]
<b>输出：</b>23
<b>解释：</b>最小总开销购买糖果方案为：
- 购买价格为 9 和 7 的糖果
- 免费获得价格为 6 的糖果
- 购买价格为 5 和 2 的糖果
- 免费获得价格为 2 的最后一个糖果
因此，最小总开销为 9 + 7 + 5 + 2 = 23 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>cost = [5,5]
<b>输出：</b>10
<b>解释：</b>由于只有 2 个糖果，我们需要将它们都购买，而且没有免费糖果。
所以总最小开销为 5 + 5 = 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= cost.length &lt;= 100</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 排序

## 提示

1. If we consider costs from high to low, what is the maximum cost of a single candy that we can get for free?
2. How can we generalize this approach to maximize the costs of the candies we get for free?
3. Can “sorting” the array help us find the minimum cost?

## 示例

```
[1,2,3]
[6,5,7,9,2,2]
[5,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumCost(vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumCost(int[] cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
```

### C

```c
int minimumCost(int* cost, int costSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumCost(int[] cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(cost) {
    
};
```

### TypeScript

```typescript
function minimumCost(cost: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ cost: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(cost: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(List<int> cost) {
    
  }
}
```

### Go

```golang
func minimumCost(cost []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(cost)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(cost: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(cost: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost cost)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Cost :: [integer()]) -> integer().
minimum_cost(Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(cost :: [integer]) :: integer
  def minimum_cost(cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(cost: Array<Int64>): Int64 {

    }
}
```

