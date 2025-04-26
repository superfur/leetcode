# 1792. 最大平均通过率

## 题目描述

<p>一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 <code>classes</code> ，其中 <code>classes[i] = [pass<sub>i</sub>, total<sub>i</sub>]</code> ，表示你提前知道了第 <code>i</code> 个班级总共有 <code>total<sub>i</sub></code> 个学生，其中只有 <code>pass<sub>i</sub></code> 个学生可以通过考试。</p>

<p>给你一个整数 <code>extraStudents</code> ，表示额外有 <code>extraStudents</code> 个聪明的学生，他们 <strong>一定</strong> 能通过任何班级的期末考。你需要给这 <code>extraStudents</code> 个学生每人都安排一个班级，使得 <strong>所有</strong> 班级的 <strong>平均</strong> 通过率 <strong>最大</strong> 。</p>

<p>一个班级的 <strong>通过率</strong> 等于这个班级通过考试的学生人数除以这个班级的总人数。<strong>平均通过率</strong> 是所有班级的通过率之和除以班级数目。</p>

<p>请你返回在安排这 <code><span style="">extraStudents</span></code> 个学生去对应班级后的 <strong>最大</strong> 平均通过率。与标准答案误差范围在 <code>10<sup>-5</sup></code> 以内的结果都会视为正确结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>classes = [[1,2],[3,5],[2,2]], <code>extraStudents</code> = 2
<b>输出：</b>0.78333
<b>解释：</b>你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>classes = [[2,4],[3,9],[4,5],[2,10]], <code>extraStudents</code> = 4
<strong>输出：</strong>0.53485
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= classes.length <= 10<sup>5</sup></code></li>
	<li><code>classes[i].length == 2</code></li>
	<li><code>1 <= pass<sub>i</sub> <= total<sub>i</sub> <= 10<sup>5</sup></code></li>
	<li><code>1 <= extraStudents <= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 提示

1. Pay attention to how much the pass ratio changes when you add a student to the class. If you keep adding students, what happens to the change in pass ratio? The more students you add to a class, the smaller the change in pass ratio becomes.
2. Since the change in the pass ratio is always decreasing with the more students you add, then the very first student you add to each class is the one that makes the biggest change in the pass ratio.
3. Because each class's pass ratio is weighted equally, it's always optimal to put the student in the class that makes the biggest change among all the other classes.
4. Keep a max heap of the current class sizes and order them by the change in pass ratio. For each extra student, take the top of the heap, update the class size, and put it back in the heap.

## 示例

```
[[1,2],[3,5],[2,2]]
2
[[2,4],[3,9],[4,5],[2,10]]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        
    }
};
```

### Java

```java
class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
```

### C

```c
double maxAverageRatio(int** classes, int classesSize, int* classesColSize, int extraStudents) {
    
}
```

### C#

```csharp
public class Solution {
    public double MaxAverageRatio(int[][] classes, int extraStudents) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} classes
 * @param {number} extraStudents
 * @return {number}
 */
var maxAverageRatio = function(classes, extraStudents) {
    
};
```

### TypeScript

```typescript
function maxAverageRatio(classes: number[][], extraStudents: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $classes
     * @param Integer $extraStudents
     * @return Float
     */
    function maxAverageRatio($classes, $extraStudents) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAverageRatio(_ classes: [[Int]], _ extraStudents: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAverageRatio(classes: Array<IntArray>, extraStudents: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double maxAverageRatio(List<List<int>> classes, int extraStudents) {
    
  }
}
```

### Go

```golang
func maxAverageRatio(classes [][]int, extraStudents int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} classes
# @param {Integer} extra_students
# @return {Float}
def max_average_ratio(classes, extra_students)
    
end
```

### Scala

```scala
object Solution {
    def maxAverageRatio(classes: Array[Array[Int]], extraStudents: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_average_ratio(classes: Vec<Vec<i32>>, extra_students: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-average-ratio classes extraStudents)
  (-> (listof (listof exact-integer?)) exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec max_average_ratio(Classes :: [[integer()]], ExtraStudents :: integer()) -> float().
max_average_ratio(Classes, ExtraStudents) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_average_ratio(classes :: [[integer]], extra_students :: integer) :: float
  def max_average_ratio(classes, extra_students) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAverageRatio(classes: Array<Array<Int64>>, extraStudents: Int64): Float64 {

    }
}
```

