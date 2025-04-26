# 3440. 重新安排会议得到最多空余时间 II

## 题目描述

<p>给你一个整数&nbsp;<code>eventTime</code>&nbsp;表示一个活动的总时长，这个活动开始于&nbsp;<code>t = 0</code>&nbsp;，结束于&nbsp;<code>t = eventTime</code>&nbsp;。</p>

<p>同时给你两个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>startTime</code> 和&nbsp;<code>endTime</code>&nbsp;。它们表示这次活动中 <code>n</code>&nbsp;个时间&nbsp;<strong>没有重叠</strong>&nbsp;的会议，其中第&nbsp;<code>i</code>&nbsp;个会议的时间为&nbsp;<code>[startTime[i], endTime[i]]</code>&nbsp;。</p>

<p>你可以重新安排 <strong>至多</strong>&nbsp;一个会议，安排的规则是将会议时间平移，且保持原来的 <strong>会议时长</strong>&nbsp;，你的目的是移动会议后 <strong>最大化</strong>&nbsp;相邻两个会议之间的 <strong>最长</strong> 连续空余时间。</p>

<p>请你返回重新安排会议以后，可以得到的 <strong>最大</strong>&nbsp;空余时间。</p>

<p><b>注意</b>，会议 <strong>不能</strong>&nbsp;安排到整个活动的时间以外，且会议之间需要保持互不重叠。</p>

<p><b>注意：</b>重新安排会议以后，会议之间的顺序可以发生改变。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>eventTime = 5, startTime = [1,3], endTime = [2,5]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/22/example0_rescheduled.png" style="width: 375px; height: 123px;" /></p>

<p>将&nbsp;<code>[1, 2]</code>&nbsp;的会议安排到&nbsp;<code>[2, 3]</code>&nbsp;，得到空余时间&nbsp;<code>[0, 2]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]</span></p>

<p><span class="example-io"><b>输出：</b>7</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/22/rescheduled_example0.png" style="width: 375px; height: 125px;" /></p>

<p>将&nbsp;<code>[0, 1]</code>&nbsp;的会议安排到&nbsp;<code>[8, 9]</code>&nbsp;，得到空余时间&nbsp;<code>[0, 7]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]</span></p>

<p><b>输出：</b>6</p>

<p><b>解释：</b></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2025/01/28/image3.png" style="width: 375px; height: 125px;" /></strong></p>

<p>将&nbsp;<code>[3, 4]</code>&nbsp;的会议安排到&nbsp;<code>[8, 9]</code>&nbsp;，得到空余时间&nbsp;<code>[1, 7]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p>活动中的所有时间都被会议安排满了。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= eventTime &lt;= 10<sup>9</sup></code></li>
	<li><code>n == startTime.length == endTime.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= startTime[i] &lt; endTime[i] &lt;= eventTime</code></li>
	<li><code>endTime[i] &lt;= startTime[i + 1]</code> 其中&nbsp;<code>i</code> 在范围&nbsp;<code>[0, n - 2]</code>&nbsp;之间。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 枚举

## 提示

1. If we reschedule a meeting earlier or later, we need to find a gap of length at least <code>endTime[i] - startTime[i]</code>. Try maintaining the gaps in some sorted data structure.

## 示例

```
5
[1,3]
[2,5]
10
[0,7,9]
[1,8,10]
10
[0,3,7,9]
[1,4,8,10]
5
[0,1,2,3,4]
[1,2,3,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        
```

### C

```c
int maxFreeTime(int eventTime, int* startTime, int startTimeSize, int* endTime, int endTimeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} eventTime
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @return {number}
 */
var maxFreeTime = function(eventTime, startTime, endTime) {
    
};
```

### TypeScript

```typescript
function maxFreeTime(eventTime: number, startTime: number[], endTime: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $eventTime
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @return Integer
     */
    function maxFreeTime($eventTime, $startTime, $endTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxFreeTime(_ eventTime: Int, _ startTime: [Int], _ endTime: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxFreeTime(eventTime: Int, startTime: IntArray, endTime: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxFreeTime(int eventTime, List<int> startTime, List<int> endTime) {
    
  }
}
```

### Go

```golang
func maxFreeTime(eventTime int, startTime []int, endTime []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} event_time
# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @return {Integer}
def max_free_time(event_time, start_time, end_time)
    
end
```

### Scala

```scala
object Solution {
    def maxFreeTime(eventTime: Int, startTime: Array[Int], endTime: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_free_time(event_time: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-free-time eventTime startTime endTime)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_free_time(EventTime :: integer(), StartTime :: [integer()], EndTime :: [integer()]) -> integer().
max_free_time(EventTime, StartTime, EndTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_free_time(event_time :: integer, start_time :: [integer], end_time :: [integer]) :: integer
  def max_free_time(event_time, start_time, end_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxFreeTime(eventTime: Int64, startTime: Array<Int64>, endTime: Array<Int64>): Int64 {

    }
}
```

