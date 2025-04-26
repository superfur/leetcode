# 1582. 二进制矩阵中的特殊位置

## 题目描述

<p>给定一个 <code>m x n</code> 的二进制矩阵 <code>mat</code>，返回矩阵 <code>mat</code> 中特殊位置的数量。</p>

<p>如果位置 <code>(i, j)</code> 满足 <code>mat[i][j] == 1</code> 并且行 <code>i</code> 与列 <code>j</code> 中的所有其他元素都是 <code>0</code>（行和列的下标从 <strong>0 </strong>开始计数），那么它被称为<strong> 特殊 </strong>位置。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/special1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>mat = [[1,0,0],[0,0,1],[1,0,0]]
<strong>输出：</strong>1
<strong>解释：</strong>位置 (1, 2) 是一个特殊位置，因为 mat[1][2] == 1 且第 1 行和第 2 列的其他所有元素都是 0。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>mat = [[1,0,0],[0,1,0],[0,0,1]]
<strong>输出：</strong>3
<strong>解释：</strong>位置 (0, 0)，(1, 1) 和 (2, 2) 都是特殊位置。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>mat[i][j]</code> 是 <code>0</code> 或 <code>1</code>。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Keep track of 1s in each row and in each column. Then while iterating over matrix, if the current position is 1 and current row as well as current column contains exactly one occurrence of 1.

## 示例

```
[[1,0,0],[0,0,1],[1,0,0]]
[[1,0,0],[0,1,0],[0,0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSpecial(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
```

### C

```c
int numSpecial(int** mat, int matSize, int* matColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSpecial(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(mat) {
    
};
```

### TypeScript

```typescript
function numSpecial(mat: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSpecial($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSpecial(_ mat: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSpecial(mat: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSpecial(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func numSpecial(mat [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer}
def num_special(mat)
    
end
```

### Scala

```scala
object Solution {
    def numSpecial(mat: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-special mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_special(Mat :: [[integer()]]) -> integer().
num_special(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_special(mat :: [[integer]]) :: integer
  def num_special(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSpecial(mat: Array<Array<Int64>>): Int64 {

    }
}
```

