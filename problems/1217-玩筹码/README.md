# 1217. 玩筹码

## 题目描述

<p>有&nbsp;<code>n</code>&nbsp;个筹码。第 <code>i</code> 个筹码的位置是<meta charset="UTF-8" />&nbsp;<code>position[i]</code>&nbsp;。</p>

<p>我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 <code>i</code> 个筹码的位置从&nbsp;<code>position[i]</code>&nbsp;改变为:</p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li><code>position[i] + 2</code>&nbsp;或&nbsp;<code>position[i] - 2</code>&nbsp;，此时&nbsp;<code>cost = 0</code></li>
	<li><code>position[i] + 1</code>&nbsp;或&nbsp;<code>position[i] - 1</code>&nbsp;，此时&nbsp;<code>cost = 1</code></li>
</ul>

<p>返回将所有筹码移动到同一位置上所需要的 <em>最小代价</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg" style="height: 217px; width: 750px;" /></p>

<pre>
<strong>输入：</strong>position = [1,2,3]
<strong>输出：</strong>1
<strong>解释：</strong>第一步:将位置3的筹码移动到位置1，成本为0。
第二步:将位置2的筹码移动到位置1，成本= 1。
总成本是1。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg" style="height: 306px; width: 750px;" /></p>

<pre>
<strong>输入：</strong>position = [2,2,2,3,3]
<strong>输出：</strong>2
<strong>解释：</strong>我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入：</strong>position = [1,1000000000]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= position.length &lt;= 100</code></li>
	<li><code>1 &lt;= position[i] &lt;= 10^9</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 数学

## 提示

1. The first move keeps the parity of the element as it is.
2. The second move changes the parity of the element.
3. Since the first move is free, if all the numbers have the same parity, the answer would be zero.
4. Find the minimum cost to make all the numbers have the same parity.

## 示例

```
[1,2,3]
[2,2,2,3,3]
[1,1000000000]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCostToMoveChips(int[] position) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
```

### C

```c
int minCostToMoveChips(int* position, int positionSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCostToMoveChips(int[] position) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function(position) {
    
};
```

### TypeScript

```typescript
function minCostToMoveChips(position: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $position
     * @return Integer
     */
    function minCostToMoveChips($position) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCostToMoveChips(_ position: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCostToMoveChips(position: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCostToMoveChips(List<int> position) {
    
  }
}
```

### Go

```golang
func minCostToMoveChips(position []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} position
# @return {Integer}
def min_cost_to_move_chips(position)
    
end
```

### Scala

```scala
object Solution {
    def minCostToMoveChips(position: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost_to_move_chips(position: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost-to-move-chips position)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost_to_move_chips(Position :: [integer()]) -> integer().
min_cost_to_move_chips(Position) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost_to_move_chips(position :: [integer]) :: integer
  def min_cost_to_move_chips(position) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCostToMoveChips(position: Array<Int64>): Int64 {

    }
}
```

