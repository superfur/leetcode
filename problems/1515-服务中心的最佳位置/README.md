# 1515. 服务中心的最佳位置

## 题目描述

<p>一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，并希望能够以此为依据为新的服务中心选址：使服务中心 <strong>到所有客户的欧几里得距离的总和最小</strong> 。</p>

<p>给你一个数组 <code>positions</code> ，其中 <code>positions[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示第 <code>i</code> 个客户在二维地图上的位置，返回到所有客户的 <strong>欧几里得距离的最小总和 。</strong></p>

<p>换句话说，请你为服务中心选址，该位置的坐标 <code>[x<sub>centre</sub>, y<sub>centre</sub>]</code> 需要使下面的公式取到最小值：</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/q4_edited.jpg" /></p>

<p>与真实值误差在 <code>10<sup>-5</sup></code>之内的答案将被视作正确答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/q4_e1.jpg" /></p>

<pre>
<strong>输入：</strong>positions = [[0,1],[1,0],[1,2],[2,1]]
<strong>输出：</strong>4.00000
<strong>解释：</strong>如图所示，你可以选 [x<sub>centre</sub>, y<sub>centre</sub>] = [1, 1] 作为新中心的位置，这样一来到每个客户的距离就都是 1，所有距离之和为 4 ，这也是可以找到的最小值。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/q4_e3.jpg" /></p>

<pre>
<strong>输入：</strong>positions = [[1,1],[3,3]]
<strong>输出：</strong>2.82843
<strong>解释：</strong>欧几里得距离可能的最小总和为 sqrt(2) + sqrt(2) = 2.82843
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= positions.length &lt;= 50</code></li>
	<li><code>positions[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 数学
- 随机化

## 提示

1. The problem can be reworded as, giving a set of points on a 2d-plane, return the geometric median.
2. Loop over each triplet of points (positions[i], positions[j], positions[k]) where i < j < k, get the centre of the circle which goes throw the 3 points, check if all other points lie in this circle.

## 示例

```
[[0,1],[1,0],[1,2],[2,1]]
[[1,1],[3,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        
    }
};
```

### Java

```java
class Solution {
    public double getMinDistSum(int[][] positions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        
```

### C

```c
double getMinDistSum(int** positions, int positionsSize, int* positionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double GetMinDistSum(int[][] positions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} positions
 * @return {number}
 */
var getMinDistSum = function(positions) {
    
};
```

### TypeScript

```typescript
function getMinDistSum(positions: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $positions
     * @return Float
     */
    function getMinDistSum($positions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMinDistSum(_ positions: [[Int]]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMinDistSum(positions: Array<IntArray>): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double getMinDistSum(List<List<int>> positions) {
    
  }
}
```

### Go

```golang
func getMinDistSum(positions [][]int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} positions
# @return {Float}
def get_min_dist_sum(positions)
    
end
```

### Scala

```scala
object Solution {
    def getMinDistSum(positions: Array[Array[Int]]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_min_dist_sum(positions: Vec<Vec<i32>>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (get-min-dist-sum positions)
  (-> (listof (listof exact-integer?)) flonum?)
  )
```

### Erlang

```erlang
-spec get_min_dist_sum(Positions :: [[integer()]]) -> float().
get_min_dist_sum(Positions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_min_dist_sum(positions :: [[integer]]) :: float
  def get_min_dist_sum(positions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMinDistSum(positions: Array<Array<Int64>>): Float64 {

    }
}
```

