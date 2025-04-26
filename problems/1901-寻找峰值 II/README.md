# 1901. 寻找峰值 II

## 题目描述

<p>一个 2D 网格中的 <strong>峰值</strong><strong> </strong>是指那些 <strong>严格大于 </strong>其相邻格子(上、下、左、右)的元素。</p>

<p>给你一个<strong> 从 0 开始编号 </strong>的 <code>m x n</code> 矩阵 <code>mat</code> ，其中任意两个相邻格子的值都<strong> 不相同</strong> 。找出 <strong>任意一个 峰值</strong> <code>mat[i][j]</code> 并 <strong>返回其位置 </strong><code>[i,j]</code> 。</p>

<p>你可以假设整个矩阵周边环绕着一圈值为 <code>-1</code> 的格子。</p>

<p>要求必须写出时间复杂度为 <code>O(m log(n))</code> 或 <code>O(n log(m))</code> 的算法</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/1.png" style="width: 206px; height: 209px;" /></p>

<pre>
<strong>输入:</strong> mat = [[1,4],[3,2]]
<strong>输出:</strong> [0,1]
<strong>解释:</strong>&nbsp;3 和 4 都是峰值，所以[1,0]和[0,1]都是可接受的答案。
</pre>

<p><strong>示例 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/07/3.png" style="width: 254px; height: 257px;" /></strong></p>

<pre>
<strong>输入:</strong> mat = [[10,20,15],[21,30,14],[7,16,32]]
<strong>输出:</strong> [1,1]
<strong>解释:</strong>&nbsp;30 和 32 都是峰值，所以[1,1]和[2,2]都是可接受的答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
	<li>任意两个相邻元素均不相等.</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 矩阵

## 提示

1. Let's assume that the width of the array is bigger than the height, otherwise, we will split in another direction.
2. Split the array into three parts: central column left side and right side.
3. Go through the central column and two neighbor columns and look for maximum.
4. If it's in the central column - this is our peak.
5. If it's on the left side, run this algorithm on subarray left_side + central_column.
6. If it's on the right side, run this algorithm on subarray right_side + central_column

## 示例

```
[[1,4],[3,2]]
[[10,20,15],[21,30,14],[7,16,32]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findPeakGrid(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPeakGrid(int** mat, int matSize, int* matColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindPeakGrid(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findPeakGrid = function(mat) {
    
};
```

### TypeScript

```typescript
function findPeakGrid(mat: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function findPeakGrid($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPeakGrid(_ mat: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPeakGrid(mat: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findPeakGrid(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func findPeakGrid(mat [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer[]}
def find_peak_grid(mat)
    
end
```

### Scala

```scala
object Solution {
    def findPeakGrid(mat: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_peak_grid(mat: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-peak-grid mat)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_peak_grid(Mat :: [[integer()]]) -> [integer()].
find_peak_grid(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_peak_grid(mat :: [[integer]]) :: [integer]
  def find_peak_grid(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPeakGrid(mat: Array<Array<Int64>>): Array<Int64> {

    }
}
```

