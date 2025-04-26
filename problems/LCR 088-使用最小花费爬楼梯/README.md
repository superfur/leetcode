# LCR 088. 使用最小花费爬楼梯

## 题目描述

<p>数组的每个下标作为一个阶梯，第 <code>i</code> 个阶梯对应着一个非负数的体力花费值&nbsp;<code>cost[i]</code>（下标从 <code>0</code> 开始）。</p>

<p>每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。</p>

<p>请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>cost = [10, 15, 20]
<strong>输出：</strong>15
<strong>解释：</strong>最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
</pre>

<p><strong>&nbsp;示例 2：</strong></p>

<pre>
<strong>输入：</strong>cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
<strong>输出：</strong>6
<strong>解释：</strong>最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= cost.length &lt;= 1000</code></li>
	<li><code>0 &lt;= cost[i] &lt;= 999</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 746&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/min-cost-climbing-stairs/">https://leetcode-cn.com/problems/min-cost-climbing-stairs/</a></p>


## 难度

Easy

## 标签

- 数组
- 动态规划

## 示例

```
[10,15,20]
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


int minCostClimbingStairs(int* cost, int costSize){

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

