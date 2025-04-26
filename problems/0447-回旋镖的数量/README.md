# 447. 回旋镖的数量

## 题目描述

<p>给定平面上<em>&nbsp;</em><code>n</code><em> </em>对 <strong>互不相同</strong> 的点&nbsp;<code>points</code> ，其中 <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 。<strong>回旋镖</strong> 是由点&nbsp;<code>(i, j, k)</code> 表示的元组 ，其中&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;之间的欧式距离和&nbsp;<code>i</code>&nbsp;和&nbsp;<code>k</code>&nbsp;之间的欧式距离相等（<strong>需要考虑元组的顺序</strong>）。</p>

<p>返回平面上所有回旋镖的数量。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>points = [[0,0],[1,0],[2,0]]
<strong>输出：</strong>2
<strong>解释：</strong>两个回旋镖为 <strong>[[1,0],[0,0],[2,0]]</strong> 和 <strong>[[1,0],[2,0],[0,0]]</strong>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,1],[2,2],[3,3]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,1]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n ==&nbsp;points.length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>所有点都 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学

## 示例

```
[[0,0],[1,0],[2,0]]
[[1,1],[2,2],[3,3]]
[[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
```

### C

```c
int numberOfBoomerangs(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfBoomerangs(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfBoomerangs = function(points) {
    
};
```

### TypeScript

```typescript
function numberOfBoomerangs(points: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function numberOfBoomerangs($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfBoomerangs(_ points: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfBoomerangs(points: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfBoomerangs(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func numberOfBoomerangs(points [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer}
def number_of_boomerangs(points)
    
end
```

### Scala

```scala
object Solution {
    def numberOfBoomerangs(points: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_boomerangs(points: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-boomerangs points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_boomerangs(Points :: [[integer()]]) -> integer().
number_of_boomerangs(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_boomerangs(points :: [[integer]]) :: integer
  def number_of_boomerangs(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfBoomerangs(points: Array<Array<Int64>>): Int64 {

    }
}
```

