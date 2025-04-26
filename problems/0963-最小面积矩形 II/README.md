# 963. 最小面积矩形 II

## 题目描述

<p>给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边<strong>不一定平行于</strong> x 轴和 y 轴。</p>

<p>如果没有任何矩形，就返回 0。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/22/1a.png" style="height: 151px; width: 150px;"></strong></p>

<pre><strong>输入：</strong>[[1,2],[2,1],[1,0],[0,1]]
<strong>输出：</strong>2.00000
<strong>解释：</strong>最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/23/2.png" style="height: 94px; width: 150px;"></p>

<pre><strong>输入：</strong>[[0,1],[2,1],[1,1],[1,0],[2,0]]
<strong>输出：</strong>1.00000
<strong>解释：</strong>最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/23/3.png" style="height: 94px; width: 150px;"></p>

<pre><strong>输入：</strong>[[0,3],[1,2],[3,1],[1,3],[2,1]]
<strong>输出：</strong>0
<strong>解释：</strong>没法从这些点中组成任何矩形。
</pre>

<p><strong>示例 4：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/21/4c.png" style="height: 155px; width: 160px;"></strong></p>

<pre><strong>输入：</strong>[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
<strong>输出：</strong>2.00000
<strong>解释：</strong>最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= points.length &lt;= 50</code></li>
	<li><code>0 &lt;=&nbsp;points[i][0] &lt;=&nbsp;40000</code></li>
	<li><code>0 &lt;=&nbsp;points[i][1] &lt;=&nbsp;40000</code></li>
	<li>所有的点都是不同的。</li>
	<li>与真实值误差不超过 <code>10^-5</code>&nbsp;的答案将视为正确结果。</li>
</ol>


## 难度

Medium

## 标签

- 几何
- 数组
- 数学

## 示例

```
[[1,2],[2,1],[1,0],[0,1]]
[[0,1],[2,1],[1,1],[1,0],[2,0]]
[[0,3],[1,2],[3,1],[1,3],[2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double minAreaFreeRect(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public double minAreaFreeRect(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
```

### C

```c
double minAreaFreeRect(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double MinAreaFreeRect(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minAreaFreeRect = function(points) {
    
};
```

### TypeScript

```typescript
function minAreaFreeRect(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Float
     */
    function minAreaFreeRect($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minAreaFreeRect(_ points: [[Int]]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minAreaFreeRect(points: Array<IntArray>): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double minAreaFreeRect(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func minAreaFreeRect(points [][]int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Float}
def min_area_free_rect(points)
    
end
```

### Scala

```scala
object Solution {
    def minAreaFreeRect(points: Array[Array[Int]]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_area_free_rect(points: Vec<Vec<i32>>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-area-free-rect points)
  (-> (listof (listof exact-integer?)) flonum?)
  )
```

### Erlang

```erlang
-spec min_area_free_rect(Points :: [[integer()]]) -> float().
min_area_free_rect(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_area_free_rect(points :: [[integer]]) :: float
  def min_area_free_rect(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minAreaFreeRect(points: Array<Array<Int64>>): Float64 {

    }
}
```

