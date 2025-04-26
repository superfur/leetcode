# 1443. 收集树上所有苹果的最少时间

## 题目描述

<p>给你一棵有&nbsp;<code>n</code>&nbsp;个节点的无向树，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>&nbsp;，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从&nbsp;<strong>节点 0&nbsp;</strong>出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。</p>

<p>无向树的边由&nbsp;<code>edges</code>&nbsp;给出，其中&nbsp;<code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>]</code>&nbsp;，表示有一条边连接&nbsp;<code>from</code>&nbsp;和&nbsp;<code>to<sub>i</sub></code> 。除此以外，还有一个布尔数组&nbsp;<code>hasApple</code> ，其中&nbsp;<code>hasApple[i] = true</code>&nbsp;代表节点&nbsp;<code>i</code>&nbsp;有一个苹果，否则，节点&nbsp;<code>i</code>&nbsp;没有苹果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_1.png" style="height: 212px; width: 300px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
<strong>输出：</strong>8 
<strong>解释：</strong>上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_2.png" style="height: 212px; width: 300px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
<strong>输出：</strong>6
<strong>解释：</strong>上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>&nbsp;&lt; b<sub>i</sub>&nbsp;&lt;= n - 1</code></li>
	<li><code>hasApple.length == n</code></li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 哈希表

## 提示

1. Note that if a node u contains an apple then all edges in the path from the root to the node u have to be used forward and backward (2 times).
2. Therefore use a depth-first search (DFS) to check if an edge will be used or not.

## 示例

```
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,true,false,true,true,false]
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,true,false,false,true,false]
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
[false,false,false,false,false,false,false]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        
    }
};
```

### Java

```java
class Solution {
    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
```

### C

```c
int minTime(int n, int** edges, int edgesSize, int* edgesColSize, bool* hasApple, int hasAppleSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinTime(int n, int[][] edges, IList<bool> hasApple) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function(n, edges, hasApple) {
    
};
```

### TypeScript

```typescript
function minTime(n: number, edges: number[][], hasApple: boolean[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Boolean[] $hasApple
     * @return Integer
     */
    function minTime($n, $edges, $hasApple) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minTime(_ n: Int, _ edges: [[Int]], _ hasApple: [Bool]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minTime(n: Int, edges: Array<IntArray>, hasApple: List<Boolean>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minTime(int n, List<List<int>> edges, List<bool> hasApple) {
    
  }
}
```

### Go

```golang
func minTime(n int, edges [][]int, hasApple []bool) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Boolean[]} has_apple
# @return {Integer}
def min_time(n, edges, has_apple)
    
end
```

### Scala

```scala
object Solution {
    def minTime(n: Int, edges: Array[Array[Int]], hasApple: List[Boolean]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, has_apple: Vec<bool>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-time n edges hasApple)
  (-> exact-integer? (listof (listof exact-integer?)) (listof boolean?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_time(N :: integer(), Edges :: [[integer()]], HasApple :: [boolean()]) -> integer().
min_time(N, Edges, HasApple) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_time(n :: integer, edges :: [[integer]], has_apple :: [boolean]) :: integer
  def min_time(n, edges, has_apple) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minTime(n: Int64, edges: Array<Array<Int64>>, hasApple: ArrayList<Bool>): Int64 {

    }
}
```

