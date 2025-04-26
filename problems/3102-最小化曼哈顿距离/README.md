# 3102. 最小化曼哈顿距离

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>points</code> ，它表示二维平面上一些点的整数坐标，其中 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 。</p>

<p>两点之间的距离定义为它们的<span data-keyword="manhattan-distance">曼哈顿距离</span>。</p>

<p>请你恰好移除一个点，返回移除后任意两点之间的 <strong>最大 </strong>距离可能的 <strong>最小 </strong>值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>points = [[3,10],[5,15],[10,2],[4,4]]
<strong>输出：</strong>12
<strong>解释：</strong>移除每个点后的最大距离如下所示：
- 移除第 0 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间，为 |5 - 10| + |15 - 2| = 18 。
- 移除第 1 个点后，最大距离在点 (3, 10) 和 (10, 2) 之间，为 |3 - 10| + |10 - 2| = 15 。
- 移除第 2 个点后，最大距离在点 (5, 15) 和 (4, 4) 之间，为 |5 - 4| + |15 - 4| = 12 。
- 移除第 3 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间的，为 |5 - 10| + |15 - 2| = 18 。
在恰好移除一个点后，任意两点之间的最大距离可能的最小值是 12 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,1],[1,1],[1,1]]
<strong>输出：</strong>0
<strong>解释：</strong>移除任一点后，任意两点之间的最大距离都是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>1 &lt;= points[i][0], points[i][1] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 数学
- 有序集合
- 排序

## 提示

1. Notice that the Manhattan distance between two points <code>[x<sub>i</sub>, y<sub>i</sub>]</code> and <code>[x<sub>j</sub>, y<sub>j</sub>] is <code> max({x<sub>i</sub> - x<sub>j</sub> + y<sub>i</sub> - y<sub>j</sub>, x<sub>i</sub> - x<sub>j</sub> - y<sub>i</sub> + y<sub>j</sub>, - x<sub>i</sub> + x<sub>j</sub> + y<sub>i</sub> - y<sub>j</sub>, - x<sub>i</sub> + x<sub>j</sub> - y<sub>i</sub> + y<sub>j</sub>})</code></code>.
2. If you replace points as <code>[x<sub>i</sub> - y<sub>i</sub>, x<sub>i</sub> + y<sub>i</sub>]</code> then the Manhattan distance is <code>max(max(x<sub>i</sub>) - min(x<sub>i</sub>), max(y<sub>i</sub>) - min(y<sub>i</sub>))</code> over all <code>i</code>.
3. After those observations, the problem just becomes a simulation. Create multiset of points <code>[x<sub>i</sub> - y<sub>i</sub>, x<sub>i</sub> + y<sub>i</sub>]</code>, you can iterate on a point you might remove and get the maximum Manhattan distance over all other points.

## 示例

```
[[3,10],[5,15],[10,2],[4,4]]
[[1,1],[1,1],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDistance(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDistance(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        
```

### C

```c
int minimumDistance(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDistance(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minimumDistance = function(points) {
    
};
```

### TypeScript

```typescript
function minimumDistance(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minimumDistance($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDistance(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDistance(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDistance(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func minimumDistance(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def minimum_distance(points)
    
end
```

### Scala

```scala
object Solution {
    def minimumDistance(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_distance(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-distance points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_distance(Points :: [[integer()]]) -> integer().
minimum_distance(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_distance(points :: [[integer]]) :: integer
  def minimum_distance(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDistance(points: Array<Array<Int64>>): Int64 {

    }
}
```

