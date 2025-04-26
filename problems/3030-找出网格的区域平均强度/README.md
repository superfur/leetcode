# 3030. 找出网格的区域平均强度

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>m x n</code> 的网格 <code>image</code> ，表示一个灰度图像，其中 <code>image[i][j]</code> 表示在范围 <code>[0..255]</code> 内的某个像素强度。另给你一个<strong> 非负 </strong>整数 <code>threshold</code> 。</p>

<p>如果 <code>image[a][b]</code> 和 <code>image[c][d]</code> 满足 <code>|a - c| + |b - d| == 1</code> ，则称这两个像素是<strong> 相邻像素</strong> 。</p>

<p><strong>区域 </strong>是一个 <code>3 x 3</code> 的子网格，且满足区域中任意两个 <strong>相邻</strong> 像素之间，像素强度的<strong> 绝对差 </strong><strong> 小于或等于 </strong><code>threshold</code> 。</p>

<p><strong>区域</strong> 内的所有像素都认为属于该区域，而一个像素 <strong>可以 </strong>属于 <strong>多个</strong> 区域。</p>

<p>你需要计算一个下标从 <strong>0</strong> 开始、大小为 <code>m x n</code> 的网格 <code>result</code> ，其中 <code>result[i][j]</code> 是 <code>image[i][j]</code> 所属区域的 <strong>平均 </strong>强度，<strong>向下取整 </strong>到最接近的整数。如果 <code>image[i][j]</code> 属于多个区域，<code>result[i][j]</code> 是这些区域的<strong> </strong><strong>“取整后的平均强度”</strong> 的<strong> 平均值</strong>，也 <strong>向下取整 </strong>到最接近的整数。如果 <code>image[i][j]</code> 不属于任何区域，则 <code>result[i][j]</code><strong> 等于 </strong><code>image[i][j]</code> 。</p>

<p>返回网格 <code>result</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/21/example0corrected.png" style="width: 832px; height: 275px;" />
<pre>
<strong>输入：</strong>image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3
<strong>输出：</strong>[[9,9,9,9],[9,9,9,9],[9,9,9,9]]
<strong>解释：</strong>图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 9 ，而第二个区域的平均强度为 9.67 ，向下取整为 9 。两个区域的平均强度为 (9 + 9) / 2 = 9 。由于所有像素都属于区域 1 、区域 2 或两者，因此 result 中每个像素的强度都为 9 。
注意，在计算多个区域的平均值时使用了向下取整的值，因此使用区域 2 的平均强度 9 来进行计算，而不是 9.67 。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/21/example1corrected.png" style="width: 805px; height: 377px;" />
<pre>
<strong>输入：</strong>image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12
<strong>输出：</strong>[[25,25,25],[27,27,27],[27,27,27],[30,30,30]]
<strong>解释：</strong>图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 25 ，而第二个区域的平均强度为 30 。两个区域的平均强度为 (25 + 30) / 2 = 27.5 ，向下取整为 27 。图像中第 0 行的所有像素属于区域 1 ，因此 result 中第 0 行的所有像素为 25 。同理，result 中第 3 行的所有像素为 30 。图像中第 1 行和第 2 行的像素属于区域 1 和区域 2 ，因此它们在 result 中的值为 27 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1
<strong>输出：</strong>[[5,6,7],[8,9,10],[11,12,13]]
<strong>解释：</strong>图像中不存在任何区域，因此对于所有像素，result[i][j] == image[i][j] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n, m &lt;= 500</code></li>
	<li><code>0 &lt;= image[i][j] &lt;= 255</code></li>
	<li><code>0 &lt;= threshold &lt;= 255</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵

## 提示

1. Try all the <code>3 * 3</code> sub-grids to find all the regions.
2. Keep two 2-D arrays <code>sum</code> and <code>num</code>, for each position <code>(x, y)</code> in a region, increase <code>sum[x][y]</code> by the average sum of the region and increase <code>num[x][y]</code> by <code>1</code>.
3. For each position (x, y), <code>sum[x][y] / num[x][y]</code> is the answer. Note when <code>num[x][y] == 0</code>, we use the original value in <code>image</code> instead.

## 示例

```
[[5,6,7,10],[8,9,10,10],[11,12,13,10]]
3
[[10,20,30],[15,25,35],[20,30,40],[25,35,45]]
12
[[5,6,7],[8,9,10],[11,12,13]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> resultGrid(vector<vector<int>>& image, int threshold) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] resultGrid(int[][] image, int threshold) {
        
    }
}
```

### Python

```python
class Solution(object):
    def resultGrid(self, image, threshold):
        """
        :type image: List[List[int]]
        :type threshold: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** resultGrid(int** image, int imageSize, int* imageColSize, int threshold, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] ResultGrid(int[][] image, int threshold) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} image
 * @param {number} threshold
 * @return {number[][]}
 */
var resultGrid = function(image, threshold) {
    
};
```

### TypeScript

```typescript
function resultGrid(image: number[][], threshold: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $image
     * @param Integer $threshold
     * @return Integer[][]
     */
    function resultGrid($image, $threshold) {
        
    }
}
```

### Swift

```swift
class Solution {
    func resultGrid(_ image: [[Int]], _ threshold: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun resultGrid(image: Array<IntArray>, threshold: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> resultGrid(List<List<int>> image, int threshold) {
    
  }
}
```

### Go

```golang
func resultGrid(image [][]int, threshold int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} image
# @param {Integer} threshold
# @return {Integer[][]}
def result_grid(image, threshold)
    
end
```

### Scala

```scala
object Solution {
    def resultGrid(image: Array[Array[Int]], threshold: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn result_grid(image: Vec<Vec<i32>>, threshold: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (result-grid image threshold)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec result_grid(Image :: [[integer()]], Threshold :: integer()) -> [[integer()]].
result_grid(Image, Threshold) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec result_grid(image :: [[integer]], threshold :: integer) :: [[integer]]
  def result_grid(image, threshold) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func resultGrid(image: Array<Array<Int64>>, threshold: Int64): Array<Array<Int64>> {

    }
}
```

