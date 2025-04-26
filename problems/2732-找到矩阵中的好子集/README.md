# 2732. 找到矩阵中的好子集

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始大小为&nbsp;<code>m x n</code>&nbsp;的二进制矩阵&nbsp;<code>grid</code>&nbsp;。</p>

<p>从原矩阵中选出若干行构成一个行的 <strong>非空&nbsp;</strong>子集，如果子集中任何一列的和至多为子集大小的一半，那么我们称这个子集是 <strong>好子集</strong>。</p>

<p>更正式的，如果选出来的行子集大小（即行的数量）为 k，那么每一列的和至多为&nbsp;<code>floor(k / 2)</code>&nbsp;。</p>

<p>请你返回一个整数数组，它包含好子集的行下标，请你将其&nbsp;<b>升序</b>&nbsp;返回。</p>

<p>如果有多个好子集，你可以返回任意一个。如果没有好子集，请你返回一个空数组。</p>

<p>一个矩阵 <code>grid</code>&nbsp;的行 <strong>子集</strong> ，是删除 <code>grid</code>&nbsp;中某些（也可能不删除）行后，剩余行构成的元素集合。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]
<b>输出：</b>[0,1]
<b>解释：</b>我们可以选择第 0 和第 1 行构成一个好子集。
选出来的子集大小为 2 。
- 第 0&nbsp;列的和为 0 + 0 = 0 ，小于等于子集大小的一半。
- 第 1&nbsp;列的和为 1 + 0 = 1 ，小于等于子集大小的一半。
- 第 2&nbsp;列的和为 1 + 0 = 1 ，小于等于子集大小的一半。
- 第 3&nbsp;列的和为 0 + 1 = 1 ，小于等于子集大小的一半。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>grid = [[0]]
<b>输出：</b>[0]
<strong>解释：</strong>我们可以选择第 0 行构成一个好子集。
选出来的子集大小为 1 。
- 第 0 列的和为 0 ，小于等于子集大小的一半。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>grid = [[1,1,1],[1,1,1]]
<b>输出：</b>[]
<b>解释：</b>没有办法得到一个好子集。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= n &lt;= 5</code></li>
	<li><code>grid[i][j]</code>&nbsp;要么是&nbsp;<code>0</code>&nbsp;，要么是&nbsp;<code>1</code> 。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 哈希表
- 矩阵

## 提示

1. It can be proven, that if there exists a good subset of rows then there exists a good subset of rows with the size of either 1 or 2.
2. To check if there exists a good subset of rows of size 1, we check if there exists a row containing only zeros, if it does, we return its index as a good subset.
3. To check if there exists a good subset of rows of size 2, we iterate over two bit-masks, check if both are presented in the array and if they form a good subset, if they do, return their indices as a good subset.

## 示例

```
[[0,1,1,0],[0,0,0,1],[1,1,1,1]]
[[0]]
[[1,1,1],[1,1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> goodSubsetofBinaryMatrix(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> goodSubsetofBinaryMatrix(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodSubsetofBinaryMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> GoodSubsetofBinaryMatrix(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var goodSubsetofBinaryMatrix = function(grid) {
    
};
```

### TypeScript

```typescript
function goodSubsetofBinaryMatrix(grid: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function goodSubsetofBinaryMatrix($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func goodSubsetofBinaryMatrix(_ grid: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun goodSubsetofBinaryMatrix(grid: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> goodSubsetofBinaryMatrix(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func goodSubsetofBinaryMatrix(grid [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[]}
def good_subsetof_binary_matrix(grid)
    
end
```

### Scala

```scala
object Solution {
    def goodSubsetofBinaryMatrix(grid: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn good_subsetof_binary_matrix(grid: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (good-subsetof-binary-matrix grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec good_subsetof_binary_matrix(Grid :: [[integer()]]) -> [integer()].
good_subsetof_binary_matrix(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec good_subsetof_binary_matrix(grid :: [[integer]]) :: [integer]
  def good_subsetof_binary_matrix(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func goodSubsetofBinaryMatrix(grid: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

