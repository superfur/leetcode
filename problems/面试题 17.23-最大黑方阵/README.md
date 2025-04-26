# 面试题 17.23. 最大黑方阵

## 题目描述

<p>给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。</p>

<p>返回一个数组 <code>[r, c, size]</code> ，其中&nbsp;<code>r</code>,&nbsp;<code>c</code>&nbsp;分别代表子方阵左上角的行号和列号，<code>size</code> 是子方阵的边长。若有多个满足条件的子方阵，返回 <code>r</code> 最小的，若 <code>r</code> 相同，返回 <code>c</code> 最小的子方阵。若无满足条件的子方阵，返回空数组。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：
</strong>[
&nbsp;  [1,0,1],
&nbsp;  [<strong>0,0</strong>,1],
&nbsp;  [<strong>0,0</strong>,1]
]
<strong>输出：</strong>[1,0,2]
<strong>解释：</strong>输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：
</strong>[
&nbsp;  [<strong>0</strong>,1,1],
&nbsp;  [1,0,1],
&nbsp;  [1,1,0]
]
<strong>输出：</strong>[0,0,1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>matrix.length == matrix[0].length &lt;= 200</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. 从蛮力解法开始。你能先试试最大的正方形吗?
2. 最大的正方形是N×N。所以你先试一下该正方形，如果可行，那么你便知道已经找到了最佳正方形。否则，可以尝试下一个最小的正方形。
3. 描述蛮力解法的时间复杂度。
4. 你能通过预处理来优化这个解决方案吗？
5. 你应该能在O(N^3)时间内完成，其中N是正方形一边的长度。
6. 当你检查一个特定的正方形是否有效时（所有边框为黑色），需要检查在一个坐标的上面（或下面）和这个坐标的左边（或右边）有多少个黑色像素。你能预先计算出给定单元格上面和左边的黑色像素的数量吗？

## 示例

```
[[1,0,1],[0,0,1],[0,0,1]]
[[0,1,1],[1,0,1],[1,1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findSquare(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findSquare(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findSquare(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSquare(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindSquare(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var findSquare = function(matrix) {
    
};
```

### TypeScript

```typescript
function findSquare(matrix: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[]
     */
    function findSquare($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findSquare(_ matrix: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findSquare(matrix: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findSquare(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func findSquare(matrix [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer[]}
def find_square(matrix)
    
end
```

### Scala

```scala
object Solution {
    def findSquare(matrix: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_square(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-square matrix)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_square(Matrix :: [[integer()]]) -> [integer()].
find_square(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_square(matrix :: [[integer]]) :: [integer]
  def find_square(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findSquare(matrix: Array<Array<Int64>>): Array<Int64> {

    }
}
```

