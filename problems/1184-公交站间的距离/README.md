# 1184. 公交站间的距离

## 题目描述

<p>环形公交路线上有&nbsp;<code>n</code>&nbsp;个站，按次序从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;进行编号。我们已知每一对相邻公交站之间的距离，<code>distance[i]</code>&nbsp;表示编号为&nbsp;<code>i</code>&nbsp;的车站和编号为&nbsp;<code>(i + 1) % n</code>&nbsp;的车站之间的距离。</p>

<p>环线上的公交车都可以按顺时针和逆时针的方向行驶。</p>

<p>返回乘客从出发点&nbsp;<code>start</code>&nbsp;到目的地&nbsp;<code>destination</code>&nbsp;之间的最短距离。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1.jpg" style="height: 240px; width: 388px;"></p>

<pre><strong>输入：</strong>distance = [1,2,3,4], start = 0, destination = 1
<strong>输出：</strong>1
<strong>解释：</strong>公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1-1.jpg" style="height: 240px; width: 388px;"></p>

<pre><strong>输入：</strong>distance = [1,2,3,4], start = 0, destination = 2
<strong>输出：</strong>3
<strong>解释：</strong>公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。
</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1-2.jpg" style="height: 240px; width: 388px;"></p>

<pre><strong>输入：</strong>distance = [1,2,3,4], start = 0, destination = 3
<strong>输出：</strong>4
<strong>解释：</strong>公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n&nbsp;&lt;= 10^4</code></li>
	<li><code>distance.length == n</code></li>
	<li><code>0 &lt;= start, destination &lt; n</code></li>
	<li><code>0 &lt;= distance[i] &lt;= 10^4</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Find the distance between the two stops if the bus moved in clockwise or counterclockwise directions.

## 示例

```
[1,2,3,4]
0
1
[1,2,3,4]
0
2
[1,2,3,4]
0
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        
    }
};
```

### Java

```java
class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
```

### C

```c
int distanceBetweenBusStops(int* distance, int distanceSize, int start, int destination) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistanceBetweenBusStops(int[] distance, int start, int destination) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
    
};
```

### TypeScript

```typescript
function distanceBetweenBusStops(distance: number[], start: number, destination: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $distance
     * @param Integer $start
     * @param Integer $destination
     * @return Integer
     */
    function distanceBetweenBusStops($distance, $start, $destination) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distanceBetweenBusStops(_ distance: [Int], _ start: Int, _ destination: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distanceBetweenBusStops(distance: IntArray, start: Int, destination: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distanceBetweenBusStops(List<int> distance, int start, int destination) {
    
  }
}
```

### Go

```golang
func distanceBetweenBusStops(distance []int, start int, destination int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} distance
# @param {Integer} start
# @param {Integer} destination
# @return {Integer}
def distance_between_bus_stops(distance, start, destination)
    
end
```

### Scala

```scala
object Solution {
    def distanceBetweenBusStops(distance: Array[Int], start: Int, destination: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distance_between_bus_stops(distance: Vec<i32>, start: i32, destination: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distance-between-bus-stops distance start destination)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec distance_between_bus_stops(Distance :: [integer()], Start :: integer(), Destination :: integer()) -> integer().
distance_between_bus_stops(Distance, Start, Destination) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distance_between_bus_stops(distance :: [integer], start :: integer, destination :: integer) :: integer
  def distance_between_bus_stops(distance, start, destination) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distanceBetweenBusStops(distance: Array<Int64>, start: Int64, destination: Int64): Int64 {

    }
}
```

