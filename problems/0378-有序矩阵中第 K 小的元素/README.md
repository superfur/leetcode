# 378. 有序矩阵中第 K 小的元素

## 题目描述

<p>给你一个&nbsp;<code>n x n</code><em>&nbsp;</em>矩阵&nbsp;<code>matrix</code> ，其中每行和每列元素均按升序排序，找到矩阵中第 <code>k</code> 小的元素。<br />
请注意，它是 <strong>排序后</strong> 的第 <code>k</code> 小元素，而不是第 <code>k</code> 个 <strong>不同</strong> 的元素。</p>

<p>你必须找到一个内存复杂度优于&nbsp;<code>O(n<sup>2</sup>)</code> 的解决方案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
<strong>输出：</strong>13
<strong>解释：</strong>矩阵中的元素为 [1,5,9,10,11,12,13,<strong>13</strong>,15]，第 8 小元素是 13
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[-5]], k = 1
<strong>输出：</strong>-5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>题目数据 <strong>保证</strong> <code>matrix</code> 中的所有行和列都按 <strong>非递减顺序</strong> 排列</li>
	<li><code>1 &lt;= k &lt;= n<sup>2</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你能否用一个恒定的内存(即 <code>O(1)</code> 内存复杂度)来解决这个问题?</li>
	<li>你能在 <code>O(n)</code> 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（&nbsp;<a href="http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf" target="_blank">this paper</a>&nbsp;）很有趣。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 矩阵
- 排序
- 堆（优先队列）

## 示例

```
[[1,5,9],[10,11,13],[12,13,15]]
8
[[-5]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
```

### C

```c
int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KthSmallest(int[][] matrix, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
    
};
```

### TypeScript

```typescript
function kthSmallest(matrix: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function kthSmallest($matrix, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthSmallest(_ matrix: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthSmallest(matrix: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kthSmallest(List<List<int>> matrix, int k) {
    
  }
}
```

### Go

```golang
func kthSmallest(matrix [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @param {Integer} k
# @return {Integer}
def kth_smallest(matrix, k)
    
end
```

### Scala

```scala
object Solution {
    def kthSmallest(matrix: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_smallest(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (kth-smallest matrix k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec kth_smallest(Matrix :: [[integer()]], K :: integer()) -> integer().
kth_smallest(Matrix, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_smallest(matrix :: [[integer]], k :: integer) :: integer
  def kth_smallest(matrix, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthSmallest(matrix: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

