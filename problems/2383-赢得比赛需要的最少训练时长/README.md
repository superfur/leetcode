# 2383. 赢得比赛需要的最少训练时长

## 题目描述

<p>你正在参加一场比赛，给你两个 <strong>正</strong> 整数 <code>initialEnergy</code> 和 <code>initialExperience</code> 分别表示你的初始精力和初始经验。</p>

<p>另给你两个下标从 <strong>0</strong> 开始的整数数组 <code>energy</code> 和 <code>experience</code>，长度均为 <code>n</code> 。</p>

<p>你将会 <strong>依次</strong> 对上 <code>n</code> 个对手。第 <code>i</code> 个对手的精力和经验分别用 <code>energy[i]</code> 和 <code>experience[i]</code> 表示。当你对上对手时，需要在经验和精力上都 <strong>严格</strong> 超过对手才能击败他们，然后在可能的情况下继续对上下一个对手。</p>

<p>击败第 <code>i</code> 个对手会使你的经验 <strong>增加</strong> <code>experience[i]</code>，但会将你的精力 <strong>减少</strong>&nbsp; <code>energy[i]</code> 。</p>

<p>在开始比赛前，你可以训练几个小时。每训练一个小时，你可以选择将增加经验增加 1 <strong>或者</strong> 将精力增加 1 。</p>

<p>返回击败全部 <code>n</code> 个对手需要训练的 <strong>最少</strong> 小时数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]
<strong>输出：</strong>8
<strong>解释：</strong>在 6 小时训练后，你可以将精力提高到 11 ，并且再训练 2 个小时将经验提高到 5 。
按以下顺序与对手比赛：
- 你的精力与经验都超过第 0 个对手，所以获胜。
  精力变为：11 - 1 = 10 ，经验变为：5 + 2 = 7 。
- 你的精力与经验都超过第 1 个对手，所以获胜。
  精力变为：10 - 4 = 6 ，经验变为：7 + 6 = 13 。
- 你的精力与经验都超过第 2 个对手，所以获胜。
  精力变为：6 - 3 = 3 ，经验变为：13 + 3 = 16 。
- 你的精力与经验都超过第 3 个对手，所以获胜。
  精力变为：3 - 2 = 1 ，经验变为：16 + 1 = 17 。
在比赛前进行了 8 小时训练，所以返回 8 。
可以证明不存在更小的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]
<strong>输出：</strong>0
<strong>解释：</strong>你不需要额外的精力和经验就可以赢得比赛，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == energy.length == experience.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= initialEnergy, initialExperience, energy[i], experience[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组

## 提示

1. Find the minimum number of training hours needed for the energy and experience separately, and sum the results.
2. Try to increase the energy and experience until you find how much is enough to win the competition.

## 示例

```
5
3
[1,4,3,2]
[2,6,3,1]
2
4
[1]
[3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        
    }
};
```

### Java

```java
class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
```

### C

```c
int minNumberOfHours(int initialEnergy, int initialExperience, int* energy, int energySize, int* experience, int experienceSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} initialEnergy
 * @param {number} initialExperience
 * @param {number[]} energy
 * @param {number[]} experience
 * @return {number}
 */
var minNumberOfHours = function(initialEnergy, initialExperience, energy, experience) {
    
};
```

### TypeScript

```typescript
function minNumberOfHours(initialEnergy: number, initialExperience: number, energy: number[], experience: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $initialEnergy
     * @param Integer $initialExperience
     * @param Integer[] $energy
     * @param Integer[] $experience
     * @return Integer
     */
    function minNumberOfHours($initialEnergy, $initialExperience, $energy, $experience) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minNumberOfHours(_ initialEnergy: Int, _ initialExperience: Int, _ energy: [Int], _ experience: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minNumberOfHours(initialEnergy: Int, initialExperience: Int, energy: IntArray, experience: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minNumberOfHours(int initialEnergy, int initialExperience, List<int> energy, List<int> experience) {
    
  }
}
```

### Go

```golang
func minNumberOfHours(initialEnergy int, initialExperience int, energy []int, experience []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} initial_energy
# @param {Integer} initial_experience
# @param {Integer[]} energy
# @param {Integer[]} experience
# @return {Integer}
def min_number_of_hours(initial_energy, initial_experience, energy, experience)
    
end
```

### Scala

```scala
object Solution {
    def minNumberOfHours(initialEnergy: Int, initialExperience: Int, energy: Array[Int], experience: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_number_of_hours(initial_energy: i32, initial_experience: i32, energy: Vec<i32>, experience: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-number-of-hours initialEnergy initialExperience energy experience)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_number_of_hours(InitialEnergy :: integer(), InitialExperience :: integer(), Energy :: [integer()], Experience :: [integer()]) -> integer().
min_number_of_hours(InitialEnergy, InitialExperience, Energy, Experience) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_number_of_hours(initial_energy :: integer, initial_experience :: integer, energy :: [integer], experience :: [integer]) :: integer
  def min_number_of_hours(initial_energy, initial_experience, energy, experience) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minNumberOfHours(initialEnergy: Int64, initialExperience: Int64, energy: Array<Int64>, experience: Array<Int64>): Int64 {

    }
}
```

