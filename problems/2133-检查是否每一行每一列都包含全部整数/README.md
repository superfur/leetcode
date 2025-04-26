# 2133. 检查是否每一行每一列都包含全部整数

## 题目描述

<p>对一个大小为 <code>n x n</code> 的矩阵而言，如果其每一行和每一列都包含从 <code>1</code> 到 <code>n</code> 的 <strong>全部</strong> 整数（含 <code>1</code> 和 <code>n</code>），则认为该矩阵是一个 <strong>有效</strong> 矩阵。</p>

<p>给你一个大小为 <code>n x n</code> 的整数矩阵 <code>matrix</code> ，请你判断矩阵是否为一个有效矩阵：如果是，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/example1drawio.png" style="width: 250px; height: 251px;" /></p>

<pre>
<strong>输入：</strong>matrix = [[1,2,3],[3,1,2],[2,3,1]]
<strong>输出：</strong>true
<strong>解释：</strong>在此例中，n = 3 ，每一行和每一列都包含数字 1、2、3 。
因此，返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/example2drawio.png" style="width: 250px; height: 251px;" /></p>

<pre>
<strong>输入：</strong>matrix = [[1,1,1],[1,2,3],[1,2,3]]
<strong>输出：</strong>false
<strong>解释：</strong>在此例中，n = 3 ，但第一行和第一列不包含数字 2 和 3 。
因此，返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= matrix[i][j] &lt;= n</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 矩阵

## 提示

1. Use for loops to check each row for every number from 1 to n. Similarly, do the same for each column.
2. For each check, you can keep a set of the unique elements in the checked row/col. By the end of the check, the size of the set should be n.

## 示例

```
[[1,2,3],[3,1,2],[2,3,1]]
[[1,1,1],[1,2,3],[1,2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkValid(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
```

### C

```c
bool checkValid(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckValid(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var checkValid = function(matrix) {
    
};
```

### TypeScript

```typescript
function checkValid(matrix: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Boolean
     */
    function checkValid($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkValid(_ matrix: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkValid(matrix: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkValid(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func checkValid(matrix [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Boolean}
def check_valid(matrix)
    
end
```

### Scala

```scala
object Solution {
    def checkValid(matrix: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_valid(matrix: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-valid matrix)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec check_valid(Matrix :: [[integer()]]) -> boolean().
check_valid(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_valid(matrix :: [[integer]]) :: boolean
  def check_valid(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkValid(matrix: Array<Array<Int64>>): Bool {

    }
}
```

