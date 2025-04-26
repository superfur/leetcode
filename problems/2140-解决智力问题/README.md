# 2140. 解决智力问题

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>questions</code>&nbsp;，其中&nbsp;<code>questions[i] = [points<sub>i</sub>, brainpower<sub>i</sub>]</code>&nbsp;。</p>

<p>这个数组表示一场考试里的一系列题目，你需要 <strong>按顺序</strong>&nbsp;（也就是从问题 <code>0</code><strong>&nbsp;</strong>开始依次解决），针对每个问题选择 <strong>解决</strong>&nbsp;或者 <strong>跳过</strong>&nbsp;操作。解决问题 <code>i</code>&nbsp;将让你 <b>获得</b>&nbsp;&nbsp;<code>points<sub>i</sub></code>&nbsp;的分数，但是你将 <strong>无法</strong>&nbsp;解决接下来的&nbsp;<code>brainpower<sub>i</sub></code>&nbsp;个问题（即只能跳过接下来的 <code>brainpower<sub>i</sub></code><sub>&nbsp;</sub>个问题）。如果你跳过问题&nbsp;<code>i</code>&nbsp;，你可以对下一个问题决定使用哪种操作。</p>

<ul>
	<li>比方说，给你&nbsp;<code>questions = [[3, 2], [4, 3], [4, 4], [2, 5]]</code>&nbsp;：

	<ul>
		<li>如果问题&nbsp;<code>0</code>&nbsp;被解决了， 那么你可以获得&nbsp;<code>3</code>&nbsp;分，但你不能解决问题&nbsp;<code>1</code> 和&nbsp;<code>2</code>&nbsp;。</li>
		<li>如果你跳过问题&nbsp;<code>0</code>&nbsp;，且解决问题&nbsp;<code>1</code>&nbsp;，你将获得 <code>4</code> 分但是不能解决问题&nbsp;<code>2</code> 和&nbsp;<code>3</code>&nbsp;。</li>
	</ul>
	</li>
</ul>

<p>请你返回这场考试里你能获得的 <strong>最高</strong>&nbsp;分数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>questions = [[3,2],[4,3],[4,4],[2,5]]
<b>输出：</b>5
<b>解释：</b>解决问题 0 和 3 得到最高分。
- 解决问题 0 ：获得 3 分，但接下来 2 个问题都不能解决。
- 不能解决问题 1 和 2
- 解决问题 3 ：获得 2 分
总得分为：3 + 2 = 5 。没有别的办法获得 5 分或者多于 5 分。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
<b>输出：</b>7
<b>解释：</b>解决问题 1 和 4 得到最高分。
- 跳过问题 0
- 解决问题 1 ：获得 2 分，但接下来 2 个问题都不能解决。
- 不能解决问题 2 和 3
- 解决问题 4 ：获得 5 分
总得分为：2 + 5 = 7 。没有别的办法获得 7 分或者多于 7 分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= questions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>questions[i].length == 2</code></li>
	<li><code>1 &lt;= points<sub>i</sub>, brainpower<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. For each question, we can either solve it or skip it. How can we use Dynamic Programming to decide the most optimal option for each problem?
2. We store for each question the maximum points we can earn if we started the exam on that question.
3. If we skip a question, then the answer for it will be the same as the answer for the next question.
4. If we solve a question, then the answer for it will be the points of the current question plus the answer for the next solvable question.
5. The maximum of these two values will be the answer to the current question.

## 示例

```
[[3,2],[4,3],[4,4],[2,5]]
[[1,1],[2,2],[3,3],[4,4],[5,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        
    }
};
```

### Java

```java
class Solution {
    public long mostPoints(int[][] questions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
```

### C

```c
long long mostPoints(int** questions, int questionsSize, int* questionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MostPoints(int[][] questions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function(questions) {
    
};
```

### TypeScript

```typescript
function mostPoints(questions: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $questions
     * @return Integer
     */
    function mostPoints($questions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostPoints(_ questions: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostPoints(questions: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int mostPoints(List<List<int>> questions) {
    
  }
}
```

### Go

```golang
func mostPoints(questions [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} questions
# @return {Integer}
def most_points(questions)
    
end
```

### Scala

```scala
object Solution {
    def mostPoints(questions: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (most-points questions)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec most_points(Questions :: [[integer()]]) -> integer().
most_points(Questions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_points(questions :: [[integer]]) :: integer
  def most_points(questions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostPoints(questions: Array<Array<Int64>>): Int64 {

    }
}
```

