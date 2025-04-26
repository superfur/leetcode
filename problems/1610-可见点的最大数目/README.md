# 1610. 可见点的最大数目

## 题目描述

<p>给你一个点数组 <code>points</code> 和一个表示角度的整数 <code>angle</code> ，你的位置是 <code>location</code> ，其中 <code>location = [pos<sub>x</sub>, pos<sub>y</sub>]</code> 且 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 都表示 X-Y 平面上的整数坐标。</p>

<p>最开始，你面向东方进行观测。你 <strong>不能</strong> 进行移动改变位置，但可以通过 <strong>自转</strong> 调整观测角度。换句话说，<code>pos<sub>x</sub></code> 和 <code>pos<sub>y</sub></code> 不能改变。你的视野范围的角度用 <code>angle</code> 表示， 这决定了你观测任意方向时可以多宽。设 <code>d</code> 为你逆时针自转旋转的度数，那么你的视野就是角度范围 <code>[d - angle/2, d + angle/2]</code> 所指示的那片区域。</p>

<video autoplay="" controls="" height="360" muted="" style="max-width:100%;height:auto;" width="750"><source src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/angle.mp4" type="video/mp4" />Your browser does not support the video tag or this video format.</video>

<p>对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 <strong>位于你的视野中</strong> ，那么你就可以看到它。</p>

<p>同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。</p>

<p>返回你能看到的点的最大数目。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/89a07e9b-00ab-4967-976a-c723b2aa8656.png" style="height: 300px; width: 400px;" /></p>

<pre>
<strong>输入：</strong>points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
<strong>输出：</strong>3
<strong>解释：</strong>阴影区域代表你的视野。在你的视野中，所有的点都清晰可见，尽管 [2,2] 和 [3,3]在同一条直线上，你仍然可以看到 [3,3] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
<strong>输出：</strong>4
<strong>解释：</strong>在你的视野中，所有的点都清晰可见，包括你所在位置的那个点。</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/5010bfd3-86e6-465f-ac64-e9df941d2e49.png" style="height: 348px; width: 690px;" /></p>

<pre>
<strong>输入：</strong>points = [[1,0],[2,1]], angle = 13, location = [1,1]
<strong>输出：</strong>1
<strong>解释：</strong>如图所示，你只能看到两点之一。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= points.length <= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>location.length == 2</code></li>
	<li><code>0 <= angle < 360</code></li>
	<li><code>0 <= pos<sub>x</sub>, pos<sub>y</sub>, x<sub>i</sub>, y<sub>i</sub> <= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 数学
- 排序
- 滑动窗口

## 提示

1. Sort the points by polar angle with the original position. Now only a consecutive collection of points would be visible from any coordinate.
2. We can use two pointers to keep track of visible points for each start point
3. For handling the cyclic condition, it’d be helpful to append the point list to itself after sorting.

## 示例

```
[[2,1],[2,2],[3,3]]
90
[1,1]
[[2,1],[2,2],[3,4],[1,1]]
90
[1,1]
[[1,0],[2,1]]
13
[1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        
    }
};
```

### Java

```java
class Solution {
    public int visiblePoints(List<List<Integer>> points, int angle, List<Integer> location) {
        
    }
}
```

### Python

```python
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
```

### C

```c
int visiblePoints(int** points, int pointsSize, int* pointsColSize, int angle, int* location, int locationSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int VisiblePoints(IList<IList<int>> points, int angle, IList<int> location) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @param {number} angle
 * @param {number[]} location
 * @return {number}
 */
var visiblePoints = function(points, angle, location) {
    
};
```

### TypeScript

```typescript
function visiblePoints(points: number[][], angle: number, location: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $angle
     * @param Integer[] $location
     * @return Integer
     */
    function visiblePoints($points, $angle, $location) {
        
    }
}
```

### Swift

```swift
class Solution {
    func visiblePoints(_ points: [[Int]], _ angle: Int, _ location: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun visiblePoints(points: List<List<Int>>, angle: Int, location: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int visiblePoints(List<List<int>> points, int angle, List<int> location) {
    
  }
}
```

### Go

```golang
func visiblePoints(points [][]int, angle int, location []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @param {Integer} angle
# @param {Integer[]} location
# @return {Integer}
def visible_points(points, angle, location)
    
end
```

### Scala

```scala
object Solution {
    def visiblePoints(points: List[List[Int]], angle: Int, location: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn visible_points(points: Vec<Vec<i32>>, angle: i32, location: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (visible-points points angle location)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec visible_points(Points :: [[integer()]], Angle :: integer(), Location :: [integer()]) -> integer().
visible_points(Points, Angle, Location) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec visible_points(points :: [[integer]], angle :: integer, location :: [integer]) :: integer
  def visible_points(points, angle, location) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func visiblePoints(points: ArrayList<ArrayList<Int64>>, angle: Int64, location: ArrayList<Int64>): Int64 {

    }
}
```

