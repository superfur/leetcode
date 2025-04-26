# 1834. 单线程 CPU

## 题目描述

<p>给你一个二维数组 <code>tasks</code> ，用于表示 <code>n</code>​​​​​​ 项从 <code>0</code> 到 <code>n - 1</code> 编号的任务。其中 <code>tasks[i] = [enqueueTime<sub>i</sub>, processingTime<sub>i</sub>]</code> 意味着第 <code>i<sup>​​​​​​</sup></code>​​​​ 项任务将会于 <code>enqueueTime<sub>i</sub></code> 时进入任务队列，需要 <code>processingTime<sub>i</sub></code><sub> </sub>的时长完成执行。</p>

<p>现有一个单线程 CPU ，同一时间只能执行 <strong>最多一项</strong> 任务，该 CPU 将会按照下述方式运行：</p>

<ul>
	<li>如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。</li>
	<li>如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 <strong>执行时间最短</strong> 的任务开始执行。如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。</li>
	<li>一旦某项任务开始执行，CPU 在 <strong>执行完整个任务</strong> 前都不会停止。</li>
	<li>CPU 可以在完成一项任务后，立即开始执行一项新任务。</li>
</ul>

<p>返回<em> </em>CPU<em> </em>处理任务的顺序。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>tasks = [[1,2],[2,4],[3,2],[4,1]]
<strong>输出：</strong>[0,2,3,1]
<strong>解释：</strong>事件按下述流程运行： 
- time = 1 ，任务 0 进入任务队列，可执行任务项 = {0}
- 同样在 time = 1 ，空闲状态的 CPU 开始执行任务 0 ，可执行任务项 = {}
- time = 2 ，任务 1 进入任务队列，可执行任务项 = {1}
- time = 3 ，任务 2 进入任务队列，可执行任务项 = {1, 2}
- 同样在 time = 3 ，CPU 完成任务 0 并开始执行队列中用时最短的任务 2 ，可执行任务项 = {1}
- time = 4 ，任务 3 进入任务队列，可执行任务项 = {1, 3}
- time = 5 ，CPU 完成任务 2 并开始执行队列中用时最短的任务 3 ，可执行任务项 = {1}
- time = 6 ，CPU 完成任务 3 并开始执行任务 1 ，可执行任务项 = {}
- time = 10 ，CPU 完成任务 1 并进入空闲状态
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
<strong>输出：</strong>[4,3,2,0,1]
<strong>解释：</strong>事件按下述流程运行： 
- time = 7 ，所有任务同时进入任务队列，可执行任务项  = {0,1,2,3,4}
- 同样在 time = 7 ，空闲状态的 CPU 开始执行任务 4 ，可执行任务项 = {0,1,2,3}
- time = 9 ，CPU 完成任务 4 并开始执行任务 3 ，可执行任务项 = {0,1,2}
- time = 13 ，CPU 完成任务 3 并开始执行任务 2 ，可执行任务项 = {0,1}
- time = 18 ，CPU 完成任务 2 并开始执行任务 0 ，可执行任务项 = {1}
- time = 28 ，CPU 完成任务 0 并开始执行任务 1 ，可执行任务项 = {}
- time = 40 ，CPU 完成任务 1 并进入空闲状态</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>tasks.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= enqueueTime<sub>i</sub>, processingTime<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序
- 堆（优先队列）

## 提示

1. To simulate the problem we first need to note that if at any point in time there are no enqueued tasks we need to wait to the smallest enqueue time of a non-processed element
2. We need a data structure like a min-heap to support choosing the task with the smallest processing time from all the enqueued tasks

## 示例

```
[[1,2],[2,4],[3,2],[4,1]]
[[7,10],[7,12],[7,5],[7,4],[7,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getOrder(int[][] tasks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getOrder(int** tasks, int tasksSize, int* tasksColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetOrder(int[][] tasks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number[]}
 */
var getOrder = function(tasks) {
    
};
```

### TypeScript

```typescript
function getOrder(tasks: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer[]
     */
    function getOrder($tasks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getOrder(_ tasks: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getOrder(tasks: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getOrder(List<List<int>> tasks) {
    
  }
}
```

### Go

```golang
func getOrder(tasks [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} tasks
# @return {Integer[]}
def get_order(tasks)
    
end
```

### Scala

```scala
object Solution {
    def getOrder(tasks: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_order(tasks: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-order tasks)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_order(Tasks :: [[integer()]]) -> [integer()].
get_order(Tasks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_order(tasks :: [[integer]]) :: [integer]
  def get_order(tasks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getOrder(tasks: Array<Array<Int64>>): Array<Int64> {

    }
}
```

