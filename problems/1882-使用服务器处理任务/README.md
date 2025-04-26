# 1882. 使用服务器处理任务

## 题目描述

<p>给你两个 <strong>下标从 0 开始</strong> 的整数数组 <code>servers</code> 和 <code>tasks</code> ，长度分别为 <code>n</code>​​​​​​ 和 <code>m</code>​​​​​​ 。<code>servers[i]</code> 是第 <code>i<sup>​​​​​​</sup></code>​​​​ 台服务器的 <strong>权重</strong> ，而 <code>tasks[j]</code> 是处理第 <code>j<sup>​​​​​​</sup></code> 项任务 <strong>所需要的时间</strong>（单位：秒）。</p>

<p>你正在运行一个仿真系统，在处理完所有任务后，该系统将会关闭。每台服务器只能同时处理一项任务。第 <code>0</code> 项任务在第 <code>0</code> 秒可以开始处理，相应地，第 <code>j</code> 项任务在第 <code>j</code> 秒可以开始处理。处理第 <code>j</code> 项任务时，你需要为它分配一台 <strong>权重最小</strong> 的空闲服务器。如果存在多台相同权重的空闲服务器，请选择 <strong>下标最小</strong> 的服务器。如果一台空闲服务器在第 <code>t</code> 秒分配到第 <code>j</code> 项任务，那么在 <code>t + tasks[j]</code> 时它将恢复空闲状态。</p>

<p>如果没有空闲服务器，则必须等待，直到出现一台空闲服务器，并 <strong>尽可能早</strong> 地处理剩余任务。 如果有多项任务等待分配，则按照 <strong>下标递增</strong> 的顺序完成分配。</p>

<p>如果同一时刻存在多台空闲服务器，可以同时将多项任务分别分配给它们。</p>

<p>构建长度为 <code>m</code> 的答案数组 <code>ans</code> ，其中 <code>ans[j]</code> 是第 <code>j</code> 项任务分配的服务器的下标。</p>

<p>返回答案数组<em> </em><code>ans</code>​​​​ 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>servers = [3,3,2], tasks = [1,2,3,2,1,2]
<strong>输出：</strong>[2,2,0,2,1,2]
<strong>解释：</strong>事件按时间顺序如下：
- 0 秒时，第 0 项任务加入到任务队列，使用第 2 台服务器处理到 1 秒。
- 1 秒时，第 2 台服务器空闲，第 1 项任务加入到任务队列，使用第 2 台服务器处理到 3 秒。
- 2 秒时，第 2 项任务加入到任务队列，使用第 0 台服务器处理到 5 秒。
- 3 秒时，第 2 台服务器空闲，第 3 项任务加入到任务队列，使用第 2 台服务器处理到 5 秒。
- 4 秒时，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 5 秒。
- 5 秒时，所有服务器都空闲，第 5 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
<strong>输出：</strong>[1,4,1,4,1,3,2]
<strong>解释：</strong>事件按时间顺序如下：
- 0 秒时，第 0 项任务加入到任务队列，使用第 1 台服务器处理到 2 秒。
- 1 秒时，第 1 项任务加入到任务队列，使用第 4 台服务器处理到 2 秒。
- 2 秒时，第 1 台和第 4 台服务器空闲，第 2 项任务加入到任务队列，使用第 1 台服务器处理到 4 秒。
- 3 秒时，第 3 项任务加入到任务队列，使用第 4 台服务器处理到 7 秒。
- 4 秒时，第 1 台服务器空闲，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 9 秒。
- 5 秒时，第 5 项任务加入到任务队列，使用第 3 台服务器处理到 7 秒。
- 6 秒时，第 6 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>servers.length == n</code></li>
	<li><code>tasks.length == m</code></li>
	<li><code>1 <= n, m <= 2 * 10<sup>5</sup></code></li>
	<li><code>1 <= servers[i], tasks[j] <= 2 * 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 堆（优先队列）

## 提示

1. You can maintain a Heap of available Servers and a Heap of unavailable servers
2. Note that the tasks will be processed in the input order so you just need to find the x-th server that will be available according to the rules

## 示例

```
[3,3,2]
[1,2,3,2,1,2]
[5,1,4,3,2]
[2,1,2,4,5,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* assignTasks(int* servers, int serversSize, int* tasks, int tasksSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] AssignTasks(int[] servers, int[] tasks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} servers
 * @param {number[]} tasks
 * @return {number[]}
 */
var assignTasks = function(servers, tasks) {
    
};
```

### TypeScript

```typescript
function assignTasks(servers: number[], tasks: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $servers
     * @param Integer[] $tasks
     * @return Integer[]
     */
    function assignTasks($servers, $tasks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func assignTasks(_ servers: [Int], _ tasks: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun assignTasks(servers: IntArray, tasks: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> assignTasks(List<int> servers, List<int> tasks) {
    
  }
}
```

### Go

```golang
func assignTasks(servers []int, tasks []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} servers
# @param {Integer[]} tasks
# @return {Integer[]}
def assign_tasks(servers, tasks)
    
end
```

### Scala

```scala
object Solution {
    def assignTasks(servers: Array[Int], tasks: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (assign-tasks servers tasks)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec assign_tasks(Servers :: [integer()], Tasks :: [integer()]) -> [integer()].
assign_tasks(Servers, Tasks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec assign_tasks(servers :: [integer], tasks :: [integer]) :: [integer]
  def assign_tasks(servers, tasks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func assignTasks(servers: Array<Int64>, tasks: Array<Int64>): Array<Int64> {

    }
}
```

