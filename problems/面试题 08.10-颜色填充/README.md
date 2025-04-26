# 面试题 08.10. 颜色填充

## 题目描述

<p>编写函数，实现许多图片编辑软件都支持的「颜色填充」功能。</p>

<p>待填充的图像用二维数组 <code>image</code> 表示，元素为初始颜色值。初始坐标点的行坐标为 <code>sr</code> 列坐标为 <code>sc</code>。需要填充的新颜色为 <code>newColor</code> 。</p>

<p>「周围区域」是指颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。</p>

<p>请用新颜色填充初始坐标点的周围区域，并返回填充后的图像。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>：
image = [[1,1,1],[1,1,0],[1,0,1]] 
sr = 1, sc = 1, newColor = 2
<strong>输出</strong>：[[2,2,2],[2,2,0],[2,0,1]]
<strong>解释</strong>: 
初始坐标点位于图像的正中间，坐标 (sr,sc)=(1,1) 。
初始坐标点周围区域上所有符合条件的像素点的颜色都被更改成 2 。
注意，右下角的像素没有更改为 2 ，因为它不属于初始坐标点的周围区域。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>image</code> 和 <code>image[0]</code> 的长度均在范围 [1, 50] 内。</li>
	<li>初始坐标点 <code>(sr,sc)</code> 满足 <code>0 <= sr < image.length</code> 和 <code>0 <= sc < image[0].length</code> 。</li>
	<li><code>image[i][j]</code> 和 <code>newColor</code> 表示的颜色值在范围 <code>[0, 65535]</code> 内。</li>
</ul>


## 难度

Easy

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵

## 提示

1. 把这个看成一个图。
2. 你可以使用深度优先搜索（或广度优先搜索）。“正确”颜色的每个相邻像素都是一个连接边。

## 示例

```
[[1,1,1],[1,1,0],[1,0,1]]
1
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        
    }
}
```

### Python

```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int newColor, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int newColor) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    
};
```

### TypeScript

```typescript
function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $image
     * @param Integer $sr
     * @param Integer $sc
     * @param Integer $newColor
     * @return Integer[][]
     */
    function floodFill($image, $sr, $sc, $newColor) {
        
    }
}
```

### Swift

```swift
class Solution {
    func floodFill(_ image: [[Int]], _ sr: Int, _ sc: Int, _ newColor: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, newColor: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> floodFill(List<List<int>> image, int sr, int sc, int newColor) {
    
  }
}
```

### Go

```golang
func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} new_color
# @return {Integer[][]}
def flood_fill(image, sr, sc, new_color)
    
end
```

### Scala

```scala
object Solution {
    def floodFill(image: Array[Array[Int]], sr: Int, sc: Int, newColor: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn flood_fill(image: Vec<Vec<i32>>, sr: i32, sc: i32, new_color: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (flood-fill image sr sc newColor)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec flood_fill(Image :: [[integer()]], Sr :: integer(), Sc :: integer(), NewColor :: integer()) -> [[integer()]].
flood_fill(Image, Sr, Sc, NewColor) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec flood_fill(image :: [[integer]], sr :: integer, sc :: integer, new_color :: integer) :: [[integer]]
  def flood_fill(image, sr, sc, new_color) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func floodFill(image: Array<Array<Int64>>, sr: Int64, sc: Int64, newColor: Int64): Array<Array<Int64>> {

    }
}
```

