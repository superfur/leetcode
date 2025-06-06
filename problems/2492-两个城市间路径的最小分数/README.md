# 2492. 两个城市间路径的最小分数

## 题目描述

<p>给你一个正整数&nbsp;<code>n</code>&nbsp;，表示总共有&nbsp;<code>n</code>&nbsp;个城市，城市从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;编号。给你一个二维数组&nbsp;<code>roads</code>&nbsp;，其中&nbsp;<code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>, distance<sub>i</sub>]</code>&nbsp;表示城市&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条 <strong>双向</strong>&nbsp;道路，道路距离为&nbsp;<code>distance<sub>i</sub></code>&nbsp;。城市构成的图不一定是连通的。</p>

<p>两个城市之间一条路径的 <strong>分数</strong>&nbsp;定义为这条路径中道路的 <strong>最小</strong>&nbsp;距离。</p>

<p><span class="text-only" data-eleid="20" style="white-space: pre;">城市</span><span class="text-only text-font-italic" data-eleid="21" style="white-space: pre;"> </span><code><span class="text-only" data-eleid="22" style="white-space: pre;">1</span></code><span class="text-only text-font-italic" data-eleid="23" style="white-space: pre;"> </span><span class="text-only" data-eleid="24" style="white-space: pre;">和城市</span><span class="text-only text-font-italic" data-eleid="25" style="white-space: pre;"> </span><span class="text-only" data-eleid="26" style="white-space: pre;"><code>n</code> 之间的所有路径的 </span><strong><span class="text-only" data-eleid="27" style="white-space: pre;">最小</span></strong><span class="text-only" data-eleid="28" style="white-space: pre;"> 分数。</span></p>

<p><b>注意：</b></p>

<ul>
	<li>一条路径指的是两个城市之间的道路序列。</li>
	<li>一条路径可以 <strong>多次</strong> 包含同一条道路，你也可以沿着路径多次到达城市 <code>1</code>&nbsp;和城市 <code>n</code>&nbsp;。</li>
	<li>测试数据保证城市 <code>1</code>&nbsp;和城市<code>n</code>&nbsp;之间 <strong>至少</strong>&nbsp;有一条路径。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph11.png" style="width: 190px; height: 231px;" /></p>

<pre>
<b>输入：</b>n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
<b>输出：</b>5
<b>解释：</b>城市 1 到城市 4 的路径中，分数最小的一条为：1 -&gt; 2 -&gt; 4 。这条路径的分数是 min(9,5) = 5 。
不存在分数更小的路径。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph22.png" style="width: 190px; height: 231px;" /></p>

<pre>
<b>输入：</b>n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
<b>输出：</b>2
<b>解释：</b>城市 1 到城市 4 分数最小的路径是：1 -&gt; 2 -&gt; 1 -&gt; 3 -&gt; 4 。这条路径的分数是 min(2,2,4,7) = 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= roads.length &lt;= 10<sup>5</sup></code></li>
	<li><code>roads[i].length == 3</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= distance<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>不会有重复的边。</li>
	<li>城市 <code>1</code>&nbsp;和城市 <code>n</code>&nbsp;之间至少有一条路径。</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 提示

1. Can you solve the problem if the whole graph is connected?
2. Notice that if the graph is connected, you can always use any edge of the graph in your path.
3. How to solve the general problem in a similar way? Remove all the nodes that are not connected to 1 and n, then apply the previous solution in the new graph.

## 示例

```
4
[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
4
[[1,2,2],[1,3,4],[3,4,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        
    }
};
```

### Java

```java
class Solution {
    public int minScore(int n, int[][] roads) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
```

### C

```c
int minScore(int n, int** roads, int roadsSize, int* roadsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinScore(int n, int[][] roads) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var minScore = function(n, roads) {
    
};
```

### TypeScript

```typescript
function minScore(n: number, roads: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $roads
     * @return Integer
     */
    function minScore($n, $roads) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minScore(_ n: Int, _ roads: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minScore(n: Int, roads: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minScore(int n, List<List<int>> roads) {
    
  }
}
```

### Go

```golang
func minScore(n int, roads [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def min_score(n, roads)
    
end
```

### Scala

```scala
object Solution {
    def minScore(n: Int, roads: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-score n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_score(N :: integer(), Roads :: [[integer()]]) -> integer().
min_score(N, Roads) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_score(n :: integer, roads :: [[integer]]) :: integer
  def min_score(n, roads) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minScore(n: Int64, roads: Array<Array<Int64>>): Int64 {

    }
}
```

