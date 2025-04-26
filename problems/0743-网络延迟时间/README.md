# 743. 网络延迟时间

## 题目描述

<p>有 <code>n</code> 个网络节点，标记为&nbsp;<code>1</code>&nbsp;到 <code>n</code>。</p>

<p>给你一个列表&nbsp;<code>times</code>，表示信号经过 <strong>有向</strong> 边的传递时间。&nbsp;<code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>，其中&nbsp;<code>u<sub>i</sub></code>&nbsp;是源节点，<code>v<sub>i</sub></code>&nbsp;是目标节点， <code>w<sub>i</sub></code>&nbsp;是一个信号从源节点传递到目标节点的时间。</p>

<p>现在，从某个节点&nbsp;<code>K</code>&nbsp;发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回&nbsp;<code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="height: 220px; width: 200px;" /></p>

<pre>
<strong>输入：</strong>times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>times = [[1,2,1]], n = 2, k = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>times = [[1,2,1]], n = 2, k = 2
<strong>输出：</strong>-1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= times.length &lt;= 6000</code></li>
	<li><code>times[i].length == 3</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= w<sub>i</sub> &lt;= 100</code></li>
	<li>所有 <code>(u<sub>i</sub>, v<sub>i</sub>)</code> 对都 <strong>互不相同</strong>（即，不含重复边）</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 最短路
- 堆（优先队列）

## 提示

1. We visit each node at some time, and if that time is better than the fastest time we've reached this node, we travel along outgoing edges in sorted order.  Alternatively, we could use Dijkstra's algorithm.

## 示例

```
[[2,1,1],[2,3,1],[3,4,1]]
4
2
[[1,2,1]]
2
1
[[1,2,1]]
2
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
```

### C

```c
int networkDelayTime(int** times, int timesSize, int* timesColSize, int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NetworkDelayTime(int[][] times, int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
    
};
```

### TypeScript

```typescript
function networkDelayTime(times: number[][], n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $times
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function networkDelayTime($times, $n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func networkDelayTime(_ times: [[Int]], _ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int networkDelayTime(List<List<int>> times, int n, int k) {
    
  }
}
```

### Go

```golang
func networkDelayTime(times [][]int, n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} times
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def network_delay_time(times, n, k)
    
end
```

### Scala

```scala
object Solution {
    def networkDelayTime(times: Array[Array[Int]], n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (network-delay-time times n k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec network_delay_time(Times :: [[integer()]], N :: integer(), K :: integer()) -> integer().
network_delay_time(Times, N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec network_delay_time(times :: [[integer]], n :: integer, k :: integer) :: integer
  def network_delay_time(times, n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func networkDelayTime(times: Array<Array<Int64>>, n: Int64, k: Int64): Int64 {

    }
}
```

