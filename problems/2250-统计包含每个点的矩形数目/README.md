# 2250. 统计包含每个点的矩形数目

## 题目描述

<p>给你一个二维整数数组&nbsp;<code>rectangles</code>&nbsp;，其中&nbsp;<code>rectangles[i] = [l<sub>i</sub>, h<sub>i</sub>]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个矩形长为&nbsp;<code>l<sub>i</sub></code>&nbsp;高为&nbsp;<code>h<sub>i</sub></code>&nbsp;。给你一个二维整数数组&nbsp;<code>points</code>&nbsp;，其中&nbsp;<code>points[j] = [x<sub>j</sub>, y<sub>j</sub>]</code>&nbsp;是坐标为&nbsp;<code>(x<sub>j</sub>, y<sub>j</sub>)</code>&nbsp;的一个点。</p>

<p>第&nbsp;<code>i</code>&nbsp;个矩形的 <strong>左下角</strong>&nbsp;在&nbsp;<code>(0, 0)</code>&nbsp;处，<strong>右上角</strong>&nbsp;在&nbsp;<code>(l<sub>i</sub>, h<sub>i</sub>)</code>&nbsp;。</p>

<p>请你返回一个整数数组<em>&nbsp;</em><code>count</code>&nbsp;，长度为&nbsp;<code>points.length</code>，其中<em>&nbsp;</em><code>count[j]</code>是 <strong>包含</strong> 第<em>&nbsp;</em><code>j</code>&nbsp;个点的矩形数目。</p>

<p>如果&nbsp;<code>0 &lt;= x<sub>j</sub> &lt;= l<sub>i</sub></code> 且&nbsp;<code>0 &lt;= y<sub>j</sub> &lt;= h<sub>i</sub></code>&nbsp;，那么我们说第&nbsp;<code>i</code>&nbsp;个矩形包含第&nbsp;<code>j</code>&nbsp;个点。如果一个点刚好在矩形的 <strong>边上</strong>&nbsp;，这个点也被视为被矩形包含。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/example1.png" style="width: 300px; height: 509px;"></p>

<pre><b>输入：</b>rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
<b>输出：</b>[2,1]
<b>解释：</b>
第一个矩形不包含任何点。
第二个矩形只包含一个点 (2, 1) 。
第三个矩形包含点 (2, 1) 和 (1, 4) 。
包含点 (2, 1) 的矩形数目为 2 。
包含点 (1, 4) 的矩形数目为 1 。
所以，我们返回 [2, 1] 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/example2.png" style="width: 300px; height: 312px;"></p>

<pre><b>输入：</b>rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
<b>输出：</b>[1,3]
<strong>解释：
</strong>第一个矩形只包含点 (1, 1) 。
第二个矩形只包含点 (1, 1) 。
第三个矩形包含点 (1, 3) 和 (1, 1) 。
包含点 (1, 3) 的矩形数目为 1 。
包含点 (1, 1) 的矩形数目为 3 。
所以，我们返回 [1, 3] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length, points.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>rectangles[i].length == points[j].length == 2</code></li>
	<li><code>1 &lt;= l<sub>i</sub>, x<sub>j</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= h<sub>i</sub>, y<sub>j</sub> &lt;= 100</code></li>
	<li>所有&nbsp;<code>rectangles</code>&nbsp;<strong>互不相同</strong>&nbsp;。</li>
	<li>所有&nbsp;<code>points</code> <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 树状数组
- 数组
- 哈希表
- 二分查找
- 排序

## 提示

1. The heights of the rectangles and the y-coordinates of the points are only at most 100, so for each point, we can iterate over the possible heights of the rectangles that contain a given point.
2. For a given point and height, can we efficiently count how many rectangles with that height contain our point?
3. Sort the rectangles at each height and use binary search.

## 示例

```
[[1,2],[2,3],[2,5]]
[[2,1],[1,4]]
[[1,1],[2,2],[3,3]]
[[1,3],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countRectangles(vector<vector<int>>& rectangles, vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countRectangles(int[][] rectangles, int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize, int** points, int pointsSize, int* pointsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountRectangles(int[][] rectangles, int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} rectangles
 * @param {number[][]} points
 * @return {number[]}
 */
var countRectangles = function(rectangles, points) {
    
};
```

### TypeScript

```typescript
function countRectangles(rectangles: number[][], points: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @param Integer[][] $points
     * @return Integer[]
     */
    function countRectangles($rectangles, $points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countRectangles(_ rectangles: [[Int]], _ points: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countRectangles(rectangles: Array<IntArray>, points: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countRectangles(List<List<int>> rectangles, List<List<int>> points) {
    
  }
}
```

### Go

```golang
func countRectangles(rectangles [][]int, points [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} rectangles
# @param {Integer[][]} points
# @return {Integer[]}
def count_rectangles(rectangles, points)
    
end
```

### Scala

```scala
object Solution {
    def countRectangles(rectangles: Array[Array[Int]], points: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_rectangles(rectangles: Vec<Vec<i32>>, points: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-rectangles rectangles points)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_rectangles(Rectangles :: [[integer()]], Points :: [[integer()]]) -> [integer()].
count_rectangles(Rectangles, Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_rectangles(rectangles :: [[integer]], points :: [[integer]]) :: [integer]
  def count_rectangles(rectangles, points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countRectangles(rectangles: Array<Array<Int64>>, points: Array<Array<Int64>>): Array<Int64> {

    }
}
```

