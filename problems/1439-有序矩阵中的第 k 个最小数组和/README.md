# 1439. 有序矩阵中的第 k 个最小数组和

## 题目描述

<p>给你一个 <code>m&nbsp;* n</code> 的矩阵 <code>mat</code>，以及一个整数 <code>k</code> ，矩阵中的每一行都以非递减的顺序排列。</p>

<p>你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 <strong>最小</strong> 数组和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>mat = [[1,3,11],[2,4,6]], k = 5
<strong>输出：</strong>7
<strong>解释：</strong>从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。  </pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>mat = [[1,3,11],[2,4,6]], k = 9
<strong>输出：</strong>17
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
<strong>输出：</strong>9
<strong>解释：</strong>从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。 
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>mat = [[1,1,10],[2,2,9]], k = 7
<strong>输出：</strong>12
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat.length[i]</code></li>
	<li><code>1 &lt;= m, n &lt;= 40</code></li>
	<li><code>1 &lt;= k &lt;= min(200, n ^&nbsp;m)</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 5000</code></li>
	<li><code>mat[i]</code> 是一个非递减数组</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 矩阵
- 堆（优先队列）

## 提示

1. Save all visited sums and corresponding indexes in a priority queue. Then, once you pop the smallest sum so far, you can quickly identify the next m candidates for smallest sum by incrementing each row index by 1.

## 示例

```
[[1,3,11],[2,4,6]]
5
[[1,3,11],[2,4,6]]
9
[[1,10,10],[1,4,5],[2,3,6]]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kthSmallest(vector<vector<int>>& mat, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kthSmallest(int[][] mat, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
```

### C

```c
int kthSmallest(int** mat, int matSize, int* matColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KthSmallest(int[][] mat, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(mat, k) {
    
};
```

### TypeScript

```typescript
function kthSmallest(mat: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Integer
     */
    function kthSmallest($mat, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthSmallest(_ mat: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthSmallest(mat: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kthSmallest(List<List<int>> mat, int k) {
    
  }
}
```

### Go

```golang
func kthSmallest(mat [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer} k
# @return {Integer}
def kth_smallest(mat, k)
    
end
```

### Scala

```scala
object Solution {
    def kthSmallest(mat: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_smallest(mat: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (kth-smallest mat k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec kth_smallest(Mat :: [[integer()]], K :: integer()) -> integer().
kth_smallest(Mat, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_smallest(mat :: [[integer]], k :: integer) :: integer
  def kth_smallest(mat, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthSmallest(mat: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

