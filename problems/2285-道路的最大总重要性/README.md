# 2285. 道路的最大总重要性

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，表示一个国家里的城市数目。城市编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。</p>

<p>给你一个二维整数数组&nbsp;<code>roads</code>&nbsp;，其中&nbsp;<code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示城市&nbsp;<code>a<sub>i</sub></code>&nbsp;和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条&nbsp;<strong>双向</strong>&nbsp;道路。</p>

<p>你需要给每个城市安排一个从 <code>1</code>&nbsp;到 <code>n</code>&nbsp;之间的整数值，且每个值只能被使用 <strong>一次</strong>&nbsp;。道路的 <strong>重要性</strong>&nbsp;定义为这条道路连接的两座城市数值 <strong>之和</strong>&nbsp;。</p>

<p>请你返回在最优安排下，<strong>所有道路重要性</strong> 之和 <strong>最大</strong>&nbsp;为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/04/07/ex1drawio.png" style="width: 290px; height: 215px;"></p>

<pre><b>输入：</b>n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
<b>输出：</b>43
<b>解释：</b>上图展示了国家图和每个城市被安排的值 [2,4,5,3,1] 。
- 道路 (0,1) 重要性为 2 + 4 = 6 。
- 道路 (1,2) 重要性为 4 + 5 = 9 。
- 道路 (2,3) 重要性为 5 + 3 = 8 。
- 道路 (0,2) 重要性为 2 + 5 = 7 。
- 道路 (1,3) 重要性为 4 + 3 = 7 。
- 道路 (2,4) 重要性为 5 + 1 = 6 。
所有道路重要性之和为 6 + 9 + 8 + 7 + 7 + 6 = 43 。
可以证明，重要性之和不可能超过 43 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/04/07/ex2drawio.png" style="width: 281px; height: 151px;"></p>

<pre><b>输入：</b>n = 5, roads = [[0,3],[2,4],[1,3]]
<b>输出：</b>20
<b>解释：</b>上图展示了国家图和每个城市被安排的值 [4,3,2,5,1] 。
- 道路 (0,3) 重要性为 4 + 5 = 9 。
- 道路 (2,4) 重要性为 2 + 1 = 3 。
- 道路 (1,3) 重要性为 3 + 5 = 8 。
所有道路重要性之和为 9 + 3 + 8 = 20 。
可以证明，重要性之和不可能超过 20 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= roads.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>roads[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>没有重复道路。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 图
- 排序
- 堆（优先队列）

## 提示

1. Consider what each city contributes to the total importance of all roads.
2. Based on that, how can you sort the cities such that assigning them values in that order will yield the maximum total importance?

## 示例

```
5
[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
5
[[0,3],[2,4],[1,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumImportance(int n, int[][] roads) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
```

### C

```c
long long maximumImportance(int n, int** roads, int roadsSize, int* roadsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumImportance(int n, int[][] roads) {
        
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
var maximumImportance = function(n, roads) {
    
};
```

### TypeScript

```typescript
function maximumImportance(n: number, roads: number[][]): number {
    
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
    function maximumImportance($n, $roads) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumImportance(_ n: Int, _ roads: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumImportance(n: Int, roads: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumImportance(int n, List<List<int>> roads) {
    
  }
}
```

### Go

```golang
func maximumImportance(n int, roads [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def maximum_importance(n, roads)
    
end
```

### Scala

```scala
object Solution {
    def maximumImportance(n: Int, roads: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_importance(n: i32, roads: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-importance n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_importance(N :: integer(), Roads :: [[integer()]]) -> integer().
maximum_importance(N, Roads) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_importance(n :: integer, roads :: [[integer]]) :: integer
  def maximum_importance(n, roads) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumImportance(n: Int64, roads: Array<Array<Int64>>): Int64 {

    }
}
```

