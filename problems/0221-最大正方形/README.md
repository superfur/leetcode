# 221. 最大正方形

## 题目描述

<p>在一个由 <code>'0'</code> 和 <code>'1'</code> 组成的二维矩阵内，找到只包含 <code>'1'</code> 的最大正方形，并返回其面积。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;" />
<pre>
<strong>输入：</strong>matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" style="width: 165px; height: 165px;" />
<pre>
<strong>输入：</strong>matrix = [["0","1"],["1","0"]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["0"]]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 300</code></li>
	<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 示例

```
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
[["0","1"],["1","0"]]
[["0"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
```

### C

```c
int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximalSquare(char[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    
};
```

### TypeScript

```typescript
function maximalSquare(matrix: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $matrix
     * @return Integer
     */
    function maximalSquare($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximalSquare(_ matrix: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximalSquare(matrix: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximalSquare(List<List<String>> matrix) {
    
  }
}
```

### Go

```golang
func maximalSquare(matrix [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} matrix
# @return {Integer}
def maximal_square(matrix)
    
end
```

### Scala

```scala
object Solution {
    def maximalSquare(matrix: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximal-square matrix)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximal_square(Matrix :: [[char()]]) -> integer().
maximal_square(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximal_square(matrix :: [[char]]) :: integer
  def maximal_square(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximalSquare(matrix: Array<Array<Rune>>): Int64 {

    }
}
```

