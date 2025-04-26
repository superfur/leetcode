# 85. 最大矩形

## 题目描述

<p>给定一个仅包含&nbsp;<code>0</code> 和 <code>1</code> 、大小为 <code>rows x cols</code> 的二维二进制矩阵，找出只包含 <code>1</code> 的最大矩形，并返回其面积。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1722912576-boIxpm-image.png" style="width: 402px; height: 322px;" />
<pre>
<strong>输入：</strong>matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>输出：</strong>6
<strong>解释：</strong>最大矩形如上图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["0"]]
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["1"]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rows == matrix.length</code></li>
	<li><code>cols == matrix[0].length</code></li>
	<li><code>1 &lt;= row, cols &lt;= 200</code></li>
	<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数组
- 动态规划
- 矩阵
- 单调栈

## 示例

```
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
[["0"]]
[["1"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximalRectangle(char[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
```

### C

```c
int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximalRectangle(char[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    
};
```

### TypeScript

```typescript
function maximalRectangle(matrix: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $matrix
     * @return Integer
     */
    function maximalRectangle($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximalRectangle(List<List<String>> matrix) {
    
  }
}
```

### Go

```golang
func maximalRectangle(matrix [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
    
end
```

### Scala

```scala
object Solution {
    def maximalRectangle(matrix: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximal-rectangle matrix)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximal_rectangle(Matrix :: [[char()]]) -> integer().
maximal_rectangle(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximal_rectangle(matrix :: [[char]]) :: integer
  def maximal_rectangle(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximalRectangle(matrix: Array<Array<Rune>>): Int64 {

    }
}
```

