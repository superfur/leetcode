# 498. 对角线遍历

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的矩阵 <code>mat</code> ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;" />
<pre>
<strong>输入：</strong>mat = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>[1,2,4,7,5,3,6,8,9]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,2],[3,4]]
<strong>输出：</strong>[1,2,3,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 模拟

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2],[3,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDiagonalOrder(int** mat, int matSize, int* matColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindDiagonalOrder(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function(mat) {
    
};
```

### TypeScript

```typescript
function findDiagonalOrder(mat: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function findDiagonalOrder($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDiagonalOrder(_ mat: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findDiagonalOrder(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func findDiagonalOrder(mat [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer[]}
def find_diagonal_order(mat)
    
end
```

### Scala

```scala
object Solution {
    def findDiagonalOrder(mat: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-diagonal-order mat)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_diagonal_order(Mat :: [[integer()]]) -> [integer()].
find_diagonal_order(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_diagonal_order(mat :: [[integer]]) :: [integer]
  def find_diagonal_order(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDiagonalOrder(mat: Array<Array<Int64>>): Array<Int64> {

    }
}
```

