# 1292. 元素和小于等于阈值的正方形的最大边长

## 题目描述

<p>给你一个大小为&nbsp;<code>m x n</code>&nbsp;的矩阵&nbsp;<code>mat</code>&nbsp;和一个整数阈值&nbsp;<code>threshold</code>。</p>

<p>请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 <strong>0&nbsp;</strong>。<br />
&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/15/e1.png" style="height: 186px; width: 335px;" /></p>

<pre>
<strong>输入：</strong>mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
<strong>输出：</strong>2
<strong>解释：</strong>总和小于或等于 4 的正方形的最大边长为 2，如图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>0 &lt;= mat[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= threshold &lt;= 10<sup>5</sup></code><sup>&nbsp;</sup></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 矩阵
- 前缀和

## 提示

1. Store prefix sum of all grids in another 2D array.
2. Try all possible solutions and if you cannot find one return -1.
3. If x is a valid answer then any y < x is also valid answer. Use binary search to find answer.

## 示例

```
[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
4
[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
```

### C

```c
int maxSideLength(int** mat, int matSize, int* matColSize, int threshold) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSideLength(int[][] mat, int threshold) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} threshold
 * @return {number}
 */
var maxSideLength = function(mat, threshold) {
    
};
```

### TypeScript

```typescript
function maxSideLength(mat: number[][], threshold: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $threshold
     * @return Integer
     */
    function maxSideLength($mat, $threshold) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSideLength(_ mat: [[Int]], _ threshold: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSideLength(mat: Array<IntArray>, threshold: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSideLength(List<List<int>> mat, int threshold) {
    
  }
}
```

### Go

```golang
func maxSideLength(mat [][]int, threshold int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer} threshold
# @return {Integer}
def max_side_length(mat, threshold)
    
end
```

### Scala

```scala
object Solution {
    def maxSideLength(mat: Array[Array[Int]], threshold: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-side-length mat threshold)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_side_length(Mat :: [[integer()]], Threshold :: integer()) -> integer().
max_side_length(Mat, Threshold) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_side_length(mat :: [[integer]], threshold :: integer) :: integer
  def max_side_length(mat, threshold) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSideLength(mat: Array<Array<Int64>>, threshold: Int64): Int64 {

    }
}
```

