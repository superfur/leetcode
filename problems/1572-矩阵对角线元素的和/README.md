# 1572. 矩阵对角线元素的和

## 题目描述

<p>给你一个正方形矩阵 <code>mat</code>，请你返回矩阵对角线元素的和。</p>

<p>请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp; 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png" style="height:174px; width:336px" /></p>

<pre>
<strong>输入：</strong>mat = [[<strong>1</strong>,2,<strong>3</strong>],
&nbsp;           [4,<strong>5</strong>,6],
&nbsp;           [<strong>7</strong>,8,<strong>9</strong>]]
<strong>输出：</strong>25
<strong>解释：</strong>对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。
</pre>

<p><strong>示例&nbsp; 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[<strong>1</strong>,1,1,<strong>1</strong>],
&nbsp;           [1,<strong>1</strong>,<strong>1</strong>,1],
&nbsp;           [1,<strong>1</strong>,<strong>1</strong>,1],
&nbsp;           [<strong>1</strong>,1,1,<strong>1</strong>]]
<strong>输出：</strong>8
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>mat = [[<strong>5</strong>]]
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == mat.length == mat[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. There will be overlap of elements in the primary and secondary diagonals if and only if the length of the matrix is odd, which is at the center.

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
[[5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int diagonalSum(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
```

### C

```c
int diagonalSum(int** mat, int matSize, int* matColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DiagonalSum(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    
};
```

### TypeScript

```typescript
function diagonalSum(mat: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function diagonalSum($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func diagonalSum(_ mat: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun diagonalSum(mat: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int diagonalSum(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func diagonalSum(mat [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer}
def diagonal_sum(mat)
    
end
```

### Scala

```scala
object Solution {
    def diagonalSum(mat: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (diagonal-sum mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec diagonal_sum(Mat :: [[integer()]]) -> integer().
diagonal_sum(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec diagonal_sum(mat :: [[integer]]) :: integer
  def diagonal_sum(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func diagonalSum(mat: Array<Array<Int64>>): Int64 {

    }
}
```

