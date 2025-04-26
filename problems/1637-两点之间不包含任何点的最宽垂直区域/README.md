# 1637. 两点之间不包含任何点的最宽垂直区域

## 题目描述

<p>给你&nbsp;<code>n</code>&nbsp;个二维平面上的点 <code>points</code> ，其中&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;，请你返回两点之间内部不包含任何点的&nbsp;<strong>最宽垂直区域</strong> 的宽度。</p>

<p><strong>垂直区域</strong> 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 <strong>最宽垂直区域</strong> 为宽度最大的一个垂直区域。</p>

<p>请注意，垂直区域&nbsp;<strong>边上</strong>&nbsp;的点&nbsp;<strong>不在</strong>&nbsp;区域内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/31/points3.png" style="width: 276px; height: 371px;" />​
<pre>
<b>输入：</b>points = [[8,7],[9,9],[7,4],[9,7]]
<b>输出：</b>1
<b>解释：</b>红色区域和蓝色区域都是最优区域。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
<b>输出：</b>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == points.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. Try sorting the points
2. Think whether the y-axis of a point is relevant

## 示例

```
[[8,7],[9,9],[7,4],[9,7]]
[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
```

### C

```c
int maxWidthOfVerticalArea(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxWidthOfVerticalArea(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {
    
};
```

### TypeScript

```typescript
function maxWidthOfVerticalArea(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxWidthOfVerticalArea($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxWidthOfVerticalArea(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxWidthOfVerticalArea(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxWidthOfVerticalArea(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func maxWidthOfVerticalArea(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def max_width_of_vertical_area(points)
    
end
```

### Scala

```scala
object Solution {
    def maxWidthOfVerticalArea(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_width_of_vertical_area(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-width-of-vertical-area points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_width_of_vertical_area(Points :: [[integer()]]) -> integer().
max_width_of_vertical_area(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_width_of_vertical_area(points :: [[integer]]) :: integer
  def max_width_of_vertical_area(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxWidthOfVerticalArea(points: Array<Array<Int64>>): Int64 {

    }
}
```

