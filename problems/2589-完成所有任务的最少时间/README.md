# 2589. 完成所有任务的最少时间

## 题目描述

<p>你有一台电脑，它可以 <strong>同时</strong>&nbsp;运行无数个任务。给你一个二维整数数组&nbsp;<code>tasks</code>&nbsp;，其中&nbsp;<code>tasks[i] = [start<sub>i</sub>, end<sub>i</sub>, duration<sub>i</sub>]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个任务需要在 <strong>闭区间</strong>&nbsp;时间段&nbsp;<code>[start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;内运行&nbsp;<code>duration<sub>i</sub></code>&nbsp;个整数时间点（但不需要连续）。</p>

<p>当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。</p>

<p>请你返回完成所有任务的情况下，电脑最少需要运行多少秒。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>tasks = [[2,3,1],[4,5,1],[1,5,2]]
<b>输出：</b>2
<b>解释：</b>
- 第一个任务在闭区间 [2, 2] 运行。
- 第二个任务在闭区间 [5, 5] 运行。
- 第三个任务在闭区间 [2, 2] 和 [5, 5] 运行。
电脑总共运行 2 个整数时间点。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>tasks = [[1,3,2],[2,5,3],[5,6,2]]
<b>输出：</b>4
<b>解释：</b>
- 第一个任务在闭区间 [2, 3] 运行
- 第二个任务在闭区间 [2, 3] 和 [5, 5] 运行。
- 第三个任务在闭区间 [5, 6] 运行。
电脑总共运行 4 个整数时间点。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 2000</code></li>
	<li><code>tasks[i].length == 3</code></li>
	<li><code>1 &lt;= start<sub>i</sub>, end<sub>i</sub> &lt;= 2000</code></li>
	<li><code>1 &lt;= duration<sub>i</sub> &lt;= end<sub>i</sub> - start<sub>i</sub> + 1 </code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 数组
- 二分查找
- 排序

## 提示

1. Sort the tasks in ascending order of end time
2. Since there are only up to 2000 time points to consider, you can check them one by one
3. It is always beneficial to run the task as late as possible so that later tasks can run simultaneously.

## 示例

```
[[2,3,1],[4,5,1],[1,5,2]]
[[1,3,2],[2,5,3],[5,6,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMinimumTime(int[][] tasks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMinimumTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        
```

### C

```c
int findMinimumTime(int** tasks, int tasksSize, int* tasksColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMinimumTime(int[][] tasks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number}
 */
var findMinimumTime = function(tasks) {
    
};
```

### TypeScript

```typescript
function findMinimumTime(tasks: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer
     */
    function findMinimumTime($tasks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMinimumTime(_ tasks: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMinimumTime(tasks: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMinimumTime(List<List<int>> tasks) {
    
  }
}
```

### Go

```golang
func findMinimumTime(tasks [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} tasks
# @return {Integer}
def find_minimum_time(tasks)
    
end
```

### Scala

```scala
object Solution {
    def findMinimumTime(tasks: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_minimum_time(tasks: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-minimum-time tasks)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_minimum_time(Tasks :: [[integer()]]) -> integer().
find_minimum_time(Tasks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_minimum_time(tasks :: [[integer]]) :: integer
  def find_minimum_time(tasks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMinimumTime(tasks: Array<Array<Int64>>): Int64 {

    }
}
```

