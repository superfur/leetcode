# 3027. 人员站位的方案数 II

## 题目描述

<p>给你一个&nbsp;&nbsp;<code>n x 2</code>&nbsp;的二维数组 <code>points</code>&nbsp;，它表示二维平面上的一些点坐标，其中&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;。</p>

<p>我们定义 x 轴的正方向为 <strong>右</strong>&nbsp;（<strong>x 轴递增的方向</strong>），x 轴的负方向为 <strong>左</strong>&nbsp;（<strong>x 轴递减的方向</strong>）。类似的，我们定义 y 轴的正方向为 <strong>上</strong>&nbsp;（<strong>y 轴递增的方向</strong>），y 轴的负方向为 <strong>下</strong>&nbsp;（<strong>y 轴递减的方向</strong>）。</p>

<p>你需要安排这 <code>n</code>&nbsp;个人的站位，这 <code>n</code>&nbsp;个人中包括 Alice 和 Bob 。你需要确保每个点处&nbsp;<strong>恰好</strong>&nbsp;有&nbsp;<strong>一个</strong>&nbsp;人。同时，Alice 想跟 Bob 单独玩耍，所以&nbsp;Alice 会以 Alice<b>&nbsp;</b>的坐标为 <strong>左上角</strong>&nbsp;，Bob 的坐标为 <strong>右下角</strong>&nbsp;建立一个矩形的围栏（<strong>注意</strong>，围栏可能&nbsp;<strong>不</strong> 包含任何区域，也就是说围栏可能是一条线段）。如果围栏的 <strong>内部</strong>&nbsp;或者 <strong>边缘</strong>&nbsp;上有任何其他人，Alice 都会难过。</p>

<p>请你在确保 Alice&nbsp;<strong>不会</strong> 难过的前提下，返回 Alice 和 Bob 可以选择的 <strong>点对</strong>&nbsp;数目。</p>

<p><b>注意</b>，Alice 建立的围栏必须确保 Alice 的位置是矩形的左上角，Bob 的位置是矩形的右下角。比方说，以&nbsp;<code>(1, 1)</code>&nbsp;，<code>(1, 3)</code>&nbsp;，<code>(3, 1)</code>&nbsp;和&nbsp;<code>(3, 3)</code>&nbsp;为矩形的四个角，给定下图的两个输入，Alice 都不能建立围栏，原因如下：</p>

<ul>
	<li>图一中，Alice 在&nbsp;<code>(3, 3)</code>&nbsp;且 Bob 在&nbsp;<code>(1, 1)</code>&nbsp;，Alice 的位置不是左上角且 Bob 的位置不是右下角。</li>
	<li>图二中，Alice 在&nbsp;<code>(1, 3)</code>&nbsp;且 Bob 在&nbsp;<code>(1, 1)</code>&nbsp;，Bob 的位置不是在围栏的右下角。</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/example0alicebob-1.png" style="width: 750px; height: 308px;padding: 10px; background: #fff; border-radius: .5rem;" />
<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/example1alicebob.png" style="width: 376px; height: 308px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;" /></p>

<pre>
<b>输入：</b>points = [[1,1],[2,2],[3,3]]
<b>输出：</b>0
<strong>解释：</strong>没有办法可以让 Alice 的围栏以 Alice 的位置为左上角且 Bob 的位置为右下角。所以我们返回 0 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><strong class="example"><a href="https://pic.leetcode.cn/1706880313-YelabI-example2.jpeg"><img alt="" src="https://pic.leetcode.cn/1708226715-CxjXKb-20240218-112338.jpeg" style="width: 900px; height: 248px;" /></a></strong></p>

<pre>
<b>输入：</b>points = [[6,2],[4,4],[2,6]]
<b>输出：</b>2
<b>解释：</b>总共有 2 种方案安排 Alice 和 Bob 的位置，使得 Alice 不会难过：
- Alice 站在 (4, 4) ，Bob 站在 (6, 2) 。
- Alice 站在 (2, 6) ，Bob 站在 (4, 4) 。
不能安排 Alice 站在 (2, 6) 且 Bob 站在 (6, 2) ，因为站在 (4, 4) 的人处于围栏内。
</pre>

<p><strong class="example">示例 3：</strong></p>

<p><strong class="example"><a href="https://pic.leetcode.cn/1706880311-mtPGYC-example3.jpeg"><img alt="" src="https://pic.leetcode.cn/1708226721-wTbEuK-20240218-112351.jpeg" style="width: 911px; height: 250px;" /></a></strong></p>

<pre>
<b>输入：</b>points = [[3,1],[1,3],[1,1]]
<b>输出：</b>2
<b>解释：</b>总共有 2 种方案安排 Alice 和 Bob 的位置，使得 Alice 不会难过：
- Alice 站在 (1, 1) ，Bob 站在 (3, 1) 。
- Alice 站在 (1, 3) ，Bob 站在 (1, 1) 。
不能安排 Alice 站在 (1, 3) 且 Bob 站在 (3, 1) ，因为站在 (1, 1) 的人处于围栏内。
注意围栏是可以不包含任何面积的，上图中第一和第二个围栏都是合法的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>9</sup> &lt;= points[i][0], points[i][1] &lt;= 10<sup>9</sup></code></li>
	<li><code>points[i]</code>&nbsp;点对两两不同。</li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 数学
- 枚举
- 排序

## 提示

1. Sort the points by x-coordinate in non-decreasing order and break the tie by sorting the y-coordinate in non-increasing order.
2. Now consider two points upper-left corner <code>points[i]</code> and lower-right corner <code>points[j]</code>, such that <code>i < j</code> and <code>points[i][0] <= points[j][0]</code> and <code>points[i][1] >= points[j][1]</code>.
3. Instead of brute force looping, we can save the largest y-coordinate that is no larger than <code>points[i][1]</code> when looping on <code>j</code>, say the value is <code>m</code>. And if <code>m < points[j][1]</code>, the upper-left and lower-right corner pair is valid.
4. The actual values don’t matter, we can compress all x-coordinates and y-coordinates to the range <code>[1, n]</code>. Can we use prefix sum now?

## 示例

```
[[1,1],[2,2],[3,3]]
[[6,2],[4,4],[2,6]]
[[3,1],[1,3],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfPairs(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
```

### C

```c
int numberOfPairs(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfPairs(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfPairs = function(points) {
    
};
```

### TypeScript

```typescript
function numberOfPairs(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function numberOfPairs($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPairs(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPairs(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPairs(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func numberOfPairs(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def number_of_pairs(points)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPairs(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_pairs(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-pairs points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_pairs(Points :: [[integer()]]) -> integer().
number_of_pairs(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(points :: [[integer]]) :: integer
  def number_of_pairs(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPairs(points: Array<Array<Int64>>): Int64 {

    }
}
```

