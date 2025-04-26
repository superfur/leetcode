# LCR 039. 柱状图中最大的矩形

## 题目描述

<p>给定非负整数数组 <code>heights</code>&nbsp;，数组中的数字用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 <code>1</code> 。</p>

<p>求在该柱状图中，能够勾勒出来的矩形的最大面积。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" /></p>

<pre>
<strong>输入：</strong>heights = [2,1,5,6,2,3]
<strong>输出：</strong>10
<strong>解释：</strong>最大的矩形为图中红色区域，面积为 10
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" /></p>

<pre>
<strong>输入：</strong> heights = [2,4]
<strong>输出：</strong> 4</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;=10<sup>5</sup></code></li>
	<li><code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 84&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/largest-rectangle-in-histogram/">https://leetcode-cn.com/problems/largest-rectangle-in-histogram/</a></p>


## 难度

Hard

## 标签

- 栈
- 数组
- 单调栈

## 示例

```
[2,1,5,6,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {

    }
};
```

### Java

```java
class Solution {
    public int largestRectangleArea(int[] heights) {

    }
}
```

### Python

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
```

### C

```c


int largestRectangleArea(int* heights, int heightsSize){

}
```

### C#

```csharp
public class Solution {
    public int LargestRectangleArea(int[] heights) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {

};
```

### TypeScript

```typescript
function largestRectangleArea(heights: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @return Integer
     */
    function largestRectangleArea($heights) {

    }
}
```

### Swift

```swift
class Solution {
    func largestRectangleArea(_ heights: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestRectangleArea(heights: IntArray): Int {

    }
}
```

### Go

```golang
func largestRectangleArea(heights []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)

end
```

### Scala

```scala
object Solution {
    def largestRectangleArea(heights: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (largest-rectangle-area heights)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec largest_rectangle_area(Heights :: [integer()]) -> integer().
largest_rectangle_area(Heights) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_rectangle_area(heights :: [integer]) :: integer
  def largest_rectangle_area(heights) do

  end
end
```

