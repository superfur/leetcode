# 1499. 满足不等式的最大值

## 题目描述

<p>给你一个数组 <code>points</code> 和一个整数 <code>k</code> 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> ，并且在 <code>1 &lt;= i &lt; j &lt;= points.length</code> 的前提下， <code>x<sub>i</sub> &lt; x<sub>j</sub></code> 总成立。</p>

<p>请你找出<em> </em><code>y<sub>i</sub>&nbsp;+ y<sub>j</sub>&nbsp;+ |x<sub>i</sub>&nbsp;- x<sub>j</sub>|</code> 的 <strong>最大值</strong>，其中 <code>|x<sub>i</sub>&nbsp;- x<sub>j</sub>|&nbsp;&lt;= k</code> 且 <code>1 &lt;= i &lt; j &lt;= points.length</code>。</p>

<p>题目测试数据保证至少存在一对能够满足 <code>|x<sub>i</sub>&nbsp;- x<sub>j</sub>|&nbsp;&lt;= k</code> 的点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
<strong>输出：</strong>4
<strong>解释：</strong>前两个点满足 |x<sub>i</sub>&nbsp;- x<sub>j</sub>| &lt;= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6| = 1 。
没有其他满足条件的点，所以返回 4 和 1 中最大的那个。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>points = [[0,0],[3,0],[9,2]], k = 3
<strong>输出：</strong>3
<strong>解释：</strong>只有前两个点满足 |x<sub>i</sub>&nbsp;- x<sub>j</sub>| &lt;= 3 ，代入方程后得到值 0 + 0 + |0 - 3| = 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= points.length &lt;= 10^5</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10^8&nbsp;&lt;= points[i][0], points[i][1] &lt;= 10^8</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10^8</code></li>
	<li>对于所有的<code>1 &lt;= i &lt; j &lt;= points.length</code> ，<code>points[i][0] &lt; points[j][0]</code> 都成立。也就是说，<code>x<sub>i</sub></code> 是严格递增的。</li>
</ul>


## 难度

Hard

## 标签

- 队列
- 数组
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 提示

1. Use a priority queue to store for each point i, the tuple [yi-xi, xi]
2. Loop through the array and pop elements from the heap if the condition xj - xi > k, where j is the current index and i is the point on top the queue.
3. After popping elements from the queue. If the queue is not empty, calculate the equation with the current point and the point on top of the queue and maximize the answer.

## 示例

```
[[1,3],[2,0],[5,10],[6,-10]]
1
[[0,0],[3,0],[9,2]]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
```

### C

```c
int findMaxValueOfEquation(int** points, int pointsSize, int* pointsColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMaxValueOfEquation(int[][] points, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number}
 */
var findMaxValueOfEquation = function(points, k) {
    
};
```

### TypeScript

```typescript
function findMaxValueOfEquation(points: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $k
     * @return Integer
     */
    function findMaxValueOfEquation($points, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaxValueOfEquation(_ points: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxValueOfEquation(points: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaxValueOfEquation(List<List<int>> points, int k) {
    
  }
}
```

### Go

```golang
func findMaxValueOfEquation(points [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer}
def find_max_value_of_equation(points, k)
    
end
```

### Scala

```scala
object Solution {
    def findMaxValueOfEquation(points: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_value_of_equation(points: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-max-value-of-equation points k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_max_value_of_equation(Points :: [[integer()]], K :: integer()) -> integer().
find_max_value_of_equation(Points, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_value_of_equation(points :: [[integer]], k :: integer) :: integer
  def find_max_value_of_equation(points, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaxValueOfEquation(points: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

