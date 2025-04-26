# 2106. 摘水果

## 题目描述

<p>在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。给你一个二维整数数组 <code>fruits</code> ，其中 <code>fruits[i] = [position<sub>i</sub>, amount<sub>i</sub>]</code> 表示共有 <code>amount<sub>i</sub></code> 个水果放置在 <code>position<sub>i</sub></code> 上。<code>fruits</code> 已经按 <code>position<sub>i</sub></code> <strong>升序排列</strong> ，每个 <code>position<sub>i</sub></code> <strong>互不相同</strong> 。</p>

<p>另给你两个整数 <code>startPos</code> 和 <code>k</code> 。最初，你位于 <code>startPos</code> 。从任何位置，你可以选择 <strong>向左或者向右</strong> 走。在 x 轴上每移动 <strong>一个单位</strong> ，就记作 <strong>一步</strong> 。你总共可以走 <strong>最多</strong> <code>k</code> 步。你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。</p>

<p>返回你可以摘到水果的 <strong>最大总数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/21/1.png" style="width: 472px; height: 115px;">
<pre><strong>输入：</strong>fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
<strong>输出：</strong>9
<strong>解释：</strong>
最佳路线为：
- 向右移动到位置 6 ，摘到 3 个水果
- 向右移动到位置 8 ，摘到 6 个水果
移动 3 步，共摘到 3 + 6 = 9 个水果
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/21/2.png" style="width: 512px; height: 129px;">
<pre><strong>输入：</strong>fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
<strong>输出：</strong>14
<strong>解释：</strong>
可以移动最多 k = 4 步，所以无法到达位置 0 和位置 10 。
最佳路线为：
- 在初始位置 5 ，摘到 7 个水果
- 向左移动到位置 4 ，摘到 1 个水果
- 向右移动到位置 6 ，摘到 2 个水果
- 向右移动到位置 7 ，摘到 4 个水果
移动 1 + 3 = 4 步，共摘到 7 + 1 + 2 + 4 = 14 个水果
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/21/3.png" style="width: 476px; height: 100px;">
<pre><strong>输入：</strong>fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
<strong>输出：</strong>0
<strong>解释：</strong>
最多可以移动 k = 2 步，无法到达任一有水果的地方
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= fruits.length &lt;= 10<sup>5</sup></code></li>
	<li><code>fruits[i].length == 2</code></li>
	<li><code>0 &lt;= startPos, position<sub>i</sub> &lt;= 2 * 10<sup>5</sup></code></li>
	<li>对于任意 <code>i &gt; 0</code> ，<code>position<sub>i-1</sub> &lt; position<sub>i</sub></code> 均成立（下标从 <strong>0</strong> 开始计数）</li>
	<li><code>1 &lt;= amount<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 前缀和
- 滑动窗口

## 提示

1. Does an optimal path have very few patterns? For example, could a path that goes left, turns and goes right, then turns again and goes left be any better than a path that simply goes left, turns, and goes right?
2. The optimal path turns at most once. That is, the optimal path is one of these: to go left only; to go right only; to go left, turn and go right; or to go right, turn and go left.
3. Moving x steps left then k-x steps right gives you a range of positions that you can reach.
4. Use prefix sums to get the sum of all fruits for each possible range.
5. Use a similar strategy for all the paths that go right, then turn and go left.

## 示例

```
[[2,8],[6,3],[8,6]]
5
4
[[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
5
4
[[0,3],[6,4],[8,5]]
3
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
```

### C

```c
int maxTotalFruits(int** fruits, int fruitsSize, int* fruitsColSize, int startPos, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxTotalFruits(int[][] fruits, int startPos, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} fruits
 * @param {number} startPos
 * @param {number} k
 * @return {number}
 */
var maxTotalFruits = function(fruits, startPos, k) {
    
};
```

### TypeScript

```typescript
function maxTotalFruits(fruits: number[][], startPos: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $fruits
     * @param Integer $startPos
     * @param Integer $k
     * @return Integer
     */
    function maxTotalFruits($fruits, $startPos, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxTotalFruits(_ fruits: [[Int]], _ startPos: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxTotalFruits(fruits: Array<IntArray>, startPos: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxTotalFruits(List<List<int>> fruits, int startPos, int k) {
    
  }
}
```

### Go

```golang
func maxTotalFruits(fruits [][]int, startPos int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} fruits
# @param {Integer} start_pos
# @param {Integer} k
# @return {Integer}
def max_total_fruits(fruits, start_pos, k)
    
end
```

### Scala

```scala
object Solution {
    def maxTotalFruits(fruits: Array[Array[Int]], startPos: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_total_fruits(fruits: Vec<Vec<i32>>, start_pos: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-total-fruits fruits startPos k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_total_fruits(Fruits :: [[integer()]], StartPos :: integer(), K :: integer()) -> integer().
max_total_fruits(Fruits, StartPos, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_total_fruits(fruits :: [[integer]], start_pos :: integer, k :: integer) :: integer
  def max_total_fruits(fruits, start_pos, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxTotalFruits(fruits: Array<Array<Int64>>, startPos: Int64, k: Int64): Int64 {

    }
}
```

