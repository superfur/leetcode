# 面试题 17.24. 最大子矩阵

## 题目描述

<p>给定一个正整数、负整数和 0 组成的 N &times; M&nbsp;矩阵，编写代码找出元素总和最大的子矩阵。</p>

<p>返回一个数组 <code>[r1, c1, r2, c2]</code>，其中 <code>r1</code>, <code>c1</code> 分别代表子矩阵左上角的行号和列号，<code>r2</code>, <code>c2</code> 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。</p>

<p><strong>注意：</strong>本题相对书上原题稍作改动</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：
</strong><code>[
&nbsp;  [-1,<strong>0</strong>],
&nbsp;  [0,-1]
]</code>
<strong>输出：</strong>[0,1,0,1]
<strong>解释：</strong>输入中标粗的元素即为输出所表示的矩阵</pre>

<p>&nbsp;</p>

<p><strong>说明：</strong></p>

<ul>
	<li><code>1 &lt;= matrix.length, matrix[0].length &lt;= 200</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵
- 前缀和

## 提示

1. 从蛮力解法开始。
2. 蛮力解法要求连续计算每个矩阵的和。能优化它吗？
3. 你能做任何形式的预计算来使计算子矩阵和的运行时间为O(1)吗？
4. 如果你预先计算从左上角开始并扩展到全部单元格的子矩阵的和会怎样？计算它需要多长时间？计算完以后，你能在O(1)时间内得到任意子矩阵的和吗？
5. 如果你能预先计算从左上角到每个单元格的和，那么便可以在O(1)时间内用它来计算任意子矩阵的和。画一个特定的子矩阵。这个子矩阵上面的数组（C）、左边的数组（B），以及上边和左边的数组（A）的和均分别预先计算完成。你如何计算目标矩阵（D）的和？
6. D的和将是sum(A&B&C&D) - sum(A&B) - sum(A&C) + sum(A)。
7. 通过预计算，你应该能够得到O(N4)的时间复杂度。可以更快些吗?
8. 假设这只是一个数组。如何计算有最大和的子数组呢？详见16.17。
9. 假设我只是想让你找出从第r1行开始到第r2行结束的最大子矩阵，怎么才能最有效地做到这一点（参见前面的提示）？如果我现在让你找出从r1到(r2+2)的最大子数组，你能有效地做到吗?

## 示例

```
[[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getMaxMatrix(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getMaxMatrix(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaxMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getMaxMatrix(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetMaxMatrix(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var getMaxMatrix = function(matrix) {
    
};
```

### TypeScript

```typescript
function getMaxMatrix(matrix: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[]
     */
    function getMaxMatrix($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaxMatrix(_ matrix: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaxMatrix(matrix: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getMaxMatrix(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func getMaxMatrix(matrix [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer[]}
def get_max_matrix(matrix)
    
end
```

### Scala

```scala
object Solution {
    def getMaxMatrix(matrix: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_max_matrix(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-max-matrix matrix)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_max_matrix(Matrix :: [[integer()]]) -> [integer()].
get_max_matrix(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_max_matrix(matrix :: [[integer]]) :: [integer]
  def get_max_matrix(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaxMatrix(matrix: Array<Array<Int64>>): Array<Int64> {

    }
}
```

