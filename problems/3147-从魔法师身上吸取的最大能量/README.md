# 3147. 从魔法师身上吸取的最大能量

## 题目描述

<p>在神秘的地牢中，<code>n</code> 个魔法师站成一排。每个魔法师都拥有一个属性，这个属性可以给你提供能量。有些魔法师可能会给你负能量，即从你身上吸取能量。</p>

<p>你被施加了一种诅咒，当你从魔法师 <code>i</code> 处吸收能量后，你将被立即传送到魔法师 <code>(i + k)</code> 处。这一过程将重复进行，直到你到达一个不存在 <code>(i + k)</code> 的魔法师为止。</p>

<p>换句话说，你将选择一个起点，然后以 <code>k</code> 为间隔跳跃，直到到达魔法师序列的末端，<strong>在过程中吸收所有的能量</strong>。</p>

<p>给定一个数组 <code>energy</code> 和一个整数<code>k</code>，返回你能获得的<strong> 最大 </strong>能量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>输入：</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> energy = [5,2,-10,-5,1], k = 3</span></p>

<p><strong>输出：</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> 3</span></p>

<p><strong>解释：</strong>可以从魔法师 1 开始，吸收能量 2 + 1 = 3。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>输入：</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> energy = [-2,-3,-1], k = 2</span></p>

<p><strong>输出：</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> -1</span></p>

<p><strong>解释：</strong>可以从魔法师 2 开始，吸收能量 -1。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= energy.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-1000 &lt;= energy[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= energy.length - 1</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. Let <code>dp[i]</code> denote the energy we gain starting from index <code>i</code>.
2. We can notice, that <code> dp[i] = dp[i + k] + energy[i]</code>.

## 示例

```
[5,2,-10,-5,1]
3
[-2,-3,-1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumEnergy(int[] energy, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
```

### C

```c
int maximumEnergy(int* energy, int energySize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumEnergy(int[] energy, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} energy
 * @param {number} k
 * @return {number}
 */
var maximumEnergy = function(energy, k) {
    
};
```

### TypeScript

```typescript
function maximumEnergy(energy: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $energy
     * @param Integer $k
     * @return Integer
     */
    function maximumEnergy($energy, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumEnergy(_ energy: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumEnergy(energy: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumEnergy(List<int> energy, int k) {
    
  }
}
```

### Go

```golang
func maximumEnergy(energy []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} energy
# @param {Integer} k
# @return {Integer}
def maximum_energy(energy, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumEnergy(energy: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_energy(energy: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-energy energy k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_energy(Energy :: [integer()], K :: integer()) -> integer().
maximum_energy(Energy, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_energy(energy :: [integer], k :: integer) :: integer
  def maximum_energy(energy, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumEnergy(energy: Array<Int64>, k: Int64): Int64 {

    }
}
```

