# 3259. 超级饮料的最大强化能量

## 题目描述

<p>来自未来的体育科学家给你两个整数数组 <code>energyDrinkA</code> 和 <code>energyDrinkB</code>，数组长度都等于 <code>n</code>。这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。</p>

<p>你需要每小时饮用一种能量饮料来 <strong>最大化 </strong>你的总强化能量。然而，如果从一种能量饮料切换到另一种，你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。</p>

<p>返回在接下来的 <code>n</code> 小时内你能获得的<strong> 最大 </strong>总强化能量。</p>

<p><strong>注意 </strong>你可以选择从饮用任意一种能量饮料开始。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>energyDrinkA<span class="example-io"> = [1,3,1], </span>energyDrinkB<span class="example-io"> = [3,1,1]</span></p>

<p><strong>输出：</strong><span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>要想获得 5 点强化能量，需要选择只饮用能量饮料 A（或者只饮用 B）。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>energyDrinkA<span class="example-io"> = [4,1,1], </span>energyDrinkB<span class="example-io"> = [1,1,3]</span></p>

<p><strong>输出：</strong><span class="example-io">7</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第一个小时饮用能量饮料 A。</li>
	<li>切换到能量饮料 B ，在第二个小时无法获得强化能量。</li>
	<li>第三个小时饮用能量饮料 B ，并获得强化能量。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == energyDrinkA.length == energyDrinkB.length</code></li>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= energyDrinkA[i], energyDrinkB[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Can we solve it using dynamic programming?
2. Define <code>dpA[i]</code> as the maximum energy boost if we consider only the first <code>i + 1</code> hours such that in the last hour, we drink the energy drink A.
3. Similarly define <code>dpB[i]</code>.
4. <code>dpA[i] = max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i]</code>
5. Similarly, fill <code>dpB</code>.
6. The answer is <code>max(dpA[n - 1], dpB[n - 1])</code>.

## 示例

```
[1,3,1]
[3,1,1]
[4,1,1]
[1,1,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxEnergyBoost(vector<int>& energyDrinkA, vector<int>& energyDrinkB) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxEnergyBoost(int[] energyDrinkA, int[] energyDrinkB) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
```

### C

```c
long long maxEnergyBoost(int* energyDrinkA, int energyDrinkASize, int* energyDrinkB, int energyDrinkBSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxEnergyBoost(int[] energyDrinkA, int[] energyDrinkB) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} energyDrinkA
 * @param {number[]} energyDrinkB
 * @return {number}
 */
var maxEnergyBoost = function(energyDrinkA, energyDrinkB) {
    
};
```

### TypeScript

```typescript
function maxEnergyBoost(energyDrinkA: number[], energyDrinkB: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $energyDrinkA
     * @param Integer[] $energyDrinkB
     * @return Integer
     */
    function maxEnergyBoost($energyDrinkA, $energyDrinkB) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxEnergyBoost(_ energyDrinkA: [Int], _ energyDrinkB: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxEnergyBoost(energyDrinkA: IntArray, energyDrinkB: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxEnergyBoost(List<int> energyDrinkA, List<int> energyDrinkB) {
    
  }
}
```

### Go

```golang
func maxEnergyBoost(energyDrinkA []int, energyDrinkB []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} energy_drink_a
# @param {Integer[]} energy_drink_b
# @return {Integer}
def max_energy_boost(energy_drink_a, energy_drink_b)
    
end
```

### Scala

```scala
object Solution {
    def maxEnergyBoost(energyDrinkA: Array[Int], energyDrinkB: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_energy_boost(energy_drink_a: Vec<i32>, energy_drink_b: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-energy-boost energyDrinkA energyDrinkB)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_energy_boost(EnergyDrinkA :: [integer()], EnergyDrinkB :: [integer()]) -> integer().
max_energy_boost(EnergyDrinkA, EnergyDrinkB) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_energy_boost(energy_drink_a :: [integer], energy_drink_b :: [integer]) :: integer
  def max_energy_boost(energy_drink_a, energy_drink_b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxEnergyBoost(energyDrinkA: Array<Int64>, energyDrinkB: Array<Int64>): Int64 {

    }
}
```

