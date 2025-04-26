# 1203. 项目管理

## 题目描述

<p>有 <code>n</code> 个项目，每个项目或者不属于任何小组，或者属于 <code>m</code> 个小组之一。<code>group[i]</code> 表示第 <code>i</code> 个项目所属的小组，如果第 <code>i</code> 个项目不属于任何小组，则 <code>group[i]</code> 等于 <code>-1</code>。项目和小组都是从零开始编号的。可能存在小组不负责任何项目，即没有任何项目属于这个小组。</p>

<p>请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：</p>

<ul>
	<li>同一小组的项目，排序后在列表中彼此相邻。</li>
	<li>项目之间存在一定的依赖关系，我们用一个列表 <code>beforeItems</code> 来表示，其中 <code>beforeItems[i]</code> 表示在进行第 <code>i</code> 个项目前（位于第 <code>i</code> 个项目左侧）应该完成的所有项目。</li>
</ul>

<p>如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 <strong>空列表 </strong>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/22/1359_ex1.png" style="height: 181px; width: 191px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
<strong>输出：</strong>[6,3,4,1,5,2,0,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
<strong>输出：</strong>[]
<strong>解释：</strong>与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= m <= n <= 3 * 10<sup>4</sup></code></li>
	<li><code>group.length == beforeItems.length == n</code></li>
	<li><code>-1 <= group[i] <= m - 1</code></li>
	<li><code>0 <= beforeItems[i].length <= n - 1</code></li>
	<li><code>0 <= beforeItems[i][j] <= n - 1</code></li>
	<li><code>i != beforeItems[i][j]</code></li>
	<li><code>beforeItems[i]</code> 不含重复元素</li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 拓扑排序

## 提示

1. Think of it as a graph problem.
2. We need to find a topological order on the dependency graph.
3. Build two graphs, one for the groups and another for the items.

## 示例

```
8
2
[-1,-1,1,0,0,1,0,-1]
[[],[6],[5],[6],[3,6],[],[],[]]
8
2
[-1,-1,1,0,0,1,0,-1]
[[],[6],[5],[6],[3],[],[4],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortItems(int n, int m, int* group, int groupSize, int** beforeItems, int beforeItemsSize, int* beforeItemsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SortItems(int n, int m, int[] group, IList<IList<int>> beforeItems) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
var sortItems = function(n, m, group, beforeItems) {
    
};
```

### TypeScript

```typescript
function sortItems(n: number, m: number, group: number[], beforeItems: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[] $group
     * @param Integer[][] $beforeItems
     * @return Integer[]
     */
    function sortItems($n, $m, $group, $beforeItems) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortItems(_ n: Int, _ m: Int, _ group: [Int], _ beforeItems: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortItems(n: Int, m: Int, group: IntArray, beforeItems: List<List<Int>>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sortItems(int n, int m, List<int> group, List<List<int>> beforeItems) {
    
  }
}
```

### Go

```golang
func sortItems(n int, m int, group []int, beforeItems [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} m
# @param {Integer[]} group
# @param {Integer[][]} before_items
# @return {Integer[]}
def sort_items(n, m, group, before_items)
    
end
```

### Scala

```scala
object Solution {
    def sortItems(n: Int, m: Int, group: Array[Int], beforeItems: List[List[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_items(n: i32, m: i32, group: Vec<i32>, before_items: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sort-items n m group beforeItems)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sort_items(N :: integer(), M :: integer(), Group :: [integer()], BeforeItems :: [[integer()]]) -> [integer()].
sort_items(N, M, Group, BeforeItems) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_items(n :: integer, m :: integer, group :: [integer], before_items :: [[integer]]) :: [integer]
  def sort_items(n, m, group, before_items) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortItems(n: Int64, m: Int64, group: Array<Int64>, beforeItems: ArrayList<ArrayList<Int64>>): Array<Int64> {

    }
}
```

