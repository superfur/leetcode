# 1595. 连通两组点的最小成本

## 题目描述

<p>给你两组点，其中第一组中有 <code>size<sub>1</sub></code> 个点，第二组中有 <code>size<sub>2</sub></code> 个点，且 <code>size<sub>1</sub> &gt;= size<sub>2</sub></code> 。</p>

<p>任意两点间的连接成本 <code>cost</code> 由大小为 <code>size<sub>1</sub> x size<sub>2</sub></code> 矩阵给出，其中 <code>cost[i][j]</code> 是第一组中的点 <code>i</code> 和第二组中的点 <code>j</code> 的连接成本。<strong>如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。</strong>换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至少与第一组中的一个点连接。</p>

<p>返回连通两组点所需的最小成本。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/20/ex1.jpg" style="height: 243px; width: 322px;"></p>

<pre><strong>输入：</strong>cost = [[15, 96], [36, 2]]
<strong>输出：</strong>17
<strong>解释：</strong>连通两组点的最佳方法是：
1--A
2--B
总成本为 17 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/20/ex2.jpg" style="height: 403px; width: 322px;"></p>

<pre><strong>输入：</strong>cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
<strong>输出：</strong>4
<strong>解释：</strong>连通两组点的最佳方法是：
1--A
2--B
2--C
3--A
最小成本为 4 。
请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需要关心最低总成本。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
<strong>输出：</strong>10
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>size<sub>1</sub> == cost.length</code></li>
	<li><code>size<sub>2</sub> == cost[i].length</code></li>
	<li><code>1 &lt;= size<sub>1</sub>, size<sub>2</sub> &lt;= 12</code></li>
	<li><code>size<sub>1</sub> &gt;=&nbsp;size<sub>2</sub></code></li>
	<li><code>0 &lt;= cost[i][j] &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩
- 矩阵

## 提示

1. Each point on the left would either be connected to exactly point already connected to some left node, or a subset of the nodes on the right which are not connected to any node
2. Use dynamic programming with bitmasking, where the state will be (number of points assigned in first group, bitmask of points assigned in second group).

## 示例

```
[[15,96],[36,2]]
[[1,3,5],[4,1,1],[1,5,3]]
[[2,5,1],[3,4,7],[8,1,2],[6,2,4],[3,8,8]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int connectTwoGroups(vector<vector<int>>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public int connectTwoGroups(List<List<Integer>> cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        
```

### C

```c
int connectTwoGroups(int** cost, int costSize, int* costColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ConnectTwoGroups(IList<IList<int>> cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} cost
 * @return {number}
 */
var connectTwoGroups = function(cost) {
    
};
```

### TypeScript

```typescript
function connectTwoGroups(cost: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $cost
     * @return Integer
     */
    function connectTwoGroups($cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func connectTwoGroups(_ cost: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun connectTwoGroups(cost: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int connectTwoGroups(List<List<int>> cost) {
    
  }
}
```

### Go

```golang
func connectTwoGroups(cost [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} cost
# @return {Integer}
def connect_two_groups(cost)
    
end
```

### Scala

```scala
object Solution {
    def connectTwoGroups(cost: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn connect_two_groups(cost: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (connect-two-groups cost)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec connect_two_groups(Cost :: [[integer()]]) -> integer().
connect_two_groups(Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec connect_two_groups(cost :: [[integer]]) :: integer
  def connect_two_groups(cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func connectTwoGroups(cost: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

