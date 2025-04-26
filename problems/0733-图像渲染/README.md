# 733. 图像渲染

## 题目描述

<p>有一幅以&nbsp;<code>m x n</code>&nbsp;的二维整数数组表示的图画&nbsp;<code>image</code>&nbsp;，其中&nbsp;<code>image[i][j]</code>&nbsp;表示该图画的像素值大小。你也被给予三个整数 <code>sr</code> ,&nbsp; <code>sc</code> 和 <code>color</code> 。你应该从像素&nbsp;<code>image[sr][sc]</code>&nbsp;开始对图像进行上色&nbsp;<strong>填充</strong> 。</p>

<p>为了完成 <strong>上色工作</strong>：</p>

<ol>
	<li>从初始像素开始，将其颜色改为 <code>color</code>。</li>
	<li>对初始坐标的 <strong>上下左右四个方向上</strong> 相邻且与初始像素的原始颜色同色的像素点执行相同操作。</li>
	<li>通过检查与初始像素的原始颜色相同的相邻像素并修改其颜色来继续 <strong>重复</strong> 此过程。</li>
	<li>当 <strong>没有</strong> 其它原始颜色的相邻像素时 <strong>停止</strong> 操作。</li>
</ol>

<p>最后返回经过上色渲染&nbsp;<strong>修改</strong> 后的图像&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg" /></p>

<div class="example-block"><strong>输入：</strong>image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, color = 2</div>

<div class="example-block"><strong>输出：</strong>[[2,2,2],[2,2,0],[2,0,1]]</div>

<div class="example-block"><b>解释：</b>在图像的正中间，坐标 <code>(sr,sc)=(1,1)</code>&nbsp;（即红色像素）,在路径上所有符合条件的像素点的颜色都被更改成相同的新颜色（即蓝色像素）。</div>

<div class="example-block">注意，右下角的像素 <strong>没有</strong> 更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。</div>

<div class="example-block">&nbsp;</div>

<p><strong>示例 2:</strong></p>

<div class="example-block"><strong>输入：</strong>image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0</div>

<div class="example-block"><strong>输出：</strong>[[0,0,0],[0,0,0]]</div>

<div class="example-block"><strong>解释：</strong>初始像素已经用 0 着色，这与目标颜色相同。因此，不会对图像进行任何更改。</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>m == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= image[i][j], color &lt; 2<sup>16</sup></code></li>
	<li><code>0 &lt;= sr &lt;&nbsp;m</code></li>
	<li><code>0 &lt;= sc &lt;&nbsp;n</code></li>
</ul>


## 难度

Easy

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵

## 提示

1. Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.

## 示例

```
[[1,1,1],[1,1,0],[1,0,1]]
1
1
2
[[0,0,0],[0,0,0]]
0
0
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
    }
}
```

### Python

```python
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    
};
```

### TypeScript

```typescript
function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $image
     * @param Integer $sr
     * @param Integer $sc
     * @param Integer $color
     * @return Integer[][]
     */
    function floodFill($image, $sr, $sc, $color) {
        
    }
}
```

### Swift

```swift
class Solution {
    func floodFill(_ image: [[Int]], _ sr: Int, _ sc: Int, _ color: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> floodFill(List<List<int>> image, int sr, int sc, int color) {
    
  }
}
```

### Go

```golang
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} color
# @return {Integer[][]}
def flood_fill(image, sr, sc, color)
    
end
```

### Scala

```scala
object Solution {
    def floodFill(image: Array[Array[Int]], sr: Int, sc: Int, color: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn flood_fill(image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (flood-fill image sr sc color)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec flood_fill(Image :: [[integer()]], Sr :: integer(), Sc :: integer(), Color :: integer()) -> [[integer()]].
flood_fill(Image, Sr, Sc, Color) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec flood_fill(image :: [[integer]], sr :: integer, sc :: integer, color :: integer) :: [[integer]]
  def flood_fill(image, sr, sc, color) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func floodFill(image: Array<Array<Int64>>, sr: Int64, sc: Int64, color: Int64): Array<Array<Int64>> {

    }
}
```

