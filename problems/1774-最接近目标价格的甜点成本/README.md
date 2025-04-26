# 1774. 最接近目标价格的甜点成本

## 题目描述

<p>你打算做甜点，现在需要购买配料。目前共有 <code>n</code> 种冰激凌基料和 <code>m</code> 种配料可供选购。而制作甜点需要遵循以下几条规则：</p>

<ul>
	<li>必须选择 <strong>一种</strong> 冰激凌基料。</li>
	<li>可以添加 <strong>一种或多种</strong> 配料，也可以不添加任何配料。</li>
	<li>每种类型的配料 <strong>最多两份</strong> 。</li>
</ul>

<p>给你以下三个输入：</p>

<ul>
	<li><code>baseCosts</code> ，一个长度为 <code>n</code> 的整数数组，其中每个 <code>baseCosts[i]</code> 表示第 <code>i</code> 种冰激凌基料的价格。</li>
	<li><code>toppingCosts</code>，一个长度为 <code>m</code> 的整数数组，其中每个 <code>toppingCosts[i]</code> 表示 <strong>一份</strong> 第 <code>i</code> 种冰激凌配料的价格。</li>
	<li><code>target</code> ，一个整数，表示你制作甜点的目标价格。</li>
</ul>

<p>你希望自己做的甜点总成本尽可能接近目标价格 <code>target</code> 。</p>

<p>返回最接近<em> </em><code>target</code> 的甜点成本。如果有多种方案，返回 <strong>成本相对较低</strong> 的一种。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>baseCosts = [1,7], toppingCosts = [3,4], target = 10
<strong>输出：</strong>10
<strong>解释：</strong>考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 7
- 选择 1 份 0 号配料：成本 1 x 3 = 3
- 选择 0 份 1 号配料：成本 0 x 4 = 0
总成本：7 + 3 + 0 = 10 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
<strong>输出：</strong>17
<strong>解释：</strong>考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 3
- 选择 1 份 0 号配料：成本 1 x 4 = 4
- 选择 2 份 1 号配料：成本 2 x 5 = 10
- 选择 0 份 2 号配料：成本 0 x 100 = 0
总成本：3 + 4 + 10 + 0 = 17 。不存在总成本为 18 的甜点制作方案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>baseCosts = [3,10], toppingCosts = [2,5], target = 9
<strong>输出：</strong>8
<strong>解释：</strong>可以制作总成本为 8 和 10 的甜点。返回 8 ，因为这是成本更低的方案。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>baseCosts = [10], toppingCosts = [1], target = 1
<strong>输出：</strong>10
<strong>解释：</strong>注意，你可以选择不添加任何配料，但你必须选择一种基料。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == baseCosts.length</code></li>
	<li><code>m == toppingCosts.length</code></li>
	<li><code>1 <= n, m <= 10</code></li>
	<li><code>1 <= baseCosts[i], toppingCosts[i] <= 10<sup>4</sup></code></li>
	<li><code>1 <= target <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 回溯

## 提示

1. As the constraints are not large, you can brute force and enumerate all the possibilities.

## 示例

```
[1,7]
[3,4]
10
[2,3]
[4,5,100]
18
[3,10]
[2,5]
9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int closestCost(int[] baseCosts, int[] toppingCosts, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
```

### C

```c
int closestCost(int* baseCosts, int baseCostsSize, int* toppingCosts, int toppingCostsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int ClosestCost(int[] baseCosts, int[] toppingCosts, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} baseCosts
 * @param {number[]} toppingCosts
 * @param {number} target
 * @return {number}
 */
var closestCost = function(baseCosts, toppingCosts, target) {
    
};
```

### TypeScript

```typescript
function closestCost(baseCosts: number[], toppingCosts: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $baseCosts
     * @param Integer[] $toppingCosts
     * @param Integer $target
     * @return Integer
     */
    function closestCost($baseCosts, $toppingCosts, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closestCost(_ baseCosts: [Int], _ toppingCosts: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closestCost(baseCosts: IntArray, toppingCosts: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int closestCost(List<int> baseCosts, List<int> toppingCosts, int target) {
    
  }
}
```

### Go

```golang
func closestCost(baseCosts []int, toppingCosts []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} base_costs
# @param {Integer[]} topping_costs
# @param {Integer} target
# @return {Integer}
def closest_cost(base_costs, topping_costs, target)
    
end
```

### Scala

```scala
object Solution {
    def closestCost(baseCosts: Array[Int], toppingCosts: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn closest_cost(base_costs: Vec<i32>, topping_costs: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (closest-cost baseCosts toppingCosts target)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec closest_cost(BaseCosts :: [integer()], ToppingCosts :: [integer()], Target :: integer()) -> integer().
closest_cost(BaseCosts, ToppingCosts, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec closest_cost(base_costs :: [integer], topping_costs :: [integer], target :: integer) :: integer
  def closest_cost(base_costs, topping_costs, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closestCost(baseCosts: Array<Int64>, toppingCosts: Array<Int64>, target: Int64): Int64 {

    }
}
```

