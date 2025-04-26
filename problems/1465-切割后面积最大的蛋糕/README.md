# 1465. 切割后面积最大的蛋糕

## 题目描述

<p>矩形蛋糕的高度为 <code>h</code> 且宽度为 <code>w</code>，给你两个整数数组 <code>horizontalCuts</code> 和 <code>verticalCuts</code>，其中：</p>

<ul>
	<li>&nbsp;<code>horizontalCuts[i]</code> 是从矩形蛋糕顶部到第&nbsp; <code>i</code> 个水平切口的距离</li>
	<li><code>verticalCuts[j]</code> 是从矩形蛋糕的左侧到第 <code>j</code> 个竖直切口的距离</li>
</ul>

<p>请你按数组 <em><code>horizontalCuts</code> </em>和<em> <code>verticalCuts</code> </em>中提供的水平和竖直位置切割后，请你找出 <strong>面积最大</strong> 的那份蛋糕，并返回其 <strong>面积</strong> 。由于答案可能是一个很大的数字，因此需要将结果&nbsp;<strong>对</strong>&nbsp;<code>10<sup>9</sup>&nbsp;+ 7</code>&nbsp;<strong>取余</strong> 后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_2.png" /></p>

<pre>
<strong>输入：</strong>h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
<strong>输出：</strong>4 
<strong>解释：</strong>上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_3.png" /></strong></p>

<pre>
<strong>输入：</strong>h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
<strong>输出：</strong>6
<strong>解释：</strong>上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
<strong>输出：</strong>9
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= h, w &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= horizontalCuts.length &lt;= min(h - 1, 10<sup>5</sup>)</code></li>
	<li><code>1 &lt;= verticalCuts.length &lt;= min(w - 1, 10<sup>5</sup>)</code></li>
	<li><code>1 &lt;= horizontalCuts[i] &lt; h</code></li>
	<li><code>1 &lt;= verticalCuts[i] &lt; w</code></li>
	<li>题目数据保证 <code>horizontalCuts</code> 中的所有元素各不相同</li>
	<li>题目数据保证 <code>verticalCuts</code>&nbsp;中的所有元素各不相同</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Sort the arrays, then compute the maximum difference between two consecutive elements for horizontal cuts and vertical cuts.
2. The answer is the product of these maximum values in horizontal cuts and vertical cuts.

## 示例

```
5
4
[1,2,4]
[1,3]
5
4
[3,1]
[1]
5
4
[3]
[3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
```

### C

```c
int maxArea(int h, int w, int* horizontalCuts, int horizontalCutsSize, int* verticalCuts, int verticalCutsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} horizontalCuts
 * @param {number[]} verticalCuts
 * @return {number}
 */
var maxArea = function(h, w, horizontalCuts, verticalCuts) {
    
};
```

### TypeScript

```typescript
function maxArea(h: number, w: number, horizontalCuts: number[], verticalCuts: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $h
     * @param Integer $w
     * @param Integer[] $horizontalCuts
     * @param Integer[] $verticalCuts
     * @return Integer
     */
    function maxArea($h, $w, $horizontalCuts, $verticalCuts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxArea(_ h: Int, _ w: Int, _ horizontalCuts: [Int], _ verticalCuts: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxArea(h: Int, w: Int, horizontalCuts: IntArray, verticalCuts: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxArea(int h, int w, List<int> horizontalCuts, List<int> verticalCuts) {
    
  }
}
```

### Go

```golang
func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} h
# @param {Integer} w
# @param {Integer[]} horizontal_cuts
# @param {Integer[]} vertical_cuts
# @return {Integer}
def max_area(h, w, horizontal_cuts, vertical_cuts)
    
end
```

### Scala

```scala
object Solution {
    def maxArea(h: Int, w: Int, horizontalCuts: Array[Int], verticalCuts: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_area(h: i32, w: i32, horizontal_cuts: Vec<i32>, vertical_cuts: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-area h w horizontalCuts verticalCuts)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_area(H :: integer(), W :: integer(), HorizontalCuts :: [integer()], VerticalCuts :: [integer()]) -> integer().
max_area(H, W, HorizontalCuts, VerticalCuts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_area(h :: integer, w :: integer, horizontal_cuts :: [integer], vertical_cuts :: [integer]) :: integer
  def max_area(h, w, horizontal_cuts, vertical_cuts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxArea(h: Int64, w: Int64, horizontalCuts: Array<Int64>, verticalCuts: Array<Int64>): Int64 {

    }
}
```

