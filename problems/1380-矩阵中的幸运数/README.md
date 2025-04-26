# 1380. 矩阵中的幸运数

## 题目描述

<p>给你一个 <code>m x&nbsp;n</code> 的矩阵，矩阵中的数字 <strong>各不相同</strong> 。请你按 <strong>任意</strong> 顺序返回矩阵中的所有幸运数。</p>

<p><strong>幸运数</strong> 是指矩阵中满足同时下列两个条件的元素：</p>

<ul>
	<li>在同一行的所有元素中最小</li>
	<li>在同一列的所有元素中最大</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[3,7,8],[9,11,13],[15,16,17]]
<strong>输出：</strong>[15]
<strong>解释：</strong>15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
<strong>输出：</strong>[12]
<strong>解释：</strong>12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[7,8],[1,2]]
<strong>输出：</strong>[7]
<strong>解释：</strong>7 是唯一的幸运数字，因为它是行中的最小值，列中的最大值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 50</code></li>
	<li><code>1 &lt;=&nbsp;matrix[i][j]&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li>矩阵中的所有元素都是不同的</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Find out and save the minimum of each row and maximum of each column in two lists.
2. Then scan through the whole matrix to identify the elements that satisfy the criteria.

## 示例

```
[[3,7,8],[9,11,13],[15,16,17]]
[[1,10,4,2],[9,3,8,7],[15,16,17,12]]
[[7,8],[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* luckyNumbers(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> LuckyNumbers(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers = function(matrix) {
    
};
```

### TypeScript

```typescript
function luckyNumbers(matrix: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[]
     */
    function luckyNumbers($matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func luckyNumbers(_ matrix: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun luckyNumbers(matrix: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> luckyNumbers(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func luckyNumbers(matrix [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer[]}
def lucky_numbers(matrix)
    
end
```

### Scala

```scala
object Solution {
    def luckyNumbers(matrix: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn lucky_numbers(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (lucky-numbers matrix)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec lucky_numbers(Matrix :: [[integer()]]) -> [integer()].
lucky_numbers(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec lucky_numbers(matrix :: [[integer]]) :: [integer]
  def lucky_numbers(matrix) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func luckyNumbers(matrix: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

