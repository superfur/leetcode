# 1252. 奇数值单元格的数目

## 题目描述

<p>给你一个 <code>m x n</code> 的矩阵，最开始的时候，每个单元格中的值都是 <code>0</code>。</p>

<p>另有一个二维索引数组 <code>indices</code>，<code>indices[i] = [ri, ci]</code> 指向矩阵中的某个位置，其中 <code>ri</code> 和 <code>ci</code> 分别表示指定的行和列（<strong>从 <code>0</code> 开始编号</strong>）。</p>

<p>对 <code>indices[i]</code> 所指向的每个位置，应同时执行下述增量操作：</p>

<ol>
	<li><code>r<sub>i</sub></code> 行上的所有单元格，加 <code>1</code> 。</li>
	<li><code>c<sub>i</sub></code> 列上的所有单元格，加 <code>1</code> 。</li>
</ol>

<p>给你 <code>m</code>、<code>n</code> 和 <code>indices</code> 。请你在执行完所有 <code>indices</code> 指定的增量操作后，返回矩阵中 <strong>奇数值单元格</strong> 的数目。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e1.png" style="height: 118px; width: 600px;" /></p>

<pre>
<strong>输入：</strong>m = 2, n = 3, indices = [[0,1],[1,1]]
<strong>输出：</strong>6
<strong>解释：</strong>最开始的矩阵是 [[0,0,0],[0,0,0]]。
第一次增量操作后得到 [[1,2,1],[0,1,0]]。
最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e2.png" style="height: 150px; width: 600px;" /></p>

<pre>
<strong>输入：</strong>m = 2, n = 2, indices = [[1,1],[0,0]]
<strong>输出：</strong>0
<strong>解释：</strong>最后的矩阵是 [[2,2],[2,2]]，里面没有奇数。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= m, n <= 50</code></li>
	<li><code>1 <= indices.length <= 100</code></li>
	<li><code>0 <= r<sub>i</sub> < m</code></li>
	<li><code>0 <= c<sub>i</sub> < n</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(n + m + indices.length)</code> 且仅用 <code>O(n + m)</code> 额外空间的算法来解决此问题吗？</p>


## 难度

Easy

## 标签

- 数组
- 数学
- 模拟

## 提示

1. Simulation : With small constraints, it is possible to apply changes to each row and column and count odd cells after applying it.
2. You can accumulate the number you should add to each row and column and then you can count the number of odd cells.

## 示例

```
2
3
[[0,1],[1,1]]
2
2
[[1,1],[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        
    }
};
```

### Java

```java
class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
```

### C

```c
int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int OddCells(int m, int n, int[][] indices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function(m, n, indices) {
    
};
```

### TypeScript

```typescript
function oddCells(m: number, n: number, indices: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $indices
     * @return Integer
     */
    function oddCells($m, $n, $indices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func oddCells(_ m: Int, _ n: Int, _ indices: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun oddCells(m: Int, n: Int, indices: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int oddCells(int m, int n, List<List<int>> indices) {
    
  }
}
```

### Go

```golang
func oddCells(m int, n int, indices [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} indices
# @return {Integer}
def odd_cells(m, n, indices)
    
end
```

### Scala

```scala
object Solution {
    def oddCells(m: Int, n: Int, indices: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn odd_cells(m: i32, n: i32, indices: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (odd-cells m n indices)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec odd_cells(M :: integer(), N :: integer(), Indices :: [[integer()]]) -> integer().
odd_cells(M, N, Indices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec odd_cells(m :: integer, n :: integer, indices :: [[integer]]) :: integer
  def odd_cells(m, n, indices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func oddCells(m: Int64, n: Int64, indices: Array<Array<Int64>>): Int64 {

    }
}
```

