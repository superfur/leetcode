# 1992. 找到所有的农场组

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始，大小为&nbsp;<code>m x n</code>&nbsp;的二进制矩阵&nbsp;<code>land</code>&nbsp;，其中 <code>0</code>&nbsp;表示一单位的森林土地，<code>1</code>&nbsp;表示一单位的农场土地。</p>

<p>为了让农场保持有序，农场土地之间以矩形的 <strong>农场组</strong> 的形式存在。每一个农场组都 <strong>仅</strong>&nbsp;包含农场土地。且题目保证不会有两个农场组相邻，也就是说一个农场组中的任何一块土地都 <strong>不会</strong>&nbsp;与另一个农场组的任何一块土地在四个方向上相邻。</p>

<p><code>land</code>&nbsp;可以用坐标系统表示，其中 <code>land</code>&nbsp;左上角坐标为&nbsp;<code>(0, 0)</code>&nbsp;，右下角坐标为&nbsp;<code>(m-1, n-1)</code>&nbsp;。请你找到所有 <b>农场组</b>&nbsp;最左上角和最右下角的坐标。一个左上角坐标为&nbsp;<code>(r<sub>1</sub>, c<sub>1</sub>)</code>&nbsp;且右下角坐标为&nbsp;<code>(r<sub>2</sub>, c<sub>2</sub>)</code>&nbsp;的 <strong>农场组</strong> 用长度为 4 的数组&nbsp;<code>[r<sub>1</sub>, c<sub>1</sub>, r<sub>2</sub>, c<sub>2</sub>]</code>&nbsp;表示。</p>

<p>请你返回一个二维数组，它包含若干个长度为 4 的子数组，每个子数组表示 <code>land</code>&nbsp;中的一个 <strong>农场组</strong>&nbsp;。如果没有任何农场组，请你返回一个空数组。可以以 <strong>任意顺序</strong>&nbsp;返回所有农场组。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-23-15-copy-of-diagram-drawio-diagrams-net.png" style="width: 300px; height: 300px;"></p>

<pre><b>输入：</b>land = [[1,0,0],[0,1,1],[0,1,1]]
<b>输出：</b>[[0,0,0,0],[1,1,2,2]]
<strong>解释：</strong>
第一个农场组的左上角为 land[0][0] ，右下角为 land[0][0] 。
第二个农场组的左上角为 land[1][1] ，右下角为 land[2][2] 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-30-26-copy-of-diagram-drawio-diagrams-net.png" style="width: 200px; height: 200px;"></p>

<pre><b>输入：</b>land = [[1,1],[1,1]]
<b>输出：</b>[[0,0,1,1]]
<strong>解释：</strong>
第一个农场组左上角为 land[0][0] ，右下角为 land[1][1] 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-32-24-copy-of-diagram-drawio-diagrams-net.png" style="width: 100px; height: 100px;"></p>

<pre><b>输入：</b>land = [[0]]
<b>输出：</b>[]
<b>解释：</b>
没有任何农场组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == land.length</code></li>
	<li><code>n == land[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>land</code>&nbsp;只包含&nbsp;<code>0</code>&nbsp;和&nbsp;<code>1</code>&nbsp;。</li>
	<li>农场组都是 <strong>矩形</strong>&nbsp;的形状。</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵

## 提示

1. Since every group of farmland is rectangular, the top left corner of each group will have the smallest x-coordinate and y-coordinate of any farmland in the group.
2. Similarly, the bottom right corner of each group will have the largest x-coordinate and y-coordinate of any farmland in the group.
3. Use DFS to traverse through different groups of farmlands and keep track of the smallest and largest x-coordinate and y-coordinates you have seen in each group.

## 示例

```
[[1,0,0],[0,1,1],[0,1,1]]
[[1,1],[1,1]]
[[0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] findFarmland(int[][] land) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findFarmland(int** land, int landSize, int* landColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] FindFarmland(int[][] land) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} land
 * @return {number[][]}
 */
var findFarmland = function(land) {
    
};
```

### TypeScript

```typescript
function findFarmland(land: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $land
     * @return Integer[][]
     */
    function findFarmland($land) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findFarmland(_ land: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findFarmland(land: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> findFarmland(List<List<int>> land) {
    
  }
}
```

### Go

```golang
func findFarmland(land [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} land
# @return {Integer[][]}
def find_farmland(land)
    
end
```

### Scala

```scala
object Solution {
    def findFarmland(land: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_farmland(land: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (find-farmland land)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec find_farmland(Land :: [[integer()]]) -> [[integer()]].
find_farmland(Land) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_farmland(land :: [[integer]]) :: [[integer]]
  def find_farmland(land) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findFarmland(land: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

