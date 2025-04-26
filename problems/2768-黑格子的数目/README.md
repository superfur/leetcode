# 2768. 黑格子的数目

## 题目描述

<p>给你两个整数&nbsp;<code>m</code> 和&nbsp;<code>n</code>&nbsp;，表示一个下标从 <strong>0</strong>&nbsp;开始的&nbsp;<code>m x n</code>&nbsp;的网格图。</p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数矩阵&nbsp;<code>coordinates</code>&nbsp;，其中&nbsp;<code>coordinates[i] = [x, y]</code>&nbsp;表示坐标为&nbsp;<code>[x, y]</code>&nbsp;的格子是 <strong>黑色的</strong>&nbsp;，所有没出现在&nbsp;<code>coordinates</code>&nbsp;中的格子都是 <strong>白色的</strong>。</p>

<p>一个块定义为网格图中&nbsp;<code>2 x 2</code>&nbsp;的一个子矩阵。更正式的，对于左上角格子为 <code>[x, y]</code> 的块，其中 <code>0 &lt;= x &lt; m - 1</code> 且&nbsp;<code>0 &lt;= y &lt; n - 1</code> ，包含坐标为&nbsp;<code>[x, y]</code>&nbsp;，<code>[x + 1, y]</code>&nbsp;，<code>[x, y + 1]</code>&nbsp;和&nbsp;<code>[x + 1, y + 1]</code>&nbsp;的格子。</p>

<p>请你返回一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>5</code>&nbsp;的整数数组&nbsp;<code>arr</code>&nbsp;，<code>arr[i]</code>&nbsp;表示恰好包含&nbsp;<code>i</code>&nbsp;个&nbsp;<strong>黑色</strong>&nbsp;格子的块的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>m = 3, n = 3, coordinates = [[0,0]]
<b>输出：</b>[3,1,0,0,0]
<b>解释：</b>网格图如下：
<img alt="" src="https://assets.leetcode.com/uploads/2023/06/18/screen-shot-2023-06-18-at-44656-am.png" style="width: 150px; height: 128px;" />
只有 1 个块有一个黑色格子，这个块是左上角为 [0,0] 的块。
其他 3 个左上角分别为 [0,1] ，[1,0] 和 [1,1] 的块都有 0 个黑格子。
所以我们返回 [3,1,0,0,0] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]
<b>输出：</b>[0,2,2,0,0]
<b>解释：</b>网格图如下：
<img alt="" src="https://assets.leetcode.com/uploads/2023/06/18/screen-shot-2023-06-18-at-45018-am.png" style="width: 150px; height: 128px;" />
有 2 个块有 2 个黑色格子（左上角格子分别为 [0,0] 和 [0,1]）。
左上角为 [1,0] 和 [1,1] 的两个块，都有 1 个黑格子。
所以我们返回 [0,2,2,0,0] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= coordinates.length &lt;= 10<sup>4</sup></code></li>
	<li><code>coordinates[i].length == 2</code></li>
	<li><code>0 &lt;= coordinates[i][0] &lt; m</code></li>
	<li><code>0 &lt;= coordinates[i][1] &lt; n</code></li>
	<li><code>coordinates</code>&nbsp;中的坐标对两两互不相同。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 枚举

## 提示

1. The number of blocks is too much but the number of black cells is less than that.
2. It means the number of blocks with at least one black cell is O(|coordinates|). let’s just hold them.
3. Iterate through the coordinates and update the block counts accordingly. For each coordinate, determine which block(s) it belongs to and increment the count of black cells for those block(s).
4. After processing all the coordinates, count the number of blocks with different numbers of black cells. You can use another data structure to keep track of the counts of blocks with 0 black cells, 1 black cell, and so on.

## 示例

```
3
3
[[0,0]]
3
3
[[0,0],[1,1],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> countBlackBlocks(int m, int n, vector<vector<int>>& coordinates) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] countBlackBlocks(int m, int n, int[][] coordinates) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        """
        :type m: int
        :type n: int
        :type coordinates: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countBlackBlocks(int m, int n, int** coordinates, int coordinatesSize, int* coordinatesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] CountBlackBlocks(int m, int n, int[][] coordinates) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} coordinates
 * @return {number[]}
 */
var countBlackBlocks = function(m, n, coordinates) {
    
};
```

### TypeScript

```typescript
function countBlackBlocks(m: number, n: number, coordinates: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $coordinates
     * @return Integer[]
     */
    function countBlackBlocks($m, $n, $coordinates) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countBlackBlocks(_ m: Int, _ n: Int, _ coordinates: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countBlackBlocks(m: Int, n: Int, coordinates: Array<IntArray>): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countBlackBlocks(int m, int n, List<List<int>> coordinates) {
    
  }
}
```

### Go

```golang
func countBlackBlocks(m int, n int, coordinates [][]int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} coordinates
# @return {Integer[]}
def count_black_blocks(m, n, coordinates)
    
end
```

### Scala

```scala
object Solution {
    def countBlackBlocks(m: Int, n: Int, coordinates: Array[Array[Int]]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_black_blocks(m: i32, n: i32, coordinates: Vec<Vec<i32>>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (count-black-blocks m n coordinates)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_black_blocks(M :: integer(), N :: integer(), Coordinates :: [[integer()]]) -> [integer()].
count_black_blocks(M, N, Coordinates) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_black_blocks(m :: integer, n :: integer, coordinates :: [[integer]]) :: [integer]
  def count_black_blocks(m, n, coordinates) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countBlackBlocks(m: Int64, n: Int64, coordinates: Array<Array<Int64>>): Array<Int64> {

    }
}
```

