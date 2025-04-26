# 746. 使用最小花费爬楼梯

## 题目描述

<p>给你一个整数数组 <code>cost</code> ，其中 <code>cost[i]</code> 是从楼梯第 <code>i</code> 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。</p>

<p>你可以选择从下标为 <code>0</code> 或下标为 <code>1</code> 的台阶开始爬楼梯。</p>

<p>请你计算并返回达到楼梯顶部的最低花费。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>cost = [10,<em><strong>15</strong></em>,20]
<strong>输出：</strong>15
<strong>解释：</strong>你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>cost = [<em><strong>1</strong></em>,100,<em><strong>1</strong></em>,1,<em><strong>1</strong></em>,100,<em><strong>1</strong></em>,<em><strong>1</strong></em>,100,<em><strong>1</strong></em>]
<strong>输出：</strong>6
<strong>解释：</strong>你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= cost.length &lt;= 1000</code></li>
	<li><code>0 &lt;= cost[i] &lt;= 999</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 动态规划

## 提示

1. Build an array dp where dp[i] is the minimum cost to climb to the top starting from the ith staircase.
2. Assuming we have n staircase labeled from 0 to n - 1 and assuming the top is n, then dp[n] = 0, marking that if you are at the top, the cost is 0.
3. Now, looping from n - 1 to 0, the dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]). The answer will be the minimum of dp[0] and dp[1]

## 示例

```
[10,15,20]
[1,100,1,1,1,100,1,1,100,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
```

### C

```c
int minCostClimbingStairs(int* cost, int costSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    
};
```

### TypeScript

```typescript
function minCostClimbingStairs(cost: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @return Integer
     */
    function minCostClimbingStairs($cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCostClimbingStairs(_ cost: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCostClimbingStairs(cost: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCostClimbingStairs(List<int> cost) {
    
  }
}
```

### Go

```golang
func minCostClimbingStairs(cost []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cost
# @return {Integer}
def min_cost_climbing_stairs(cost)
    
end
```

### Scala

```scala
object Solution {
    def minCostClimbingStairs(cost: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost-climbing-stairs cost)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost_climbing_stairs(Cost :: [integer()]) -> integer().
min_cost_climbing_stairs(Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost_climbing_stairs(cost :: [integer]) :: integer
  def min_cost_climbing_stairs(cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCostClimbingStairs(cost: Array<Int64>): Int64 {

    }
}
```

