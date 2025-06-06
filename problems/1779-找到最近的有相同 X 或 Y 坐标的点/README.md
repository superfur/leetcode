# 1779. 找到最近的有相同 X 或 Y 坐标的点

## 题目描述

<p>给你两个整数&nbsp;<code>x</code> 和&nbsp;<code>y</code>&nbsp;，表示你在一个笛卡尔坐标系下的&nbsp;<code>(x, y)</code>&nbsp;处。同时，在同一个坐标系下给你一个数组&nbsp;<code>points</code>&nbsp;，其中&nbsp;<code>points[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示在&nbsp;<code>(a<sub>i</sub>, b<sub>i</sub>)</code>&nbsp;处有一个点。当一个点与你所在的位置有相同的 <code>x</code> 坐标或者相同的 <code>y</code> 坐标时，我们称这个点是 <b>有效的</b>&nbsp;。</p>

<p>请返回距离你当前位置&nbsp;<strong>曼哈顿距离</strong>&nbsp;最近的&nbsp;<strong>有效</strong>&nbsp;点的下标（下标从 <strong>0</strong> 开始）。如果有多个最近的有效点，请返回下标&nbsp;<strong>最小</strong>&nbsp;的一个。如果没有有效点，请返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>两个点 <code>(x<sub>1</sub>, y<sub>1</sub>)</code>&nbsp;和 <code>(x<sub>2</sub>, y<sub>2</sub>)</code>&nbsp;之间的 <strong>曼哈顿距离</strong>&nbsp;为&nbsp;<code>abs(x<sub>1</sub> - x<sub>2</sub>) + abs(y<sub>1</sub> - y<sub>2</sub>)</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
<b>输出：</b>2
<b>解释：</b>所有点中，[3,1]，[2,4] 和 [4,4] 是有效点。有效点中，[2,4] 和 [4,4] 距离你当前位置的曼哈顿距离最小，都为 1 。[2,4] 的下标最小，所以返回 2 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>x = 3, y = 4, points = [[3,4]]
<b>输出：</b>0
<b>提示：</b>答案可以与你当前所在位置坐标相同。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>x = 3, y = 4, points = [[2,3]]
<b>输出：</b>-1
<b>解释：</b>没有 有效点。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 10<sup>4</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>1 &lt;= x, y, a<sub>i</sub>, b<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Iterate through each point, and keep track of the current point with the smallest Manhattan distance from your current location.

## 示例

```
3
4
[[1,2],[3,1],[2,4],[2,3],[4,4]]
3
4
[[3,4]]
3
4
[[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
```

### C

```c
int nearestValidPoint(int x, int y, int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NearestValidPoint(int x, int y, int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number[][]} points
 * @return {number}
 */
var nearestValidPoint = function(x, y, points) {
    
};
```

### TypeScript

```typescript
function nearestValidPoint(x: number, y: number, points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer[][] $points
     * @return Integer
     */
    function nearestValidPoint($x, $y, $points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nearestValidPoint(_ x: Int, _ y: Int, _ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nearestValidPoint(x: Int, y: Int, points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int nearestValidPoint(int x, int y, List<List<int>> points) {
    
  }
}
```

### Go

```golang
func nearestValidPoint(x int, y int, points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @param {Integer} y
# @param {Integer[][]} points
# @return {Integer}
def nearest_valid_point(x, y, points)
    
end
```

### Scala

```scala
object Solution {
    def nearestValidPoint(x: Int, y: Int, points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nearest_valid_point(x: i32, y: i32, points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (nearest-valid-point x y points)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec nearest_valid_point(X :: integer(), Y :: integer(), Points :: [[integer()]]) -> integer().
nearest_valid_point(X, Y, Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nearest_valid_point(x :: integer, y :: integer, points :: [[integer]]) :: integer
  def nearest_valid_point(x, y, points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nearestValidPoint(x: Int64, y: Int64, points: Array<Array<Int64>>): Int64 {

    }
}
```

