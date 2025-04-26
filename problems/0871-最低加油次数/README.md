# 871. 最低加油次数

## 题目描述

<p>汽车从起点出发驶向目的地，该目的地位于出发位置东面 <code>target</code>&nbsp;英里处。</p>

<p>沿途有加油站，用数组&nbsp;<code>stations</code> 表示。其中 <code>stations[i] = [position<sub>i</sub>, fuel<sub>i</sub>]</code> 表示第 <code>i</code> 个加油站位于出发位置东面&nbsp;<code>position<sub>i</sub></code> 英里处，并且有&nbsp;<code>fuel<sub>i</sub></code>&nbsp;升汽油。</p>

<p>假设汽车油箱的容量是无限的，其中最初有&nbsp;<code>startFuel</code>&nbsp;升燃料。它每行驶 1 英里就会用掉 1 升汽油。当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。</p>

<p>为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 <code>-1</code> 。</p>

<p>注意：如果汽车到达加油站时剩余燃料为 <code>0</code>，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 <code>0</code>，仍然认为它已经到达目的地。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = 1, startFuel = 1, stations = []
<strong>输出：</strong>0
<strong>解释：</strong>可以在不加油的情况下到达目的地。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = 100, startFuel = 1, stations = [[10,100]]
<strong>输出：</strong>-1
<strong>解释：</strong>无法抵达目的地，甚至无法到达第一个加油站。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
<strong>输出：</strong>2
<strong>解释：</strong>
出发时有 10 升燃料。
开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后开车抵达目的地。
沿途在两个加油站停靠，所以返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target, startFuel &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= stations.length &lt;= 500</code></li>
	<li><code>1 &lt;= position<sub>i</sub> &lt; position<sub>i+1</sub> &lt; target</code></li>
	<li><code>1 &lt;= fuel<sub>i</sub> &lt; 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 动态规划
- 堆（优先队列）

## 示例

```
1
1
[]
100
1
[[10,100]]
100
10
[[10,60],[20,30],[30,30],[60,40]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        
    }
};
```

### Java

```java
class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
```

### C

```c
int minRefuelStops(int target, int startFuel, int** stations, int stationsSize, int* stationsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinRefuelStops(int target, int startFuel, int[][] stations) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} target
 * @param {number} startFuel
 * @param {number[][]} stations
 * @return {number}
 */
var minRefuelStops = function(target, startFuel, stations) {
    
};
```

### TypeScript

```typescript
function minRefuelStops(target: number, startFuel: number, stations: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer $startFuel
     * @param Integer[][] $stations
     * @return Integer
     */
    function minRefuelStops($target, $startFuel, $stations) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minRefuelStops(_ target: Int, _ startFuel: Int, _ stations: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minRefuelStops(target: Int, startFuel: Int, stations: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minRefuelStops(int target, int startFuel, List<List<int>> stations) {
    
  }
}
```

### Go

```golang
func minRefuelStops(target int, startFuel int, stations [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} target
# @param {Integer} start_fuel
# @param {Integer[][]} stations
# @return {Integer}
def min_refuel_stops(target, start_fuel, stations)
    
end
```

### Scala

```scala
object Solution {
    def minRefuelStops(target: Int, startFuel: Int, stations: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_refuel_stops(target: i32, start_fuel: i32, stations: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-refuel-stops target startFuel stations)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_refuel_stops(Target :: integer(), StartFuel :: integer(), Stations :: [[integer()]]) -> integer().
min_refuel_stops(Target, StartFuel, Stations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_refuel_stops(target :: integer, start_fuel :: integer, stations :: [[integer]]) :: integer
  def min_refuel_stops(target, start_fuel, stations) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minRefuelStops(target: Int64, startFuel: Int64, stations: Array<Array<Int64>>): Int64 {

    }
}
```

