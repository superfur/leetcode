# 1599. 经营摩天轮的最大利润

## 题目描述

<p>你正在经营一座摩天轮，该摩天轮共有 <strong>4 个座舱</strong> ，每个座舱<strong> 最多可以容纳 4 位游客</strong> 。你可以 <strong>逆时针</strong>&nbsp;轮转座舱，但每次轮转都需要支付一定的运行成本 <code>runningCost</code> 。</p>

<p>给你一个长度为 <code>n</code> 的数组 <code>customers</code> ， <code>customers[i]</code> 是在第 <code>i</code> 次轮转（下标从 0 开始）之前到达的新游客的数量。这也意味着你必须在新游客到来前轮转 <code>i</code> 次。<strong>如果有座舱空闲就不能让游客等待。</strong>每位游客在登上离地面最近的座舱前都会支付登舱成本 <code>boardingCost</code> ，一旦该座舱再次抵达地面，他们就会离开座舱结束游玩。</p>

<p>你可以随时停下摩天轮，即便是 <strong>在服务所有游客之前</strong> 。如果你决定停止运营摩天轮，为了保证所有游客安全着陆，<strong>将免费进行</strong><strong>所有后续轮转</strong>&nbsp;。注意，如果有超过 4 位游客在等摩天轮，那么只有 4 位游客可以登上摩天轮，其余的需要等待 <strong>下一次轮转</strong> 。</p>

<p>返回最大化利润所需执行的 <strong>最小轮转次数</strong> 。 如果不存在利润为正的方案，则返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/wheeldiagram12.png" /></p>

<pre>
<strong>输入：</strong>customers = [8,3], boardingCost = 5, runningCost = 6
<strong>输出：</strong>3
<strong>解释：</strong>座舱上标注的数字是该座舱的当前游客数。
1. 8 位游客抵达，4 位登舱，4 位等待下一舱，摩天轮轮转。当前利润为 4 * $5 - 1 * $6 = $14 。
2. 3 位游客抵达，4 位在等待的游客登舱，其他 3 位等待，摩天轮轮转。当前利润为 8 * $5 - 2 * $6 = $28 。
3. 最后 3 位游客登舱，摩天轮轮转。当前利润为 11 * $5 - 3 * $6 = $37 。
轮转 3 次得到最大利润，最大利润为 $37 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>customers = [10,9,6], boardingCost = 6, runningCost = 4
<strong>输出：</strong>7
<strong>解释：</strong>
1. 10 位游客抵达，4 位登舱，6 位等待下一舱，摩天轮轮转。当前利润为 4 * $6 - 1 * $4 = $20 。
2. 9 位游客抵达，4 位登舱，11 位等待（2 位是先前就在等待的，9 位新加入等待的），摩天轮轮转。当前利润为 8 * $6 - 2 * $4 = $40 。
3. 最后 6 位游客抵达，4 位登舱，13 位等待，摩天轮轮转。当前利润为 12 * $6 - 3 * $4 = $60 。
4. 4 位登舱，9 位等待，摩天轮轮转。当前利润为 * $6 - 4 * $4 = $80 。
5. 4 位登舱，5 位等待，摩天轮轮转。当前利润为 20 * $6 - 5 * $4 = $100 。
6. 4 位登舱，1 位等待，摩天轮轮转。当前利润为 24 * $6 - 6 * $4 = $120 。
7. 1 位登舱，摩天轮轮转。当前利润为 25 * $6 - 7 * $4 = $122 。
轮转 7 次得到最大利润，最大利润为$122 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92
<strong>输出：</strong>-1
<strong>解释：</strong>
1. 3 位游客抵达，3 位登舱，0 位等待，摩天轮轮转。当前利润为 3 * $1 - 1 * $92 = -$89 。
2. 4 位游客抵达，4 位登舱，0 位等待，摩天轮轮转。当前利润为 7 * $1 - 2 * $92 = -$177 。
3. 0 位游客抵达，0 位登舱，0 位等待，摩天轮轮转。当前利润为 7 * $1 - 3 * $92 = -$269 。
4. 5 位游客抵达，4 位登舱，1 位等待，摩天轮轮转。当前利润为 11 * $1 - 4 * $92 = -$357 。
5. 1 位游客抵达，2 位登舱，0 位等待，摩天轮轮转。当前利润为 13 * $1 - 5 * $92 = -$447 。
利润永不为正，所以返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == customers.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= customers[i] &lt;= 50</code></li>
	<li><code>1 &lt;= boardingCost, runningCost &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 模拟

## 提示

1. Think simulation
2. Note that the number of turns will never be more than 50 / 4 * n

## 示例

```
[8,3]
5
6
[10,9,6]
6
4
[3,4,0,5,1]
1
92
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost, int runningCost) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
```

### C

```c
int minOperationsMaxProfit(int* customers, int customersSize, int boardingCost, int runningCost) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} customers
 * @param {number} boardingCost
 * @param {number} runningCost
 * @return {number}
 */
var minOperationsMaxProfit = function(customers, boardingCost, runningCost) {
    
};
```

### TypeScript

```typescript
function minOperationsMaxProfit(customers: number[], boardingCost: number, runningCost: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $customers
     * @param Integer $boardingCost
     * @param Integer $runningCost
     * @return Integer
     */
    function minOperationsMaxProfit($customers, $boardingCost, $runningCost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperationsMaxProfit(_ customers: [Int], _ boardingCost: Int, _ runningCost: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperationsMaxProfit(customers: IntArray, boardingCost: Int, runningCost: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperationsMaxProfit(List<int> customers, int boardingCost, int runningCost) {
    
  }
}
```

### Go

```golang
func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} customers
# @param {Integer} boarding_cost
# @param {Integer} running_cost
# @return {Integer}
def min_operations_max_profit(customers, boarding_cost, running_cost)
    
end
```

### Scala

```scala
object Solution {
    def minOperationsMaxProfit(customers: Array[Int], boardingCost: Int, runningCost: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations_max_profit(customers: Vec<i32>, boarding_cost: i32, running_cost: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations-max-profit customers boardingCost runningCost)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations_max_profit(Customers :: [integer()], BoardingCost :: integer(), RunningCost :: integer()) -> integer().
min_operations_max_profit(Customers, BoardingCost, RunningCost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations_max_profit(customers :: [integer], boarding_cost :: integer, running_cost :: integer) :: integer
  def min_operations_max_profit(customers, boarding_cost, running_cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperationsMaxProfit(customers: Array<Int64>, boardingCost: Int64, runningCost: Int64): Int64 {

    }
}
```

