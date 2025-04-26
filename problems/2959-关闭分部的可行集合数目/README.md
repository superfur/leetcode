# 2959. 关闭分部的可行集合数目

## 题目描述

<p>一个公司在全国有 <code>n</code>&nbsp;个分部，它们之间有的有道路连接。一开始，所有分部通过这些道路两两之间互相可以到达。</p>

<p>公司意识到在分部之间旅行花费了太多时间，所以它们决定关闭一些分部（<b>也可能不关闭任何分部</b>），同时保证剩下的分部之间两两互相可以到达且最远距离不超过&nbsp;<code>maxDistance</code>&nbsp;。</p>

<p>两个分部之间的 <strong>距离</strong> 是通过道路长度之和的 <strong>最小值</strong>&nbsp;。</p>

<p>给你整数&nbsp;<code>n</code>&nbsp;，<code>maxDistance</code>&nbsp;和下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>roads</code>&nbsp;，其中&nbsp;<code>roads[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code>&nbsp;表示一条从&nbsp;<code>u<sub>i</sub></code>&nbsp;到&nbsp;<code>v<sub>i</sub></code>&nbsp;长度为&nbsp;<code>w<sub>i</sub></code>的&nbsp;<strong>无向</strong>&nbsp;道路。</p>

<p>请你返回关闭分部的可行方案数目，满足每个方案里剩余分部之间的最远距离不超过<em>&nbsp;</em><code>maxDistance</code>。</p>

<p><strong>注意</strong>，关闭一个分部后，与之相连的所有道路不可通行。</p>

<p><b>注意</b>，两个分部之间可能会有多条道路。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/08/example11.png" style="width: 221px; height: 191px;" /></p>

<pre>
<b>输入：</b>n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]
<b>输出：</b>5
<b>解释：</b>可行的关闭分部方案有：
- 关闭分部集合 [2] ，剩余分部为 [0,1] ，它们之间的距离为 2 。
- 关闭分部集合 [0,1] ，剩余分部为 [2] 。
- 关闭分部集合 [1,2] ，剩余分部为 [0] 。
- 关闭分部集合 [0,2] ，剩余分部为 [1] 。
- 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
总共有 5 种可行的关闭方案。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/08/example22.png" style="width: 221px; height: 241px;" /></p>

<pre>
<b>输入：</b>n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
<b>输出：</b>7
<b>解释：</b>可行的关闭分部方案有：
- 关闭分部集合 [] ，剩余分部为 [0,1,2] ，它们之间的最远距离为 4 。
- 关闭分部集合 [0] ，剩余分部为 [1,2] ，它们之间的距离为 2 。
- 关闭分部集合 [1] ，剩余分部为 [0,2] ，它们之间的距离为 2 。
- 关闭分部集合 [0,1] ，剩余分部为 [2] 。
- 关闭分部集合 [1,2] ，剩余分部为 [0] 。
- 关闭分部集合 [0,2] ，剩余分部为 [1] 。
- 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
总共有 7 种可行的关闭方案。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>n = 1, maxDistance = 10, roads = []
<b>输出：</b>2
<b>解释：</b>可行的关闭分部方案有：
- 关闭分部集合 [] ，剩余分部为 [0] 。
- 关闭分部集合 [0] ，关闭后没有剩余分部。
总共有 2 种可行的关闭方案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= maxDistance &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= roads.length &lt;= 1000</code></li>
	<li><code>roads[i].length == 3</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= 1000</code></li>
	<li>一开始所有分部之间通过道路互相可以到达。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 图
- 枚举
- 最短路
- 堆（优先队列）

## 提示

1. Try all the possibilities of closing branches.
2. On the vertices that are not closed, use Floyd-Warshall algorithm to find the shortest paths.

## 示例

```
3
5
[[0,1,2],[1,2,10],[0,2,10]]
3
5
[[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
1
10
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSets(int n, int maxDistance, vector<vector<int>>& roads) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSets(int n, int maxDistance, int[][] roads) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        
```

### C

```c
int numberOfSets(int n, int maxDistance, int** roads, int roadsSize, int* roadsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSets(int n, int maxDistance, int[][] roads) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} maxDistance
 * @param {number[][]} roads
 * @return {number}
 */
var numberOfSets = function(n, maxDistance, roads) {
    
};
```

### TypeScript

```typescript
function numberOfSets(n: number, maxDistance: number, roads: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $maxDistance
     * @param Integer[][] $roads
     * @return Integer
     */
    function numberOfSets($n, $maxDistance, $roads) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSets(_ n: Int, _ maxDistance: Int, _ roads: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSets(n: Int, maxDistance: Int, roads: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSets(int n, int maxDistance, List<List<int>> roads) {
    
  }
}
```

### Go

```golang
func numberOfSets(n int, maxDistance int, roads [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} max_distance
# @param {Integer[][]} roads
# @return {Integer}
def number_of_sets(n, max_distance, roads)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSets(n: Int, maxDistance: Int, roads: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_sets(n: i32, max_distance: i32, roads: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-sets n maxDistance roads)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_sets(N :: integer(), MaxDistance :: integer(), Roads :: [[integer()]]) -> integer().
number_of_sets(N, MaxDistance, Roads) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_sets(n :: integer, max_distance :: integer, roads :: [[integer]]) :: integer
  def number_of_sets(n, max_distance, roads) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSets(n: Int64, maxDistance: Int64, roads: Array<Array<Int64>>): Int64 {

    }
}
```

