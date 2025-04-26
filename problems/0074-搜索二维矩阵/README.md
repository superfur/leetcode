# 74. 搜索二维矩阵

## 题目描述

<p>给你一个满足下述两条属性的 <code>m x n</code> 整数矩阵：</p>

<ul>
	<li>每行中的整数从左到右按非严格递增顺序排列。</li>
	<li>每行的第一个整数大于前一行的最后一个整数。</li>
</ul>

<p>给你一个整数 <code>target</code> ，如果 <code>target</code> 在矩阵中，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-10<sup>4</sup> &lt;= matrix[i][j], target &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 矩阵

## 示例

```
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
3
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
13
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
```

### C

```c
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    
};
```

### TypeScript

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Boolean
     */
    function searchMatrix($matrix, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool searchMatrix(List<List<int>> matrix, int target) {
    
  }
}
```

### Go

```golang
func searchMatrix(matrix [][]int, target int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
    
end
```

### Scala

```scala
object Solution {
    def searchMatrix(matrix: Array[Array[Int]], target: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (search-matrix matrix target)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec search_matrix(Matrix :: [[integer()]], Target :: integer()) -> boolean().
search_matrix(Matrix, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec search_matrix(matrix :: [[integer]], target :: integer) :: boolean
  def search_matrix(matrix, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func searchMatrix(matrix: Array<Array<Int64>>, target: Int64): Bool {

    }
}
```

