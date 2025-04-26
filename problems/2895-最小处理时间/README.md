# 2895. 最小处理时间

## 题目描述

<p>你有 <code>n</code> 颗处理器，每颗处理器都有 <code>4</code> 个核心。现有 <code>n * 4</code> 个待执行任务，每个核心只执行 <strong>一次</strong>&nbsp;任务。</p>

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>processorTime</code> ，表示每颗处理器最早空闲时间。另给你一个下标从 <strong>0</strong> 开始的整数数组 <code>tasks</code> ，表示执行每个任务所需的时间。返回所有任务都执行完毕需要的 <strong>最小时间</strong> 。</p>

<p>注意：每个核心独立执行任务。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]
<strong>输出：</strong>16
<strong>解释：</strong>
最优的方案是将下标为 4, 5, 6, 7 的任务分配给第一颗处理器（最早空闲时间 time = 8），下标为 0, 1, 2, 3 的任务分配给第二颗处理器（最早空闲时间 time = 10）。 
第一颗处理器执行完所有任务需要花费的时间 = max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16 。
第二颗处理器执行完所有任务需要花费的时间 = max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13 。
因此，可以证明执行完所有任务需要花费的最小时间是 16 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]
<strong>输出：</strong>23
<strong>解释：</strong>
最优的方案是将下标为 1, 4, 5, 6 的任务分配给第一颗处理器（最早空闲时间 time = 10），下标为 0, 2, 3, 7 的任务分配给第二颗处理器（最早空闲时间 time = 20）。 
第一颗处理器执行完所有任务需要花费的时间 = max(10 + 3, 10 + 5, 10 + 8, 10 + 4) = 18 。 
第二颗处理器执行完所有任务需要花费的时间 = max(20 + 2, 20 + 1, 20 + 2, 20 + 3) = 23 。 
因此，可以证明执行完所有任务需要花费的最小时间是 23 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == processorTime.length &lt;= 25000</code></li>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= processorTime[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>tasks.length == 4 * n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. It’s optimal to make the processor with earlier process time run 4 longer tasks.****
2. The largest <code>processTime[i] + tasks[j]</code> (when matched) is the answer.

## 示例

```
[8,10]
[2,2,3,1,8,7,4,5]
[10,20]
[2,3,1,2,5,8,4,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
        
    }
};
```

### Java

```java
class Solution {
    public int minProcessingTime(List<Integer> processorTime, List<Integer> tasks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
```

### C

```c
int minProcessingTime(int* processorTime, int processorTimeSize, int* tasks, int tasksSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinProcessingTime(IList<int> processorTime, IList<int> tasks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} processorTime
 * @param {number[]} tasks
 * @return {number}
 */
var minProcessingTime = function(processorTime, tasks) {
    
};
```

### TypeScript

```typescript
function minProcessingTime(processorTime: number[], tasks: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $processorTime
     * @param Integer[] $tasks
     * @return Integer
     */
    function minProcessingTime($processorTime, $tasks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minProcessingTime(_ processorTime: [Int], _ tasks: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minProcessingTime(processorTime: List<Int>, tasks: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minProcessingTime(List<int> processorTime, List<int> tasks) {
    
  }
}
```

### Go

```golang
func minProcessingTime(processorTime []int, tasks []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} processor_time
# @param {Integer[]} tasks
# @return {Integer}
def min_processing_time(processor_time, tasks)
    
end
```

### Scala

```scala
object Solution {
    def minProcessingTime(processorTime: List[Int], tasks: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_processing_time(processor_time: Vec<i32>, tasks: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-processing-time processorTime tasks)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_processing_time(ProcessorTime :: [integer()], Tasks :: [integer()]) -> integer().
min_processing_time(ProcessorTime, Tasks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_processing_time(processor_time :: [integer], tasks :: [integer]) :: integer
  def min_processing_time(processor_time, tasks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minProcessingTime(processorTime: ArrayList<Int64>, tasks: ArrayList<Int64>): Int64 {

    }
}
```

