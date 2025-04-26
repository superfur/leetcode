# 2477. 到达首都的最少油耗

## 题目描述

<p>给你一棵 <code>n</code>&nbsp;个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，且恰好有&nbsp;<code>n - 1</code>&nbsp;条路。<code>0</code>&nbsp;是首都。给你一个二维整数数组&nbsp;<code>roads</code>&nbsp;，其中&nbsp;<code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;，表示城市&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条&nbsp;<strong>双向路</strong>&nbsp;。</p>

<p>每个城市里有一个代表，他们都要去首都参加一个会议。</p>

<p>每座城市里有一辆车。给你一个整数&nbsp;<code>seats</code>&nbsp;表示每辆车里面座位的数目。</p>

<p>城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。</p>

<p>请你返回到达首都最少需要多少升汽油。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/09/22/a4c380025e3ff0c379525e96a7d63a3.png" style="width: 303px; height: 332px;"></p>

<pre><b>输入：</b>roads = [[0,1],[0,2],[0,3]], seats = 5
<b>输出：</b>3
<b>解释：</b>
- 代表 1 直接到达首都，消耗 1 升汽油。
- 代表 2 直接到达首都，消耗 1 升汽油。
- 代表 3 直接到达首都，消耗 1 升汽油。
最少消耗 3 升汽油。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/16/2.png" style="width: 274px; height: 340px;"></p>

<pre><b>输入：</b>roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
<b>输出：</b>7
<b>解释：</b>
- 代表 2 到达城市 3 ，消耗 1 升汽油。
- 代表 2 和代表 3 一起到达城市 1 ，消耗 1 升汽油。
- 代表 2 和代表 3 一起到达首都，消耗 1 升汽油。
- 代表 1 直接到达首都，消耗 1 升汽油。
- 代表 5 直接到达首都，消耗 1 升汽油。
- 代表 6 到达城市 4 ，消耗 1 升汽油。
- 代表 4 和代表 6 一起到达首都，消耗 1 升汽油。
最少消耗 7 升汽油。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/09/27/efcf7f7be6830b8763639cfd01b690a.png" style="width: 108px; height: 86px;"></p>

<pre><b>输入：</b>roads = [], seats = 1
<b>输出：</b>0
<b>解释：</b>没有代表需要从别的城市到达首都。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>roads.length == n - 1</code></li>
	<li><code>roads[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>roads</code>&nbsp;表示一棵合法的树。</li>
	<li><code>1 &lt;= seats &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 图

## 提示

1. Can you record the size of each subtree?
2. If n people meet on the same node, what is the minimum number of cars needed?

## 示例

```
[[0,1],[0,2],[0,3]]
5
[[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
2
[]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumFuelCost(int[][] roads, int seats) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
```

### C

```c
long long minimumFuelCost(int** roads, int roadsSize, int* roadsColSize, int seats) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumFuelCost(int[][] roads, int seats) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function(roads, seats) {
    
};
```

### TypeScript

```typescript
function minimumFuelCost(roads: number[][], seats: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $roads
     * @param Integer $seats
     * @return Integer
     */
    function minimumFuelCost($roads, $seats) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumFuelCost(_ roads: [[Int]], _ seats: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumFuelCost(roads: Array<IntArray>, seats: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumFuelCost(List<List<int>> roads, int seats) {
    
  }
}
```

### Go

```golang
func minimumFuelCost(roads [][]int, seats int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} roads
# @param {Integer} seats
# @return {Integer}
def minimum_fuel_cost(roads, seats)
    
end
```

### Scala

```scala
object Solution {
    def minimumFuelCost(roads: Array[Array[Int]], seats: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_fuel_cost(roads: Vec<Vec<i32>>, seats: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-fuel-cost roads seats)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_fuel_cost(Roads :: [[integer()]], Seats :: integer()) -> integer().
minimum_fuel_cost(Roads, Seats) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_fuel_cost(roads :: [[integer]], seats :: integer) :: integer
  def minimum_fuel_cost(roads, seats) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumFuelCost(roads: Array<Array<Int64>>, seats: Int64): Int64 {

    }
}
```

