# 1947. 最大兼容性评分和

## 题目描述

<p>有一份由 <code>n</code> 个问题组成的调查问卷，每个问题的答案要么是 <code>0</code>（no，否），要么是 <code>1</code>（yes，是）。</p>

<p>这份调查问卷被分发给 <code>m</code> 名学生和 <code>m</code> 名导师，学生和导师的编号都是从 <code>0</code> 到 <code>m - 1</code> 。学生的答案用一个二维整数数组 <code>students</code> 表示，其中 <code>students[i]</code> 是一个整数数组，包含第 <code>i</code> 名学生对调查问卷给出的答案（<strong>下标从 0 开始</strong>）。导师的答案用一个二维整数数组 <code>mentors</code> 表示，其中 <code>mentors[j]</code> 是一个整数数组，包含第 <code>j</code> 名导师对调查问卷给出的答案（<strong>下标从 0 开始</strong>）。</p>

<p>每个学生都会被分配给 <strong>一名</strong> 导师，而每位导师也会分配到 <strong>一名</strong> 学生。配对的学生与导师之间的兼容性评分等于学生和导师答案相同的次数。</p>

<ul>
	<li>例如，学生答案为<code>[1, <strong><em>0</em></strong>, <strong><em>1</em></strong>]</code> 而导师答案为 <code>[0, <strong><em>0</em></strong>, <strong><em>1</em></strong>]</code> ，那么他们的兼容性评分为 2 ，因为只有第二个和第三个答案相同。</li>
</ul>

<p>请你找出最优的学生与导师的配对方案，以 <strong>最大程度上</strong> 提高 <strong>兼容性评分和</strong> 。</p>

<p>给你 <code>students</code> 和 <code>mentors</code> ，返回可以得到的<em> </em><strong>最大兼容性评分和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
<strong>输出：</strong>8
<strong>解释：</strong>按下述方式分配学生和导师：
- 学生 0 分配给导师 2 ，兼容性评分为 3 。
- 学生 1 分配给导师 0 ，兼容性评分为 2 。
- 学生 2 分配给导师 1 ，兼容性评分为 3 。
最大兼容性评分和为 3 + 2 + 3 = 8 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
<strong>输出：</strong>0
<strong>解释：</strong>任意学生与导师配对的兼容性评分都是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == students.length == mentors.length</code></li>
	<li><code>n == students[i].length == mentors[j].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 8</code></li>
	<li><code>students[i][k]</code> 为 <code>0</code> 或 <code>1</code></li>
	<li><code>mentors[j][k]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 动态规划
- 回溯
- 状态压缩

## 提示

1. Calculate the compatibility score for each student-mentor pair.
2. Try every permutation of students with the original mentors array.

## 示例

```
[[1,1,0],[1,0,1],[0,0,1]]
[[1,0,0],[0,0,1],[1,1,0]]
[[0,0],[0,0],[0,0]]
[[1,1],[1,1],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxCompatibilitySum(vector<vector<int>>& students, vector<vector<int>>& mentors) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxCompatibilitySum(int[][] students, int[][] mentors) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
```

### C

```c
int maxCompatibilitySum(int** students, int studentsSize, int* studentsColSize, int** mentors, int mentorsSize, int* mentorsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxCompatibilitySum(int[][] students, int[][] mentors) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} students
 * @param {number[][]} mentors
 * @return {number}
 */
var maxCompatibilitySum = function(students, mentors) {
    
};
```

### TypeScript

```typescript
function maxCompatibilitySum(students: number[][], mentors: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $students
     * @param Integer[][] $mentors
     * @return Integer
     */
    function maxCompatibilitySum($students, $mentors) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxCompatibilitySum(_ students: [[Int]], _ mentors: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxCompatibilitySum(students: Array<IntArray>, mentors: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxCompatibilitySum(List<List<int>> students, List<List<int>> mentors) {
    
  }
}
```

### Go

```golang
func maxCompatibilitySum(students [][]int, mentors [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} students
# @param {Integer[][]} mentors
# @return {Integer}
def max_compatibility_sum(students, mentors)
    
end
```

### Scala

```scala
object Solution {
    def maxCompatibilitySum(students: Array[Array[Int]], mentors: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_compatibility_sum(students: Vec<Vec<i32>>, mentors: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-compatibility-sum students mentors)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_compatibility_sum(Students :: [[integer()]], Mentors :: [[integer()]]) -> integer().
max_compatibility_sum(Students, Mentors) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_compatibility_sum(students :: [[integer]], mentors :: [[integer]]) :: integer
  def max_compatibility_sum(students, mentors) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxCompatibilitySum(students: Array<Array<Int64>>, mentors: Array<Array<Int64>>): Int64 {

    }
}
```

