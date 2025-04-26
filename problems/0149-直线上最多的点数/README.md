# 149. 直线上最多的点数

## 题目描述

<p>给你一个数组 <code>points</code> ，其中 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示 <strong>X-Y</strong> 平面上的一个点。求最多有多少个点在同一条直线上。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>输入：</strong>points = [[1,1],[2,2],[3,3]]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>输入：</strong>points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>输出：</strong>4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= points.length <= 300</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>4</sup></code></li>
	<li><code>points</code> 中的所有点 <strong>互不相同</strong></li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 哈希表
- 数学

## 示例

```
[[1,1],[2,2],[3,3]]
[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxPoints(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
```

### C

```c
int maxPoints(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxPoints(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxPoints = function(points) {
    
};
```

### TypeScript

```typescript
function maxPoints(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxPoints($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPoints(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPoints(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPoints(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func maxPoints(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def max_points(points)
    
end
```

### Scala

```scala
object Solution {
    def maxPoints(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_points(Points :: [[integer()]]) -> integer().
max_points(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_points(points :: [[integer]]) :: integer
  def max_points(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPoints(points: Array<Array<Int64>>): Int64 {

    }
}
```

