# 2071. 你可以安排的最多任务数目

## 题目描述

<p>给你&nbsp;<code>n</code>&nbsp;个任务和&nbsp;<code>m</code>&nbsp;个工人。每个任务需要一定的力量值才能完成，需要的力量值保存在下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>tasks</code>&nbsp;中，第 <code>i</code>&nbsp;个任务需要&nbsp;<code>tasks[i]</code>&nbsp;的力量才能完成。每个工人的力量值保存在下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>workers</code>&nbsp;中，第&nbsp;<code>j</code>&nbsp;个工人的力量值为&nbsp;<code>workers[j]</code>&nbsp;。每个工人只能完成 <strong>一个</strong>&nbsp;任务，且力量值需要 <strong>大于等于</strong>&nbsp;该任务的力量要求值（即&nbsp;<code>workers[j] &gt;= tasks[i]</code>&nbsp;）。</p>

<p>除此以外，你还有&nbsp;<code>pills</code>&nbsp;个神奇药丸，可以给 <strong>一个工人的力量值</strong>&nbsp;增加&nbsp;<code>strength</code>&nbsp;。你可以决定给哪些工人使用药丸，但每个工人&nbsp;<strong>最多</strong>&nbsp;只能使用&nbsp;<strong>一片</strong>&nbsp;药丸。</p>

<p>给你下标从 <strong>0</strong>&nbsp;开始的整数数组<code>tasks</code> 和&nbsp;<code>workers</code>&nbsp;以及两个整数&nbsp;<code>pills</code> 和&nbsp;<code>strength</code>&nbsp;，请你返回 <strong>最多</strong>&nbsp;有多少个任务可以被完成。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>tasks = [<em><strong>3</strong></em>,<em><strong>2</strong></em>,<em><strong>1</strong></em>], workers = [<em><strong>0</strong></em>,<em><strong>3</strong></em>,<em><strong>3</strong></em>], pills = 1, strength = 1
<b>输出：</b>3
<strong>解释：</strong>
我们可以按照如下方案安排药丸：
- 给 0 号工人药丸。
- 0 号工人完成任务 2（0 + 1 &gt;= 1）
- 1 号工人完成任务 1（3 &gt;= 2）
- 2 号工人完成任务 0（3 &gt;= 3）
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>tasks = [<em><strong>5</strong></em>,4], workers = [<em><strong>0</strong></em>,0,0], pills = 1, strength = 5
<b>输出：</b>1
<strong>解释：</strong>
我们可以按照如下方案安排药丸：
- 给 0 号工人药丸。
- 0 号工人完成任务 0（0 + 5 &gt;= 5）
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>tasks = [<em><strong>10</strong></em>,<em><strong>15</strong></em>,30], workers = [<em><strong>0</strong></em>,<em><strong>10</strong></em>,10,10,10], pills = 3, strength = 10
<b>输出：</b>2
<strong>解释：</strong>
我们可以按照如下方案安排药丸：
- 给 0 号和 1 号工人药丸。
- 0 号工人完成任务 0（0 + 10 &gt;= 10）
- 1 号工人完成任务 1（10 + 10 &gt;= 15）
</pre>

<p><strong>示例 4：</strong></p>

<pre><b>输入：</b>tasks = [<em><strong>5</strong></em>,9,<em><strong>8</strong></em>,<em><strong>5</strong></em>,9], workers = [1,<em><strong>6</strong></em>,<em><strong>4</strong></em>,2,<em><strong>6</strong></em>], pills = 1, strength = 5
<b>输出：</b>3
<strong>解释：</strong>
我们可以按照如下方案安排药丸：
- 给 2 号工人药丸。
- 1 号工人完成任务 0（6 &gt;= 5）
- 2 号工人完成任务 2（4 + 5 &gt;= 8）
- 4 号工人完成任务 3（6 &gt;= 5）
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == tasks.length</code></li>
	<li><code>m == workers.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= pills &lt;= m</code></li>
	<li><code>0 &lt;= tasks[i], workers[j], strength &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 队列
- 数组
- 二分查找
- 排序
- 单调队列

## 提示

1. Is it possible to assign the first k smallest tasks to the workers?
2. How can you efficiently try every k?

## 示例

```
[3,2,1]
[0,3,3]
1
1
[5,4]
[0,0,0]
1
5
[10,15,30]
[0,10,10,10,10]
3
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
```

### C

```c
int maxTaskAssign(int* tasks, int tasksSize, int* workers, int workersSize, int pills, int strength) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} tasks
 * @param {number[]} workers
 * @param {number} pills
 * @param {number} strength
 * @return {number}
 */
var maxTaskAssign = function(tasks, workers, pills, strength) {
    
};
```

### TypeScript

```typescript
function maxTaskAssign(tasks: number[], workers: number[], pills: number, strength: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $tasks
     * @param Integer[] $workers
     * @param Integer $pills
     * @param Integer $strength
     * @return Integer
     */
    function maxTaskAssign($tasks, $workers, $pills, $strength) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxTaskAssign(_ tasks: [Int], _ workers: [Int], _ pills: Int, _ strength: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxTaskAssign(tasks: IntArray, workers: IntArray, pills: Int, strength: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxTaskAssign(List<int> tasks, List<int> workers, int pills, int strength) {
    
  }
}
```

### Go

```golang
func maxTaskAssign(tasks []int, workers []int, pills int, strength int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} tasks
# @param {Integer[]} workers
# @param {Integer} pills
# @param {Integer} strength
# @return {Integer}
def max_task_assign(tasks, workers, pills, strength)
    
end
```

### Scala

```scala
object Solution {
    def maxTaskAssign(tasks: Array[Int], workers: Array[Int], pills: Int, strength: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_task_assign(tasks: Vec<i32>, workers: Vec<i32>, pills: i32, strength: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-task-assign tasks workers pills strength)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_task_assign(Tasks :: [integer()], Workers :: [integer()], Pills :: integer(), Strength :: integer()) -> integer().
max_task_assign(Tasks, Workers, Pills, Strength) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_task_assign(tasks :: [integer], workers :: [integer], pills :: integer, strength :: integer) :: integer
  def max_task_assign(tasks, workers, pills, strength) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxTaskAssign(tasks: Array<Int64>, workers: Array<Int64>, pills: Int64, strength: Int64): Int64 {

    }
}
```

