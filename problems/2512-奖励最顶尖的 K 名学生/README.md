# 2512. 奖励最顶尖的 K 名学生

## 题目描述

<p>给你两个字符串数组&nbsp;<code>positive_feedback</code> 和&nbsp;<code>negative_feedback</code>&nbsp;，分别包含表示正面的和负面的词汇。<strong>不会</strong>&nbsp;有单词同时是正面的和负面的。</p>

<p>一开始，每位学生分数为&nbsp;<code>0</code>&nbsp;。每个正面的单词会给学生的分数 <strong>加&nbsp;</strong><code>3</code>&nbsp;分，每个负面的词会给学生的分数 <strong>减&nbsp;</strong>&nbsp;<code>1</code>&nbsp;分。</p>

<p>给你&nbsp;<code>n</code>&nbsp;个学生的评语，用一个下标从 <strong>0</strong>&nbsp;开始的字符串数组&nbsp;<code>report</code>&nbsp;和一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>student_id</code>&nbsp;表示，其中&nbsp;<code>student_id[i]</code>&nbsp;表示这名学生的 ID ，这名学生的评语是&nbsp;<code>report[i]</code>&nbsp;。每名学生的 ID <strong>互不相同</strong>。</p>

<p>给你一个整数&nbsp;<code>k</code>&nbsp;，请你返回按照得分&nbsp;<strong>从高到低</strong>&nbsp;最顶尖的<em>&nbsp;</em><code>k</code>&nbsp;名学生。如果有多名学生分数相同，ID 越小排名越前。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
<b>输出：</b>[1,2]
<b>解释：</b>
两名学生都有 1 个正面词汇，都得到 3 分，学生 1 的 ID 更小所以排名更前。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
<b>输出：</b>[2,1]
<b>解释：</b>
- ID 为 1 的学生有 1 个正面词汇和 1 个负面词汇，所以得分为 3-1=2 分。
- ID 为 2 的学生有 1 个正面词汇，得分为 3 分。
学生 2 分数更高，所以返回 [2,1] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= positive_feedback.length, negative_feedback.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= positive_feedback[i].length, negative_feedback[j].length &lt;= 100</code></li>
	<li><code>positive_feedback[i]</code> 和&nbsp;<code>negative_feedback[j]</code>&nbsp;都只包含小写英文字母。</li>
	<li><code>positive_feedback</code> 和&nbsp;<code>negative_feedback</code>&nbsp;中不会有相同单词。</li>
	<li><code>n == report.length == student_id.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>report[i]</code>&nbsp;只包含小写英文字母和空格&nbsp;<code>' '</code>&nbsp;。</li>
	<li><code>report[i]</code>&nbsp;中连续单词之间有单个空格隔开。</li>
	<li><code>1 &lt;= report[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= student_id[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>student_id[i]</code>&nbsp;的值 <strong>互不相同</strong>&nbsp;。</li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 排序
- 堆（优先队列）

## 提示

1. Hash the positive and negative feedback words separately.
2. Calculate the points for each student’s feedback.
3. Sort the students accordingly to find the top <em>k</em> among them.

## 示例

```
["smart","brilliant","studious"]
["not"]
["this student is studious","the student is smart"]
[1,2]
2
["smart","brilliant","studious"]
["not"]
["this student is not studious","the student is smart"]
[1,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> topStudents(vector<string>& positive_feedback, vector<string>& negative_feedback, vector<string>& report, vector<int>& student_id, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> topStudents(String[] positive_feedback, String[] negative_feedback, String[] report, int[] student_id, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* topStudents(char** positive_feedback, int positive_feedbackSize, char** negative_feedback, int negative_feedbackSize, char** report, int reportSize, int* student_id, int student_idSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> TopStudents(string[] positive_feedback, string[] negative_feedback, string[] report, int[] student_id, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} positive_feedback
 * @param {string[]} negative_feedback
 * @param {string[]} report
 * @param {number[]} student_id
 * @param {number} k
 * @return {number[]}
 */
var topStudents = function(positive_feedback, negative_feedback, report, student_id, k) {
    
};
```

### TypeScript

```typescript
function topStudents(positive_feedback: string[], negative_feedback: string[], report: string[], student_id: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $positive_feedback
     * @param String[] $negative_feedback
     * @param String[] $report
     * @param Integer[] $student_id
     * @param Integer $k
     * @return Integer[]
     */
    function topStudents($positive_feedback, $negative_feedback, $report, $student_id, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func topStudents(_ positive_feedback: [String], _ negative_feedback: [String], _ report: [String], _ student_id: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun topStudents(positive_feedback: Array<String>, negative_feedback: Array<String>, report: Array<String>, student_id: IntArray, k: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> topStudents(List<String> positive_feedback, List<String> negative_feedback, List<String> report, List<int> student_id, int k) {
    
  }
}
```

### Go

```golang
func topStudents(positive_feedback []string, negative_feedback []string, report []string, student_id []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} positive_feedback
# @param {String[]} negative_feedback
# @param {String[]} report
# @param {Integer[]} student_id
# @param {Integer} k
# @return {Integer[]}
def top_students(positive_feedback, negative_feedback, report, student_id, k)
    
end
```

### Scala

```scala
object Solution {
    def topStudents(positive_feedback: Array[String], negative_feedback: Array[String], report: Array[String], student_id: Array[Int], k: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn top_students(positive_feedback: Vec<String>, negative_feedback: Vec<String>, report: Vec<String>, student_id: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (top-students positive_feedback negative_feedback report student_id k)
  (-> (listof string?) (listof string?) (listof string?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec top_students(Positive_feedback :: [unicode:unicode_binary()], Negative_feedback :: [unicode:unicode_binary()], Report :: [unicode:unicode_binary()], Student_id :: [integer()], K :: integer()) -> [integer()].
top_students(Positive_feedback, Negative_feedback, Report, Student_id, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec top_students(positive_feedback :: [String.t], negative_feedback :: [String.t], report :: [String.t], student_id :: [integer], k :: integer) :: [integer]
  def top_students(positive_feedback, negative_feedback, report, student_id, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func topStudents(positive_feedback: Array<String>, negative_feedback: Array<String>, report: Array<String>, student_id: Array<Int64>, k: Int64): ArrayList<Int64> {

    }
}
```

