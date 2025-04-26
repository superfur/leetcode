# 面试题 16.03. 交点

## 题目描述

<p>给定两条线段（表示为起点<code>start = {X1, Y1}</code>和终点<code>end = {X2, Y2}</code>），如果它们有交点，请计算其交点，没有交点则返回空值。</p>

<p>要求浮点型误差不超过<code>10^-6</code>。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
<strong>输出：</strong> {0.5, 0}
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
<strong>输出：</strong> {1, 1}
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
<strong>输出：</strong> {}，两条线段没有交点
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>坐标绝对值不会超过 2^7</li>
	<li>输入的坐标均是有效的二维坐标</li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数学

## 提示

1. 所有的线都会相交吗？什么决定两条线是否相交？
2. 无限长的线几乎总会相交，除非它们相互平行。平行线也仍然有可能“相交”——如果它们是同一条线。这对线段来说意味着什么？
3. 我们怎样才能找到两条线的交点。如果两条线相交，那么交点必须与它们的“无限”延伸处于同一点。这两条线之间是交点吗？
4. 仔细考虑如何处理线段具有相同斜率和与y轴相交的情况。

## 示例

```
[0,0]
[0,1]
[1,0]
[1,1]
[0,-1]
[0,1]
[-1,1]
[1,3]
[0,3]
[0,6]
[0,1]
[0,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<double> intersection(vector<int>& start1, vector<int>& end1, vector<int>& start2, vector<int>& end2) {
        
    }
};
```

### Java

```java
class Solution {
    public double[] intersection(int[] start1, int[] end1, int[] start2, int[] end2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def intersection(self, start1, end1, start2, end2):
        """
        :type start1: List[int]
        :type end1: List[int]
        :type start2: List[int]
        :type end2: List[int]
        :rtype: List[float]
        """
        
```

### Python3

```python3
class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* intersection(int* start1, int start1Size, int* end1, int end1Size, int* start2, int start2Size, int* end2, int end2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double[] Intersection(int[] start1, int[] end1, int[] start2, int[] end2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} start1
 * @param {number[]} end1
 * @param {number[]} start2
 * @param {number[]} end2
 * @return {number[]}
 */
var intersection = function(start1, end1, start2, end2) {
    
};
```

### TypeScript

```typescript
function intersection(start1: number[], end1: number[], start2: number[], end2: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $start1
     * @param Integer[] $end1
     * @param Integer[] $start2
     * @param Integer[] $end2
     * @return Float[]
     */
    function intersection($start1, $end1, $start2, $end2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func intersection(_ start1: [Int], _ end1: [Int], _ start2: [Int], _ end2: [Int]) -> [Double] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun intersection(start1: IntArray, end1: IntArray, start2: IntArray, end2: IntArray): DoubleArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<double> intersection(List<int> start1, List<int> end1, List<int> start2, List<int> end2) {
    
  }
}
```

### Go

```golang
func intersection(start1 []int, end1 []int, start2 []int, end2 []int) []float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} start1
# @param {Integer[]} end1
# @param {Integer[]} start2
# @param {Integer[]} end2
# @return {Float[]}
def intersection(start1, end1, start2, end2)
    
end
```

### Scala

```scala
object Solution {
    def intersection(start1: Array[Int], end1: Array[Int], start2: Array[Int], end2: Array[Int]): Array[Double] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn intersection(start1: Vec<i32>, end1: Vec<i32>, start2: Vec<i32>, end2: Vec<i32>) -> Vec<f64> {
        
    }
}
```

### Racket

```racket
(define/contract (intersection start1 end1 start2 end2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof flonum?))
  )
```

### Erlang

```erlang
-spec intersection(Start1 :: [integer()], End1 :: [integer()], Start2 :: [integer()], End2 :: [integer()]) -> [float()].
intersection(Start1, End1, Start2, End2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec intersection(start1 :: [integer], end1 :: [integer], start2 :: [integer], end2 :: [integer]) :: [float]
  def intersection(start1, end1, start2, end2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func intersection(start1: Array<Int64>, end1: Array<Int64>, start2: Array<Int64>, end2: Array<Int64>): Array<Float64> {

    }
}
```

