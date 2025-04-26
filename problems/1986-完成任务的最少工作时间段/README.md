# 1986. 完成任务的最少工作时间段

## 题目描述

<p>你被安排了 <code>n</code>&nbsp;个任务。任务需要花费的时间用长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>tasks</code>&nbsp;表示，第 <code>i</code>&nbsp;个任务需要花费&nbsp;<code>tasks[i]</code>&nbsp;小时完成。一个 <strong>工作时间段</strong>&nbsp;中，你可以 <strong>至多</strong>&nbsp;连续工作&nbsp;<code>sessionTime</code>&nbsp;个小时，然后休息一会儿。</p>

<p>你需要按照如下条件完成给定任务：</p>

<ul>
	<li>如果你在某一个时间段开始一个任务，你需要在 <strong>同一个</strong>&nbsp;时间段完成它。</li>
	<li>完成一个任务后，你可以 <strong>立马</strong>&nbsp;开始一个新的任务。</li>
	<li>你可以按 <strong>任意顺序</strong>&nbsp;完成任务。</li>
</ul>

<p>给你&nbsp;<code>tasks</code> 和&nbsp;<code>sessionTime</code>&nbsp;，请你按照上述要求，返回完成所有任务所需要的&nbsp;<strong>最少</strong>&nbsp;数目的&nbsp;<strong>工作时间段</strong>&nbsp;。</p>

<p>测试数据保证&nbsp;<code>sessionTime</code> <strong>大于等于</strong>&nbsp;<code>tasks[i]</code>&nbsp;中的&nbsp;<strong>最大值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>tasks = [1,2,3], sessionTime = 3
<b>输出：</b>2
<b>解释：</b>你可以在两个工作时间段内完成所有任务。
- 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。
- 第二个工作时间段：完成第三个任务，花费 3 小时。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>tasks = [3,1,3,1,1], sessionTime = 8
<b>输出：</b>2
<b>解释：</b>你可以在两个工作时间段内完成所有任务。
- 第一个工作时间段：完成除了最后一个任务以外的所有任务，花费 3 + 1 + 3 + 1 = 8 小时。
- 第二个工作时间段，完成最后一个任务，花费 1 小时。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>tasks = [1,2,3,4,5], sessionTime = 15
<b>输出：</b>1
<b>解释：</b>你可以在一个工作时间段以内完成所有任务。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == tasks.length</code></li>
	<li><code>1 &lt;= n &lt;= 14</code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10</code></li>
	<li><code>max(tasks[i]) &lt;= sessionTime &lt;= 15</code></li>
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

1. Try all possible ways of assignment.
2. If we can store the assignments in form of a state then we can reuse that state and solve the problem in a faster way.

## 示例

```
[1,2,3]
3
[3,1,3,1,1]
8
[1,2,3,4,5]
15
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSessions(vector<int>& tasks, int sessionTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSessions(int[] tasks, int sessionTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
```

### C

```c
int minSessions(int* tasks, int tasksSize, int sessionTime) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSessions(int[] tasks, int sessionTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} tasks
 * @param {number} sessionTime
 * @return {number}
 */
var minSessions = function(tasks, sessionTime) {
    
};
```

### TypeScript

```typescript
function minSessions(tasks: number[], sessionTime: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $tasks
     * @param Integer $sessionTime
     * @return Integer
     */
    function minSessions($tasks, $sessionTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSessions(_ tasks: [Int], _ sessionTime: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSessions(tasks: IntArray, sessionTime: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSessions(List<int> tasks, int sessionTime) {
    
  }
}
```

### Go

```golang
func minSessions(tasks []int, sessionTime int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} tasks
# @param {Integer} session_time
# @return {Integer}
def min_sessions(tasks, session_time)
    
end
```

### Scala

```scala
object Solution {
    def minSessions(tasks: Array[Int], sessionTime: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_sessions(tasks: Vec<i32>, session_time: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-sessions tasks sessionTime)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_sessions(Tasks :: [integer()], SessionTime :: integer()) -> integer().
min_sessions(Tasks, SessionTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_sessions(tasks :: [integer], session_time :: integer) :: integer
  def min_sessions(tasks, session_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSessions(tasks: Array<Int64>, sessionTime: Int64): Int64 {

    }
}
```

