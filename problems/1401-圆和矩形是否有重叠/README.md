# 1401. 圆和矩形是否有重叠

## 题目描述

<p>给你一个以 <code>(radius, xCenter, yCenter)</code> 表示的圆和一个与坐标轴平行的矩形 <code>(x1, y1, x2, y2)</code> ，其中 <code>(x1, y1)</code> 是矩形左下角的坐标，而 <code>(x2, y2)</code> 是右上角的坐标。</p>

<p>如果圆和矩形有重叠的部分，请你返回 <code>true</code> ，否则返回 <code>false</code>&nbsp;。</p>

<p>换句话说，请你检测是否 <strong>存在</strong> 点 <code>(x<sub>i</sub>, y<sub>i</sub>)</code> ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1 ：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png" style="width: 258px; height: 167px;" />
<pre>
<strong>输入：</strong>radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
<strong>输出：</strong>true
<strong>解释：</strong>圆和矩形存在公共点 (1,0) 。
</pre>

<p><strong class="example">示例 2 ：</strong></p>

<pre>
<strong>输入：</strong>radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
<strong>输出：</strong>false
</pre>

<p><strong class="example">示例 3 ：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png" style="width: 150px; height: 135px;" />
<pre>
<strong>输入：</strong>radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= radius &lt;= 2000</code></li>
	<li><code>-10<sup>4</sup> &lt;= xCenter, yCenter &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= x1 &lt; x2 &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= y1 &lt; y2 &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数学

## 提示

1. Locate the closest point of the square to the circle, you can then find the distance from this point to the center of the circle and check if this is less than or equal to the radius.

## 示例

```
1
0
0
1
-1
3
1
1
1
1
1
-3
2
-1
1
0
0
-1
0
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
```

### C

```c
bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} radius
 * @param {number} xCenter
 * @param {number} yCenter
 * @param {number} x1
 * @param {number} y1
 * @param {number} x2
 * @param {number} y2
 * @return {boolean}
 */
var checkOverlap = function(radius, xCenter, yCenter, x1, y1, x2, y2) {
    
};
```

### TypeScript

```typescript
function checkOverlap(radius: number, xCenter: number, yCenter: number, x1: number, y1: number, x2: number, y2: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $radius
     * @param Integer $xCenter
     * @param Integer $yCenter
     * @param Integer $x1
     * @param Integer $y1
     * @param Integer $x2
     * @param Integer $y2
     * @return Boolean
     */
    function checkOverlap($radius, $xCenter, $yCenter, $x1, $y1, $x2, $y2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkOverlap(_ radius: Int, _ xCenter: Int, _ yCenter: Int, _ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
    
  }
}
```

### Go

```golang
func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} radius
# @param {Integer} x_center
# @param {Integer} y_center
# @param {Integer} x1
# @param {Integer} y1
# @param {Integer} x2
# @param {Integer} y2
# @return {Boolean}
def check_overlap(radius, x_center, y_center, x1, y1, x2, y2)
    
end
```

### Scala

```scala
object Solution {
    def checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_overlap(radius: i32, x_center: i32, y_center: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-overlap radius xCenter yCenter x1 y1 x2 y2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec check_overlap(Radius :: integer(), XCenter :: integer(), YCenter :: integer(), X1 :: integer(), Y1 :: integer(), X2 :: integer(), Y2 :: integer()) -> boolean().
check_overlap(Radius, XCenter, YCenter, X1, Y1, X2, Y2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_overlap(radius :: integer, x_center :: integer, y_center :: integer, x1 :: integer, y1 :: integer, x2 :: integer, y2 :: integer) :: boolean
  def check_overlap(radius, x_center, y_center, x1, y1, x2, y2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkOverlap(radius: Int64, xCenter: Int64, yCenter: Int64, x1: Int64, y1: Int64, x2: Int64, y2: Int64): Bool {

    }
}
```

