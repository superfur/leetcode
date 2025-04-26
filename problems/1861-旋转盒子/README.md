# 1861. 旋转盒子

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的字符矩阵&nbsp;<code>boxGrid</code>&nbsp;，它表示一个箱子的侧视图。箱子的每一个格子可能为：</p>

<ul>
	<li><code>'#'</code>&nbsp;表示石头</li>
	<li><code>'*'</code>&nbsp;表示固定的障碍物</li>
	<li><code>'.'</code>&nbsp;表示空位置</li>
</ul>

<p>这个箱子被 <strong>顺时针旋转 90 度</strong>&nbsp;，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力 <strong>不会</strong>&nbsp;影响障碍物的位置，同时箱子旋转不会产生<strong>惯性</strong>&nbsp;，也就是说石头的水平位置不会发生改变。</p>

<p>题目保证初始时&nbsp;<code>boxGrid</code>&nbsp;中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。</p>

<p>请你返回一个<em>&nbsp;</em><code>n x m</code>&nbsp;的矩阵，表示按照上述旋转后，箱子内的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png" style="width: 300px; height: 150px;" /></p>

<pre>
<b>输入：</b>box = [["#",".","#"]]
<b>输出：</b>[["."],
&nbsp;     ["#"],
&nbsp;     ["#"]]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png" style="width: 375px; height: 195px;" /></p>

<pre>
<b>输入：</b>box = [["#",".","*","."],
&nbsp;           ["#","#","*","."]]
<b>输出：</b>[["#","."],
&nbsp;     ["#","#"],
&nbsp;     ["*","*"],
&nbsp;     [".","."]]
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png" style="width: 400px; height: 218px;" /></p>

<pre>
<b>输入：</b>box = [["#","#","*",".","*","."],
&nbsp;           ["#","#","#","*",".","."],
&nbsp;           ["#","#","#",".","#","."]]
<b>输出：</b>[[".","#","#"],
&nbsp;     [".","#","#"],
&nbsp;     ["#","#","*"],
&nbsp;     ["#","*","."],
&nbsp;     ["#",".","*"],
&nbsp;     ["#",".","."]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == boxGrid.length</code></li>
	<li><code>n == boxGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>boxGrid[i][j]</code>&nbsp;只可能是&nbsp;<code>'#'</code>&nbsp;，<code>'*'</code>&nbsp;或者&nbsp;<code>'.'</code>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 矩阵

## 提示

1. Rotate the box using the relation rotatedBox[i][j] = box[m - 1 - j][i].
2. Start iterating from the bottom of the box and for each empty cell check if there is any stone above it with no obstacles between them.

## 示例

```
[["#",".","#"]]
[["#",".","*","."],["#","#","*","."]]
[["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        
    }
};
```

### Java

```java
class Solution {
    public char[][] rotateTheBox(char[][] boxGrid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char** rotateTheBox(char** boxGrid, int boxGridSize, int* boxGridColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public char[][] RotateTheBox(char[][] boxGrid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} boxGrid
 * @return {character[][]}
 */
var rotateTheBox = function(boxGrid) {
    
};
```

### TypeScript

```typescript
function rotateTheBox(boxGrid: string[][]): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $boxGrid
     * @return String[][]
     */
    function rotateTheBox($boxGrid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rotateTheBox(_ boxGrid: [[Character]]) -> [[Character]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rotateTheBox(boxGrid: Array<CharArray>): Array<CharArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> rotateTheBox(List<List<String>> boxGrid) {
    
  }
}
```

### Go

```golang
func rotateTheBox(boxGrid [][]byte) [][]byte {
    
}
```

### Ruby

```ruby
# @param {Character[][]} box_grid
# @return {Character[][]}
def rotate_the_box(box_grid)
    
end
```

### Scala

```scala
object Solution {
    def rotateTheBox(boxGrid: Array[Array[Char]]): Array[Array[Char]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rotate_the_box(box_grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
        
    }
}
```

### Racket

```racket
(define/contract (rotate-the-box boxGrid)
  (-> (listof (listof char?)) (listof (listof char?)))
  )
```

### Erlang

```erlang
-spec rotate_the_box(BoxGrid :: [[char()]]) -> [[char()]].
rotate_the_box(BoxGrid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rotate_the_box(box_grid :: [[char]]) :: [[char]]
  def rotate_the_box(box_grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rotateTheBox(boxGrid: Array<Array<Rune>>): Array<Array<Rune>> {

    }
}
```

