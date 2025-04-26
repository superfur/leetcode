# 1981. 最小化目标值与所选元素的差

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的整数矩阵 <code>mat</code> 和一个整数 <code>target</code> 。</p>

<p>从矩阵的 <strong>每一行</strong> 中选择一个整数，你的目标是&nbsp;<strong>最小化</strong>&nbsp;所有选中元素之&nbsp;<strong>和</strong>&nbsp;与目标值 <code>target</code> 的 <strong>绝对差</strong> 。</p>

<p>返回 <strong>最小的绝对差</strong> 。</p>

<p><code>a</code> 和 <code>b</code> 两数字的 <strong>绝对差</strong> 是 <code>a - b</code> 的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/matrix1.png" style="width: 181px; height: 181px;" /></p>

<pre>
<strong>输入：</strong>mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
<strong>输出：</strong>0
<strong>解释：</strong>一种可能的最优选择方案是：
- 第一行选出 1
- 第二行选出 5
- 第三行选出 7
所选元素的和是 13 ，等于目标值，所以绝对差是 0 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/matrix1-1.png" style="width: 61px; height: 181px;" /></p>

<pre>
<strong>输入：</strong>mat = [[1],[2],[3]], target = 100
<strong>输出：</strong>94
<strong>解释：</strong>唯一一种选择方案是：
- 第一行选出 1
- 第二行选出 2
- 第三行选出 3
所选元素的和是 6 ，绝对差是 94 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/matrix1-3.png" style="width: 301px; height: 61px;" /></p>

<pre>
<strong>输入：</strong>mat = [[1,2,9,8,7]], target = 6
<strong>输出：</strong>1
<strong>解释：</strong>最优的选择方案是选出第一行的 7 。
绝对差是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 70</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 70</code></li>
	<li><code>1 &lt;= target &lt;= 800</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. The sum of chosen elements will not be too large. Consider using a hash set to record all possible sums while iterating each row.
2. Instead of keeping track of all possible sums, since in each row, we are adding positive numbers, only keep those that can be a candidate, not exceeding the target by too much.

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
13
[[1],[2],[3]]
100
[[1,2,9,8,7]]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizeTheDifference(vector<vector<int>>& mat, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizeTheDifference(int[][] mat, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
```

### C

```c
int minimizeTheDifference(int** mat, int matSize, int* matColSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizeTheDifference(int[][] mat, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} target
 * @return {number}
 */
var minimizeTheDifference = function(mat, target) {
    
};
```

### TypeScript

```typescript
function minimizeTheDifference(mat: number[][], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $target
     * @return Integer
     */
    function minimizeTheDifference($mat, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeTheDifference(_ mat: [[Int]], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeTheDifference(mat: Array<IntArray>, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizeTheDifference(List<List<int>> mat, int target) {
    
  }
}
```

### Go

```golang
func minimizeTheDifference(mat [][]int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer} target
# @return {Integer}
def minimize_the_difference(mat, target)
    
end
```

### Scala

```scala
object Solution {
    def minimizeTheDifference(mat: Array[Array[Int]], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_the_difference(mat: Vec<Vec<i32>>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-the-difference mat target)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimize_the_difference(Mat :: [[integer()]], Target :: integer()) -> integer().
minimize_the_difference(Mat, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_the_difference(mat :: [[integer]], target :: integer) :: integer
  def minimize_the_difference(mat, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeTheDifference(mat: Array<Array<Int64>>, target: Int64): Int64 {

    }
}
```

