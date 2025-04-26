# 598. 区间加法 II

## 题目描述

<p>给你一个 <code>m x&nbsp;n</code> 的矩阵&nbsp;<code>M</code><strong> </strong>和一个操作数组 <code>op</code> 。矩阵初始化时所有的单元格都为 <code>0</code> 。<code>ops[i] = [ai, bi]</code> 意味着当所有的 <code>0 &lt;= x &lt; ai</code> 和 <code>0 &lt;= y &lt; bi</code> 时， <code>M[x][y]</code> 应该加 1。</p>

<p>在&nbsp;<em>执行完所有操作后</em>&nbsp;，计算并返回&nbsp;<em>矩阵中最大整数的个数</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg" style="height: 176px; width: 750px;" /></p>

<pre>
<strong>输入:</strong> m = 3, n = 3，ops = [[2,2],[3,3]]
<strong>输出:</strong> 4
<strong>解释:</strong> M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
<strong>输出:</strong> 4
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> m = 3, n = 3, ops = []
<strong>输出:</strong> 9
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ops.length &lt;= 10<sup>4</sup></code></li>
	<li><code>ops[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub>&nbsp;&lt;= m</code></li>
	<li><code>1 &lt;= b<sub>i</sub>&nbsp;&lt;= n</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 示例

```
3
3
[[2,2],[3,3]]
3
3
[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
3
3
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
```

### C

```c
int maxCount(int m, int n, int** ops, int opsSize, int* opsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxCount(int m, int n, int[][] ops) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} ops
 * @return {number}
 */
var maxCount = function(m, n, ops) {
    
};
```

### TypeScript

```typescript
function maxCount(m: number, n: number, ops: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $ops
     * @return Integer
     */
    function maxCount($m, $n, $ops) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxCount(_ m: Int, _ n: Int, _ ops: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxCount(m: Int, n: Int, ops: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxCount(int m, int n, List<List<int>> ops) {
    
  }
}
```

### Go

```golang
func maxCount(m int, n int, ops [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} ops
# @return {Integer}
def max_count(m, n, ops)
    
end
```

### Scala

```scala
object Solution {
    def maxCount(m: Int, n: Int, ops: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_count(m: i32, n: i32, ops: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-count m n ops)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_count(M :: integer(), N :: integer(), Ops :: [[integer()]]) -> integer().
max_count(M, N, Ops) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_count(m :: integer, n :: integer, ops :: [[integer]]) :: integer
  def max_count(m, n, ops) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxCount(m: Int64, n: Int64, ops: Array<Array<Int64>>): Int64 {

    }
}
```

