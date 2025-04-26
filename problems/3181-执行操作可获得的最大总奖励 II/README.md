# 3181. 执行操作可获得的最大总奖励 II

## 题目描述

<p>给你一个整数数组 <code>rewardValues</code>，长度为 <code>n</code>，代表奖励的值。</p>

<p>最初，你的总奖励 <code>x</code> 为 0，所有下标都是<strong> 未标记 </strong>的。你可以执行以下操作 <strong>任意次 </strong>：</p>

<ul>
	<li>从区间 <code>[0, n - 1]</code> 中选择一个 <strong>未标记 </strong>的下标 <code>i</code>。</li>
	<li>如果 <code>rewardValues[i]</code> <strong>大于</strong> 你当前的总奖励 <code>x</code>，则将 <code>rewardValues[i]</code> 加到 <code>x</code> 上（即 <code>x = x + rewardValues[i]</code>），并<strong> 标记</strong> 下标 <code>i</code>。</li>
</ul>

<p>以整数形式返回执行最优操作能够获得的<strong> 最大</strong><em> </em>总奖励。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">rewardValues = [1,1,3,3]</span></p>

<p><strong>输出：</strong><span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">rewardValues = [1,6,4,3,2]</span></p>

<p><strong>输出：</strong><span class="example-io">11</span></p>

<p><strong>解释：</strong></p>

<p>依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rewardValues.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= rewardValues[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划

## 提示

1. Sort the rewards array first.
2. If we decide to apply some rewards, it's always optimal to apply them in order.
3. The transition is given by: <code>dp[i][j] = dp[i - 1][j − rewardValues[i]]</code> if <code>j − rewardValues[i] < rewardValues[i]</code>.
4. Note that the dp array is a boolean array. We just need 1 bit per element, so we can use a bitset or something similar. We just need a "stream" of bits and apply bitwise operations to optimize the computations by a constant factor.

## 示例

```
[1,1,3,3]
[1,6,4,3,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxTotalReward(vector<int>& rewardValues) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxTotalReward(int[] rewardValues) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        
```

### C

```c
int maxTotalReward(int* rewardValues, int rewardValuesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxTotalReward(int[] rewardValues) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rewardValues
 * @return {number}
 */
var maxTotalReward = function(rewardValues) {
    
};
```

### TypeScript

```typescript
function maxTotalReward(rewardValues: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rewardValues
     * @return Integer
     */
    function maxTotalReward($rewardValues) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxTotalReward(_ rewardValues: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxTotalReward(rewardValues: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxTotalReward(List<int> rewardValues) {
    
  }
}
```

### Go

```golang
func maxTotalReward(rewardValues []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} reward_values
# @return {Integer}
def max_total_reward(reward_values)
    
end
```

### Scala

```scala
object Solution {
    def maxTotalReward(rewardValues: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_total_reward(reward_values: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-total-reward rewardValues)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_total_reward(RewardValues :: [integer()]) -> integer().
max_total_reward(RewardValues) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_total_reward(reward_values :: [integer]) :: integer
  def max_total_reward(reward_values) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxTotalReward(rewardValues: Array<Int64>): Int64 {

    }
}
```

