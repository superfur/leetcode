# 1284. 转化为全零矩阵的最少反转次数

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的二进制矩阵&nbsp;<code>mat</code>。每一步，你可以选择一个单元格并将它反转（反转表示 <code>0</code> 变 <code>1</code> ，<code>1</code> 变 <code>0</code> ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。相邻的两个单元格共享同一条边。</p>

<p>请你返回将矩阵&nbsp;<code>mat</code> 转化为全零矩阵的<em>最少反转次数</em>，如果无法转化为全零矩阵，请返回&nbsp;<code>-1</code>&nbsp;。</p>

<p><strong>二进制矩阵</strong>&nbsp;的每一个格子要么是 <code>0</code> 要么是 <code>1</code> 。</p>

<p><strong>全零矩阵</strong>&nbsp;是所有格子都为 <code>0</code> 的矩阵。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/13/matrix.png" /></p>

<pre>
<strong>输入：</strong>mat = [[0,0],[0,1]]
<strong>输出：</strong>3
<strong>解释：</strong>一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[0]]
<strong>输出：</strong>0
<strong>解释：</strong>给出的矩阵是全零矩阵，所以你不需要改变它。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,0,0],[1,0,0]]
<strong>输出：</strong>-1
<strong>解释：</strong>该矩阵无法转变成全零矩阵
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m ==&nbsp;mat.length</code></li>
	<li><code>n ==&nbsp;mat[0].length</code></li>
	<li><code>1 &lt;= m&nbsp;&lt;= 3</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 3</code></li>
	<li><code>mat[i][j]</code>&nbsp;是 0 或 1 。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 广度优先搜索
- 数组
- 哈希表
- 矩阵

## 提示

1. Flipping same index two times is like not flipping it at all. Each index can be flipped one time. Try all possible combinations. O(2^(n*m)).

## 示例

```
[[0,0],[0,1]]
[[0]]
[[1,0,0],[1,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFlips(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFlips(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
```

### C

```c
int minFlips(int** mat, int matSize, int* matColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFlips(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var minFlips = function(mat) {
    
};
```

### TypeScript

```typescript
function minFlips(mat: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function minFlips($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFlips(_ mat: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFlips(mat: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFlips(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func minFlips(mat [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer}
def min_flips(mat)
    
end
```

### Scala

```scala
object Solution {
    def minFlips(mat: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_flips(mat: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-flips mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_flips(Mat :: [[integer()]]) -> integer().
min_flips(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_flips(mat :: [[integer]]) :: integer
  def min_flips(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFlips(mat: Array<Array<Int64>>): Int64 {

    }
}
```

