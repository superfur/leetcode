# 2432. 处理用时最长的那个任务的员工

## 题目描述

<p>共有 <code>n</code> 位员工，每位员工都有一个从 <code>0</code> 到 <code>n - 1</code> 的唯一 id 。</p>

<p>给你一个二维整数数组 <code>logs</code> ，其中 <code>logs[i] = [id<sub>i</sub>, leaveTime<sub>i</sub>]</code> ：</p>

<ul>
	<li><code>id<sub>i</sub></code> 是处理第 <code>i</code> 个任务的员工的 id ，且</li>
	<li><code>leaveTime<sub>i</sub></code> 是员工完成第 <code>i</code> 个任务的时刻。所有 <code>leaveTime<sub>i</sub></code> 的值都是 <strong>唯一</strong> 的。</li>
</ul>

<p>注意，第 <code>i</code> 个任务在第 <code>(i - 1)</code> 个任务结束后立即开始，且第 <code>0</code> 个任务从时刻 <code>0</code> 开始。</p>

<p>返回处理用时最长的那个任务的员工的 id 。如果存在两个或多个员工同时满足，则返回几人中 <strong>最小</strong> 的 id 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]
<strong>输出：</strong>1
<strong>解释：</strong>
任务 0 于时刻 0 开始，且在时刻 3 结束，共计 3 个单位时间。
任务 1 于时刻 3 开始，且在时刻 5 结束，共计 2 个单位时间。
任务 2 于时刻 5 开始，且在时刻 9 结束，共计 4 个单位时间。
任务 3 于时刻 9 开始，且在时刻 15 结束，共计 6 个单位时间。
时间最长的任务是任务 3 ，而 id 为 1 的员工是处理此任务的员工，所以返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]
<strong>输出：</strong>3
<strong>解释：</strong>
任务 0 于时刻 0 开始，且在时刻 1 结束，共计 1 个单位时间。
任务 1 于时刻 1 开始，且在时刻 7 结束，共计 6 个单位时间。
任务 2 于时刻 7 开始，且在时刻 12 结束，共计 5 个单位时间。
任务 3 于时刻 12 开始，且在时刻 17 结束，共计 5 个单位时间。
时间最长的任务是任务 1 ，而 id 为 3 的员工是处理此任务的员工，所以返回 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 2, logs = [[0,10],[1,20]]
<strong>输出：</strong>0
<strong>解释：</strong>
任务 0 于时刻 0 开始，且在时刻 10 结束，共计 10 个单位时间。
任务 1 于时刻 10 开始，且在时刻 20 结束，共计 10 个单位时间。
时间最长的任务是任务 0 和 1 ，处理这两个任务的员工的 id 分别是 0 和 1 ，所以返回最小的 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= logs.length &lt;= 500</code></li>
	<li><code>logs[i].length == 2</code></li>
	<li><code>0 &lt;= id<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>1 &lt;= leaveTime<sub>i</sub> &lt;= 500</code></li>
	<li><code>id<sub>i</sub> != id<sub>i + 1</sub></code></li>
	<li><code>leaveTime<sub>i</sub></code> 按严格递增顺序排列</li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Find the time of the longest task
2. Store each employee’s longest task time in a hash table
3. For employees that have the same longest task time, we only need the employee with the smallest ID

## 示例

```
10
[[0,3],[2,5],[0,9],[1,15]]
26
[[1,1],[3,7],[2,12],[7,17]]
2
[[0,10],[1,20]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int hardestWorker(int n, vector<vector<int>>& logs) {
        
    }
};
```

### Java

```java
class Solution {
    public int hardestWorker(int n, int[][] logs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
```

### C

```c
int hardestWorker(int n, int** logs, int logsSize, int* logsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int HardestWorker(int n, int[][] logs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} logs
 * @return {number}
 */
var hardestWorker = function(n, logs) {
    
};
```

### TypeScript

```typescript
function hardestWorker(n: number, logs: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $logs
     * @return Integer
     */
    function hardestWorker($n, $logs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hardestWorker(_ n: Int, _ logs: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hardestWorker(n: Int, logs: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int hardestWorker(int n, List<List<int>> logs) {
    
  }
}
```

### Go

```golang
func hardestWorker(n int, logs [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} logs
# @return {Integer}
def hardest_worker(n, logs)
    
end
```

### Scala

```scala
object Solution {
    def hardestWorker(n: Int, logs: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn hardest_worker(n: i32, logs: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (hardest-worker n logs)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec hardest_worker(N :: integer(), Logs :: [[integer()]]) -> integer().
hardest_worker(N, Logs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec hardest_worker(n :: integer, logs :: [[integer]]) :: integer
  def hardest_worker(n, logs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hardestWorker(n: Int64, logs: Array<Array<Int64>>): Int64 {

    }
}
```

