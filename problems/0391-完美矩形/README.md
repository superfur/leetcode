# 391. 完美矩形

## 题目描述

<p>给你一个数组 <code>rectangles</code> ，其中 <code>rectangles[i] = [x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub>]</code> 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 <code>(x<sub>i</sub>, y<sub>i</sub>)</code> ，右上顶点是 <code>(a<sub>i</sub>, b<sub>i</sub>)</code> 。</p>

<p>如果所有矩形一起精确覆盖了某个矩形区域，则返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>
&nbsp;

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg" style="height: 294px; width: 300px;" />
<pre>
<strong>输入：</strong>rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
<strong>输出：</strong>true
<strong>解释：</strong>5 个矩形一起可以精确地覆盖一个矩形区域。 
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg" style="height: 294px; width: 300px;" />
<pre>
<strong>输入：</strong>rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
<strong>输出：</strong>false
<strong>解释：</strong>两个矩形之间有间隔，无法覆盖成一个矩形。</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg" style="height: 294px; width: 300px;" />
<pre>
<strong>输入：</strong>rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
<strong>输出：</strong>false
<strong>解释：</strong>因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>rectangles[i].length == 4</code></li>
	<li><code>-10<sup>5</sup> &lt;= x<sub>i</sub> &lt; a<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= y<sub>i</sub> &lt; b<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 扫描线

## 示例

```
[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
[[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
[[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
```

### C

```c
bool isRectangleCover(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsRectangleCover(int[][] rectangles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var isRectangleCover = function(rectangles) {
    
};
```

### TypeScript

```typescript
function isRectangleCover(rectangles: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @return Boolean
     */
    function isRectangleCover($rectangles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isRectangleCover(_ rectangles: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isRectangleCover(rectangles: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isRectangleCover(List<List<int>> rectangles) {
    
  }
}
```

### Go

```golang
func isRectangleCover(rectangles [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} rectangles
# @return {Boolean}
def is_rectangle_cover(rectangles)
    
end
```

### Scala

```scala
object Solution {
    def isRectangleCover(rectangles: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_rectangle_cover(rectangles: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-rectangle-cover rectangles)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec is_rectangle_cover(Rectangles :: [[integer()]]) -> boolean().
is_rectangle_cover(Rectangles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_rectangle_cover(rectangles :: [[integer]]) :: boolean
  def is_rectangle_cover(rectangles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isRectangleCover(rectangles: Array<Array<Int64>>): Bool {

    }
}
```

