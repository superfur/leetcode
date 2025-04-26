# 1776. 车队 II

## 题目描述

<p>在一条单车道上有 <code>n</code> 辆车，它们朝着同样的方向行驶。给你一个长度为 <code>n</code> 的数组 <code>cars</code> ，其中 <code>cars[i] = [position<sub>i</sub>, speed<sub>i</sub>]</code> ，它表示：</p>

<ul>
	<li><code>position<sub>i</sub></code> 是第 <code>i</code> 辆车和道路起点之间的距离（单位：米）。题目保证 <code>position<sub>i</sub> < position<sub>i+1</sub></code><sub> </sub>。</li>
	<li><code>speed<sub>i</sub></code> 是第 <code>i</code> 辆车的初始速度（单位：米/秒）。</li>
</ul>

<p>简单起见，所有车子可以视为在数轴上移动的点。当两辆车占据同一个位置时，我们称它们相遇了。一旦两辆车相遇，它们会合并成一个车队，这个车队里的车有着同样的位置和相同的速度，速度为这个车队里 <strong>最慢</strong> 一辆车的速度。</p>

<p>请你返回一个数组 <code>answer</code> ，其中 <code>answer[i]</code> 是第 <code>i</code> 辆车与下一辆车相遇的时间（单位：秒），如果这辆车不会与下一辆车相遇，则 <code>answer[i]</code> 为 <code>-1</code> 。答案精度误差需在 <code>10<sup>-5</sup></code> 以内。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>cars = [[1,2],[2,1],[4,3],[7,2]]
<b>输出：</b>[1.00000,-1.00000,3.00000,-1.00000]
<b>解释：</b>经过恰好 1 秒以后，第一辆车会与第二辆车相遇，并形成一个 1 m/s 的车队。经过恰好 3 秒以后，第三辆车会与第四辆车相遇，并形成一个 2 m/s 的车队。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>cars = [[3,4],[5,4],[6,3],[9,1]]
<b>输出：</b>[2.00000,1.00000,1.50000,-1.00000]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= cars.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= position<sub>i</sub>, speed<sub>i</sub> <= 10<sup>6</sup></code></li>
	<li><code>position<sub>i</sub> < position<sub>i+1</sub></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数组
- 数学
- 单调栈
- 堆（优先队列）

## 提示

1. We can simply ignore the merging of any car fleet, simply assume they cross each other. Now the aim is to find the first car to the right, which intersects with the current car before any other.
2. Assume we have already considered all cars to the right already, now the current car is to be considered. Let’s ignore all cars with speeds higher than the current car since the current car cannot intersect with those ones. Now, all cars to the right having speed strictly less than current car are to be considered. Now, for two cars c1 and c2 with positions p1 and p2 (p1 < p2) and speed s1 and s2 (s1 > s2), if c1 and c2 intersect before the current car and c2, then c1 can never be the first car of intersection for any car to the left of current car including current car. So we can remove that car from our consideration.
3. We can see that we can maintain candidate cars in this way using a stack, removing cars with speed greater than or equal to current car, and then removing cars which can never be first point of intersection. The first car after this process (if any) would be first point of intersection.

## 示例

```
[[1,2],[2,1],[4,3],[7,2]]
[[3,4],[5,4],[6,3],[9,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<double> getCollisionTimes(vector<vector<int>>& cars) {
        
    }
};
```

### Java

```java
class Solution {
    public double[] getCollisionTimes(int[][] cars) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        
```

### Python3

```python3
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* getCollisionTimes(int** cars, int carsSize, int* carsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double[] GetCollisionTimes(int[][] cars) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} cars
 * @return {number[]}
 */
var getCollisionTimes = function(cars) {
    
};
```

### TypeScript

```typescript
function getCollisionTimes(cars: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $cars
     * @return Float[]
     */
    function getCollisionTimes($cars) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getCollisionTimes(_ cars: [[Int]]) -> [Double] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getCollisionTimes(cars: Array<IntArray>): DoubleArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<double> getCollisionTimes(List<List<int>> cars) {
    
  }
}
```

### Go

```golang
func getCollisionTimes(cars [][]int) []float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} cars
# @return {Float[]}
def get_collision_times(cars)
    
end
```

### Scala

```scala
object Solution {
    def getCollisionTimes(cars: Array[Array[Int]]): Array[Double] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_collision_times(cars: Vec<Vec<i32>>) -> Vec<f64> {
        
    }
}
```

### Racket

```racket
(define/contract (get-collision-times cars)
  (-> (listof (listof exact-integer?)) (listof flonum?))
  )
```

### Erlang

```erlang
-spec get_collision_times(Cars :: [[integer()]]) -> [float()].
get_collision_times(Cars) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_collision_times(cars :: [[integer]]) :: [float]
  def get_collision_times(cars) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getCollisionTimes(cars: Array<Array<Int64>>): Array<Float64> {

    }
}
```

