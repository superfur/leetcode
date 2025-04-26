# 1665. 完成所有任务的最少初始能量

## 题目描述

<p>给你一个任务数组 <code>tasks</code> ，其中 <code>tasks[i] = [actual<sub>i</sub>, minimum<sub>i</sub>]</code> ：</p>

<ul>
	<li><code>actual<sub>i</sub></code> 是完成第 <code>i</code> 个任务 <strong>需要耗费</strong> 的实际能量。</li>
	<li><code>minimum<sub>i</sub></code> 是开始第 <code>i</code> 个任务前需要达到的最低能量。</li>
</ul>

<p>比方说，如果任务为 <code>[10, 12]</code> 且你当前的能量为 <code>11</code> ，那么你不能开始这个任务。如果你当前的能量为 <code>13</code> ，你可以完成这个任务，且完成它后剩余能量为 <code>3</code> 。</p>

<p>你可以按照 <strong>任意顺序</strong> 完成任务。</p>

<p>请你返回完成所有任务的 <strong>最少</strong> 初始能量。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>tasks = [[1,2],[2,4],[4,8]]
<b>输出：</b>8
<strong>解释：</strong>
一开始有 8 能量，我们按照如下顺序完成任务：
    - 完成第 3 个任务，剩余能量为 8 - 4 = 4 。
    - 完成第 2 个任务，剩余能量为 4 - 2 = 2 。
    - 完成第 1 个任务，剩余能量为 2 - 1 = 1 。
注意到尽管我们有能量剩余，但是如果一开始只有 7 能量是不能完成所有任务的，因为我们无法开始第 3 个任务。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
<b>输出：</b>32
<strong>解释：</strong>
一开始有 32 能量，我们按照如下顺序完成任务：
    - 完成第 1 个任务，剩余能量为 32 - 1 = 31 。
    - 完成第 2 个任务，剩余能量为 31 - 2 = 29 。
    - 完成第 3 个任务，剩余能量为 29 - 10 = 19 。
    - 完成第 4 个任务，剩余能量为 19 - 10 = 9 。
    - 完成第 5 个任务，剩余能量为 9 - 8 = 1 。</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
<b>输出：</b>27
<strong>解释：</strong>
一开始有 27 能量，我们按照如下顺序完成任务：
    - 完成第 5 个任务，剩余能量为 27 - 5 = 22 。
    - 完成第 2 个任务，剩余能量为 22 - 2 = 20 。
    - 完成第 3 个任务，剩余能量为 20 - 3 = 17 。
    - 完成第 1 个任务，剩余能量为 17 - 1 = 16 。
    - 完成第 4 个任务，剩余能量为 16 - 4 = 12 。
    - 完成第 6 个任务，剩余能量为 12 - 6 = 6 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= actual<sub>​i</sub> &lt;= minimum<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序

## 提示

1. We can easily figure that the f(x) : does x solve this array is monotonic so binary Search is doable
2. Figure a sorting pattern

## 示例

```
[[1,2],[2,4],[4,8]]
[[1,3],[2,4],[10,11],[10,12],[8,9]]
[[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumEffort(int[][] tasks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
```

### C

```c
int minimumEffort(int** tasks, int tasksSize, int* tasksColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumEffort(int[][] tasks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number}
 */
var minimumEffort = function(tasks) {
    
};
```

### TypeScript

```typescript
function minimumEffort(tasks: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer
     */
    function minimumEffort($tasks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumEffort(_ tasks: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumEffort(tasks: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumEffort(List<List<int>> tasks) {
    
  }
}
```

### Go

```golang
func minimumEffort(tasks [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} tasks
# @return {Integer}
def minimum_effort(tasks)
    
end
```

### Scala

```scala
object Solution {
    def minimumEffort(tasks: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_effort(tasks: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-effort tasks)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_effort(Tasks :: [[integer()]]) -> integer().
minimum_effort(Tasks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_effort(tasks :: [[integer]]) :: integer
  def minimum_effort(tasks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumEffort(tasks: Array<Array<Int64>>): Int64 {

    }
}
```

