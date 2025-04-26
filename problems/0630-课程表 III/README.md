# 630. 课程表 III

## 题目描述

<p>这里有 <code>n</code> 门不同的在线课程，按从 <code>1</code> 到 <code>n</code>&nbsp;编号。给你一个数组 <code>courses</code> ，其中 <code>courses[i] = [duration<sub>i</sub>, lastDay<sub>i</sub>]</code> 表示第 <code>i</code> 门课将会 <strong>持续</strong> 上 <code>duration<sub>i</sub></code> 天课，并且必须在不晚于 <code>lastDay<sub>i</sub></code> 的时候完成。</p>

<p>你的学期从第 <code>1</code> 天开始。且不能同时修读两门及两门以上的课程。</p>

<p>返回你最多可以修读的课程数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
<strong>输出：</strong>3
<strong>解释：</strong>
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>courses = [[1,2]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>courses = [[3,2],[4,3]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= courses.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= duration<sub>i</sub>, lastDay<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 提示

1. During iteration, say I want to add the current course, currentTotalTime being total time of all courses taken till now, but adding the current course might exceed my deadline or it doesn’t.</br></br>

1. If it doesn’t, then I have added one new course. Increment the currentTotalTime with duration of current course.
2. 2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.</br>
* No harm done and I might have just reduced the currentTotalTime, right? </br>
* What preprocessing do I need to do on my course processing order so that this swap is always legal?

## 示例

```
[[100,200],[200,1300],[1000,1250],[2000,3200]]
[[1,2]]
[[3,2],[4,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        
    }
};
```

### Java

```java
class Solution {
    public int scheduleCourse(int[][] courses) {
        
    }
}
```

### Python

```python
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
```

### C

```c
int scheduleCourse(int** courses, int coursesSize, int* coursesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ScheduleCourse(int[][] courses) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} courses
 * @return {number}
 */
var scheduleCourse = function(courses) {
    
};
```

### TypeScript

```typescript
function scheduleCourse(courses: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $courses
     * @return Integer
     */
    function scheduleCourse($courses) {
        
    }
}
```

### Swift

```swift
class Solution {
    func scheduleCourse(_ courses: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun scheduleCourse(courses: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int scheduleCourse(List<List<int>> courses) {
    
  }
}
```

### Go

```golang
func scheduleCourse(courses [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} courses
# @return {Integer}
def schedule_course(courses)
    
end
```

### Scala

```scala
object Solution {
    def scheduleCourse(courses: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn schedule_course(courses: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (schedule-course courses)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec schedule_course(Courses :: [[integer()]]) -> integer().
schedule_course(Courses) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec schedule_course(courses :: [[integer]]) :: integer
  def schedule_course(courses) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func scheduleCourse(courses: Array<Array<Int64>>): Int64 {

    }
}
```

