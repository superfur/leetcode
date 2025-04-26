# 2244. 完成所有任务需要的最少轮数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>tasks</code> ，其中 <code>tasks[i]</code> 表示任务的难度级别。在每一轮中，你可以完成 2 个或者 3 个 <strong>相同难度级别</strong> 的任务。</p>

<p>返回完成所有任务需要的 <strong>最少</strong> 轮数，如果无法完成所有任务，返回<em> </em><code>-1</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>tasks = [2,2,3,3,2,4,4,4,4,4]
<strong>输出：</strong>4
<strong>解释：</strong>要想完成所有任务，一个可能的计划是：
- 第一轮，完成难度级别为 2 的 3 个任务。 
- 第二轮，完成难度级别为 3 的 2 个任务。 
- 第三轮，完成难度级别为 4 的 3 个任务。 
- 第四轮，完成难度级别为 4 的 2 个任务。 
可以证明，无法在少于 4 轮的情况下完成所有任务，所以答案为 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>tasks = [2,3,3]
<strong>输出：</strong>-1
<strong>解释：</strong>难度级别为 2 的任务只有 1 个，但每一轮执行中，只能选择完成 2 个或者 3 个相同难度级别的任务。因此，无法完成所有任务，答案为 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 计数

## 提示

1. Which data structure can you use to store the number of tasks of each difficulty level?
2. For any particular difficulty level, what can be the optimal strategy to complete the tasks using minimum rounds?
3. When can we not complete all tasks of a difficulty level?

## 示例

```
[2,2,3,3,2,4,4,4,4,4]
[2,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumRounds(int[] tasks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
```

### C

```c
int minimumRounds(int* tasks, int tasksSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumRounds(int[] tasks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} tasks
 * @return {number}
 */
var minimumRounds = function(tasks) {
    
};
```

### TypeScript

```typescript
function minimumRounds(tasks: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $tasks
     * @return Integer
     */
    function minimumRounds($tasks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumRounds(_ tasks: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumRounds(tasks: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumRounds(List<int> tasks) {
    
  }
}
```

### Go

```golang
func minimumRounds(tasks []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} tasks
# @return {Integer}
def minimum_rounds(tasks)
    
end
```

### Scala

```scala
object Solution {
    def minimumRounds(tasks: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_rounds(tasks: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-rounds tasks)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_rounds(Tasks :: [integer()]) -> integer().
minimum_rounds(Tasks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_rounds(tasks :: [integer]) :: integer
  def minimum_rounds(tasks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumRounds(tasks: Array<Int64>): Int64 {

    }
}
```

