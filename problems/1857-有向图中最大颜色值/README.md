# 1857. 有向图中最大颜色值

## 题目描述

<p>给你一个 <strong>有向图</strong> ，它含有 <code>n</code> 个节点和 <code>m</code> 条边。节点编号从 <code>0</code> 到 <code>n - 1</code> 。</p>

<p>给你一个字符串 <code>colors</code> ，其中 <code>colors[i]</code> 是小写英文字母，表示图中第 <code>i</code> 个节点的 <b>颜色</b> （下标从 <strong>0</strong> 开始）。同时给你一个二维数组 <code>edges</code> ，其中 <code>edges[j] = [a<sub>j</sub>, b<sub>j</sub>]</code> 表示从节点 <code>a<sub>j</sub></code> 到节点 <code>b<sub>j</sub></code><sub> </sub>有一条 <strong>有向边</strong> 。</p>

<p>图中一条有效 <strong>路径</strong> 是一个点序列 <code>x<sub>1</sub> -&gt; x<sub>2</sub> -&gt; x<sub>3</sub> -&gt; ... -&gt; x<sub>k</sub></code> ，对于所有 <code>1 &lt;= i &lt; k</code> ，从 <code>x<sub>i</sub></code> 到 <code>x<sub>i+1</sub></code> 在图中有一条有向边。路径的 <strong>颜色值</strong> 是路径中 <strong>出现次数最多</strong> 颜色的节点数目。</p>

<p>请你返回给定图中有效路径里面的 <strong>最大颜色值</strong><strong> 。</strong>如果图中含有环，请返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet1.png" style="width: 400px; height: 182px;"></p>

<pre><b>输入：</b>colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
<b>输出：</b>3
<b>解释：</b>路径 0 -&gt; 2 -&gt; 3 -&gt; 4 含有 3 个颜色为 <code>"a" 的节点（上图中的红色节点）。</code>
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet2.png" style="width: 85px; height: 85px;"></p>

<pre><b>输入：</b>colors = "a", edges = [[0,0]]
<b>输出：</b>-1
<b>解释：</b>从 0 到 0 有一个环。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == colors.length</code></li>
	<li><code>m == edges.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>colors</code> 只含有小写英文字母。</li>
	<li><code>0 &lt;= a<sub>j</sub>, b<sub>j</sub> &lt; n</code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 拓扑排序
- 记忆化搜索
- 哈希表
- 动态规划
- 计数

## 提示

1. Use topological sort.
2. let dp[u][c] := the maximum count of vertices with color c of any path starting from vertex u. (by JerryJin2905)

## 示例

```
"abaca"
[[0,1],[0,2],[2,3],[3,4]]
"a"
[[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestPathValue(String colors, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
```

### C

```c
int largestPathValue(char* colors, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestPathValue(string colors, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */
var largestPathValue = function(colors, edges) {
    
};
```

### TypeScript

```typescript
function largestPathValue(colors: string, edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $colors
     * @param Integer[][] $edges
     * @return Integer
     */
    function largestPathValue($colors, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestPathValue(_ colors: String, _ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestPathValue(colors: String, edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestPathValue(String colors, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func largestPathValue(colors string, edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {String} colors
# @param {Integer[][]} edges
# @return {Integer}
def largest_path_value(colors, edges)
    
end
```

### Scala

```scala
object Solution {
    def largestPathValue(colors: String, edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-path-value colors edges)
  (-> string? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_path_value(Colors :: unicode:unicode_binary(), Edges :: [[integer()]]) -> integer().
largest_path_value(Colors, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_path_value(colors :: String.t, edges :: [[integer]]) :: integer
  def largest_path_value(colors, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestPathValue(colors: String, edges: Array<Array<Int64>>): Int64 {

    }
}
```

