# 1494. 并行课程 II

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;表示某所大学里课程的数目，编号为&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;，数组&nbsp;<code>relations</code>&nbsp;中，&nbsp;<code>relations[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp; 表示一个先修课的关系，也就是课程&nbsp;<code>x<sub>i</sub></code>&nbsp;必须在课程&nbsp;<code>y<sub>i</sub></code><sub>&nbsp;</sub>之前上。同时你还有一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>在一个学期中，你 <strong>最多</strong>&nbsp;可以同时上 <code>k</code>&nbsp;门课，前提是这些课的先修课在之前的学期里已经上过了。</p>

<p>请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_1.png" style="height: 164px; width: 300px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
<strong>输出：</strong>3 
<strong>解释：</strong>上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_2.png" style="height: 234px; width: 300px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
<strong>输出：</strong>4 
<strong>解释：</strong>上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 11, relations = [], k = 2
<strong>输出：</strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li><code>0 &lt;=&nbsp;relations.length &lt;= n * (n-1) / 2</code></li>
	<li><code>relations[i].length == 2</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= n</code></li>
	<li><code>x<sub>i</sub> != y<sub>i</sub></code></li>
	<li>所有先修关系都是不同的，也就是说&nbsp;<code>relations[i] != relations[j]</code>&nbsp;。</li>
	<li>题目输入的图是个有向无环图。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 图
- 动态规划
- 状态压缩

## 提示

1. Use backtracking with states (bitmask, degrees) where bitmask represents the set of courses, if the ith bit is 1 then the ith course was taken, otherwise, you can take the ith course. Degrees represent the degree for each course (nodes in the graph).
2. Note that you can only take nodes (courses) with degree = 0 and it is optimal at every step in the backtracking take the maximum number of courses limited by k.

## 示例

```
4
[[2,1],[3,1],[1,4]]
2
5
[[2,1],[3,1],[4,1],[1,5]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& relations, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minNumberOfSemesters(int n, int[][] relations, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minNumberOfSemesters(self, n, relations, k):
        """
        :type n: int
        :type relations: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        
```

### C

```c
int minNumberOfSemesters(int n, int** relations, int relationsSize, int* relationsColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinNumberOfSemesters(int n, int[][] relations, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number} k
 * @return {number}
 */
var minNumberOfSemesters = function(n, relations, k) {
    
};
```

### TypeScript

```typescript
function minNumberOfSemesters(n: number, relations: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $relations
     * @param Integer $k
     * @return Integer
     */
    function minNumberOfSemesters($n, $relations, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minNumberOfSemesters(_ n: Int, _ relations: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minNumberOfSemesters(n: Int, relations: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minNumberOfSemesters(int n, List<List<int>> relations, int k) {
    
  }
}
```

### Go

```golang
func minNumberOfSemesters(n int, relations [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} relations
# @param {Integer} k
# @return {Integer}
def min_number_of_semesters(n, relations, k)
    
end
```

### Scala

```scala
object Solution {
    def minNumberOfSemesters(n: Int, relations: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_number_of_semesters(n: i32, relations: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-number-of-semesters n relations k)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_number_of_semesters(N :: integer(), Relations :: [[integer()]], K :: integer()) -> integer().
min_number_of_semesters(N, Relations, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_number_of_semesters(n :: integer, relations :: [[integer]], k :: integer) :: integer
  def min_number_of_semesters(n, relations, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minNumberOfSemesters(n: Int64, relations: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

