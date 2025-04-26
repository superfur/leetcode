# 931. 下降路径最小和

## 题目描述

<p>给你一个 <code>n x n</code> 的<strong> 方形 </strong>整数数组&nbsp;<code>matrix</code> ，请你找出并返回通过 <code>matrix</code> 的<strong>下降路径</strong><em> </em>的<strong> </strong><strong>最小和</strong> 。</p>

<p><strong>下降路径</strong> 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 <code>(row, col)</code> 的下一个元素应当是 <code>(row + 1, col - 1)</code>、<code>(row + 1, col)</code> 或者 <code>(row + 1, col + 1)</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1729566253-aneDag-image.png" style="height: 500px; width: 499px;" /></p>

<pre>
<strong>输入：</strong>matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>输出：</strong>13
<strong>解释：</strong>如图所示，为和最小的两条下降路径
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1729566282-dtXwRd-image.png" style="height: 365px; width: 164px;" /></p>

<pre>
<strong>输入：</strong>matrix = [[-19,57],[-40,-5]]
<strong>输出：</strong>-59
<strong>解释：</strong>如图所示，为和最小的下降路径
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 示例

```
[[2,1,3],[6,5,4],[7,8,9]]
[[-19,57],[-40,-5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
```

### C

```c
int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFallingPathSum(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function(matrix) {
    
};
```

### TypeScript

```typescript
function minFallingPathSum(matrix: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function minFallingPathSum($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFallingPathSum(_ matrix: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFallingPathSum(matrix: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFallingPathSum(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func minFallingPathSum(matrix [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer}
def min_falling_path_sum(matrix)
    
end
```

### Scala

```scala
object Solution {
    def minFallingPathSum(matrix: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-falling-path-sum matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_falling_path_sum(Matrix :: [[integer()]]) -> integer().
min_falling_path_sum(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_falling_path_sum(matrix :: [[integer]]) :: integer
  def min_falling_path_sum(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFallingPathSum(matrix: Array<Array<Int64>>): Int64 {

    }
}
```

