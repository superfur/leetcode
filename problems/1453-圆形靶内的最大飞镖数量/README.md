# 1453. 圆形靶内的最大飞镖数量

## 题目描述

<p>Alice 向一面非常大的墙上掷出 <code>n</code> 支飞镖。给你一个数组 <code>darts</code> ，其中 <code>darts[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示 Alice 掷出的第 <code>i</code> 支飞镖落在墙上的位置。</p>

<p>Bob 知道墙上所有 <code>n</code> 支飞镖的位置。他想要往墙上放置一个半径为 <code>r</code> 的圆形靶。使 Alice 掷出的飞镖尽可能多地落在靶上。</p>

<p>给你整数 <code>r</code> ，请返回能够落在 <strong>任意</strong> 半径为 <code>r</code> 的圆形靶内或靶上的最大飞镖数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1 ：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/29/sample_1_1806.png" style="width: 248px; height: 211px;" />
<pre>
<strong>输入：</strong>darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
<strong>输出：</strong>4
<strong>解释：</strong>如果圆形靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
</pre>

<p><strong class="example">示例 2 ：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/29/sample_2_1806.png" style="width: 306px; height: 244px;" />
<pre>
<strong>输入：</strong>darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
<strong>输出：</strong>5
<strong>解释：</strong>如果圆形靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= darts.length &lt;= 100</code></li>
	<li><code>darts[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>darts</code> 中的元素互不相同</li>
	<li><code>1 &lt;= r &lt;= 5000</code></li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 数学

## 提示

1. If there is an optimal solution, you can always move the circle so that two points lie on the boundary of the circle.
2. When the radius is fixed, you can find either 0 or 1 or 2 circles that pass two given points at the same time.
3. Loop for each pair of points and find the center of the circle, after that count the number of points inside the circle.

## 示例

```
[[-2,0],[2,0],[0,2],[0,-2]]
2
[[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numPoints(vector<vector<int>>& darts, int r) {
        
    }
};
```

### Java

```java
class Solution {
    public int numPoints(int[][] darts, int r) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numPoints(self, darts, r):
        """
        :type darts: List[List[int]]
        :type r: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        
```

### C

```c
int numPoints(int** darts, int dartsSize, int* dartsColSize, int r) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumPoints(int[][] darts, int r) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} darts
 * @param {number} r
 * @return {number}
 */
var numPoints = function(darts, r) {
    
};
```

### TypeScript

```typescript
function numPoints(darts: number[][], r: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $darts
     * @param Integer $r
     * @return Integer
     */
    function numPoints($darts, $r) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numPoints(_ darts: [[Int]], _ r: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numPoints(darts: Array<IntArray>, r: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numPoints(List<List<int>> darts, int r) {
    
  }
}
```

### Go

```golang
func numPoints(darts [][]int, r int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} darts
# @param {Integer} r
# @return {Integer}
def num_points(darts, r)
    
end
```

### Scala

```scala
object Solution {
    def numPoints(darts: Array[Array[Int]], r: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_points(darts: Vec<Vec<i32>>, r: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-points darts r)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_points(Darts :: [[integer()]], R :: integer()) -> integer().
num_points(Darts, R) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_points(darts :: [[integer]], r :: integer) :: integer
  def num_points(darts, r) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numPoints(darts: Array<Array<Int64>>, r: Int64): Int64 {

    }
}
```

