# 1536. 排布二进制网格的最少交换次数

## 题目描述

<p>给你一个&nbsp;<code>n&nbsp;x n</code>&nbsp;的二进制网格&nbsp;<code>grid</code>，每一次操作中，你可以选择网格的&nbsp;<strong>相邻两行</strong>&nbsp;进行交换。</p>

<p>一个符合要求的网格需要满足主对角线以上的格子全部都是 <strong>0</strong>&nbsp;。</p>

<p>请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 <strong>-1</strong>&nbsp;。</p>

<p>主对角线指的是从&nbsp;<code>(1, 1)</code>&nbsp;到&nbsp;<code>(n, n)</code>&nbsp;的这些格子。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/02/fw.jpg" style="height: 141px; width: 750px;"></p>

<pre><strong>输入：</strong>grid = [[0,0,1],[1,1,0],[1,0,0]]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/02/e2.jpg" style="height: 270px; width: 270px;"></p>

<pre><strong>输入：</strong>grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
<strong>输出：</strong>-1
<strong>解释：</strong>所有行都是一样的，交换相邻行无法使网格符合要求。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/02/e3.jpg" style="height: 210px; width: 210px;"></p>

<pre><strong>输入：</strong>grid = [[1,0,0],[1,1,0],[1,1,1]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 200</code></li>
	<li><code>grid[i][j]</code>&nbsp;要么是&nbsp;<code>0</code>&nbsp;要么是&nbsp;<code>1</code>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 矩阵

## 提示

1. For each row of the grid calculate the most right 1 in the grid in the array maxRight.
2. To check if there exist answer, sort maxRight and check if maxRight[i] ≤ i for all possible i's.
3. If there exist an answer, simulate the swaps.

## 示例

```
[[0,0,1],[1,1,0],[1,0,0]]
[[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
[[1,0,0],[1,1,0],[1,1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSwaps(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minSwaps(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSwaps(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minSwaps = function(grid) {
    
};
```

### TypeScript

```typescript
function minSwaps(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minSwaps($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSwaps(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSwaps(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSwaps(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minSwaps(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def min_swaps(grid)
    
end
```

### Scala

```scala
object Solution {
    def minSwaps(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-swaps grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_swaps(Grid :: [[integer()]]) -> integer().
min_swaps(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_swaps(grid :: [[integer]]) :: integer
  def min_swaps(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSwaps(grid: Array<Array<Int64>>): Int64 {

    }
}
```

