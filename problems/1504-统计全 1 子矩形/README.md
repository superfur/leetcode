# 1504. 统计全 1 子矩形

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的二进制矩阵&nbsp;<code>mat</code>&nbsp;，请你返回有多少个&nbsp;<strong>子矩形</strong>&nbsp;的元素全部都是 1 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/10/27/ones1-grid.jpg" /></p>

<pre>
<strong>输入：</strong>mat = [[1,0,1],[1,1,0],[1,1,0]]
<strong>输出：</strong>13
<strong>解释：
</strong>有 <strong>6</strong>&nbsp;个 1x1 的矩形。
有 <strong>2</strong> 个 1x2 的矩形。
有 <strong>3</strong> 个 2x1 的矩形。
有 <strong>1</strong> 个 2x2 的矩形。
有 <strong>1</strong> 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = <strong>13</strong>&nbsp;。
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/10/27/ones2-grid.jpg" /></p>

<pre>
<strong>输入：</strong>mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
<strong>输出：</strong>24
<strong>解释：</strong>
有 <strong>8</strong> 个 1x1 的子矩形。
有 <strong>5</strong> 个 1x2 的子矩形。
有 <strong>2</strong> 个 1x3 的子矩形。
有 <strong>4</strong> 个 2x1 的子矩形。
有 <strong>2</strong> 个 2x2 的子矩形。
有 <strong>2</strong> 个 3x1 的子矩形。
有 <strong>1</strong> 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = <strong>24</strong><strong> 。</strong>

</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 150</code></li>
	<li><code>mat[i][j]</code>&nbsp;仅包含&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 动态规划
- 矩阵
- 单调栈

## 提示

1. For each row i, create an array nums where:  if mat[i][j] == 0 then nums[j] = 0 else nums[j] = nums[j-1] +1.
2. In the row i, number of rectangles between column j and k(inclusive) and ends in row i, is equal to SUM(min(nums[j, .. idx])) where idx go from j to k.  Expected solution is O(n^3).

## 示例

```
[[1,0,1],[1,1,0],[1,1,0]]
[[0,1,1,0],[0,1,1,1],[1,1,1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSubmat(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
```

### C

```c
int numSubmat(int** mat, int matSize, int* matColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSubmat(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSubmat = function(mat) {
    
};
```

### TypeScript

```typescript
function numSubmat(mat: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSubmat($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSubmat(_ mat: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSubmat(mat: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSubmat(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func numSubmat(mat [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer}
def num_submat(mat)
    
end
```

### Scala

```scala
object Solution {
    def numSubmat(mat: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_submat(mat: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-submat mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_submat(Mat :: [[integer()]]) -> integer().
num_submat(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_submat(mat :: [[integer]]) :: integer
  def num_submat(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSubmat(mat: Array<Array<Int64>>): Int64 {

    }
}
```

