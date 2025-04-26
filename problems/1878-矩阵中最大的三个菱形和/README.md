# 1878. 矩阵中最大的三个菱形和

## 题目描述

<p>给你一个 <code>m x n</code> 的整数矩阵 <code>grid</code> 。</p>

<p><strong>菱形和</strong> 指的是 <code>grid</code> 中一个正菱形 <strong>边界</strong> 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-desc-2.png" style="width: 385px; height: 385px;" />
<p> </p>

<p>注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。</p>

<p>请你按照 <strong>降序</strong> 返回 <code>grid</code> 中三个最大的 <strong>互不相同的菱形和</strong> 。如果不同的和少于三个，则将它们全部返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex1.png" style="width: 360px; height: 361px;" />
<pre>
<b>输入：</b>grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
<b>输出：</b>[228,216,211]
<b>解释：</b>最大的三个菱形和如上图所示。
- 蓝色：20 + 3 + 200 + 5 = 228
- 红色：200 + 2 + 10 + 4 = 216
- 绿色：5 + 200 + 4 + 2 = 211
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex2.png" style="width: 217px; height: 217px;" />
<pre>
<b>输入：</b>grid = [[1,2,3],[4,5,6],[7,8,9]]
<b>输出：</b>[20,9,8]
<b>解释：</b>最大的三个菱形和如上图所示。
- 蓝色：4 + 2 + 6 + 8 = 20
- 红色：9 （右下角红色的面积为 0 的菱形）
- 绿色：8 （下方中央面积为 0 的菱形）
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>grid = [[7,7,7]]
<b>输出：</b>[7]
<b>解释：</b>所有三个可能的菱形和都相同，所以返回 [7] 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 100</code></li>
	<li><code>1 <= grid[i][j] <= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 矩阵
- 前缀和
- 排序
- 堆（优先队列）

## 提示

1. You need to maintain only the biggest 3 distinct sums
2. The limits are small enough for you to iterate over all rhombus sizes then iterate over all possible borders to get the sums

## 示例

```
[[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
[[1,2,3],[4,5,6],[7,8,9]]
[[7,7,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getBiggestThree(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getBiggestThree(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetBiggestThree(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var getBiggestThree = function(grid) {
    
};
```

### TypeScript

```typescript
function getBiggestThree(grid: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function getBiggestThree($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getBiggestThree(_ grid: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getBiggestThree(grid: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getBiggestThree(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func getBiggestThree(grid [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[]}
def get_biggest_three(grid)
    
end
```

### Scala

```scala
object Solution {
    def getBiggestThree(grid: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-biggest-three grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_biggest_three(Grid :: [[integer()]]) -> [integer()].
get_biggest_three(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_biggest_three(grid :: [[integer]]) :: [integer]
  def get_biggest_three(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getBiggestThree(grid: Array<Array<Int64>>): Array<Int64> {

    }
}
```

