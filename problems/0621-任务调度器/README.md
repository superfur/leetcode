# 621. 任务调度器

## 题目描述

<p>给你一个用字符数组&nbsp;<code>tasks</code> 表示的 CPU 需要执行的任务列表，用字母 A 到 Z 表示，以及一个冷却时间 <code>n</code>。每个周期或时间间隔允许完成一项任务。任务可以按任何顺序完成，但有一个限制：两个<strong> 相同种类</strong> 的任务之间必须有长度为<strong>&nbsp;</strong><code>n</code><strong> </strong>的冷却时间。</p>

<p>返回完成所有任务所需要的<strong> 最短时间间隔</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block"><strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 2</div>

<div class="example-block"><strong>输出：</strong>8</div>

<div class="example-block"><strong>解释：</strong></div>

<div class="example-block">在完成任务 A 之后，你必须等待两个间隔。对任务 B 来说也是一样。在第 3 个间隔，A 和 B 都不能完成，所以你需要待命。在第 4 个间隔，由于已经经过了 2 个间隔，你可以再次执行 A 任务。</div>

<div class="example-block">&nbsp;</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><b>输入：</b>tasks = ["A","C","A","B","D","B"], n = 1</p>

<p><b>输出：</b>6</p>

<p><b>解释：</b>一种可能的序列是：A -&gt; B -&gt; C -&gt; D -&gt; A -&gt; B。</p>

<p>由于冷却间隔为 1，你可以在完成另一个任务后重复执行这个任务。</p>
</div>

<p><strong>示例 3：</strong></p>

<div class="example-block"><strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 3</div>

<div class="example-block"><strong>输出：</strong>10</div>

<div class="example-block"><strong>解释：</strong>一种可能的序列为：A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B。</div>

<div class="example-block">只有两种任务类型，A 和 B，需要被 3 个间隔分割。这导致重复执行这些任务的间隔当中有两次待命状态。</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tasks[i]</code> 是大写英文字母</li>
	<li><code>0 &lt;= n &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 计数
- 排序
- 堆（优先队列）

## 提示

1. There are many different solutions for this problem, including a greedy algorithm.
2. For every cycle, find the most frequent letter that can be placed in this cycle. After placing, decrease the frequency of that letter by one.
3. Use Priority Queue.

## 示例

```
["A","A","A","B","B","B"]
2
["A","C","A","B","D","B"]
1
["A","A","A", "B","B","B"]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
```

### C

```c
int leastInterval(char* tasks, int tasksSize, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    
};
```

### TypeScript

```typescript
function leastInterval(tasks: string[], n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $tasks
     * @param Integer $n
     * @return Integer
     */
    function leastInterval($tasks, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func leastInterval(_ tasks: [Character], _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun leastInterval(tasks: CharArray, n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int leastInterval(List<String> tasks, int n) {
    
  }
}
```

### Go

```golang
func leastInterval(tasks []byte, n int) int {
    
}
```

### Ruby

```ruby
# @param {Character[]} tasks
# @param {Integer} n
# @return {Integer}
def least_interval(tasks, n)
    
end
```

### Scala

```scala
object Solution {
    def leastInterval(tasks: Array[Char], n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (least-interval tasks n)
  (-> (listof char?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec least_interval(Tasks :: [char()], N :: integer()) -> integer().
least_interval(Tasks, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec least_interval(tasks :: [char], n :: integer) :: integer
  def least_interval(tasks, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func leastInterval(tasks: Array<Rune>, n: Int64): Int64 {

    }
}
```

