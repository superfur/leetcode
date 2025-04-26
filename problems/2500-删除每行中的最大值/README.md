# 2500. 删除每行中的最大值

## 题目描述

<p>给你一个 <code>m x n</code> 大小的矩阵 <code>grid</code> ，由若干正整数组成。</p>

<p>执行下述操作，直到 <code>grid</code> 变为空矩阵：</p>

<ul>
	<li>从每一行删除值最大的元素。如果存在多个这样的值，删除其中任何一个。</li>
	<li>将删除元素中的最大值与答案相加。</li>
</ul>

<p><strong>注意</strong> 每执行一次操作，矩阵中列的数据就会减 1 。</p>

<p>返回执行上述操作后的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/q1ex1.jpg" style="width: 600px; height: 135px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,2,4],[3,3,1]]
<strong>输出：</strong>8
<strong>解释：</strong>上图展示在每一步中需要移除的值。
- 在第一步操作中，从第一行删除 4 ，从第二行删除 3（注意，有两个单元格中的值为 3 ，我们可以删除任一）。在答案上加 4 。
- 在第二步操作中，从第一行删除 2 ，从第二行删除 3 。在答案上加 3 。
- 在第三步操作中，从第一行删除 1 ，从第二行删除 1 。在答案上加 1 。
最终，答案 = 4 + 3 + 1 = 8 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/q1ex2.jpg" style="width: 83px; height: 83px;" /></p>

<pre>
<strong>输入：</strong>grid = [[10]]
<strong>输出：</strong>10
<strong>解释：</strong>上图展示在每一步中需要移除的值。
- 在第一步操作中，从第一行删除 10 。在答案上加 10 。
最终，答案 = 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵
- 排序
- 模拟
- 堆（优先队列）

## 提示

1. Iterate from the first to the last row and if there exist some unmarked cells, take a maximum from them and mark that cell as visited.
2. Add a maximum of newly marked cells to answer and repeat that operation until the whole matrix becomes marked.

## 示例

```
[[1,2,4],[3,3,1]]
[[10]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int deleteGreatestValue(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int deleteGreatestValue(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int deleteGreatestValue(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DeleteGreatestValue(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var deleteGreatestValue = function(grid) {
    
};
```

### TypeScript

```typescript
function deleteGreatestValue(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function deleteGreatestValue($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func deleteGreatestValue(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun deleteGreatestValue(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int deleteGreatestValue(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func deleteGreatestValue(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def delete_greatest_value(grid)
    
end
```

### Scala

```scala
object Solution {
    def deleteGreatestValue(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn delete_greatest_value(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (delete-greatest-value grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec delete_greatest_value(Grid :: [[integer()]]) -> integer().
delete_greatest_value(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec delete_greatest_value(grid :: [[integer]]) :: integer
  def delete_greatest_value(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func deleteGreatestValue(grid: Array<Array<Int64>>): Int64 {

    }
}
```

