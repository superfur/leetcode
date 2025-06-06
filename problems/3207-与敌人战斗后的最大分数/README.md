# 3207. 与敌人战斗后的最大分数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>enemyEnergies</code>&nbsp;，它表示一个下标从 <strong>0</strong>&nbsp;开始的敌人能量数组。</p>

<p>同时给你一个整数&nbsp;<code>currentEnergy</code>&nbsp;，它表示你一开始拥有的能量值总量。</p>

<p>你一开始的分数为&nbsp;<code>0</code>&nbsp;，且一开始所有的敌人都未标记。</p>

<p>你可以通过以下操作 <b>之一</b>&nbsp;<strong>任意次</strong>（也可以&nbsp;<strong>0</strong>&nbsp;次）来得分：</p>

<ul>
	<li>选择一个 <strong>未标记</strong>&nbsp;且满足&nbsp;<code>currentEnergy &gt;= enemyEnergies[i]</code>&nbsp;的敌人&nbsp;<code>i</code>&nbsp;。在这个操作中：

	<ul>
		<li>你会获得 <code>1</code>&nbsp;分。</li>
		<li>你的能量值减少&nbsp;<code>enemyEnergies[i]</code>&nbsp;，也就是说&nbsp;<code>currentEnergy = currentEnergy - enemyEnergies[i]</code>&nbsp;。</li>
	</ul>
	</li>
	<li>如果你目前&nbsp;<strong>至少</strong>&nbsp;有 <code>1</code>&nbsp;分，你可以选择一个&nbsp;<strong>未标记</strong>&nbsp;的敌人&nbsp;<code>i</code>&nbsp;。在这个操作中：
	<ul>
		<li>你的能量值增加 <code>enemyEnergies[i]</code>&nbsp;，也就是说&nbsp;<code>currentEnergy = currentEnergy + enemyEnergies[i]</code>&nbsp;。</li>
		<li>敌人&nbsp;<code>i</code> <strong>被标记</strong>&nbsp;。</li>
	</ul>
	</li>
</ul>

<p>请你返回通过以上操作，<strong>最多</strong>&nbsp;可以获得多少分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><b>输入：</b>enemyEnergies = [3,2,2], currentEnergy = 2</p>

<p><b>输出：</b>3</p>

<p><strong>解释：</strong></p>

<p>通过以下操作可以得到最大得分 3 分：</p>

<ul>
	<li>对敌人 1 使用第一种操作：<code>points</code>&nbsp;增加 1 ，<code>currentEnergy</code>&nbsp;减少 2 。所以&nbsp;<code>points = 1</code>&nbsp;且&nbsp;<code>currentEnergy = 0</code>&nbsp;。</li>
	<li>对敌人 0 使用第二种操作：<code>currentEnergy</code>&nbsp;增加 3 ，敌人 0 被标记。所以&nbsp;<code>points = 1</code>&nbsp;，<code>currentEnergy = 3</code>&nbsp;，被标记的敌人包括&nbsp;<code>[0]</code>&nbsp;。</li>
	<li>对敌人 2 使用第一种操作：<code>points</code>&nbsp;增加 1 ，<code>currentEnergy</code>&nbsp;减少 2 。所以&nbsp;<code>points = 2</code>&nbsp;且&nbsp;<code>currentEnergy = 1</code>&nbsp;，被标记的敌人包括<code>[0]</code>&nbsp;。</li>
	<li>对敌人 2 使用第二种操作：<code>currentEnergy</code>&nbsp;增加 2 ，敌人 2 被标记。所以&nbsp;<code>points = 2</code>&nbsp;，<code>currentEnergy = 3</code>&nbsp;且被标记的敌人包括&nbsp;<code>[0, 2]</code>&nbsp;。</li>
	<li>对敌人 1 使用第一种操作：<code>points</code>&nbsp;增加 1 ，<code>currentEnergy</code>&nbsp;减少 2 。所以&nbsp;<code>points = 3</code>&nbsp;，<code>currentEnergy = 1</code>&nbsp;，被标记的敌人包括&nbsp;<code>[0, 2]</code>&nbsp;。</li>
</ul>

<p><strong>示例 2：</strong></p>

<p><b>输入：</b>enemyEnergies =&nbsp;[2], currentEnergy = 10</p>

<p><b>输出：</b>5</p>

<p><strong>解释：</strong></p>

<p>通过对敌人 0 进行第一种操作 5 次，得到最大得分。</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= enemyEnergies.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= enemyEnergies[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= currentEnergy &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. The problem can be solved greedily.
2. Mark all the others except the smallest one first.
3. Use the smallest one to increase the energy.
4. Note that the initial energy should be no less than the smallest enemy.

## 示例

```
[3,2,2]
2
[2]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumPoints(vector<int>& enemyEnergies, int currentEnergy) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumPoints(int[] enemyEnergies, int currentEnergy) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumPoints(self, enemyEnergies, currentEnergy):
        """
        :type enemyEnergies: List[int]
        :type currentEnergy: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        
```

### C

```c
long long maximumPoints(int* enemyEnergies, int enemyEnergiesSize, int currentEnergy) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumPoints(int[] enemyEnergies, int currentEnergy) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} enemyEnergies
 * @param {number} currentEnergy
 * @return {number}
 */
var maximumPoints = function(enemyEnergies, currentEnergy) {
    
};
```

### TypeScript

```typescript
function maximumPoints(enemyEnergies: number[], currentEnergy: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $enemyEnergies
     * @param Integer $currentEnergy
     * @return Integer
     */
    function maximumPoints($enemyEnergies, $currentEnergy) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumPoints(_ enemyEnergies: [Int], _ currentEnergy: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumPoints(enemyEnergies: IntArray, currentEnergy: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumPoints(List<int> enemyEnergies, int currentEnergy) {
    
  }
}
```

### Go

```golang
func maximumPoints(enemyEnergies []int, currentEnergy int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} enemy_energies
# @param {Integer} current_energy
# @return {Integer}
def maximum_points(enemy_energies, current_energy)
    
end
```

### Scala

```scala
object Solution {
    def maximumPoints(enemyEnergies: Array[Int], currentEnergy: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_points(enemy_energies: Vec<i32>, current_energy: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-points enemyEnergies currentEnergy)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_points(EnemyEnergies :: [integer()], CurrentEnergy :: integer()) -> integer().
maximum_points(EnemyEnergies, CurrentEnergy) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_points(enemy_energies :: [integer], current_energy :: integer) :: integer
  def maximum_points(enemy_energies, current_energy) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumPoints(enemyEnergies: Array<Int64>, currentEnergy: Int64): Int64 {

    }
}
```

