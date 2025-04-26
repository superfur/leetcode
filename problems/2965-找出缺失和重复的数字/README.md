# 2965. 找出缺失和重复的数字

## 题目描述

<p>给你一个下标从<strong> 0 </strong>开始的二维整数矩阵 <code><font face="monospace">grid</font></code>，大小为 <code>n * n</code> ，其中的值在 <code>[1, n<sup>2</sup>]</code> 范围内。除了 <code>a</code> 出现 <strong>两次</strong>，<code>b</code> <strong>缺失</strong> 之外，每个整数都<strong> 恰好出现一次</strong> 。</p>

<p>任务是找出重复的数字<code>a</code> 和缺失的数字 <code>b</code> 。</p>

<p>返回一个下标从 0 开始、长度为 <code>2</code> 的整数数组 <code>ans</code> ，其中 <code>ans[0]</code> 等于 <code>a</code> ，<code>ans[1]</code> 等于 <code>b</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,3],[2,2]]
<strong>输出：</strong>[2,4]
<strong>解释：</strong>数字 2 重复，数字 4 缺失，所以答案是 [2,4] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[9,1,7],[8,9,2],[3,4,6]]
<strong>输出：</strong>[9,5]
<strong>解释：</strong>数字 9 重复，数字 5 缺失，所以答案是 [9,5] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == grid.length == grid[i].length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= n * n</code></li>
	<li>对于所有满足<code>1 &lt;= x &lt;= n * n</code> 的 <code>x</code> ，恰好存在一个 <code>x</code> 与矩阵中的任何成员都不相等。</li>
	<li>对于所有满足<code>1 &lt;= x &lt;= n * n</code> 的 <code>x</code> ，恰好存在一个 <code>x</code> 与矩阵中的两个成员相等。</li>
	<li>除上述的两个之外，对于所有满足<code>1 &lt;= x &lt;= n * n</code> 的 <code>x</code> ，都恰好存在一对 <code>i, j</code> 满足 <code>0 &lt;= i, j &lt;= n - 1</code> 且 <code>grid[i][j] == x</code> 。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 数学
- 矩阵

## 示例

```
[[1,3],[2,2]]
[[9,1,7],[8,9,2],[3,4,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMissingAndRepeatedValues(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindMissingAndRepeatedValues(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    
};
```

### TypeScript

```typescript
function findMissingAndRepeatedValues(grid: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function findMissingAndRepeatedValues($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMissingAndRepeatedValues(_ grid: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMissingAndRepeatedValues(grid: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findMissingAndRepeatedValues(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func findMissingAndRepeatedValues(grid [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[]}
def find_missing_and_repeated_values(grid)
    
end
```

### Scala

```scala
object Solution {
    def findMissingAndRepeatedValues(grid: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-missing-and-repeated-values grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_missing_and_repeated_values(Grid :: [[integer()]]) -> [integer()].
find_missing_and_repeated_values(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_missing_and_repeated_values(grid :: [[integer]]) :: [integer]
  def find_missing_and_repeated_values(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMissingAndRepeatedValues(grid: Array<Array<Int64>>): Array<Int64> {

    }
}
```

