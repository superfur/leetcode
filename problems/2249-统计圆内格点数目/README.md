# 2249. 统计圆内格点数目

## 题目描述

<p>给你一个二维整数数组 <code>circles</code> ，其中 <code>circles[i] = [x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub>]</code> 表示网格上圆心为 <code>(x<sub>i</sub>, y<sub>i</sub>)</code> 且半径为 <code>r<sub>i</sub></code> 的第 <code>i</code> 个圆，返回出现在<strong> 至少一个 </strong>圆内的 <strong>格点数目</strong> 。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><strong>格点</strong> 是指整数坐标对应的点。</li>
	<li><strong>圆周上的点</strong> 也被视为出现在圆内的点。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/exa-11.png" style="width: 300px; height: 300px;" /></p>

<pre>
<strong>输入：</strong>circles = [[2,2,1]]
<strong>输出：</strong>5
<strong>解释：</strong>
给定的圆如上图所示。
出现在圆内的格点为 (1, 2)、(2, 1)、(2, 2)、(2, 3) 和 (3, 2)，在图中用绿色标识。
像 (1, 1) 和 (1, 3) 这样用红色标识的点，并未出现在圆内。
因此，出现在至少一个圆内的格点数目是 5 。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/exa-22.png" style="width: 300px; height: 300px;" /></p>

<pre>
<strong>输入：</strong>circles = [[2,2,2],[3,4,1]]
<strong>输出：</strong>16
<strong>解释：</strong>
给定的圆如上图所示。
共有 16 个格点出现在至少一个圆内。
其中部分点的坐标是 (0, 2)、(2, 0)、(2, 4)、(3, 2) 和 (4, 4) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= circles.length &lt;= 200</code></li>
	<li><code>circles[i].length == 3</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 100</code></li>
	<li><code>1 &lt;= r<sub>i</sub> &lt;= min(x<sub>i</sub>, y<sub>i</sub>)</code></li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数组
- 哈希表
- 数学
- 枚举

## 提示

1. For each circle, how can you check whether or not a lattice point lies inside it?
2. Since you need to reduce the search space, consider the minimum and maximum possible values of the coordinates of a lattice point contained in any circle.

## 示例

```
[[2,2,1]]
[[2,2,2],[3,4,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countLatticePoints(vector<vector<int>>& circles) {
        
    }
};
```

### Java

```java
class Solution {
    public int countLatticePoints(int[][] circles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
```

### C

```c
int countLatticePoints(int** circles, int circlesSize, int* circlesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountLatticePoints(int[][] circles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} circles
 * @return {number}
 */
var countLatticePoints = function(circles) {
    
};
```

### TypeScript

```typescript
function countLatticePoints(circles: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $circles
     * @return Integer
     */
    function countLatticePoints($circles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countLatticePoints(_ circles: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countLatticePoints(circles: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countLatticePoints(List<List<int>> circles) {
    
  }
}
```

### Go

```golang
func countLatticePoints(circles [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} circles
# @return {Integer}
def count_lattice_points(circles)
    
end
```

### Scala

```scala
object Solution {
    def countLatticePoints(circles: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_lattice_points(circles: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-lattice-points circles)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_lattice_points(Circles :: [[integer()]]) -> integer().
count_lattice_points(Circles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_lattice_points(circles :: [[integer]]) :: integer
  def count_lattice_points(circles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countLatticePoints(circles: Array<Array<Int64>>): Int64 {

    }
}
```

