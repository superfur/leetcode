# 329. 矩阵中的最长递增路径

## 题目描述

<p>给定一个 <code>m x n</code> 整数矩阵 <code>matrix</code> ，找出其中 <strong>最长递增路径</strong> 的长度。</p>

<p>对于每个单元格，你可以往上，下，左，右四个方向移动。 你 <strong>不能</strong> 在 <strong>对角线</strong> 方向上移动或移动到 <strong>边界外</strong>（即不允许环绕）。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[9,9,4],[6,6,8],[2,1,1]]
<strong>输出：</strong>4 
<strong>解释：</strong>最长递增路径为 <code>[1, 2, 6, 9]</code>。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>输入：</strong>matrix = [[3,4,5],[3,2,6],[2,2,1]]
<strong>输出：</strong>4 
<strong>解释：</strong>最长递增路径是 <code>[3, 4, 5, 6]</code>。注意不允许在对角线方向上移动。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[1]]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 200</code></li>
	<li><code>0 <= matrix[i][j] <= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 拓扑排序
- 记忆化搜索
- 数组
- 动态规划
- 矩阵

## 示例

```
[[9,9,4],[6,6,8],[2,1,1]]
[[3,4,5],[3,2,6],[2,2,1]]
[[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
```

### C

```c
int longestIncreasingPath(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestIncreasingPath(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
    
};
```

### TypeScript

```typescript
function longestIncreasingPath(matrix: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function longestIncreasingPath($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestIncreasingPath(_ matrix: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestIncreasingPath(matrix: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestIncreasingPath(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func longestIncreasingPath(matrix [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer}
def longest_increasing_path(matrix)
    
end
```

### Scala

```scala
object Solution {
    def longestIncreasingPath(matrix: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-increasing-path matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_increasing_path(Matrix :: [[integer()]]) -> integer().
longest_increasing_path(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_increasing_path(matrix :: [[integer]]) :: integer
  def longest_increasing_path(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestIncreasingPath(matrix: Array<Array<Int64>>): Int64 {

    }
}
```

