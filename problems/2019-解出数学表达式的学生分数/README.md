# 2019. 解出数学表达式的学生分数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，它 <strong>只</strong> 包含数字&nbsp;<code>0-9</code>&nbsp;，加法运算符&nbsp;<code>'+'</code>&nbsp;和乘法运算符&nbsp;<code>'*'</code>&nbsp;，这个字符串表示一个&nbsp;<strong>合法</strong>&nbsp;的只含有&nbsp;<strong>个位数</strong><strong>数字</strong>&nbsp;的数学表达式（比方说&nbsp;<code>3+5*2</code>）。有 <code>n</code>&nbsp;位小学生将计算这个数学表达式，并遵循如下 <strong>运算顺序</strong>&nbsp;：</p>

<ol>
	<li>按照 <strong>从左到右</strong>&nbsp;的顺序计算 <strong>乘法</strong>&nbsp;，然后</li>
	<li>按照 <strong>从左到右</strong>&nbsp;的顺序计算 <strong>加法</strong>&nbsp;。</li>
</ol>

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>answers</code>&nbsp;，表示每位学生提交的答案。你的任务是给 <code>answer</code>&nbsp;数组按照如下 <strong>规则</strong>&nbsp;打分：</p>

<ul>
	<li>如果一位学生的答案 <strong>等于</strong>&nbsp;表达式的正确结果，这位学生将得到 <code>5</code>&nbsp;分。</li>
	<li>否则，如果答案由&nbsp;<strong>一处或多处错误的运算顺序</strong>&nbsp;计算得到，那么这位学生能得到 <code>2</code>&nbsp;分。</li>
	<li>否则，这位学生将得到 <code>0</code>&nbsp;分。</li>
</ul>

<p>请你返回所有学生的分数和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/17/student_solving_math.png" style="width: 678px; height: 109px;"></p>

<pre><b>输入：</b>s = "7+3*1*2", answers = [20,13,42]
<b>输出：</b>7
<b>解释：</b>如上图所示，正确答案为 13 ，因此有一位学生得分为 5 分：[20,<em><strong>13</strong></em>,42] 。
一位学生可能通过错误的运算顺序得到结果 20 ：7+3=10，10*1=10，10*2=20 。所以这位学生得分为 2 分：[<em><strong>20</strong></em>,13,42] 。
所有学生得分分别为：[2,5,0] 。所有得分之和为 2+5+0=7 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "3+5*2", answers = [13,0,10,13,13,16,16]
<b>输出：</b>19
<b>解释：</b>表达式的正确结果为 13 ，所以有 3 位学生得到 5 分：[<em><strong>13</strong></em>,0,10,<em><strong>13</strong></em>,<em><strong>13</strong></em>,16,16] 。
学生可能通过错误的运算顺序得到结果 16 ：3+5=8，8*2=16 。所以两位学生得到 2 分：[13,0,10,13,13,<em><strong>16</strong></em>,<em><strong>16</strong></em>] 。
所有学生得分分别为：[5,0,0,5,5,2,2] 。所有得分之和为 5+0+0+5+5+2+2=19 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "6+0*1", answers = [12,9,6,4,8,6]
<b>输出：</b>10
<b>解释：</b>表达式的正确结果为 6 。
如果一位学生通过错误的运算顺序计算该表达式，结果仍为 6 。
根据打分规则，运算顺序错误的学生也将得到 5 分（因为他们仍然得到了正确的结果），而不是 2 分。
所有学生得分分别为：[0,0,5,0,0,5] 。所有得分之和为 10 分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 31</code></li>
	<li><code>s</code>&nbsp;表示一个只包含&nbsp;<code>0-9</code>&nbsp;，<code>'+'</code>&nbsp;和&nbsp;<code>'*'</code>&nbsp;的合法表达式。</li>
	<li>表达式中所有整数运算数字都在闭区间&nbsp;<code>[0, 9]</code>&nbsp;以内。</li>
	<li><code>1 &lt;=</code>&nbsp;数学表达式中所有运算符数目（<code>'+'</code> 和&nbsp;<code>'*'</code>）&nbsp;<code>&lt;= 15</code></li>
	<li>测试数据保证正确表达式结果在范围&nbsp;<code>[0, 1000]</code>&nbsp;以内。</li>
	<li><code>n == answers.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= answers[i] &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 记忆化搜索
- 数组
- 数学
- 字符串
- 动态规划

## 提示

1. The number of operators in the equation is less. Could you find the right answer then generate all possible answers using different orders of operations?
2. Divide the equation into blocks separated by the operators, and use memoization on the results of blocks for optimization.
3. Use set and the max limit of the answer for further optimization.

## 示例

```
"7+3*1*2"
[20,13,42]
"3+5*2"
[13,0,10,13,13,16,16]
"6+0*1"
[12,9,6,4,8,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int scoreOfStudents(string s, vector<int>& answers) {
        
    }
};
```

### Java

```java
class Solution {
    public int scoreOfStudents(String s, int[] answers) {
        
    }
}
```

### Python

```python
class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        
```

### C

```c
int scoreOfStudents(char* s, int* answers, int answersSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ScoreOfStudents(string s, int[] answers) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[]} answers
 * @return {number}
 */
var scoreOfStudents = function(s, answers) {
    
};
```

### TypeScript

```typescript
function scoreOfStudents(s: string, answers: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $answers
     * @return Integer
     */
    function scoreOfStudents($s, $answers) {
        
    }
}
```

### Swift

```swift
class Solution {
    func scoreOfStudents(_ s: String, _ answers: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun scoreOfStudents(s: String, answers: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int scoreOfStudents(String s, List<int> answers) {
    
  }
}
```

### Go

```golang
func scoreOfStudents(s string, answers []int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[]} answers
# @return {Integer}
def score_of_students(s, answers)
    
end
```

### Scala

```scala
object Solution {
    def scoreOfStudents(s: String, answers: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn score_of_students(s: String, answers: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (score-of-students s answers)
  (-> string? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec score_of_students(S :: unicode:unicode_binary(), Answers :: [integer()]) -> integer().
score_of_students(S, Answers) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec score_of_students(s :: String.t, answers :: [integer]) :: integer
  def score_of_students(s, answers) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func scoreOfStudents(s: String, answers: Array<Int64>): Int64 {

    }
}
```

