# 836. 矩形重叠

## 题目描述

<p>矩形以列表 <code>[x1, y1, x2, y2]</code> 的形式表示，其中 <code>(x1, y1)</code> 为左下角的坐标，<code>(x2, y2)</code> 是右上角的坐标。矩形的上下边平行于 x 轴，左右边平行于 y 轴。</p>

<p>如果相交的面积为 <strong>正</strong> ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。</p>

<p>给出两个矩形 <code>rec1</code> 和 <code>rec2</code> 。如果它们重叠，返回 <code>true</code>；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>rec1 = [0,0,2,2], rec2 = [1,1,3,3]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>rec1 = [0,0,1,1], rec2 = [1,0,2,1]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rec1 = [0,0,1,1], rec2 = [2,2,3,3]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rect1.length == 4</code></li>
	<li><code>rect2.length == 4</code></li>
	<li><code>-10<sup>9</sup> &lt;= rec1[i], rec2[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>rec1</code> 和 <code>rec2</code> 表示一个面积不为零的有效矩形</li>
</ul>


## 难度

Easy

## 标签

- 几何
- 数学

## 示例

```
[0,0,2,2]
[1,1,3,3]
[0,0,1,1]
[1,0,2,1]
[0,0,1,1]
[2,2,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
```

### C

```c
bool isRectangleOverlap(int* rec1, int rec1Size, int* rec2, int rec2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsRectangleOverlap(int[] rec1, int[] rec2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
    
};
```

### TypeScript

```typescript
function isRectangleOverlap(rec1: number[], rec2: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rec1
     * @param Integer[] $rec2
     * @return Boolean
     */
    function isRectangleOverlap($rec1, $rec2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isRectangleOverlap(_ rec1: [Int], _ rec2: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isRectangleOverlap(rec1: IntArray, rec2: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isRectangleOverlap(List<int> rec1, List<int> rec2) {
    
  }
}
```

### Go

```golang
func isRectangleOverlap(rec1 []int, rec2 []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} rec1
# @param {Integer[]} rec2
# @return {Boolean}
def is_rectangle_overlap(rec1, rec2)
    
end
```

### Scala

```scala
object Solution {
    def isRectangleOverlap(rec1: Array[Int], rec2: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_rectangle_overlap(rec1: Vec<i32>, rec2: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-rectangle-overlap rec1 rec2)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_rectangle_overlap(Rec1 :: [integer()], Rec2 :: [integer()]) -> boolean().
is_rectangle_overlap(Rec1, Rec2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_rectangle_overlap(rec1 :: [integer], rec2 :: [integer]) :: boolean
  def is_rectangle_overlap(rec1, rec2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isRectangleOverlap(rec1: Array<Int64>, rec2: Array<Int64>): Bool {

    }
}
```

