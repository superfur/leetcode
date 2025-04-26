# 2365. 任务调度器 II

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的正整数数组&nbsp;<code>tasks</code>&nbsp;，表示需要 <strong>按顺序</strong>&nbsp;完成的任务，其中&nbsp;<code>tasks[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;件任务的 <strong>类型</strong>&nbsp;。</p>

<p>同时给你一个正整数&nbsp;<code>space</code>&nbsp;，表示一个任务完成&nbsp;<strong>后</strong>&nbsp;，另一个&nbsp;<strong>相同</strong>&nbsp;类型任务完成前需要间隔的&nbsp;<strong>最少</strong>&nbsp;天数。</p>

<p>在所有任务完成前的每一天，你都必须进行以下两种操作中的一种：</p>

<ul>
	<li>完成&nbsp;<code>tasks</code>&nbsp;中的下一个任务</li>
	<li>休息一天</li>
</ul>

<p>请你返回完成所有任务所需的 <strong>最少</strong>&nbsp;天数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>tasks = [1,2,1,2,3,1], space = 3
<b>输出：</b>9
<strong>解释：</strong>
9 天完成所有任务的一种方法是：
第 1 天：完成任务 0 。
第 2 天：完成任务 1 。
第 3 天：休息。
第 4 天：休息。
第 5 天：完成任务 2 。
第 6 天：完成任务 3 。
第 7 天：休息。
第 8 天：完成任务 4 。
第 9 天：完成任务 5 。
可以证明无法少于 9 天完成所有任务。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>tasks = [5,8,8,5], space = 2
<b>输出：</b>6
<strong>解释：</strong>
6 天完成所有任务的一种方法是：
第 1 天：完成任务 0 。
第 2 天：完成任务 1 。
第 3 天：休息。
第 4 天：休息。
第 5 天：完成任务 2 。
第 6 天：完成任务 3 。
可以证明无法少于 6 天完成所有任务。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= space &lt;= tasks.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 模拟

## 提示

1. Try taking breaks as late as possible, such that tasks are still spaced appropriately.
2. Whenever considering whether to complete the next task, if it is not the first task of its type, check how many days ago the previous task was completed and add an appropriate number of breaks.

## 示例

```
[1,2,1,2,3,1]
3
[5,8,8,5]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long taskSchedulerII(vector<int>& tasks, int space) {
        
    }
};
```

### Java

```java
class Solution {
    public long taskSchedulerII(int[] tasks, int space) {
        
    }
}
```

### Python

```python
class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
```

### C

```c
long long taskSchedulerII(int* tasks, int tasksSize, int space) {
    
}
```

### C#

```csharp
public class Solution {
    public long TaskSchedulerII(int[] tasks, int space) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} tasks
 * @param {number} space
 * @return {number}
 */
var taskSchedulerII = function(tasks, space) {
    
};
```

### TypeScript

```typescript
function taskSchedulerII(tasks: number[], space: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $tasks
     * @param Integer $space
     * @return Integer
     */
    function taskSchedulerII($tasks, $space) {
        
    }
}
```

### Swift

```swift
class Solution {
    func taskSchedulerII(_ tasks: [Int], _ space: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun taskSchedulerII(tasks: IntArray, space: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int taskSchedulerII(List<int> tasks, int space) {
    
  }
}
```

### Go

```golang
func taskSchedulerII(tasks []int, space int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} tasks
# @param {Integer} space
# @return {Integer}
def task_scheduler_ii(tasks, space)
    
end
```

### Scala

```scala
object Solution {
    def taskSchedulerII(tasks: Array[Int], space: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn task_scheduler_ii(tasks: Vec<i32>, space: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (task-scheduler-ii tasks space)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec task_scheduler_ii(Tasks :: [integer()], Space :: integer()) -> integer().
task_scheduler_ii(Tasks, Space) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec task_scheduler_ii(tasks :: [integer], space :: integer) :: integer
  def task_scheduler_ii(tasks, space) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func taskSchedulerII(tasks: Array<Int64>, space: Int64): Int64 {

    }
}
```

