# 1953. 你可以工作的最大周数

## 题目描述

<p>给你&nbsp;<code>n</code> 个项目，编号从 <code>0</code> 到 <code>n - 1</code> 。同时给你一个整数数组 <code>milestones</code> ，其中每个 <code>milestones[i]</code> 表示第 <code>i</code> 个项目中的阶段任务数量。</p>

<p>你可以按下面两个规则参与项目中的工作：</p>

<ul>
	<li>每周，你将会完成 <strong>某一个</strong> 项目中的 <strong>恰好一个</strong>&nbsp;阶段任务。你每周都 <strong>必须</strong> 工作。</li>
	<li>在 <strong>连续的</strong> 两周中，你 <strong>不能</strong> 参与并完成同一个项目中的两个阶段任务。</li>
</ul>

<p>一旦所有项目中的全部阶段任务都完成，或者执行仅剩的一个阶段任务将会导致你违反上面的规则，你将 <strong>停止工作</strong>。注意，由于这些条件的限制，你可能无法完成所有阶段任务。</p>

<p>返回在不违反上面规则的情况下你&nbsp;<strong>最多</strong>&nbsp;能工作多少周。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>milestones = [1,2,3]
<strong>输出：</strong>6
<strong>解释：</strong>一种可能的情形是：
​​​​- 第 1 周，你参与并完成项目 0 中的一个阶段任务。
- 第 2 周，你参与并完成项目 2 中的一个阶段任务。
- 第 3 周，你参与并完成项目 1 中的一个阶段任务。
- 第 4 周，你参与并完成项目 2 中的一个阶段任务。
- 第 5 周，你参与并完成项目 1 中的一个阶段任务。
- 第 6 周，你参与并完成项目 2 中的一个阶段任务。
总周数是 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>milestones = [5,2,1]
<strong>输出：</strong>7
<strong>解释：</strong>一种可能的情形是：
- 第 1 周，你参与并完成项目 0 中的一个阶段任务。
- 第 2 周，你参与并完成项目 1 中的一个阶段任务。
- 第 3 周，你参与并完成项目 0 中的一个阶段任务。
- 第 4 周，你参与并完成项目 1 中的一个阶段任务。
- 第 5 周，你参与并完成项目 0 中的一个阶段任务。
- 第 6 周，你参与并完成项目 2 中的一个阶段任务。
- 第 7 周，你参与并完成项目 0 中的一个阶段任务。
总周数是 7 。
注意，你不能在第 8 周参与完成项目 0 中的最后一个阶段任务，因为这会违反规则。
因此，项目 0 中会有一个阶段任务维持未完成状态。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == milestones.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= milestones[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Work on the project with the largest number of milestones as long as it is possible.
2. Does the project with the largest number of milestones affect the number of weeks?

## 示例

```
[1,2,3]
[5,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        
    }
};
```

### Java

```java
class Solution {
    public long numberOfWeeks(int[] milestones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        
```

### C

```c
long long numberOfWeeks(int* milestones, int milestonesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long NumberOfWeeks(int[] milestones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} milestones
 * @return {number}
 */
var numberOfWeeks = function(milestones) {
    
};
```

### TypeScript

```typescript
function numberOfWeeks(milestones: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $milestones
     * @return Integer
     */
    function numberOfWeeks($milestones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfWeeks(_ milestones: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfWeeks(milestones: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfWeeks(List<int> milestones) {
    
  }
}
```

### Go

```golang
func numberOfWeeks(milestones []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} milestones
# @return {Integer}
def number_of_weeks(milestones)
    
end
```

### Scala

```scala
object Solution {
    def numberOfWeeks(milestones: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_weeks(milestones: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-weeks milestones)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_weeks(Milestones :: [integer()]) -> integer().
number_of_weeks(Milestones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_weeks(milestones :: [integer]) :: integer
  def number_of_weeks(milestones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfWeeks(milestones: Array<Int64>): Int64 {

    }
}
```

