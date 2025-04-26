# 1232. 缀点成线

## 题目描述

<p>给定一个数组&nbsp;<code>coordinates</code>&nbsp;，其中&nbsp;<code>coordinates[i] = [x, y]</code>&nbsp;，<meta charset="UTF-8" />&nbsp;<code>[x, y]</code>&nbsp;表示横坐标为 <code>x</code>、纵坐标为 <code>y</code>&nbsp;的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-2.jpg" /></p>

<pre>
<strong>输入：</strong>coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
<strong>输出：</strong>true
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-1.jpg" /></strong></p>

<pre>
<strong>输入：</strong>coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;=&nbsp;coordinates.length &lt;= 1000</code></li>
	<li><code>coordinates[i].length == 2</code></li>
	<li><code>-10^4 &lt;=&nbsp;coordinates[i][0],&nbsp;coordinates[i][1] &lt;= 10^4</code></li>
	<li><code>coordinates</code>&nbsp;中不含重复的点</li>
</ul>


## 难度

Easy

## 标签

- 几何
- 数组
- 数学

## 提示

1. If there're only 2 points, return true.
2. Check if all other points lie on the line defined by the first 2 points.
3. Use cross product to check collinearity.

## 示例

```
[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
```

### C

```c
bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckStraightLine(int[][] coordinates) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    
};
```

### TypeScript

```typescript
function checkStraightLine(coordinates: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $coordinates
     * @return Boolean
     */
    function checkStraightLine($coordinates) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkStraightLine(_ coordinates: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkStraightLine(coordinates: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkStraightLine(List<List<int>> coordinates) {
    
  }
}
```

### Go

```golang
func checkStraightLine(coordinates [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} coordinates
# @return {Boolean}
def check_straight_line(coordinates)
    
end
```

### Scala

```scala
object Solution {
    def checkStraightLine(coordinates: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-straight-line coordinates)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec check_straight_line(Coordinates :: [[integer()]]) -> boolean().
check_straight_line(Coordinates) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_straight_line(coordinates :: [[integer]]) :: boolean
  def check_straight_line(coordinates) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkStraightLine(coordinates: Array<Array<Int64>>): Bool {

    }
}
```

