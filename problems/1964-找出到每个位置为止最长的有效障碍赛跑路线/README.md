# 1964. 找出到每个位置为止最长的有效障碍赛跑路线

## 题目描述

<p>你打算构建一些障碍赛跑路线。给你一个 <strong>下标从 0 开始</strong> 的整数数组 <code>obstacles</code> ，数组长度为 <code>n</code> ，其中 <code>obstacles[i]</code> 表示第 <code>i</code> 个障碍的高度。</p>

<p>对于每个介于 <code>0</code> 和 <code>n - 1</code> 之间（包含 <code>0</code> 和 <code>n - 1</code>）的下标&nbsp; <code>i</code> ，在满足下述条件的前提下，请你找出&nbsp;<code>obstacles</code> 能构成的最长障碍路线的长度：</p>

<ul>
	<li>你可以选择下标介于 <code>0</code> 到 <code>i</code> 之间（包含 <code>0</code> 和 <code>i</code>）的任意个障碍。</li>
	<li>在这条路线中，必须包含第 <code>i</code> 个障碍。</li>
	<li>你必须按障碍在&nbsp;<code>obstacles</code>&nbsp;中的<strong> </strong><strong>出现顺序</strong> 布置这些障碍。</li>
	<li>除第一个障碍外，路线中每个障碍的高度都必须和前一个障碍 <strong>相同</strong> 或者 <strong>更高</strong> 。</li>
</ul>

<p>返回长度为 <code>n</code> 的答案数组 <code>ans</code> ，其中 <code>ans[i]</code> 是上面所述的下标 <code>i</code> 对应的最长障碍赛跑路线的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>obstacles = [1,2,3,2]
<strong>输出：</strong>[1,2,3,3]
<strong>解释：</strong>每个位置的最长有效障碍路线是：
- i = 0: [<em><strong>1</strong></em>], [1] 长度为 1
- i = 1: [<em><strong>1</strong></em>,<em><strong>2</strong></em>], [1,2] 长度为 2
- i = 2: [<em><strong>1</strong></em>,<em><strong>2</strong></em>,<em><strong>3</strong></em>], [1,2,3] 长度为 3
- i = 3: [<em><strong>1</strong></em>,<em><strong>2</strong></em>,3,<em><strong>2</strong></em>], [1,2,2] 长度为 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>obstacles = [2,2,1]
<strong>输出：</strong>[1,2,1]
<strong>解释：</strong>每个位置的最长有效障碍路线是：
- i = 0: [<em><strong>2</strong></em>], [2] 长度为 1
- i = 1: [<em><strong>2</strong></em>,<em><strong>2</strong></em>], [2,2] 长度为 2
- i = 2: [2,2,<em><strong>1</strong></em>], [1] 长度为 1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>obstacles = [3,1,5,6,4,2]
<strong>输出：</strong>[1,1,2,3,2,2]
<strong>解释：</strong>每个位置的最长有效障碍路线是：
- i = 0: [<em><strong>3</strong></em>], [3] 长度为 1
- i = 1: [3,<em><strong>1</strong></em>], [1] 长度为 1
- i = 2: [<em><strong>3</strong></em>,1,<em><strong>5</strong></em>], [3,5] 长度为 2, [1,5] 也是有效的障碍赛跑路线
- i = 3: [<em><strong>3</strong></em>,1,<em><strong>5</strong></em>,<em><strong>6</strong></em>], [3,5,6] 长度为 3, [1,5,6] 也是有效的障碍赛跑路线
- i = 4: [<em><strong>3</strong></em>,1,5,6,<em><strong>4</strong></em>], [3,4] 长度为 2, [1,4] 也是有效的障碍赛跑路线
- i = 5: [3,<em><strong>1</strong></em>,5,6,4,<em><strong>2</strong></em>], [1,2] 长度为 2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == obstacles.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= obstacles[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 数组
- 二分查找

## 提示

1. Can you keep track of the minimum height for each obstacle course length?
2. You can use binary search to find the longest previous obstacle course length that satisfies the conditions.

## 示例

```
[1,2,3,2]
[2,2,1]
[3,1,5,6,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestObstacleCourseAtEachPosition(int* obstacles, int obstaclesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] LongestObstacleCourseAtEachPosition(int[] obstacles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} obstacles
 * @return {number[]}
 */
var longestObstacleCourseAtEachPosition = function(obstacles) {
    
};
```

### TypeScript

```typescript
function longestObstacleCourseAtEachPosition(obstacles: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $obstacles
     * @return Integer[]
     */
    function longestObstacleCourseAtEachPosition($obstacles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestObstacleCourseAtEachPosition(_ obstacles: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestObstacleCourseAtEachPosition(obstacles: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> longestObstacleCourseAtEachPosition(List<int> obstacles) {
    
  }
}
```

### Go

```golang
func longestObstacleCourseAtEachPosition(obstacles []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} obstacles
# @return {Integer[]}
def longest_obstacle_course_at_each_position(obstacles)
    
end
```

### Scala

```scala
object Solution {
    def longestObstacleCourseAtEachPosition(obstacles: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_obstacle_course_at_each_position(obstacles: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (longest-obstacle-course-at-each-position obstacles)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec longest_obstacle_course_at_each_position(Obstacles :: [integer()]) -> [integer()].
longest_obstacle_course_at_each_position(Obstacles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_obstacle_course_at_each_position(obstacles :: [integer]) :: [integer]
  def longest_obstacle_course_at_each_position(obstacles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestObstacleCourseAtEachPosition(obstacles: Array<Int64>): Array<Int64> {

    }
}
```

