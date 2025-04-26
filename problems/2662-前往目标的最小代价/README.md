# 2662. 前往目标的最小代价

## 题目描述

<p>给你一个数组 <code>start</code> ，其中 <code>start = [startX, startY]</code> 表示你的初始位置位于二维空间上的 <code>(startX, startY)</code> 。另给你一个数组 <code>target</code> ，其中 <code>target = [targetX, targetY]</code> 表示你的目标位置 <code>(targetX, targetY)</code> 。</p>

<p>从位置 <code>(x1, y1)</code> 到空间中任一其他位置 <code>(x2, y2)</code> 的 <strong>代价</strong> 是 <code>|x2 - x1| + |y2 - y1|</code> 。</p>

<p>给你一个二维数组 <code>specialRoads</code> ，表示空间中存在的一些 <strong>特殊路径</strong>。其中 <code>specialRoads[i] = [x1<sub>i</sub>, y1<sub>i</sub>, x2<sub>i</sub>, y2<sub>i</sub>, cost<sub>i</sub>]</code> 表示第 <code>i</code> 条特殊路径可以从 <code>(x1<sub>i</sub>, y1<sub>i</sub>)</code> 到 <code>(x2<sub>i</sub>, y2<sub>i</sub>)</code> ，但成本等于 <code>cost<sub>i</sub></code> 。你可以使用每条特殊路径任意次数。</p>

<p>返回从 <code>(startX, startY)</code> 到 <code>(targetX, targetY)</code> 所需的 <strong>最小</strong> 代价。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><b>解释：</b></p>

<ol>
	<li>(1,1) 到 (1,2) 花费为 |1 - 1| + |2 - 1| = 1。</li>
	<li>(1,2) 到 (3,3)。使用&nbsp;<code><span class="example-io">specialRoads[0]</span></code><span class="example-io">&nbsp;花费为</span><span class="example-io">&nbsp;2。</span></li>
	<li><span class="example-io">(3,3) </span>到<span class="example-io"> (3,4) </span>花费为<span class="example-io"> |3 - 3| + |4 - 3| = 1。</span></li>
	<li><span class="example-io">(3,4) </span>到<span class="example-io"> (4,5)。</span>使用<span class="example-io"> </span><code><span class="example-io">specialRoads[1]</span></code><span class="example-io"> 花费为</span><span class="example-io"> 1。</span></li>
</ol>

<p><span class="example-io">所以总花费是 1 + 2 + 1 + 1 = 5。</span></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">7</span></p>

<p><b>解释：</b></p>

<p>不使用任何特殊路径，直接从开始到结束位置是最优的，花费为&nbsp;|5 - 3| + |7 - 2| = 7。</p>

<p>注意&nbsp;<span class="example-io"><code>specialRoads[0]</code>&nbsp;直接从 (5,7) 到 (3,2)。</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">8</span></p>

<p><b>解释：</b></p>

<ol>
	<li>(1,1) 到 (1,2) 花费为 |1 - 1| + |2 - 1| = 1。</li>
	<li>(1,2) 到 (7,4)。使用&nbsp;<code><span class="example-io">specialRoads[1]</span></code><span class="example-io">&nbsp;花费为</span><span class="example-io">&nbsp;4。</span></li>
	<li>(7,4) 到 (10,4) 花费为 |10 - 7| + |4 - 4| = 3。</li>
</ol>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>start.length == target.length == 2</code></li>
	<li><code>1 &lt;= startX &lt;= targetX &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= startY &lt;= targetY &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= specialRoads.length &lt;= 200</code></li>
	<li><code>specialRoads[i].length == 5</code></li>
	<li><code>startX &lt;= x1<sub>i</sub>, x2<sub>i</sub> &lt;= targetX</code></li>
	<li><code>startY &lt;= y1<sub>i</sub>, y2<sub>i</sub> &lt;= targetY</code></li>
	<li><code>1 &lt;= cost<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 图
- 数组
- 最短路
- 堆（优先队列）

## 提示

1. It can be proven that it is optimal to go only to the positions that are either the start or the end of a special road or the target position.
2. Consider all positions given to you as nodes in a graph, and the edges of the graph are the special roads.
3. Now the problem is equivalent to finding the shortest path in a directed graph.

## 示例

```
[1,1]
[4,5]
[[1,2,3,3,2],[3,4,4,5,1]]
[3,2]
[5,7]
[[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
[1,1]
[10,4]
[[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumCost(vector<int>& start, vector<int>& target, vector<vector<int>>& specialRoads) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumCost(int[] start, int[] target, int[][] specialRoads) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        
```

### C

```c
int minimumCost(int* start, int startSize, int* target, int targetSize, int** specialRoads, int specialRoadsSize, int* specialRoadsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumCost(int[] start, int[] target, int[][] specialRoads) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} start
 * @param {number[]} target
 * @param {number[][]} specialRoads
 * @return {number}
 */
var minimumCost = function(start, target, specialRoads) {
    
};
```

### TypeScript

```typescript
function minimumCost(start: number[], target: number[], specialRoads: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $start
     * @param Integer[] $target
     * @param Integer[][] $specialRoads
     * @return Integer
     */
    function minimumCost($start, $target, $specialRoads) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ start: [Int], _ target: [Int], _ specialRoads: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(start: IntArray, target: IntArray, specialRoads: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(List<int> start, List<int> target, List<List<int>> specialRoads) {
    
  }
}
```

### Go

```golang
func minimumCost(start []int, target []int, specialRoads [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} start
# @param {Integer[]} target
# @param {Integer[][]} special_roads
# @return {Integer}
def minimum_cost(start, target, special_roads)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(start: Array[Int], target: Array[Int], specialRoads: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(start: Vec<i32>, target: Vec<i32>, special_roads: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost start target specialRoads)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Start :: [integer()], Target :: [integer()], SpecialRoads :: [[integer()]]) -> integer().
minimum_cost(Start, Target, SpecialRoads) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(start :: [integer], target :: [integer], special_roads :: [[integer]]) :: integer
  def minimum_cost(start, target, special_roads) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(start: Array<Int64>, target: Array<Int64>, specialRoads: Array<Array<Int64>>): Int64 {

    }
}
```

