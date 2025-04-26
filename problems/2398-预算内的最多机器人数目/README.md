# 2398. 预算内的最多机器人数目

## 题目描述

<p>你有&nbsp;<code>n</code>&nbsp;个机器人，给你两个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>chargeTimes</code> 和&nbsp;<code>runningCosts</code>&nbsp;，两者长度都为&nbsp;<code>n</code>&nbsp;。第&nbsp;<code>i</code>&nbsp;个机器人充电时间为&nbsp;<code>chargeTimes[i]</code>&nbsp;单位时间，花费&nbsp;<code>runningCosts[i]</code>&nbsp;单位时间运行。再给你一个整数&nbsp;<code>budget</code>&nbsp;。</p>

<p>运行&nbsp;<code>k</code>&nbsp;个机器人 <strong>总开销</strong>&nbsp;是&nbsp;<code>max(chargeTimes) + k * sum(runningCosts)</code>&nbsp;，其中&nbsp;<code>max(chargeTimes)</code>&nbsp;是这&nbsp;<code>k</code>&nbsp;个机器人中最大充电时间，<code>sum(runningCosts)</code>&nbsp;是这 <code>k</code>&nbsp;个机器人的运行时间之和。</p>

<p>请你返回在 <strong>不超过</strong>&nbsp;<code>budget</code>&nbsp;的前提下，你 <strong>最多</strong>&nbsp;可以 <strong>连续</strong>&nbsp;运行的机器人数目为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
<b>输出：</b>3
<b>解释：</b>
可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。
选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于 25 。
可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
<b>输出：</b>0
<b>解释：</b>即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>chargeTimes.length == runningCosts.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= chargeTimes[i], runningCosts[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= budget &lt;= 10<sup>15</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 队列
- 数组
- 二分查找
- 前缀和
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 提示

1. Use binary search to convert the problem into checking if we can find a specific number of consecutive robots within the budget.
2. Maintain a sliding window of the consecutive robots being considered.
3. Use either a map, deque, or heap to find the maximum charge times in the window efficiently.

## 示例

```
[3,6,1,3,4]
[2,1,3,4,5]
25
[11,12,19]
[10,8,7]
19
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumRobots(vector<int>& chargeTimes, vector<int>& runningCosts, long long budget) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
```

### C

```c
int maximumRobots(int* chargeTimes, int chargeTimesSize, int* runningCosts, int runningCostsSize, long long budget) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} chargeTimes
 * @param {number[]} runningCosts
 * @param {number} budget
 * @return {number}
 */
var maximumRobots = function(chargeTimes, runningCosts, budget) {
    
};
```

### TypeScript

```typescript
function maximumRobots(chargeTimes: number[], runningCosts: number[], budget: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $chargeTimes
     * @param Integer[] $runningCosts
     * @param Integer $budget
     * @return Integer
     */
    function maximumRobots($chargeTimes, $runningCosts, $budget) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumRobots(_ chargeTimes: [Int], _ runningCosts: [Int], _ budget: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumRobots(chargeTimes: IntArray, runningCosts: IntArray, budget: Long): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumRobots(List<int> chargeTimes, List<int> runningCosts, int budget) {
    
  }
}
```

### Go

```golang
func maximumRobots(chargeTimes []int, runningCosts []int, budget int64) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} charge_times
# @param {Integer[]} running_costs
# @param {Integer} budget
# @return {Integer}
def maximum_robots(charge_times, running_costs, budget)
    
end
```

### Scala

```scala
object Solution {
    def maximumRobots(chargeTimes: Array[Int], runningCosts: Array[Int], budget: Long): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_robots(charge_times: Vec<i32>, running_costs: Vec<i32>, budget: i64) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-robots chargeTimes runningCosts budget)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_robots(ChargeTimes :: [integer()], RunningCosts :: [integer()], Budget :: integer()) -> integer().
maximum_robots(ChargeTimes, RunningCosts, Budget) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_robots(charge_times :: [integer], running_costs :: [integer], budget :: integer) :: integer
  def maximum_robots(charge_times, running_costs, budget) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumRobots(chargeTimes: Array<Int64>, runningCosts: Array<Int64>, budget: Int64): Int64 {

    }
}
```

