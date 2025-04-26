# 1473. 粉刷房子 III

## 题目描述

<p>在一个小城市里，有 <code>m</code> 个房子排成一排，你需要给每个房子涂上 <code>n</code> 种颜色之一（颜色编号为 <code>1</code> 到 <code>n</code> ）。有的房子去年夏天已经涂过颜色了，所以这些房子不可以被重新涂色。</p>

<p>我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 <code>houses = [1,2,2,3,3,2,1,1]</code> ，它包含 5 个街区 <code> [{1}, {2,2}, {3,3}, {2}, {1,1}]</code> 。）</p>

<p>给你一个数组 <code>houses</code> ，一个 <code>m * n</code> 的矩阵 <code>cost</code> 和一个整数 <code>target</code> ，其中：</p>

<ul>
	<li><code>houses[i]</code>：是第 <code>i</code> 个房子的颜色，<strong>0</strong> 表示这个房子还没有被涂色。</li>
	<li><code>cost[i][j]</code>：是将第 <code>i</code> 个房子涂成颜色 <code>j+1</code> 的花费。</li>
</ul>

<p>请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 <code>target</code> 个街区。如果没有可用的涂色方案，请返回 <strong>-1</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
<strong>输出：</strong>9
<strong>解释：</strong>房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
<strong>输出：</strong>11
<strong>解释：</strong>有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
<strong>输出：</strong>5
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
<strong>输出：</strong>-1
<strong>解释：</strong>房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == houses.length == cost.length</code></li>
	<li><code>n == cost[i].length</code></li>
	<li><code>1 <= m <= 100</code></li>
	<li><code>1 <= n <= 20</code></li>
	<li><code>1 <= target <= m</code></li>
	<li><code>0 <= houses[i] <= n</code></li>
	<li><code>1 <= cost[i][j] <= 10^4</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Use Dynamic programming.
2. Define dp[i][j][k] as the minimum cost where we have k neighborhoods in the first i houses and the i-th house is painted with the color j.

## 示例

```
[0,0,0,0,0]
[[1,10],[10,1],[10,1],[1,10],[5,1]]
5
2
3
[0,2,1,2,0]
[[1,10],[10,1],[10,1],[1,10],[5,1]]
5
2
3
[3,1,2,3]
[[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
4
3
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
```

### C

```c
int minCost(int* houses, int housesSize, int** cost, int costSize, int* costColSize, int m, int n, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCost(int[] houses, int[][] cost, int m, int n, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} houses
 * @param {number[][]} cost
 * @param {number} m
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var minCost = function(houses, cost, m, n, target) {
    
};
```

### TypeScript

```typescript
function minCost(houses: number[], cost: number[][], m: number, n: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $houses
     * @param Integer[][] $cost
     * @param Integer $m
     * @param Integer $n
     * @param Integer $target
     * @return Integer
     */
    function minCost($houses, $cost, $m, $n, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ houses: [Int], _ cost: [[Int]], _ m: Int, _ n: Int, _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(houses: IntArray, cost: Array<IntArray>, m: Int, n: Int, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(List<int> houses, List<List<int>> cost, int m, int n, int target) {
    
  }
}
```

### Go

```golang
func minCost(houses []int, cost [][]int, m int, n int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} houses
# @param {Integer[][]} cost
# @param {Integer} m
# @param {Integer} n
# @param {Integer} target
# @return {Integer}
def min_cost(houses, cost, m, n, target)
    
end
```

### Scala

```scala
object Solution {
    def minCost(houses: Array[Int], cost: Array[Array[Int]], m: Int, n: Int, target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(houses: Vec<i32>, cost: Vec<Vec<i32>>, m: i32, n: i32, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost houses cost m n target)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(Houses :: [integer()], Cost :: [[integer()]], M :: integer(), N :: integer(), Target :: integer()) -> integer().
min_cost(Houses, Cost, M, N, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(houses :: [integer], cost :: [[integer]], m :: integer, n :: integer, target :: integer) :: integer
  def min_cost(houses, cost, m, n, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(houses: Array<Int64>, cost: Array<Array<Int64>>, m: Int64, n: Int64, target: Int64): Int64 {

    }
}
```

