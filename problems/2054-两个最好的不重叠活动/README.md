# 2054. 两个最好的不重叠活动

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>events</code>&nbsp;，其中&nbsp;<code>events[i] = [startTime<sub>i</sub>, endTime<sub>i</sub>, value<sub>i</sub>]</code>&nbsp;。第&nbsp;<code>i</code>&nbsp;个活动开始于&nbsp;<code>startTime<sub>i</sub></code>&nbsp;，结束于&nbsp;<code>endTime<sub>i</sub></code>&nbsp;，如果你参加这个活动，那么你可以得到价值&nbsp;<code>value<sub>i</sub></code>&nbsp;。你 <strong>最多</strong>&nbsp;可以参加&nbsp;<strong>两个时间不重叠</strong>&nbsp;活动，使得它们的价值之和 <strong>最大</strong>&nbsp;。</p>

<p>请你返回价值之和的 <strong>最大值</strong>&nbsp;。</p>

<p>注意，活动的开始时间和结束时间是 <strong>包括</strong>&nbsp;在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 <code>t</code>&nbsp;，那么下一个活动必须在&nbsp;<code>t + 1</code>&nbsp;或之后的时间开始。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/picture5.png" style="width: 400px; height: 75px;"></p>

<pre><b>输入：</b>events = [[1,3,2],[4,5,2],[2,4,3]]
<b>输出：</b>4
<strong>解释：</strong>选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="Example 1 Diagram" src="https://assets.leetcode.com/uploads/2021/09/21/picture1.png" style="width: 400px; height: 77px;"></p>

<pre><b>输入：</b>events = [[1,3,2],[4,5,2],[1,5,5]]
<b>输出：</b>5
<strong>解释：</strong>选择活动 2 ，价值和为 5 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/picture3.png" style="width: 400px; height: 66px;"></p>

<pre><b>输入：</b>events = [[1,5,3],[1,5,1],[6,6,5]]
<b>输出：</b>8
<strong>解释：</strong>选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= events.length &lt;= 10<sup>5</sup></code></li>
	<li><code>events[i].length == 3</code></li>
	<li><code>1 &lt;= startTime<sub>i</sub> &lt;= endTime<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= value<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 动态规划
- 排序
- 堆（优先队列）

## 提示

1. How can sorting the events on the basis of their start times help? How about end times?
2. How can we quickly get the maximum score of an interval not intersecting with the interval we chose?

## 示例

```
[[1,3,2],[4,5,2],[2,4,3]]
[[1,3,2],[4,5,2],[1,5,5]]
[[1,5,3],[1,5,1],[6,6,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxTwoEvents(int[][] events) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
```

### C

```c
int maxTwoEvents(int** events, int eventsSize, int* eventsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxTwoEvents(int[][] events) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {
    
};
```

### TypeScript

```typescript
function maxTwoEvents(events: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function maxTwoEvents($events) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxTwoEvents(_ events: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxTwoEvents(events: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxTwoEvents(List<List<int>> events) {
    
  }
}
```

### Go

```golang
func maxTwoEvents(events [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} events
# @return {Integer}
def max_two_events(events)
    
end
```

### Scala

```scala
object Solution {
    def maxTwoEvents(events: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_two_events(events: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-two-events events)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_two_events(Events :: [[integer()]]) -> integer().
max_two_events(Events) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_two_events(events :: [[integer]]) :: integer
  def max_two_events(events) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxTwoEvents(events: Array<Array<Int64>>): Int64 {

    }
}
```

