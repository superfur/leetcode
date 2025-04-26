# 815. 公交路线

## 题目描述

<p>给你一个数组 <code>routes</code> ，表示一系列公交线路，其中每个 <code>routes[i]</code> 表示一条公交线路，第 <code>i</code> 辆公交车将会在上面循环行驶。</p>

<ul>
	<li>例如，路线 <code>routes[0] = [1, 5, 7]</code> 表示第 <code>0</code> 辆公交车会一直按序列 <code>1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...</code> 这样的车站路线行驶。</li>
</ul>

<p>现在从 <code>source</code> 车站出发（初始时不在公交车上），要前往 <code>target</code> 车站。 期间仅可乘坐公交车。</p>

<p>求出 <strong>最少乘坐的公交车数量</strong> 。如果不可能到达终点车站，返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>routes = [[1,2,7],[3,6,7]], source = 1, target = 6
<strong>输出：</strong>2
<strong>解释：</strong>最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
<strong>输出：</strong>-1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= routes.length <= 500</code>.</li>
	<li><code>1 <= routes[i].length <= 10<sup>5</sup></code></li>
	<li><code>routes[i]</code> 中的所有值 <strong>互不相同</strong></li>
	<li><code>sum(routes[i].length) <= 10<sup>5</sup></code></li>
	<li><code>0 <= routes[i][j] < 10<sup>6</sup></code></li>
	<li><code>0 <= source, target < 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 数组
- 哈希表

## 示例

```
[[1,2,7],[3,6,7]]
1
6
[[7,12],[4,5,15],[6],[15,19],[9,12,13]]
15
12
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
```

### C

```c
int numBusesToDestination(int** routes, int routesSize, int* routesColSize, int source, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumBusesToDestination(int[][] routes, int source, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} routes
 * @param {number} source
 * @param {number} target
 * @return {number}
 */
var numBusesToDestination = function(routes, source, target) {
    
};
```

### TypeScript

```typescript
function numBusesToDestination(routes: number[][], source: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $routes
     * @param Integer $source
     * @param Integer $target
     * @return Integer
     */
    function numBusesToDestination($routes, $source, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numBusesToDestination(_ routes: [[Int]], _ source: Int, _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numBusesToDestination(routes: Array<IntArray>, source: Int, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numBusesToDestination(List<List<int>> routes, int source, int target) {
    
  }
}
```

### Go

```golang
func numBusesToDestination(routes [][]int, source int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} routes
# @param {Integer} source
# @param {Integer} target
# @return {Integer}
def num_buses_to_destination(routes, source, target)
    
end
```

### Scala

```scala
object Solution {
    def numBusesToDestination(routes: Array[Array[Int]], source: Int, target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-buses-to-destination routes source target)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_buses_to_destination(Routes :: [[integer()]], Source :: integer(), Target :: integer()) -> integer().
num_buses_to_destination(Routes, Source, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_buses_to_destination(routes :: [[integer]], source :: integer, target :: integer) :: integer
  def num_buses_to_destination(routes, source, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numBusesToDestination(routes: Array<Array<Int64>>, source: Int64, target: Int64): Int64 {

    }
}
```

