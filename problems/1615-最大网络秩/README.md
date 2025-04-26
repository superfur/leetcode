# 1615. 最大网络秩

## 题目描述

<p><code>n</code> 座城市和一些连接这些城市的道路 <code>roads</code> 共同组成一个基础设施网络。每个 <code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 都表示在城市 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间有一条双向道路。</p>

<p>两座不同城市构成的 <strong>城市对</strong> 的 <strong>网络秩</strong> 定义为：与这两座城市 <strong>直接</strong> 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 <strong>一次</strong> 。</p>

<p>整个基础设施网络的 <strong>最大网络秩</strong> 是所有不同城市对中的 <strong>最大网络秩</strong> 。</p>

<p>给你整数 <code>n</code> 和数组 <code>roads</code>，返回整个基础设施网络的 <strong>最大网络秩</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/11/ex1.png" style="width: 292px; height: 172px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
<strong>输出：</strong>4
<strong>解释：</strong>城市 0 和 1 的网络秩是 4，因为共有 4 条道路与城市 0 或 1 相连。位于 0 和 1 之间的道路只计算一次。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/11/ex2.png" style="width: 292px; height: 172px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
<strong>输出：</strong>5
<strong>解释：</strong>共有 5 条道路与城市 1 或 2 相连。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
<strong>输出：</strong>5
<strong>解释：</strong>2 和 5 的网络秩为 5，注意并非所有的城市都需要连接起来。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 100</code></li>
	<li><code>0 <= roads.length <= n * (n - 1) / 2</code></li>
	<li><code>roads[i].length == 2</code></li>
	<li><code>0 <= a<sub>i</sub>, b<sub>i</sub> <= n-1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>每对城市之间 <strong>最多只有一条</strong> 道路相连</li>
</ul>


## 难度

Medium

## 标签

- 图

## 提示

1. Try every pair of different cities and calculate its network rank.
2. The network rank of two vertices is <i>almost</i> the sum of their degrees.
3. How can you efficiently check if there is a road connecting two different cities?

## 示例

```
4
[[0,1],[0,3],[1,2],[1,3]]
5
[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
8
[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
```

### C

```c
int maximalNetworkRank(int n, int** roads, int roadsSize, int* roadsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximalNetworkRank(int n, int[][] roads) {
        
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
var maximalNetworkRank = function(n, roads) {
    
};
```

### TypeScript

```typescript
function maximalNetworkRank(n: number, roads: number[][]): number {
    
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
    function maximalNetworkRank($n, $roads) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximalNetworkRank(_ n: Int, _ roads: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximalNetworkRank(n: Int, roads: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximalNetworkRank(int n, List<List<int>> roads) {
    
  }
}
```

### Go

```golang
func maximalNetworkRank(n int, roads [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def maximal_network_rank(n, roads)
    
end
```

### Scala

```scala
object Solution {
    def maximalNetworkRank(n: Int, roads: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximal-network-rank n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximal_network_rank(N :: integer(), Roads :: [[integer()]]) -> integer().
maximal_network_rank(N, Roads) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximal_network_rank(n :: integer, roads :: [[integer]]) :: integer
  def maximal_network_rank(n, roads) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximalNetworkRank(n: Int64, roads: Array<Array<Int64>>): Int64 {

    }
}
```

